"""任务管理器: 任务创建/执行/取消 + 日志落盘与 WebSocket 广播。

任务类型 (kind):
- lmp    → 「暂存-运行-回收」: 宿主机侧把脚本与依赖拷入数据目录工作区
           (lammps-data-docker/jobs/<id>/ = 容器 /data/jobs/<id>/),
           docker exec -w 到工作区运行, 产物天然留在宿主机工作区
- python → 本地 uv run python 运行分析/生成脚本, 工作目录 = 脚本所在项目目录

v1.1:
- 精确取消: -in 使用容器内绝对路径使命令行含任务唯一标识,
  cancel 只 pkill -f /data/jobs/<id>/, 不再波及容器内其他 LAMMPS 进程
- 依赖暂存: 解析 include/read_data/read_restart 引用闭包一并拷入
- 状态防重入: per-job 锁 + 迁移表, 取消与自然退出竞态先到先得
- thermo 解析: 日志行实时喂解析器, 经 WS 推送曲线样本
"""
import asyncio
import collections
import hashlib
import json
import logging
import os
import uuid
from datetime import datetime
from typing import Any

from common import runner
from common.runner import collect_deps  # noqa: F401  (兼容旧导入路径, tests 引用)

from . import store, thermo
from .config import (CONTAINER_NAME, JOBS_LOG_DIR, LAMMPS_DATA_HOST_DIR, ROOT)
from .docker_env import container_fingerprint

log = logging.getLogger("workbench.jobs")


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def get_project(project_id: str) -> dict | None:
    from .config import get_projects
    return next((p for p in get_projects() if p["id"] == project_id), None)


def _workspace_host(job_id: str) -> str:
    """任务工作区 (宿主机视角): 数据目录下按任务 id 隔离。"""
    return runner.workspace_host(LAMMPS_DATA_HOST_DIR, job_id)


def _workspace_container(job_id: str) -> str:
    return runner.workspace_container(job_id)


# ---- 状态迁移表 ----

VALID_TRANSITIONS: dict[str, set[str]] = {
    "queued": {"running", "failed", "canceled", "interrupted"},  # 并发上限排队
    "running": {"completed", "failed", "canceled", "interrupted"},
    "interrupted": {"canceled"},  # 后端重启遗留的任务: 仍可从列表取消以清理容器进程
    "completed": set(),
    "failed": set(),
    "canceled": set(),
}


class JobManager:
    def __init__(self) -> None:
        self._procs: dict[str, asyncio.subprocess.Process] = {}
        self._tails: dict[str, collections.deque[str]] = {}
        self._subs: dict[str, set[asyncio.Queue]] = {}
        self._canceled: set[str] = set()
        self._locks: dict[str, asyncio.Lock] = {}
        self._thermo: dict[str, thermo.ThermoBuffer] = {}
        self._pending: collections.deque[tuple[dict, list[str]]] = collections.deque()  # (job, command)

    # ---- 任务生命周期 ----

    async def start(self, project_id: str, script: str, kind: str,
                    omp_threads: int = 8) -> dict[str, Any]:
        project = get_project(project_id)
        if project is None:
            raise ValueError(f"未知项目: {project_id}")
        if kind not in ("lmp", "python", "build"):
            raise ValueError(f"不支持的任务类型: {kind}")
        if kind != "build" and (os.path.basename(script) != script or script in (".", "..")):
            raise ValueError(f"非法脚本名: {script}")
        if kind == "build":
            script = "-m common.build"  # 仅用于展示
        if not (1 <= omp_threads <= 64):
            raise ValueError(f"OMP 线程数须在 1-64: {omp_threads}")

        job_id = uuid.uuid4().hex[:12]
        workspace = _workspace_host(job_id) if kind == "lmp" else None
        command = self._build_command(project, script, kind, job_id, omp_threads)

        # 环境指纹 (任务可比性): system.json sha + 容器镜像/LAMMPS 版本; 采集失败不阻塞发车
        fingerprint: dict[str, Any] = {}
        sys_path = os.path.join(ROOT, project["dir"], "system.json")
        if os.path.isfile(sys_path):
            with open(sys_path, "rb") as f:
                fingerprint["system_sha"] = hashlib.sha256(f.read()).hexdigest()[:16]
        if kind == "lmp":
            fp = await asyncio.to_thread(container_fingerprint)
            if fp:
                fingerprint.update(fp)

        job = {
            "id": job_id,
            "project_id": project_id,
            "project_name": project["name"],
            "script": script,
            "kind": kind,
            "command": " ".join(command),
            "status": "running",
            "exit_code": None,
            "created_at": _now(),
            "started_at": _now(),
            "finished_at": None,
            "log_path": os.path.join(JOBS_LOG_DIR, f"{job_id}.log"),  # 日志文件名 = 任务 id, 便于人工查找
            "workspace": workspace,
            "omp_threads": omp_threads,
            "fingerprint": json.dumps(fingerprint, ensure_ascii=False) if fingerprint else None,
        }

        store.insert(job)
        self._tails[job_id] = collections.deque(maxlen=800)
        self._locks[job_id] = asyncio.Lock()
        self._thermo[job_id] = thermo.ThermoBuffer()
        if kind == "lmp" and self._running_lmp_count() >= MAX_CONCURRENT_LMP:
            # 并发上限: 排队等前序任务完成 (失败/取消也会触发调度)
            ok = await self._transition(job_id, "queued", None)
            if ok:
                self._pending.append((job, command))
                await self._append_line(job_id,
                    f"[workbench] 已进入队列 (并发上限 {MAX_CONCURRENT_LMP}); 前序任务完成后自动启动")
                return job
        asyncio.create_task(self._run(job, command))
        return job

    def _running_lmp_count(self) -> int:
        return sum(1 for p in self._procs.values() if p.returncode is None)

    def _build_command(self, project: dict, script: str, kind: str, job_id: str,
                       omp_threads: int = 8) -> list[str]:
        if kind == "lmp":
            # 统一执行契约 (common/runner.py): 命令与 CLI 完全同源
            return runner.lmp_command(_workspace_container(job_id), script, omp_threads)
        if kind == "build":
            # 体系构建: python -m common.build <项目目录> (读 system.json → system.data)
            return ["uv", "run", "python", "-m", "common.build",
                    os.path.join(ROOT, project["dir"])]
        # python: 分析/生成脚本, 输出约定为脚本同目录 (与 docs/workflows.md 一致)
        return ["uv", "run", "python", os.path.join(ROOT, project["dir"], script)]

    async def _stage_lmp(self, job: dict, project: dict) -> None:
        """宿主机侧暂存: 脚本 + 依赖闭包 + 顶层 *.data → 工作区 (契约见 common/runner.py)。"""
        missing = await asyncio.to_thread(
            runner.stage_dependencies,
            os.path.join(ROOT, project["dir"]), job["script"], job["workspace"],
        )
        for ref in missing:
            await self._append_line(
                job["id"], f"[workbench] 警告: 脚本引用的依赖不存在, 未暂存: {ref}")

    async def _run(self, job: dict, command: list[str]) -> None:
        job_id = job["id"]
        project = get_project(job["project_id"])
        try:
            if job["kind"] == "lmp":
                await self._stage_lmp(job, project)
                await self._append_line(
                    job_id, f"[workbench] 已暂存至工作区: {job['workspace']}")
            if job["kind"] == "lmp":
                workdir = job["workspace"]
            elif job["kind"] == "build":
                workdir = ROOT  # 保证 -m common.build 可导入
            else:
                workdir = os.path.join(ROOT, project["dir"])
            proc = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
                cwd=workdir,
            )
        except Exception as e:  # docker 不存在 / uv 缺失 / 暂存失败等启动期错误
            await self._append_line(job_id, f"[workbench] 进程启动失败: {e}")
            await self._transition(job_id, "failed", None)
            return

        self._procs[job_id] = proc
        await self._broadcast(job_id, {"type": "status", "status": "running"})
        assert proc.stdout is not None
        async for raw in proc.stdout:
            line = raw.decode("utf-8", "replace").rstrip("\r\n")
            await self._append_line(job_id, line)

        code = await proc.wait()
        self._procs.pop(job_id, None)
        final = "completed" if code == 0 else "failed"
        if await self._transition(job_id, final, code):
            note = "任务完成" if final == "completed" else f"任务失败 (exit code {code})"
            await self._append_line(job_id, f"[workbench] {note}")
        if job["kind"] == "build" and final == "completed":
            await asyncio.to_thread(self._record_built_sha, project)
        if job["kind"] == "lmp":
            self._dispatch()

    def _dispatch(self) -> None:
        """并发空位时启动下一个排队任务 (失败/取消完成均会触发)。"""
        while self._pending and self._running_lmp_count() < MAX_CONCURRENT_LMP:
            job, command = self._pending.popleft()
            if store.get(job["id"], ) is None:
                continue  # 已被删除
            cur = store.get(job["id"])
            if cur and cur["status"] != "queued":
                continue  # 已取消/中断
            log.info("队列调度: 启动排队任务 %s", job["id"])
            asyncio.get_running_loop().create_task(self._promote(job, command))
            break

    async def _promote(self, job: dict, command: list[str]) -> None:
        if await self._transition(job["id"], "running", None):
            await self._append_line(job["id"], "[workbench] 队列轮到, 开始执行")
            asyncio.create_task(self._run(job, command))

    @staticmethod
    def _record_built_sha(project: dict) -> None:
        """构建成功后把 system.json 指纹写入 project.json —
        一致性链落地 (体系配置页可检测「参数已改未重建」)。"""
        abs_dir = os.path.join(ROOT, project["dir"])
        sys_path = os.path.join(abs_dir, "system.json")
        meta_path = os.path.join(abs_dir, "project.json")
        if not (os.path.isfile(sys_path) and os.path.isfile(meta_path)):
            return
        with open(sys_path, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()
        try:
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            meta["built_system_sha"] = sha
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
                f.write("\n")
        except (OSError, json.JSONDecodeError) as e:
            log.warning("记录 built_system_sha 失败 (%s): %s", meta_path, e)

    async def _transition(self, job_id: str, new_status: str, exit_code: int | None) -> bool:
        """受控状态迁移: 持锁校验合法迁移, 先到先得; 非法迁移幂等忽略。

        锁按需创建 — 恢复路径 (进程重启后对账) 没有 start() 建过的锁也必须可用。
        """
        lock = self._locks.setdefault(job_id, asyncio.Lock())
        async with lock:
            current = store.get(job_id)
            if current is None or new_status not in VALID_TRANSITIONS.get(current["status"], set()):
                return False
            store.update(job_id, status=new_status, exit_code=exit_code, finished_at=_now())
        await self._broadcast(job_id, {"type": "status", "status": new_status, "exit_code": exit_code})
        return True

    async def recover_orphans(self) -> int:
        """后端启动时对账: 上次退出时仍为 running 的任务标记为 interrupted。

        容器内进程可能已消失 (干净退出) 或仍在计算 (残留) — 两种情况都交代清楚;
        interrupted 任务可从列表取消 (三段式精确 kill 清理残留进程)。
        """
        orphans = [j for j in store.list_jobs(limit=500) if j["status"] == "running"]
        recovered = 0
        for job in orphans:
            pids = await self._container_pids(job["id"]) if job["kind"] == "lmp" else []
            if await self._transition(job["id"], "interrupted", None):
                recovered += 1
                note = (f"[workbench] 后端重启, 任务中断; 容器内进程仍在 (PID {', '.join(pids)}), "
                        "可从任务列表取消以终止" if pids
                        else "[workbench] 后端重启, 任务中断; 容器内进程已不存在, 结果可能不完整")
                await self._append_line(job["id"], note)
        if recovered:
            log.info("孤儿任务恢复: %d/%d 个 running 任务已标记 interrupted", recovered, len(orphans))
        return recovered

    async def cancel(self, job_id: str) -> dict | None:
        job = store.get(job_id)
        if job is None:
            return None
        if not await self._transition(job_id, "canceled", None):
            return store.get(job_id)  # 非运行态: 幂等返回
        self._pending = collections.deque(
            (j, c) for j, c in self._pending if j["id"] != job_id)
        self._canceled.add(job_id)
        proc = self._procs.get(job_id)
        if proc is not None and proc.returncode is None:
            try:
                proc.terminate()  # 杀掉 docker exec 客户端
            except ProcessLookupError:
                pass
        if job["kind"] == "lmp":
            await self._kill_container_process(job_id)
        await self._append_line(job_id, "[workbench] 任务已被用户取消")
        return store.get(job_id)

    async def _container_pids(self, job_id: str) -> list[str]:
        """容器内本任务的 LAMMPS 进程 PID 列表 (命令行含工作区路径)。"""
        try:
            r = await asyncio.to_thread(
                subprocess.run,
                ["docker", "exec", CONTAINER_NAME,
                 "pgrep", "-f", f"{_workspace_container(job_id)}/"],
                capture_output=True, text=True, timeout=8,
            )
        except Exception:
            return []
        return [t for t in r.stdout.split() if t.strip().isdigit()]

    async def _kill_container_process(self, job_id: str) -> None:
        """三段式终止容器内本任务进程, 全程不静默:
        SIGTERM → 验证 → 残留升级 SIGKILL → 仍残留则把警告写入任务日志 (WS 可见)。"""
        pattern = f"{_workspace_container(job_id)}/"

        async def _pkill(extra: list[str] | None = None) -> None:
            cmd = ["docker", "exec", CONTAINER_NAME, "pkill", *(extra or []), "-f", pattern]
            try:
                await asyncio.to_thread(subprocess.run, cmd, capture_output=True, timeout=8)
            except Exception as e:
                await self._append_line(job_id, f"[workbench] 警告: 容器内 pkill 执行失败: {e}")

        await _pkill()  # SIGTERM
        await asyncio.sleep(1.0)
        pids = await self._container_pids(job_id)
        if pids:
            await self._append_line(
                job_id, f"[workbench] SIGTERM 后容器内仍有进程 {pids}, 升级 SIGKILL")
            await _pkill(["-9"])
            await asyncio.sleep(0.5)
            pids = await self._container_pids(job_id)
            if pids:
                await self._append_line(
                    job_id,
                    f"[workbench] 警告: 容器内进程未能终止 (PID {', '.join(pids)}), "
                    f"请手动处理: docker exec {CONTAINER_NAME} kill -9 {' '.join(pids)}",
                )

    # ---- 日志 / thermo / 订阅 ----

    async def _append_line(self, job_id: str, line: str) -> None:
        job = store.get(job_id)
        if job is None:
            return
        with open(job["log_path"], "a", encoding="utf-8") as f:
            f.write(line + "\n")
        tail = self._tails.get(job_id)
        if tail is not None:
            tail.append(line)
        buf = self._thermo.get(job_id)
        if buf is not None and buf.feed(line):
            await self._broadcast(job_id, {"type": "thermo", "row": buf.rows[-1]})
        await self._broadcast(job_id, {"type": "log", "line": line})

    def log_tail(self, job_id: str, n: int = 300) -> list[str]:
        tail = self._tails.get(job_id)
        if tail is not None:
            return list(tail)[-n:]
        job = store.get(job_id)
        if job is None or not os.path.isfile(job["log_path"]):
            return []
        with open(job["log_path"], encoding="utf-8", errors="replace") as f:
            return f.read().splitlines()[-n:]

    def thermo_snapshot(self, job_id: str, limit: int | None = None) -> dict:
        self._ensure_thermo_replayed(job_id)
        buf = self._thermo.get(job_id)
        if buf is None:
            return {"columns": [], "rows": []}
        return buf.snapshot(limit)

    def _ensure_thermo_replayed(self, job_id: str) -> None:
        """后端重启后内存缓冲丢失: 终态 LAMMPS 任务首次访问时从日志文件回放重建。"""
        buf = self._thermo.get(job_id)
        if buf is not None and buf.replayed:
            return
        job = store.get(job_id)
        if job is None or job["kind"] != "lmp":
            return
        if job["status"] == "running":
            self._thermo.setdefault(job_id, thermo.ThermoBuffer())
            return
        # 终态: 从日志文件回放 (权威副本)
        buf = thermo.ThermoBuffer()
        buf.replayed = True
        log_path = job.get("log_path")
        if log_path and os.path.isfile(log_path):
            try:
                with open(log_path, encoding="utf-8", errors="replace") as f:
                    for line in f:
                        buf.feed(line.rstrip("\r\n"))
            except OSError:
                pass
        self._thermo[job_id] = buf

    def subscribe(self, job_id: str) -> asyncio.Queue:
        q: asyncio.Queue = asyncio.Queue(maxsize=2000)
        self._subs.setdefault(job_id, set()).add(q)
        return q

    def unsubscribe(self, job_id: str, q: asyncio.Queue) -> None:
        subs = self._subs.get(job_id)
        if subs is not None:
            subs.discard(q)

    async def _broadcast(self, job_id: str, payload: dict) -> None:
        for q in list(self._subs.get(job_id, ())):
            try:
                q.put_nowait(payload)
            except asyncio.QueueFull:
                pass  # 慢消费者丢帧, 日志文件是权威副本


manager = JobManager()

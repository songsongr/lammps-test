"""暂存-运行-回收统一执行契约 — CLI (entrypoints) 与 workbench (job_manager) 共用。

v1.8.5 引入 Backend 抽象 (common/backends/):
- stage_dependencies / lmp_command 这两个核心函数仍保留, 作为「默认 backend 的便捷封装」
- run_cli() 改为通过 get_backend() 拼装命令 — 切换 RemoteHPC 时不需要改这里
- 工作台 job_manager 也通过 runner.lmp_command(..., backend=None) 路径自动用 backend

staging: 把 .lmp + 依赖闭包 (include/read_data/read_restart + 项目顶层 *.data)
         拷入数据工作区 lammps-data-docker/jobs/<ws_id>/ (= 容器 /data/jobs/<ws_id>/)
command: backend.run_lmp_command(workspace_container(ws_id), script, omp)  ← Backend 协议
执行循环由调用方实现 (CLI 同步流式 / workbench 异步流式), 两者共享同一契约与取消语义。
"""
from __future__ import annotations

import os
import re

CONTAINER_NAME = "lammpsd"
LAMMPS_EXE = "/usr/bin/lmp_mpi"
CONTAINER_DATA_DIR = "/data"

_DEP_PAT = re.compile(r"^\s*(?:include|read_data|read_restart)\s+(\S+)", re.M)
_SCAN_SKIP_EXT = {".lammpstrj", ".dump", ".restart", ".png", ".jpg", ".jpeg",
                  ".xlsx", ".zip", ".gz", ".pdf"}
_MAX_SCAN_BYTES = 2_000_000
_MAX_DEP_DEPTH = 10


def workspace_host(data_host_dir: str, ws_id: str) -> str:
    """任务工作区 (宿主机视角): 数据目录下按工作区 id 隔离。"""
    return os.path.join(data_host_dir, "jobs", ws_id)


def workspace_container(ws_id: str) -> str:
    """LocalDocker 后端的容器内工作区路径 (=/data/jobs/<ws_id>)。
    注意: 这是为向后兼容保留的便捷函数 — 实际拼命令已走 backend.run_lmp_command。
    """
    return f"{CONTAINER_DATA_DIR}/jobs/{ws_id}"


def collect_deps(script_name: str, project_dir: str) -> tuple[list[str], list[str]]:
    """解析脚本的 include/read_data/read_restart 引用闭包。

    返回 (项目目录内存在且需暂存的相对路径, 引用了但不存在的相对路径)。
    仅扫描小文本文件; 引用按项目目录扁平解析 (v1 不支持子目录相对引用)。
    """
    present: list[str] = []
    missing: list[str] = []
    seen: set[str] = {script_name}
    queue: list[str] = [script_name]
    depth = 0
    while queue and depth < _MAX_DEP_DEPTH:
        rel = queue.pop(0)
        depth += 1
        path = os.path.join(project_dir, rel)
        if not os.path.isfile(path) or os.path.getsize(path) > _MAX_SCAN_BYTES:
            continue
        if os.path.splitext(path)[1].lower() in _SCAN_SKIP_EXT:
            continue
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        for ref in _DEP_PAT.findall(text):
            ref = os.path.normpath(ref)
            if ref in seen:
                continue
            seen.add(ref)
            if os.path.isfile(os.path.join(project_dir, ref)):
                present.append(ref)
                queue.append(ref)  # 传递闭包: 依赖的依赖
            elif ref not in missing:
                missing.append(ref)
    return present, missing


def stage_dependencies(project_dir: str, script: str, ws_host: str,
                       skip_script: bool = False) -> list[str]:
    """便捷函数: 直接调当前 backend 的 stage_dependencies (保持向后兼容)。

    v1.8.5 之前: 暂存逻辑 (脚本 + 依赖闭包 + 顶层 *.data 拷贝) 在本文件内;
    v1.8.5+: 委派给 Backend。真实拷贝逻辑在 LocalDockerBackend /
    RemoteHPCBackend.stage_dependencies, 闭包解析共用本文件的 collect_deps。
    """
    from common.backends import get_backend
    return get_backend().stage_dependencies(project_dir, script, ws_host,
                                             skip_script=skip_script)


def lmp_command(ws_container: str, script: str, omp_threads: int = 8) -> list[str]:
    """便捷函数: 当前 backend 拼出的 LAMMPS 命令 (默认 LocalDocker)。

    工作台 job_manager 与历史 CLI 都用这个; 不传 backend 走工厂单例 (默认 local_docker)。
    行为零变化: 与原 `docker exec -w <ws> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp N -in <ws>/<script>` 一致。
    """
    from common.backends import get_backend
    return get_backend().run_lmp_command(ws_container, script, omp_threads)


def run_cli(project_dir: str, script: str, omp_threads: int = 8) -> int:
    """CLI 同步执行: 暂存 → backend.run_lmp_command → 输出流式透传到本进程 stdout。

    与工作台同账本: 任务写入工作台任务库 (source=cli, 失败静默降级不影响 CLI 本身),
    输出 tee 到 workbench/data/jobs/<id>.log (详情页可回放)。
    """
    import subprocess
    import sys
    import uuid
    from datetime import datetime

    ws_id = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
    # 数据目录: 项目根下的 lammps-data-docker (与 workbench 同一约定)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_host = os.path.join(repo_root, "lammps-data-docker")
    ws_host = workspace_host(data_host, ws_id)
    missing = stage_dependencies(project_dir, script, ws_host)
    for ref in missing:
        if ref.startswith("__"):
            # RemoteHPC 特殊失败信号 (rsync 失败等); 仍打印但不让 stderr 阻塞
            print(f"[runner] 警告: {ref}", file=sys.stderr)
        else:
            print(f"[runner] 警告: 脚本引用的依赖不存在, 未暂存: {ref}", file=sys.stderr)
    print(f"[runner] 工作区: {ws_host}", file=sys.stderr)

    job_id = ws_id.replace("-", "")[:16]
    record = _cli_record(job_id, repo_root, project_dir, script, ws_host)
    log_file = None
    if record:
        try:
            log_file = open(record["_log_path"], "w", encoding="utf-8", errors="replace")
        except OSError:
            log_file = None

    # 工作区路径: 走当前 backend 的 workspace 拼装 (LocalDocker = 容器内路径)
    # 须传 ws_id (与宿主机 jobs/<ws_id> 目录名一致), 不是去横线的 job_id
    ws_backend = _ws_backend_for(ws_id)
    cmd = lmp_command(ws_backend, script, omp_threads)
    code = 130
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert proc.stdout is not None
        for raw in proc.stdout:
            line = raw.decode("utf-8", "replace")
            sys.stdout.write(line)
            sys.stdout.flush()
            if log_file:
                try:
                    log_file.write(line)
                    log_file.flush()
                except OSError:
                    pass
        code = proc.wait()
    except KeyboardInterrupt:
        print("[runner] 中断 — 终止 LAMMPS (按 backend 协议)", file=sys.stderr)
        proc.terminate()
        code = 130
    finally:
        if log_file:
            log_file.close()
        _cli_finish(job_id, code)  # Ctrl+C/崩溃也回写终态, 不留 running 尸账
    return code


def _ws_backend_for(ws_id: str) -> str:
    """Backend 视角的工作区路径 — LocalDocker 是容器内 /data/jobs/<ws_id>,
    RemoteHPC 是远程 ~/lammps/jobs/<ws_id> (后者暂未串到 CLI)。"""
    from common.backends import get_backend
    b = get_backend()
    if b.name == "remote_hpc":
        # RemoteHPC: 远程 HPC workdir + jobs/<ws_id>
        wd = getattr(b, "hpc_workdir", "~/lammps").rstrip("/")
        return f"{wd}/jobs/{ws_id}"
    # 默认 (LocalDocker): 容器内路径
    return workspace_container(ws_id)


def _cli_record(job_id: str, repo_root: str, project_dir: str,
                script: str, ws_host: str) -> dict | None:
    """把 CLI 任务登记进工作台任务库 (source=cli); store 不可用时静默跳过。"""
    import json
    from datetime import datetime

    try:
        from workbench.backend.app import store
        from workbench.backend.app.config import JOBS_LOG_DIR

        store.init()
        log_path = os.path.join(JOBS_LOG_DIR, f"{job_id}.log")
        fingerprint = {}
        sys_path = os.path.join(project_dir, "system.json")
        if os.path.isfile(sys_path):
            import hashlib
            with open(sys_path, "rb") as f:
                fingerprint["system_sha"] = hashlib.sha256(f.read()).hexdigest()[:16]
        # backend type 写入 fingerprint (v1.8.5 任务可比性扩展)
        try:
            from common.backends import get_backend
            fingerprint["backend"] = get_backend().name
        except Exception:
            pass
        job = {
            "id": job_id,
            "project_id": os.path.basename(os.path.normpath(project_dir)),
            "project_name": os.path.basename(os.path.normpath(project_dir)),
            "script": script,
            "kind": "lmp",
            "command": f"uv run run-sim (cli) {script}",
            "status": "running",
            "exit_code": None,
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "started_at": datetime.now().isoformat(timespec="seconds"),
            "finished_at": None,
            "log_path": log_path,
            "workspace": ws_host,
            "omp_threads": 8,
            "fingerprint": json.dumps(fingerprint, ensure_ascii=False) if fingerprint else None,
            "source": "cli",
        }
        store.insert(job)
        job["_log_path"] = log_path
        return job
    except Exception:
        return None


def _cli_finish(job_id: str, code: int) -> None:
    """CLI 任务终态回写 (静默降级)。"""
    try:
        from datetime import datetime

        from workbench.backend.app import store

        store.update(job_id, status="completed" if code == 0 else "failed",
                     exit_code=code, finished_at=datetime.now().isoformat(timespec="seconds"))
    except Exception:
        pass


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) < 2:
        print("用法: python -m common.runner <project_dir> <script> [--omp N]", file=sys.stderr)
        raise SystemExit(2)
    omp = 8
    if "--omp" in args:
        i = args.index("--omp")
        omp = int(args[i + 1])
        args = args[:i] + args[i + 2 :]
    raise SystemExit(run_cli(args[0], args[1], omp))
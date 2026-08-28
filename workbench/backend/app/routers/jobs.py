"""任务 API: 创建/列表/详情/取消/删除/产物 + WebSocket 实时日志。"""
import asyncio
import json
import os
import shutil
import threading

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from common.lammps_lint import lint_lammps_input

from ..config import ROOT, get_projects
from ..failure import analyze_failure
from ..job_manager import manager
from ..schemas import JobCreate, JobDetailOut, JobOut
from ..store import counts, delete as store_delete, get, list_jobs

router = APIRouter(prefix="/api")
# WebSocket 不吃 /api 前缀 (APIRouter prefix 对 websocket 同样生效),
# 单独挂在根路径 /ws/jobs/{id}, 与前端约定一致
ws_router = APIRouter()

_TEXT_PREVIEW_MAX = 256_000  # 文本预览上限 (bytes)
_FILE_LIST_MAX = 500


@router.post("/jobs", response_model=JobOut, status_code=201)
async def create_job(body: JobCreate) -> dict:
    # LAMMPS 任务发车前确定性 lint (errors 阻止发车 — 用代码强制替代 LLM 输入评审)
    if body.kind == "lmp":
        project = next((p for p in get_projects() if p["id"] == body.project_id), None)
        script_path = os.path.join(ROOT, project["dir"], body.script) if project else None
        if script_path and os.path.isfile(script_path):
            with open(script_path, encoding="utf-8", errors="replace") as f:
                lint = lint_lammps_input(f.read(), os.path.dirname(script_path))
            if lint["errors"]:
                raise HTTPException(
                    status_code=400,
                    detail="发车前 lint 未通过, 请先修复:\n" + "\n".join(lint["errors"]),
                )
    try:
        return await manager.start(body.project_id, body.script, body.kind, body.omp_threads)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/jobs/stats")
async def job_stats() -> dict:
    """放在 /{job_id} 之前注册, 避免被路径参数吞掉。"""
    return counts()


@router.get("/jobs", response_model=list[JobOut])
async def get_jobs() -> list[dict]:
    return list_jobs()


@router.get("/jobs/{job_id}", response_model=JobDetailOut)
async def job_detail(job_id: str) -> dict:
    job = get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    log_text = "\n".join(manager.log_tail(job_id, n=400))
    failure = None
    if job["status"] == "failed":
        failure = analyze_failure(job["kind"], job.get("exit_code"), log_text)
    thermo_snap = manager.thermo_snapshot(job_id, limit=500)
    equilibrium = None
    if job["kind"] == "lmp" and thermo_snap.get("rows"):
        from common.equilibrium import analyze_equilibrium

        equilibrium = analyze_equilibrium(thermo_snap)
    fingerprint = json.loads(job["fingerprint"]) if job.get("fingerprint") else None
    return {
        **job,
        "log_tail": manager.log_tail(job_id, n=300),
        "thermo": thermo_snap,
        "failure": failure,
        "equilibrium": equilibrium,
        "fingerprint": fingerprint,
    }


@router.post("/jobs/{job_id}/cancel", response_model=JobOut)
async def cancel_job(job_id: str) -> dict:
    job = get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    if job.get("source") == "cli" and job["status"] == "running":
        raise HTTPException(status_code=409,
                            detail="CLI 任务由终端进程持有, 请在其终端 Ctrl+C 取消 (工作台无进程句柄)")
    job2 = await manager.cancel(job_id)
    if job2 is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return job2


@router.delete("/jobs/{job_id}")
async def delete_job(job_id: str) -> dict:
    """删除终态任务及其全部产物 (工作区 + 日志 + 记录), 返回释放的字节数。"""
    job = get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    if job["status"] == "running":
        raise HTTPException(status_code=409, detail="运行中任务不可删除, 请先取消")

    # 安全兜底: 已取消的 LAMMPS 任务若容器内进程残留, 删文件会与写入竞争
    if job["kind"] == "lmp" and job.get("workspace"):
        pids = await manager._container_pids(job_id)
        if pids:
            raise HTTPException(status_code=409,
                                detail=f"容器内进程仍在运行 (PID {', '.join(pids)}), 无法删除")

    freed = 0
    if job.get("workspace") and os.path.isdir(job["workspace"]):
        for dirpath, _dirs, filenames in os.walk(job["workspace"]):
            for name in filenames:
                try:
                    freed += os.path.getsize(os.path.join(dirpath, name))
                except OSError:
                    pass
        shutil.rmtree(job["workspace"], ignore_errors=True)
    if job.get("log_path") and os.path.isfile(job["log_path"]):
        freed += os.path.getsize(job["log_path"])
        try:
            os.remove(job["log_path"])
        except OSError:
            pass
    store_delete(job_id)
    return {"deleted": True, "id": job_id, "freed_bytes": freed}


# ---- 轨迹统计在线分析 (z 分布 + MSD; 后台线程计算, 工作区缓存) ----

_analysis_state: dict[str, dict] = {}  # job_id -> {"status": "running"|"done"|"error", "error": str}
_analysis_lock = threading.Lock()


def _find_trajectory(root: str) -> str | None:
    """工作区里最大的 .lammpstrj 即分析对象 (dump 可能多文件)。"""
    candidates = []
    for dirpath, _dirs, filenames in os.walk(root):
        for name in filenames:
            if name.endswith((".lammpstrj", ".dump")):
                p = os.path.join(dirpath, name)
                candidates.append((os.path.getsize(p), p))
    return max(candidates)[1] if candidates else None


def _run_analysis(job_id: str, traj_path: str, cache_path: str) -> None:
    from common.traj_analysis import analyze_trajectory

    try:
        result = analyze_trajectory(traj_path)
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
        with _analysis_lock:
            _analysis_state[job_id] = {"status": "done"}
    except Exception as e:
        with _analysis_lock:
            _analysis_state[job_id] = {"status": "error", "error": str(e)}


@router.post("/jobs/{job_id}/analysis")
async def trigger_analysis(job_id: str) -> dict:
    """对任务工作区的最大轨迹触发统计计算 (后台线程; 结果缓存到工作区)。"""
    job, root = _workspace_or_404(job_id)
    if job["kind"] != "lmp":
        raise HTTPException(status_code=400, detail="仅 LAMMPS 任务支持轨迹分析")
    cache_path = os.path.join(root, "analysis_cache.json")
    if os.path.isfile(cache_path):
        return {"status": "done", "cached": True}
    with _analysis_lock:
        st = _analysis_state.get(job_id)
        if st and st["status"] == "running":
            return {"status": "running", "cached": False}
    traj = _find_trajectory(root)
    if traj is None:
        raise HTTPException(status_code=404, detail="工作区无轨迹文件 (.lammpstrj / .dump)")
    with _analysis_lock:
        _analysis_state[job_id] = {"status": "running"}
    threading.Thread(target=_run_analysis, args=(job_id, traj, cache_path), daemon=True).start()
    return {"status": "running", "cached": False}


@router.get("/jobs/{job_id}/analysis")
async def get_analysis(job_id: str) -> dict:
    job, root = _workspace_or_404(job_id)
    if job["kind"] != "lmp":
        raise HTTPException(status_code=400, detail="仅 LAMMPS 任务支持轨迹分析")
    cache_path = os.path.join(root, "analysis_cache.json")
    if os.path.isfile(cache_path):
        with open(cache_path, encoding="utf-8") as f:
            return {"status": "done", "result": json.load(f)}
    with _analysis_lock:
        st = _analysis_state.get(job_id, {}).copy()
    if st.get("status") == "error":
        return {"status": "error", "error": st.get("error", "分析失败")}
    if st.get("status") == "running":
        return {"status": "running"}
    # 无缓存且无内存状态 → 尝试直接同步判断是否有轨迹可算 (小轨迹同步算, 大轨迹提示触发)
    traj = _find_trajectory(root)
    if traj is None:
        return {"status": "none", "note": "工作区无轨迹文件"}
    size = os.path.getsize(traj)
    if size <= 8 * 1024 * 1024:  # 8MB 内同步算 (秒级)
        _run_analysis(job_id, traj, cache_path)
        if os.path.isfile(cache_path):
            with open(cache_path, encoding="utf-8") as f:
                return {"status": "done", "result": json.load(f)}
        with _analysis_lock:
            st = _analysis_state.get(job_id, {}).copy()
        return {"status": "error", "error": st.get("error", "分析失败")}
    return {"status": "idle", "note": f"轨迹 {size // 1024 // 1024} MB, 点「计算」后台分析"}


# ---- 产物文件浏览 ----

def _workspace_or_404(job_id: str) -> tuple[dict, str]:
    job = get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    root = job.get("workspace") or ""
    if not root or not os.path.isdir(root):
        raise HTTPException(status_code=404, detail="任务无工作区 (Python 任务或目录已清理)")
    return job, root


@router.get("/jobs/{job_id}/files")
async def job_files(job_id: str) -> dict:
    _, root = _workspace_or_404(job_id)
    files: list[dict] = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            try:
                st = os.stat(full)
            except OSError:
                continue
            files.append({
                "path": os.path.relpath(full, root).replace(os.sep, "/"),
                "size": st.st_size,
                "mtime": st.st_mtime,
            })
            if len(files) >= _FILE_LIST_MAX:
                break
        if len(files) >= _FILE_LIST_MAX:
            break
    files.sort(key=lambda f: f["path"])
    return {"files": files, "truncated": len(files) >= _FILE_LIST_MAX}


@router.get("/jobs/{job_id}/files/content")
async def job_file_content(job_id: str, path: str, download: bool = False):
    _, root = _workspace_or_404(job_id)
    root_real = os.path.realpath(root)
    full = os.path.realpath(os.path.join(root, path))
    if full != root_real and not full.startswith(root_real + os.sep):
        raise HTTPException(status_code=400, detail="非法路径")
    if not os.path.isfile(full):
        raise HTTPException(status_code=404, detail="文件不存在")
    if download:
        return FileResponse(full, filename=os.path.basename(full))
    size = os.path.getsize(full)
    if size > _TEXT_PREVIEW_MAX:
        raise HTTPException(status_code=413, detail="文件过大, 请下载后查看")
    try:
        with open(full, encoding="utf-8", errors="replace") as f:
            head = f.read(4096)
            text = head + f.read()
    except OSError as e:
        raise HTTPException(status_code=500, detail=f"读取失败: {e}")
    if "\x00" in text[:4096]:
        raise HTTPException(status_code=415, detail="二进制文件不支持预览, 请下载")
    return {"path": path, "size": size, "text": text}


# ---- WebSocket 实时日志 ----

@ws_router.websocket("/ws/jobs/{job_id}")
async def ws_job_logs(ws: WebSocket, job_id: str) -> None:
    await ws.accept()
    queue = manager.subscribe(job_id)
    try:
        # 先补发历史日志 / thermo 缓冲 / 当前状态快照, 再流式推送增量
        for line in manager.log_tail(job_id, n=500):
            await ws.send_json({"type": "log", "line": line})
        snap = manager.thermo_snapshot(job_id)
        if snap["columns"]:
            await ws.send_json({"type": "thermo", **snap})
        job = get(job_id)
        if job is not None:
            await ws.send_json({"type": "status", "status": job["status"],
                                "exit_code": job["exit_code"]})
        while True:
            try:
                payload = await asyncio.wait_for(queue.get(), timeout=15)
            except asyncio.TimeoutError:
                await ws.send_json({"type": "ping"})  # 心跳
            else:
                await ws.send_json(payload)
    except WebSocketDisconnect:
        pass
    finally:
        manager.unsubscribe(job_id, queue)

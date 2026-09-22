"""任务 API: 创建/列表/详情/取消/删除/产物 + WebSocket 实时日志。"""
import asyncio
import json
import os
import shutil
import threading

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

from common.lammps_lint import lint_lammps_input

from ..config import ROOT, get_projects
from ..failure import analyze_failure
from .. import store
from ..job_manager import get_project, manager
from ..schemas import JobCreate, JobDetailOut, JobOut, JobResumeOut
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


@router.get("/jobs/compare")
async def compare_jobs(ids: str) -> dict:
    """多任务 thermo 对比 (叠加图数据源): ids=逗号分隔, 最多 6 个。"""
    id_list = [s.strip() for s in ids.split(",") if s.strip()][:6]
    if not id_list:
        raise HTTPException(status_code=400, detail="ids 必填")
    out = []
    for jid in id_list:
        j = get(jid)
        if j is None:
            continue
        out.append({
            "id": jid,
            "script": j["script"],
            "project_name": j["project_name"],
            "status": j["status"],
            "batch": j.get("batch"),
            "thermo": manager.thermo_snapshot(jid, limit=500),
        })
    if not out:
        raise HTTPException(status_code=404, detail="未找到任何任务")
    return {"series": out}


@router.get("/jobs/compare-msd")
async def compare_msd(ids: str) -> dict:
    """读取最多六个任务的轨迹分析缓存，仅返回全原子 MSD 曲线。"""
    id_list = list(dict.fromkeys(s.strip() for s in ids.split(",") if s.strip()))[:6]
    if len(id_list) < 2:
        raise HTTPException(status_code=400, detail="至少选择 2 个任务")
    out = []
    for jid in id_list:
        job = get(jid)
        if job is None:
            out.append({"id": jid, "status": "missing", "note": "任务不存在"})
            continue
        entry = {"id": jid, "script": job["script"],
                 "project_name": job["project_name"], "status": "idle"}
        root = job.get("workspace") or ""
        if job["kind"] != "lmp" or not os.path.isdir(root):
            entry.update(status="none", note="无 LAMMPS 任务工作区")
        else:
            cache_path = os.path.join(root, "analysis_cache.json")
            if os.path.isfile(cache_path):
                try:
                    with open(cache_path, encoding="utf-8") as f:
                        analysis = json.load(f)
                    all_msd = next((m for m in analysis["msd"] if m["type"] == "all"), None)
                    if all_msd and all_msd.get("points"):
                        entry.update(status="done", msd=all_msd)
                    else:
                        entry.update(status="none", note="缓存中无全原子 MSD 曲线")
                except (OSError, ValueError, KeyError, TypeError) as exc:
                    entry.update(status="error", note=f"分析缓存读取失败: {exc}")
            else:
                with _analysis_lock:
                    state = _analysis_state.get(jid, {}).copy()
                if state.get("status") == "running":
                    entry["status"] = "running"
                elif state.get("status") == "error":
                    entry.update(status="error", note=state.get("error", "分析失败"))
                elif _find_trajectory(root) is None:
                    entry.update(status="none", note="工作区无轨迹文件")
        out.append(entry)
    return {"series": out}


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


@router.get("/jobs/{job_id}/export")
async def export_job(job_id: str) -> StreamingResponse:
    """单任务溯源包导出 (roadmap #6): 记录+指纹+脚本+体系快照+日志尾部 → zip 下载。"""
    from ..provenance import build_provenance_zip

    job = get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    project_dir = None
    project = get_project(job["project_id"])
    if project:
        project_dir = os.path.join(ROOT, project["dir"])
    log_text = None
    if job.get("log_path") and os.path.isfile(job["log_path"]):
        log_text = "\n".join(manager.log_tail(job_id, n=400))
    data, _skipped = build_provenance_zip(job, project_dir, log_text)
    filename = f"provenance_{job_id}_{job.get('project_id', 'job')}.zip"
    return StreamingResponse(
        iter([data]),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


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
    manager.cleanup_memory(job_id)
    with _analysis_lock:
        _analysis_state.pop(job_id, None)
    return {"deleted": True, "id": job_id, "freed_bytes": freed}


# ---- 轨迹统计在线分析 (z 分布 + MSD; 后台线程计算, 工作区缓存) ----

_analysis_state: dict[str, dict] = {}  # job_id -> {"status": "running"|"done"|"error", "error": str}
_analysis_lock = threading.Lock()
NL = chr(10)  # 换行 (避免 heredoc 转义问题)


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

    # 推断 system.data 路径 (与轨迹同目录, 用于给 type 加元素标签)
    sys_data = os.path.join(os.path.dirname(os.path.abspath(traj_path)), "system.data")
    sys_arg = sys_data if os.path.isfile(sys_data) else None
    try:
        result = analyze_trajectory(traj_path, system_data_path=sys_arg)
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


# ---- 检查点续跑 (RadonPy 思想: 失败/完成后从最新 restart 继续) ----

@router.get("/jobs/{job_id}/restarts")
async def list_restarts(job_id: str) -> dict:
    job, root = _workspace_or_404(job_id)
    if job["kind"] != "lmp":
        raise HTTPException(status_code=400, detail="仅 LAMMPS 任务有检查点")
    items = []
    for name in sorted(os.listdir(root)):
        if name.endswith(".restart"):
            p = os.path.join(root, name)
            items.append({"name": name, "size": os.path.getsize(p),
                          "mtime": os.path.getmtime(p)})
    items.sort(key=lambda x: x["mtime"], reverse=True)
    return {"restarts": items}


_RESUME_REBUILD_PREFIXES = ("fix ", "kspace_style", "special_bonds")
    # read_restart 恢复体系/力场系数, 但不保存 fix 定义与 kspace 设置 — 需从原脚本重建


def _extract_fix_lines(run_script_path: str) -> list[str]:
    """从原脚本提取续跑需重建的行 (fix / kspace_style / special_bonds)。"""
    fixes = []
    try:
        with open(run_script_path, encoding="utf-8", errors="replace") as f:
            for line in f:
                s = line.split("#")[0].strip()
                low = s.lower()
                if any(low.startswith(p) for p in _RESUME_REBUILD_PREFIXES):
                    fixes.append(s)
    except OSError:
        pass
    return fixes


class ResumeRequest(BaseModel):
    steps: int = 50000
    omp_threads: int = 8


@router.post("/jobs/{job_id}/resume", response_model=JobResumeOut, status_code=201)
async def resume_job(job_id: str, body: ResumeRequest) -> dict:
    """从任务工作区最新 restart 生成续跑脚本并发起新任务。

    read_restart 自包含体系与力场设置; fix 定义从原脚本提取重建 (restart 不保存 fix)。
    """
    from ..job_manager import get_project, manager as mgr

    src_job, root = _workspace_or_404(job_id)
    if src_job["kind"] != "lmp":
        raise HTTPException(status_code=400, detail="仅 LAMMPS 任务支持续跑")
    restarts = [n for n in sorted(os.listdir(root)) if n.endswith(".restart")]
    if not restarts:
        raise HTTPException(status_code=404, detail="工作区无 .restart 检查点 (模板需含 write_restart)")
    mtime = {n: os.path.getmtime(os.path.join(root, n)) for n in restarts}
    latest = max(restarts, key=lambda n: mtime[n])
    src_project = get_project(src_job["project_id"])
    if src_project is None:
        raise HTTPException(status_code=404, detail="原项目不存在")

    fix_lines = _extract_fix_lines(os.path.join(ROOT, src_project["dir"], src_job["script"]))
    # 检查点在源工作区 — 用容器内绝对路径跨工作区引用 (同一 /data 挂载)
    src_ws_container = f"/data/jobs/{job_id}"
    resume_lines = [
        f"# [generated] 检查点续跑: 源任务 {job_id} · 检查点 {latest} · 继续 {body.steps} 步",
        f"# fix 定义重建自原脚本 (restart 不保存 fix); 力场/体系由 read_restart 恢复",
        f"read_restart        {src_ws_container}/{latest}",
        "thermo_style        custom step temp press density etotal",
        "thermo_modify       lost ignore flush yes",
        "thermo              500",
    ]
    resume_lines += fix_lines
    resume_lines += [
        f"run                 {body.steps}",
        f"write_restart       checkpoint_resume.restart",
        'print "=== RESUME DONE ==="',
    ]
    script_text = NL.join(resume_lines) + NL

    fingerprint_add = {"resumed_from": job_id, "restart": latest}
    try:
        prev = json.loads(src_job.get("fingerprint") or "{}")
        prev.update(fingerprint_add)
        fingerprint_add = prev
    except Exception:
        pass

    job = await mgr.start(src_job["project_id"], "resume.in", "lmp",
                          body.omp_threads, script_text=script_text)
    # 把续跑溯源写进指纹
    fp = json.loads(job["fingerprint"] or "{}") if job.get("fingerprint") else {}
    fp.update(fingerprint_add)
    store.update(job["id"], fingerprint=json.dumps(fp, ensure_ascii=False))
    return {**store.get(job["id"]), "source_restart": latest}


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

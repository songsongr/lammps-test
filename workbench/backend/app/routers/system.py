"""系统健康: docker/容器状态 (带 3s 缓存, 供前端轮询) + 工作台进程受控退出。"""
import asyncio
import logging
import platform
import time

from fastapi import APIRouter, HTTPException

from .. import store
from ..docker_env import docker_info, kill_lmp_processes, lmp_process_count

log = logging.getLogger(__name__)

router = APIRouter(prefix="/api")

_cache = {"t": 0.0, "value": None}


@router.get("/health")
async def health() -> dict:
    now = time.time()
    if _cache["value"] is None or now - _cache["t"] > 3:
        _cache["value"] = await asyncio.to_thread(docker_info)
        _cache["t"] = now
    return {
        "ok": True,
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "python": platform.python_version(),
        "docker": _cache["value"],
    }


def plan_shutdown(active_jobs: list[dict], lmp_processes: int | None) -> dict:
    """结束工作台前的决策 (纯函数, 供单测)。

    - 存在运行中任务 → blocked: 后端互锁, 结束进程会让任务失控且无地面真相可查
    - 否则 → shutdown: 容器内残留的 LAMMPS 进程 (孤儿) 一并清理
    """
    if active_jobs:
        return {"action": "blocked", "jobs": active_jobs}
    return {"action": "shutdown", "clean_processes": lmp_processes or 0}


@router.post("/workbench/shutdown")
async def shutdown_workbench() -> dict:
    """受控退出工作台后端进程 (仪表盘「结束工作台进程」)。

    返回 200 {shutting_down, orphan_processes_cleaned, residual_after_clean};
    有运行中任务时返回 409 {detail: {code: active_jobs, message, jobs: [...]}}。
    """
    active = [j for j in store.list_jobs(limit=500) if j["status"] == "running"]
    procs = await asyncio.to_thread(lmp_process_count)
    plan = plan_shutdown(active, procs)
    if plan["action"] == "blocked":
        raise HTTPException(status_code=409, detail={
            "code": "active_jobs",
            "message": f"有 {len(active)} 个任务仍在运行, 结束工作台会使其失控, 请先取消",
            "jobs": [{"id": j["id"], "project_name": j.get("project_name"),
                      "script": j.get("script")} for j in active],
        })
    residual = None
    if plan["clean_processes"] > 0:
        residual = await asyncio.to_thread(kill_lmp_processes)
        log.warning("工作台退出前清理容器内 LAMMPS 孤儿进程: 残余 %s", residual)
    _schedule_exit()
    return {
        "shutting_down": True,
        "orphan_processes_cleaned": plan["clean_processes"],
        "residual_after_clean": residual,
    }


def _schedule_exit() -> None:
    """响应返回后优雅退出; 延迟窗口内若有新任务启动则放弃退出 (竞态互锁)。

    退出路径: uvicorn 运行期间在主线程安装了 SIGTERM 处理器 (Server.handle_exit),
    检测到它后 raise_signal 触发优雅停机 — 等价于 Ctrl+C, 跨平台可用
    (Windows 上 os.kill(SIGTERM) 是硬杀, 不能用)。非 uvicorn 环境直接跳过。
    """
    import signal

    def _do_exit() -> None:
        active = [j["id"] for j in store.list_jobs(limit=50) if j["status"] == "running"]
        if active:
            log.warning("退出前检测到新启动的任务 %s, 放弃结束工作台", active)
            return
        handler = signal.getsignal(signal.SIGTERM)
        if getattr(handler, "__qualname__", "") != "Server.handle_exit":
            log.warning("未检测到 uvicorn 信号处理器, 跳过进程退出 (测试/嵌入式运行)")
            return
        log.warning("工作台进程受控退出")
        signal.raise_signal(signal.SIGTERM)

    asyncio.get_running_loop().call_later(0.5, _do_exit)

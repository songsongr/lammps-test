"""系统健康: docker/容器状态 (带 3s 缓存, 供前端轮询) + 工作台进程受控退出 + 后端配置。

v1.8.5 新增执行后端抽象 (Backend): /api/backend 系列路由提供
- GET  /api/backend           当前配置 + 当前 backend 的 info() 探测结果
- GET  /api/backend/list      所有已注册 backend 列表 (供前端配置抽屉下拉)
- PUT  /api/backend           切换 backend (type + type-specific kwargs)
- POST /api/backend/test      连通性测试 (不持久化)
/api/health 在原 docker 字段基础上加 backend.{type,name,status,action_needed}。
"""
import asyncio
import logging
import platform
import time

from fastapi import APIRouter, HTTPException

from common.backends import (configure_backend, get_backend, list_backends,
                              register_backend as _register,
                              reset_backend_cache, get_backend_config,
                              backend_config_path)
# 触发 backend 注册表填充 (LocalDockerBackend / RemoteHPCBackend 在模块底部自注册)
from common.backends import local_docker  # noqa: F401  (副作用: register_backend)
from common.backends import remote_hpc  # noqa: F401  (副作用: register_backend)

from .. import store
from ..docker_env import (
    container_metrics, docker_info, kill_lmp_processes, lmp_process_count,
    start_container,
)

log = logging.getLogger(__name__)

router = APIRouter(prefix="/api")

_cache = {"t": 0.0, "value": None}


@router.get("/health")
async def health() -> dict:
    """健康检查: 兼容原结构 (docker 字段不变) + 新增 backend.{type,name,status,action_needed}。
    仪表盘/JobDetail 仍读 docker 字段; 抽屉读 backend 字段。"""
    now = time.time()
    if _cache["value"] is None or now - _cache["t"] > 3:
        _cache["value"] = await asyncio.to_thread(docker_info)
        _cache["t"] = now
    backend_info = await asyncio.to_thread(get_backend().info)
    return {
        "ok": True,
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "python": platform.python_version(),
        "docker": _cache["value"],
        "backend": {
            "type": backend_info.get("type"),
            "name": backend_info.get("name"),
            "status": backend_info.get("status"),
            "action_needed": backend_info.get("action_needed"),
            "available": bool(backend_info.get("available")),
        },
    }


@router.get("/docker/metrics")
async def docker_metrics() -> dict:
    """容器资源监测 (CPU% / 内存 / 数据目录大小) + 5 分钟趋势 ring buffer。"""
    return await asyncio.to_thread(container_metrics)


@router.post("/docker/start")
async def docker_start() -> dict:
    """一键启动 lammpsd 容器 (容器停止时); 不影响已运行容器。"""
    return await asyncio.to_thread(start_container)


# ---- v1.8.5: 执行后端配置 ----

@router.get("/backend")
async def backend_get() -> dict:
    """当前 backend 配置 + 探测结果 (前端配置抽屉展示 + 仪表盘状态卡)。"""
    cfg = get_backend_config()
    info = await asyncio.to_thread(get_backend().info)
    return {
        "config_path": backend_config_path(),
        "config": cfg,
        "info": dict(info),
    }


@router.get("/backend/list")
async def backend_list() -> dict:
    """列出所有已注册 backend 的探活摘要 (前端抽屉下拉)。"""
    rows = await asyncio.to_thread(list_backends)
    return {"backends": rows}


@router.put("/backend")
async def backend_put(body: dict) -> dict:
    """切换 backend (持久化到 backend.json, 清掉进程内单例)。

    body = {"type": "local_docker" | "remote_hpc", ...type-specific-kwargs}

    校验: type 必须在已注册列表; type-specific 字段最小集 (RemoteHPC 必填 ssh_host/user)。
    切换后立即返回新 backend 的 info() (前端可同步显示状态)。
    """
    type_name = body.get("type")
    if not type_name:
        raise HTTPException(status_code=400, detail={
            "code": "missing_type", "message": "请求体须含 type 字段",
        })
    # 校验 kwargs: 仅透传已知字段, 避免误存敏感数据
    allowed_extra = {"ssh_host", "ssh_user", "ssh_key_path", "ssh_port",
                     "hpc_workdir", "hpc_sbatch_template", "hpc_modules"}
    kwargs = {k: v for k, v in body.items() if k != "type" and k in allowed_extra}
    try:
        cfg = configure_backend(type_name, **kwargs)
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"code": "unknown_backend", "message": str(e)})
    info = await asyncio.to_thread(get_backend().info)
    return {"config": cfg, "info": dict(info)}


@router.post("/backend/test")
async def backend_test(body: dict | None = None) -> dict:
    """连通性测试 — 不持久化, 仅调用指定 backend 的 info() 返回。

    body: {"type": "remote_hpc", "ssh_host": "...", "ssh_user": "...", ...}
          type 可选, 不传则用当前 backend。
    """
    body = body or {}
    type_name = body.get("type")
    if type_name and type_name != get_backend().name:
        # 临时构造 backend 实例 (不持久化) 用于测试
        from common.backends.local_docker import LocalDockerBackend
        from common.backends.remote_hpc import RemoteHPCBackend
        if type_name == "local_docker":
            inst = LocalDockerBackend()
        elif type_name == "remote_hpc":
            inst = RemoteHPCBackend(
                ssh_host=body.get("ssh_host"),
                ssh_user=body.get("ssh_user"),
                ssh_key_path=body.get("ssh_key_path"),
                hpc_workdir=body.get("hpc_workdir"),
                hpc_modules=body.get("hpc_modules"),
            )
        else:
            raise HTTPException(status_code=400, detail={
                "code": "unknown_backend", "message": f"未知 backend 类型: {type_name}",
            })
    else:
        inst = get_backend()
    info = await asyncio.to_thread(inst.info)
    return {"info": dict(info)}


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
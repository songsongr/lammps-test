"""执行后端抽象基类 + 工厂 (v1.8.5)。

执行契约:
- info(): 探测后端可用性 (类比 docker_info)
- stage_dependencies(...): 把脚本 + 依赖拷入工作区 (类比 stage_dependencies)
- run_lmp_command(...): 拼装 LAMMPS 启动命令 (类比 lmp_command)
- lmp_process_count(): 实时 LMP 进程数 (用于工作台仪表盘与退出清理)
- fingerprint(): 镜像/版本指纹 (任务可比性)
- start(): 一键启动/连通性修复 (类比 start_container)

工作目录的"容器路径 ↔ 宿主机路径"映射由各 backend 内部处理, runner 只接收
抽象路径字符串 — LocalDocker 用的是 /data/jobs/<id> 这类容器内路径;
RemoteHPC 用的是 ~/jobs/<id> 这类远程 HPC 路径。
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Protocol, runtime_checkable


class BackendInfo(dict):
    """后端探测结果的薄包装 — 字段:
    - type: "local_docker" | "remote_hpc"
    - name: 用户可读名 ("Local Docker" / "Remote HPC (sbatch)")
    - available: bool — 后端是否可执行任务
    - status: "running" | "stopped" | "unreachable" | "configured" | "unconfigured"
    - action_needed: "none" | "start_container" | "start_docker" | "no_op" | "unavailable"
    - details: 自由 dict (容器状态 / ssh 连通性 / 远程环境指纹 等)
    """


class BackendStartResult(dict):
    """一键启动的结果 (类比 start_container 的返回结构): 字段
    - ok: bool
    - stage: "container_started" | "daemon_unreachable" | "docker_missing" |
             "timeout" | "failed" | "no_op" | "unreachable" | "configured"
    - message: str (用户可读, 前端 message.* 直接展示)
    - hint_url: str | None
    """


@runtime_checkable
class Backend(Protocol):
    """执行后端抽象 — 任何后端 (本地 Docker / 远程 HPC / 远程 Docker) 都实现这套接口。

    不强制继承 (Protocol + runtime_checkable), 因为 RemoteHPC 早期版本可能跳脱个别方法;
    但所有方法名/签名稳定, runner/工作台只通过该接口调用。
    """

    # 类属性 (具体实现须赋值)
    name: str  # "local_docker" / "remote_hpc"

    def info(self) -> BackendInfo:
        """探测后端状态; 调用方应放线程池/缓存结果。"""
        ...

    def stage_dependencies(self, project_dir: str, script: str,
                           ws_host: str, *, skip_script: bool = False) -> list[str]:
        """把脚本 + 依赖闭包 + 顶层 *.data 暂存到工作区, 返回缺失依赖列表。
        调用方负责创建目录与向用户呈现缺失告警。"""
        ...

    def run_lmp_command(self, ws_backend: str, script: str,
                        omp_threads: int = 8) -> list[str]:
        """拼装 LAMMPS 启动命令 (与 Backend.stage_dependencies 配合使用)。

        ws_backend: 后端视角的工作目录 (LocalDocker 是容器内路径 /data/jobs/<id>;
                    RemoteHPC 是远程 HPC 路径 ~/jobs/<id>)。
        返回完整 argv list — 工作台 job_manager 与 CLI runner 直接 asyncio/subprocess 执行。
        """
        ...

    def lmp_process_count(self) -> int | None:
        """实时 LMP 进程数; 探测失败返回 None (未知, 不猜 0)。

        对 RemoteHPC 是近似 (squeue 计数, 真实 LMP 进程在 compute node 上拿不到)。
        """
        ...

    def fingerprint(self) -> dict | None:
        """镜像/版本指纹 (任务可比性); 拿不到返回 None 不阻塞。"""
        ...

    def start(self) -> BackendStartResult:
        """一键启动/连通性修复; 不可能启动的 backend (RemoteHPC) 返回 stage="no_op"。"""
        ...


# ---- 配置 + 工厂 ----

# 持久化路径 (与任务库平级, gitignore): workbench/data/backend.json
_BACKEND_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "workbench", "data", "backend.json",
)

# 后端类型 → 实现类的延迟注册表 (避免 import-time 循环, 也不强制 RemoteHPC 必须装好)
_REGISTRY: dict[str, type] = {}

# 进程内单例缓存 (info() / 工厂共用; configure_backend() / reset_backend_cache() 时清掉)
_singleton: dict[str, Any] = {"type": None, "instance": None}


def register_backend(type_name: str, cls: type) -> None:
    """后端实现类注册 (调用方在模块底部 register_backend(<name>, <class>))。"""
    _REGISTRY[type_name] = cls


def get_backend_config() -> dict:
    """读 workbench/data/backend.json; 文件不存在返回默认 local_docker。"""
    if not os.path.isfile(_BACKEND_CONFIG_PATH):
        return {"type": "local_docker"}
    try:
        with open(_BACKEND_CONFIG_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        # 配置损坏: 退到默认 (避免发车失败); 由 configure_backend 重新写入覆盖
        return {"type": "local_docker"}


def configure_backend(type_name: str, **kwargs: Any) -> dict:
    """持久化后端配置到 backend.json 并清掉进程内缓存。

    type_name: "local_docker" / "remote_hpc"
    kwargs:    type-specific 字段 (ssh_host / hpc_workdir 等, 仅 RemoteHPC 用)

    返回完整新配置 (含持久化后的 type + kwargs)。
    抛 ValueError 当 type_name 未注册时 (用户写错或拼写错误)。
    """
    _ensure_builtins_registered()
    if type_name not in _REGISTRY:
        raise ValueError(f"未知后端类型: {type_name}; 已注册: {sorted(_REGISTRY)}")
    cfg = {"type": type_name, **kwargs}
    Path(_BACKEND_CONFIG_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(_BACKEND_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    reset_backend_cache()
    return cfg


def reset_backend_cache() -> None:
    """清掉 get_backend() 进程内单例 (配置变更后必调)。"""
    _singleton["type"] = None
    _singleton["instance"] = None


def _ensure_builtins_registered() -> None:
    """内置 backend 实现懒注册 (import 即完成 register_backend 副作用)。

    CLI 路径 (common.runner.run_cli) 不经过 workbench routers, 注册表必须自举;
    import 幂等 (sys.modules 缓存), workbench 侧先导入也无害。
    """
    from . import local_docker, remote_hpc  # noqa: F401


def get_backend() -> Backend:
    """工厂: 读 backend.json 的 type 字段, 返回注册表中对应 Backend 实例 (单例)。

    未配置 (backend.json 不存在) → 默认 LocalDockerBackend (零行为变化)。
    单例缓存到 configure_backend() 时清掉。
    """
    cfg = get_backend_config()
    type_name = cfg.get("type", "local_docker")
    if _singleton["type"] == type_name and _singleton["instance"] is not None:
        return _singleton["instance"]
    _ensure_builtins_registered()
    if type_name not in _REGISTRY:
        # 配置指了未注册的 backend (旧版本残留 / 用户手改 JSON 写错):
        # 退到 LocalDocker, 但日志可见 (调用方常在 asyncio.to_thread, 容忍异常路径)
        type_name = "local_docker"
    cls = _REGISTRY[type_name]
    # 实例化时把除 type 外的所有字段当作 backend 配置传入 (LocalDocker 忽略, RemoteHPC 用)
    backend_kwargs = {k: v for k, v in cfg.items() if k != "type"}
    inst = cls(**backend_kwargs)
    _singleton["type"] = type_name
    _singleton["instance"] = inst
    return inst


def backend_config_path() -> str:
    """暴露给工作台路由层 (前端配置抽屉展示路径用)。"""
    return _BACKEND_CONFIG_PATH


def list_backends() -> list[dict]:
    """列出所有已注册 backend (供前端 /api/backend GET)。"""
    _ensure_builtins_registered()
    out = []
    for type_name, cls in sorted(_REGISTRY.items()):
        try:
            inst = cls()  # 默认构造探活
            info = inst.info()
            out.append({
                "type": type_name,
                "name": getattr(cls, "label", type_name),
                "status": info.get("status"),
                "action_needed": info.get("action_needed"),
                "available": bool(info.get("available")),
            })
        except Exception as e:  # 探活失败也要列出 (标记为 unavailable)
            out.append({
                "type": type_name,
                "name": getattr(cls, "label", type_name),
                "status": "unavailable",
                "action_needed": "unavailable",
                "available": False,
                "error": str(e),
            })
    return out
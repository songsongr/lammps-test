"""执行后端抽象 (v1.8.5): LocalDocker / RemoteHPC。

执行契约分层:
- Backend (本包): 抽象接口 — 探测 / 暂存 / 拼命令 / 启停 / 指纹
- common/runner.py: 任务编排 (暂存-运行-回收) — 拿到一个 Backend, 用其接口拼装
- workbench/backend/app/docker_env.py: 向后兼容的重新导出层
- workbench/backend/app/routers/system.py: 把 backend 选择暴露为 /api/backend*

设计原则:
- 抽象在 common 层 (CLI runner 也用同一抽象)
- 零回归: LocalDockerBackend 100% 兼容现有 docker exec 行为
- 配置驱动: backend 选择走 JSON 持久化 + 运行时读
"""
from __future__ import annotations

from .base import (Backend, BackendInfo, BackendStartResult, backend_config_path,
                    configure_backend, get_backend, get_backend_config,
                    list_backends, register_backend, reset_backend_cache)

__all__ = [
    "Backend",
    "BackendInfo",
    "BackendStartResult",
    "get_backend",
    "configure_backend",
    "reset_backend_cache",
    "get_backend_config",
    "list_backends",
    "register_backend",
    "backend_config_path",
]
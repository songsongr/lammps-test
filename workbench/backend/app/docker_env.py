"""Docker 环境探测 — 重新导出层 (v1.8.5)。

历史: 实现 (docker_info / start_container / lmp_process_count / container_fingerprint /
container_metrics / kill_lmp_processes) 都搬到了 common/backends/local_docker.py。
本模块只做向后兼容的重新导出, 旧调用方零修改:
  workbench/backend/app/docker_env.py: docker_info(), start_container(), ...
  → common/backends/local_docker.py: 同名函数

`docker_info()` 是模块级函数, 不是方法 — 我们用一个共享的 LocalDockerBackend 实例
来承载缓存 (metrics / fingerprint), 这样进程内缓存行为保持一致。
"""
from __future__ import annotations

from common.backends.local_docker import (  # noqa: F401  (模块级 API)
    LocalDockerBackend,
    _container_fingerprint,
    _container_metrics,
    _dir_size_bytes,
    _docker_info,
    _kill_lmp_processes,
    _lmp_process_count,
    _parse_mem_bytes,
    _start_container,
)

# 共享实例 — 进程内唯一, 缓存 (metrics ring buffer / fingerprint TTL) 与原实现一致
_shared: LocalDockerBackend | None = None


def _shared_backend() -> LocalDockerBackend:
    global _shared
    if _shared is None:
        _shared = LocalDockerBackend()
    return _shared


def docker_info() -> dict:
    """探测 docker 可用性 + 容器状态; 返回 dict (含 status / action_needed)。
    模块级函数, 向后兼容 (旧调用方: from .docker_env import docker_info)。
    """
    b = _shared_backend()
    return _docker_info(
        b.container_name, b.container_data_dir, b.data_host_dir,
        lmp_count_fn=lambda: b.lmp_process_count(),
    )


def lmp_process_count() -> int | None:
    return _lmp_process_count(_shared_backend().container_name)


def kill_lmp_processes() -> int | None:
    return _kill_lmp_processes(_shared_backend().container_name)


def container_metrics() -> dict:
    b = _shared_backend()
    return _container_metrics(b.container_name, b.data_host_dir)


def start_container() -> dict:
    return _start_container(_shared_backend().container_name)


def container_fingerprint() -> dict | None:
    return _container_fingerprint(_shared_backend().container_name)


# ---- 模块级常量 (向后兼容, 旧调用方偶有 from .docker_env import CONTAINER_NAME) ----
CONTAINER_NAME = "lammpsd"  # 默认; 实际值由 LocalDockerBackend 从 config 读


__all__ = [
    "docker_info", "lmp_process_count", "kill_lmp_processes",
    "container_metrics", "start_container", "container_fingerprint",
    "_parse_mem_bytes", "_dir_size_bytes",  # 私有工具 (tests 引用)
    "CONTAINER_NAME",
]
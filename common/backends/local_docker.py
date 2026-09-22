"""LocalDockerBackend — v1.8.5 之前的「docker exec lammpsd ...」封装成 Backend 协议。

零行为变化:
- 拼出的命令仍为 `docker exec -w <容器工作区> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp N -in <容器内绝对路径>/<script>`
- info() 返回结构与 workbench/backend/app/docker_env.docker_info() 完全兼容
  (前端 docker 字段不变, 新增 backend.{type,name,status,action_needed})
- start() 返回结构与原 start_container() 完全兼容

模块内私有函数是从 workbench/backend/app/docker_env.py 原样搬运的;
workbench/backend/app/docker_env.py 改为重新导出, 保持 API 兼容。
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from typing import Any

from .base import BackendInfo, BackendStartResult, register_backend

# ---- 兼容常量 (与 workbench/backend/app/config.py 同步, 由调用方构造时覆盖) ----
DEFAULT_CONTAINER_NAME = "lammpsd"
DEFAULT_LAMMPS_EXE = "/usr/bin/lmp_mpi"
DEFAULT_CONTAINER_DATA_DIR = "/data"


class LocalDockerBackend:
    """本地 Docker 后端 (现状)。"""

    name: str = "local_docker"
    label: str = "Local Docker"

    def __init__(self, container_name: str | None = None,
                 container_data_dir: str | None = None,
                 lam_mps_exe: str | None = None,
                 data_host_dir: str | None = None) -> None:
        # 优先级: 显式传入 > workbench/backend/app/config.py (向后兼容) > 默认
        self.container_name = container_name or _default("CONTAINER_NAME", DEFAULT_CONTAINER_NAME)
        self.container_data_dir = container_data_dir or _default("CONTAINER_DATA_DIR", DEFAULT_CONTAINER_DATA_DIR)
        self.lmp_exe = lam_mps_exe or _default("LAMMPS_EXE", DEFAULT_LAMMPS_EXE)
        self.data_host_dir = data_host_dir or _default("LAMMPS_DATA_HOST_DIR", None)

    # ---- Backend 协议 ----

    def info(self) -> BackendInfo:
        return _docker_info(self.container_name, self.container_data_dir, self.data_host_dir,
                              lmp_count_fn=lambda: self.lmp_process_count())

    def stage_dependencies(self, project_dir: str, script: str,
                           ws_host: str, *, skip_script: bool = False) -> list[str]:
        """暂存脚本 + 依赖闭包 + 顶层 *.data 到 ws_host (本地 copy2, 无 rsync)。

        闭包解析与 RemoteHPC 同套逻辑 (common.runner.collect_deps) — 复用避免漂移。
        v1.8.5 曾在此错误地委托回 common.runner.stage_dependencies (后者又委托回
        backend) → 无限互递归; CLI 侧当时被 get_backend 未注册的 KeyError 掩盖。
        """
        import glob
        import shutil

        from common.runner import collect_deps

        os.makedirs(ws_host, exist_ok=True)
        deps, missing = collect_deps(script, project_dir)
        copies = ([] if skip_script else [script]) + deps
        for p in glob.glob(os.path.join(project_dir, "*.data")):
            name = os.path.basename(p)
            if name not in copies:
                copies.append(name)
        for rel in copies:
            shutil.copy2(os.path.join(project_dir, rel), os.path.join(ws_host, rel))
        return missing

    def run_lmp_command(self, ws_backend: str, script: str,
                        omp_threads: int = 8) -> list[str]:
        """拼装 docker exec 命令 (与原 common/runner.lmp_command 等价)。"""
        return [
            "docker", "exec", "-w", ws_backend, self.container_name,
            self.lmp_exe, "-sf", "omp", "-pk", "omp", str(omp_threads),
            "-in", f"{ws_backend}/{script}",
        ]

    def lmp_process_count(self) -> int | None:
        return _lmp_process_count(self.container_name)

    def fingerprint(self) -> dict | None:
        return _container_fingerprint(self.container_name)

    def start(self) -> BackendStartResult:
        return _start_container(self.container_name)

    # ---- 兼容老 API (供 workbench/backend/app/docker_env.py 重新导出) ----

    def container_metrics(self) -> dict:
        """仪表盘用: 容器 CPU% / 内存 / 数据目录大小 + ring buffer 历史。
        与原 workbench/backend/app/docker_env.container_metrics 等价。"""
        return _container_metrics(self.container_name, self.data_host_dir)

    def kill_lmp_processes(self) -> int | None:
        return _kill_lmp_processes(self.container_name)


# ---- 注册 ----
register_backend(LocalDockerBackend.name, LocalDockerBackend)


# ---- 模块内私有函数 (从 workbench/backend/app/docker_env.py 原样搬运) ----

_metrics_cache: dict = {"t": 0.0, "value": None}
_METRICS_TTL = 2.0
_metrics_history: list[dict] = []
_HISTORY_MAX = 60
_fp_cache: dict = {"t": 0.0, "value": None}
_FP_TTL = 600.0


def _default(key: str, fallback: Any) -> Any:
    """从 workbench.backend.app.config 读默认值 (向后兼容);
    读不到 (例如 CLI runner 在 workbench 之外跑) 用硬编码 fallback。

    逐字段 getattr 独立取值 — 某个名字在 config 里不存在只影响它自己,
    不能让整批默认值静默失效 (v1.8.5~v1.8.8 实录: LAMMPS_EXE 缺失导致
    ImportError 吞掉 LAMMPS_DATA_HOST_DIR → /data 挂载校验被整段跳过)。
    """
    try:
        from workbench.backend.app import config as _cfg

        return getattr(_cfg, key, fallback)
    except Exception:
        return fallback


def _parse_data_mount(inspect_stdout: str, container_data_dir: str) -> str | None:
    """从 `docker inspect --format '{{range .Mounts}}{{.Source}}|{{.Destination}};{{end}}'`
    的输出中找目标为 container_data_dir 的挂载, 返回宿主机源路径; 没有则 None。"""
    for pair in inspect_stdout.split(";"):
        parts = pair.split("|")
        if len(parts) == 2 and parts[1].rstrip("/") == container_data_dir:
            return parts[0]
    return None


def _host_path_same(a: str, b: str) -> bool:
    """宿主机路径等价 (Windows case/分隔符不敏感)。"""
    return os.path.normcase(os.path.normpath(a)) == os.path.normcase(os.path.normpath(b))


def _docker_info(container_name: str, container_data_dir: str | None,
                 data_host_dir: str | None,
                 lmp_count_fn) -> BackendInfo:
    """同步探测 docker + 容器状态 + /data 挂载; 返回 BackendInfo。"""
    info: BackendInfo = BackendInfo(
        type="local_docker",
        name="Local Docker",
        available=False,
        container_running=False,
        container_status=None,
        image=None,
        error=None,
        data_mount_host=None,
        data_mount_ok=False,
        lmp_processes=None,
        status="unreachable",  # running | stopped | unreachable
        action_needed="start_docker",  # none | start_container | start_docker
    )
    try:
        r = subprocess.run(
            ["docker", "ps", "--filter", f"name={container_name}",
             "--format", "{{.Names}}|{{.Status}}|{{.Image}}"],
            capture_output=True, text=True, timeout=8,
        )
    except FileNotFoundError:
        info["error"] = "未找到 docker 命令 (Docker Desktop 未安装?)"
        info["status"] = "unreachable"
        info["action_needed"] = "start_docker"
        return info
    except subprocess.TimeoutExpired:
        info["error"] = "docker 命令超时"
        info["status"] = "unreachable"
        info["action_needed"] = "start_docker"
        return info

    if r.returncode != 0:
        stderr = (r.stderr or "").strip()
        if "npipe" in stderr or "cannot find the file" in stderr or "pipe/dockerDesktopLinuxEngine" in stderr:
            info["error"] = "Docker Desktop 未运行 (找不到 docker daemon 命名管道)"
        else:
            info["error"] = stderr or "docker 命令失败"
        info["status"] = "unreachable"
        info["action_needed"] = "start_docker"
        return info

    info["available"] = True
    for line in r.stdout.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0] == container_name:
            info["container_running"] = True
            info["container_status"] = parts[1]
            info["image"] = parts[2]
    if not info["container_running"]:
        info["error"] = f"容器 {container_name} 未运行"
        info["status"] = "stopped"
        info["action_needed"] = "start_container"
        return info
    info["status"] = "running"
    info["action_needed"] = "none"

    # 校验 /data 挂载源
    if data_host_dir and container_data_dir:
        try:
            ins = subprocess.run(
                ["docker", "inspect", container_name,
                 "--format", "{{range .Mounts}}{{.Source}}|{{.Destination}};{{end}}"],
                capture_output=True, text=True, timeout=8,
            )
            host = _parse_data_mount(ins.stdout, container_data_dir)
            if host is not None:
                info["data_mount_host"] = host
                info["data_mount_ok"] = _host_path_same(host, data_host_dir)
        except Exception:
            pass
        if not info["data_mount_ok"]:
            info["error"] = (info["error"] or "") or f"/data 未挂载到预期的数据目录 {data_host_dir}"

    info["lmp_processes"] = lmp_count_fn()
    return info


def _lmp_process_count(container_name: str) -> int | None:
    try:
        pg = subprocess.run(
            ["docker", "exec", container_name, "pgrep", "-c", "-f", "lmp_mpi"],
            capture_output=True, text=True, timeout=8,
        )
    except Exception:
        return None
    if pg.returncode == 0:
        try:
            return int(pg.stdout.strip() or 0)
        except ValueError:
            return None
    if pg.returncode == 1:
        return 0
    return None


def _kill_lmp_processes(container_name: str) -> int | None:
    try:
        subprocess.run(
            ["docker", "exec", container_name, "pkill", "-f", "lmp_mpi"],
            capture_output=True, timeout=8,
        )
    except Exception:
        pass
    return _lmp_process_count(container_name)


def _parse_mem_bytes(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    for u, mul in (("GiB", 1024 ** 3), ("MiB", 1024 ** 2), ("KiB", 1024),
                   ("G", 1024 ** 3), ("M", 1024 ** 2), ("K", 1024),
                   ("B", 1)):
        if s.endswith(u):
            try:
                return int(float(s[:-len(u)]) * mul)
            except ValueError:
                return 0
    try:
        return int(float(s))
    except ValueError:
        return 0


def _dir_size_bytes(path: str) -> int | None:
    if not os.path.isdir(path):
        return None
    try:
        total = 0
        for dirpath, _dirs, files in os.walk(path):
            for f in files:
                try:
                    total += os.path.getsize(os.path.join(dirpath, f))
                except OSError:
                    pass
        return total
    except OSError:
        return None


def _sample_container_metrics(container_name: str) -> dict | None:
    # 容器没在跑就不采样
    try:
        pg = subprocess.run(
            ["docker", "ps", "--filter", f"name={container_name}", "--format", "{{.Names}}"],
            capture_output=True, text=True, timeout=8,
        )
        if container_name not in pg.stdout:
            return None
    except Exception:
        return None
    try:
        r = subprocess.run(
            ["docker", "stats", container_name, "--no-stream",
             "--format", "{{.CPUPerc}}|{{.MemUsage}}|{{.MemPerc}}"],
            capture_output=True, text=True, timeout=8,
        )
    except Exception:
        return None
    if r.returncode != 0 or not r.stdout.strip():
        return None
    parts = r.stdout.strip().split("|")
    if len(parts) < 3:
        return None
    cpu_pct = float(parts[0].rstrip("%") or 0)
    mem_used = parts[1].partition(" / ")[0]
    mem_pct = float(parts[2].rstrip("%") or 0)
    return {
        "cpu_pct": cpu_pct,
        "mem_used_bytes": _parse_mem_bytes(mem_used),
        "mem_pct": mem_pct,
    }


def _container_metrics(container_name: str, data_host_dir: str | None) -> dict:
    now = time.time()
    if _metrics_cache["value"] is None or now - _metrics_cache["t"] > _METRICS_TTL:
        sample = _sample_container_metrics(container_name)
        if sample is not None:
            _metrics_history.append({"t": now, **sample})
            if len(_metrics_history) > _HISTORY_MAX:
                _metrics_history.pop(0)
        _metrics_cache["value"] = {
            "current": sample,
            "history": list(_metrics_history),
            "data_dir_size_bytes": _dir_size_bytes(data_host_dir) if data_host_dir else None,
            "data_dir_path": data_host_dir,
        }
        _metrics_cache["t"] = now
    return _metrics_cache["value"]


def _start_container(container_name: str) -> BackendStartResult:
    try:
        probe = subprocess.run(
            ["docker", "info", "--format", "{{.ServerVersion}}"],
            capture_output=True, text=True, timeout=6,
        )
    except FileNotFoundError:
        return BackendStartResult(
            ok=False, stage="docker_missing",
            message="未找到 docker 命令。请安装 Docker Desktop 并启动 (https://www.docker.com/products/docker-desktop)",
            hint_url="https://www.docker.com/products/docker-desktop",
        )
    except subprocess.TimeoutExpired:
        return BackendStartResult(
            ok=False, stage="timeout",
            message="docker info 超时。请检查 Docker Desktop 是否运行 (Windows 托盘)",
            hint_url=None,
        )
    if probe.returncode != 0:
        stderr = (probe.stderr or probe.stdout or "").strip()
        if "npipe" in stderr or "cannot find the file" in stderr or "pipe/dockerDesktopLinuxEngine" in stderr:
            return BackendStartResult(
                ok=False, stage="daemon_unreachable",
                message="Docker Desktop 未运行 (找不到 docker daemon 命名管道)。请启动 Docker Desktop 后重试, 或参见 docs/environment.md",
                hint_url=None,
            )
        return BackendStartResult(
            ok=False, stage="failed",
            message=f"docker info 失败: {stderr[:200] or '未知错误'}",
            hint_url=None,
        )
    try:
        r = subprocess.run(
            ["docker", "start", container_name],
            capture_output=True, text=True, timeout=15,
        )
    except subprocess.TimeoutExpired:
        return BackendStartResult(ok=False, stage="timeout", message="docker start 超时", hint_url=None)
    if r.returncode != 0:
        stderr = (r.stderr or r.stdout or "").strip()
        return BackendStartResult(
            ok=False, stage="failed",
            message=f"docker start {container_name} 失败: {stderr[:200] or '未知错误'}",
            hint_url=None,
        )
    _metrics_cache["t"] = 0.0
    return BackendStartResult(
        ok=True, stage="container_started",
        message=f"容器 {container_name} 已启动",
        hint_url=None,
    )


def _container_fingerprint(container_name: str) -> dict | None:
    now = time.time()
    if _fp_cache["value"] is not None and now - _fp_cache["t"] < _FP_TTL:
        return _fp_cache["value"]
    fp: dict = {"image_id": None, "lmp_version": None}
    try:
        ins = subprocess.run(
            ["docker", "inspect", container_name,
             "--format", "{{.Image}}|{{.Config.Image}}"],
            capture_output=True, text=True, timeout=8,
        )
        if ins.returncode == 0 and "|" in ins.stdout:
            image_id, image_name = ins.stdout.strip().split("|", 1)
            fp["image_id"] = image_id[:19]
            fp["image"] = image_name
    except Exception:
        pass
    try:
        ver = subprocess.run(
            ["docker", "exec", container_name, "/usr/bin/lmp_mpi", "-h"],
            capture_output=True, text=True, timeout=15,
        )
        if ver.returncode == 0 and ver.stdout:
            first = next((l.strip() for l in ver.stdout.splitlines() if l.strip()), "")
            fp["lmp_version"] = first[:120] or None
    except Exception:
        pass
    _fp_cache["t"] = now
    _fp_cache["value"] = fp if (fp["image_id"] or fp["lmp_version"]) else None
    return _fp_cache["value"]
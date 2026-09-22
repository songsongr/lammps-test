"""Backend 抽象 + LocalDocker / RemoteHPC 单测 (v1.8.5)。

覆盖:
- get_backend() 默认 LocalDockerBackend
- configure_backend() 持久化 + 清缓存
- LocalDockerBackend.run_lmp_command 与原 docker exec 拼法一致 (零回归)
- LocalDockerBackend.info 在 docker 不在时返回 action_needed=start_docker/unavailable
- LocalDockerBackend.start 在 daemon 不通时返回 stage=daemon_unreachable/docker_missing
- RemoteHPCBackend 未配置返回 action_needed=configure
- RemoteHPCBackend.render_sbatch_script 模板渲染
- Backend 协议满足 duck-typing (runtime_checkable)
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

import pytest

# 强制从仓库根导入 (与其它 tests 行为一致)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


# ---- 临时 backend.json 路径覆盖 (每测试一个独立目录, 互不污染) ----

@pytest.fixture
def backend_cfg_dir(tmp_path, monkeypatch):
    """隔离 workbench/data/backend.json 到 tmp_path; 同时阻止从默认位置读到 local_docker。"""
    cfg_path = tmp_path / "backend.json"
    # 让 backend_config_path() 返回临时位置
    import common.backends.base as base_mod
    monkeypatch.setattr(base_mod, "_BACKEND_CONFIG_PATH", str(cfg_path))
    # 单例缓存清掉 (configure_backend 会清, 这里防止测试间残留)
    base_mod.reset_backend_cache()
    return cfg_path


# ---- 协议 duck-typing ----

class TestBackendProtocol:
    def test_local_docker_implements_protocol(self):
        from common.backends import Backend
        from common.backends.local_docker import LocalDockerBackend
        b = LocalDockerBackend()
        assert isinstance(b, Backend)

    def test_remote_hpc_implements_protocol(self):
        from common.backends import Backend
        from common.backends.remote_hpc import RemoteHPCBackend
        b = RemoteHPCBackend(ssh_host="h", ssh_user="u")
        assert isinstance(b, Backend)


# ---- 工厂 ----

class TestGetBackend:
    def test_default_returns_local_docker(self, backend_cfg_dir, monkeypatch):
        # backend.json 不存在时, 默认 local_docker
        from common.backends import get_backend
        from common.backends.local_docker import LocalDockerBackend
        b = get_backend()
        assert isinstance(b, LocalDockerBackend)
        assert b.name == "local_docker"

    def test_configured_remote_hpc_returns_remote_hpc(self, backend_cfg_dir, monkeypatch):
        from common.backends import get_backend, configure_backend
        from common.backends.remote_hpc import RemoteHPCBackend
        configure_backend("remote_hpc", ssh_host="h.univ.edu", ssh_user="alice",
                          hpc_workdir="/home/alice/lammps")
        b = get_backend()
        assert isinstance(b, RemoteHPCBackend)
        assert b.ssh_host == "h.univ.edu"
        assert b.ssh_user == "alice"

    def test_configure_then_reset(self, backend_cfg_dir):
        from common.backends import (configure_backend, get_backend,
                                      reset_backend_cache, get_backend_config)
        # 由于 reset_backend_cache 是公开 API, 验证它清缓存
        configure_backend("remote_hpc", ssh_host="x", ssh_user="y")
        reset_backend_cache()
        # 缓存清掉后, 重新读 cfg → remote_hpc
        b = get_backend()
        assert b.name == "remote_hpc"

    def test_unknown_backend_type_raises(self, backend_cfg_dir):
        from common.backends import configure_backend
        with pytest.raises(ValueError, match="未知后端类型"):
            configure_backend("not_a_real_backend")

    def test_unregistered_type_falls_back_to_local_docker(self, backend_cfg_dir):
        # backend.json 写了不存在的 type → 工厂应回退 local_docker
        backend_cfg_dir.write_text(json.dumps({"type": "ghost_backend"}),
                                    encoding="utf-8")
        from common.backends import get_backend
        b = get_backend()
        assert b.name == "local_docker"


# ---- LocalDocker: 命令拼接 (零回归证据) ----

class TestLocalDockerCommand:
    def test_run_lmp_command_matches_old_format(self):
        """LocalDockerBackend.run_lmp_command 拼出的命令必须与 v1.8.5 之前完全一致:
        docker exec -w <ws> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp 8 -in <ws>/<script>
        """
        from common.backends.local_docker import LocalDockerBackend
        b = LocalDockerBackend(container_name="lammpsd",
                                container_data_dir="/data",
                                lam_mps_exe="/usr/bin/lmp_mpi")
        cmd = b.run_lmp_command("/data/jobs/abc123", "run.lmp", omp_threads=8)
        assert cmd == [
            "docker", "exec", "-w", "/data/jobs/abc123", "lammpsd",
            "/usr/bin/lmp_mpi", "-sf", "omp", "-pk", "omp", "8",
            "-in", "/data/jobs/abc123/run.lmp",
        ]

    def test_via_runner_lmp_command(self):
        """common.runner.lmp_command() (供工作台 job_manager 用) 也应拼出相同命令。"""
        from common.runner import lmp_command
        cmd = lmp_command("/data/jobs/xyz", "in.lmp", omp_threads=4)
        assert cmd[:6] == ["docker", "exec", "-w", "/data/jobs/xyz", "lammpsd",
                            "/usr/bin/lmp_mpi"]
        assert cmd[-2:] == ["-in", "/data/jobs/xyz/in.lmp"]


# ---- LocalDocker: 探测 / 启动 (mock subprocess) ----

class TestLocalDockerInfo:
    def test_docker_not_installed(self, monkeypatch):
        """docker 命令缺失 → status=unreachable, action_needed=start_docker"""
        from common.backends.local_docker import LocalDockerBackend

        def fake_run(*args, **kwargs):
            raise FileNotFoundError("docker not found")

        monkeypatch.setattr(subprocess, "run", fake_run)
        b = LocalDockerBackend()
        info = b.info()
        assert info["status"] == "unreachable"
        assert info["action_needed"] == "start_docker"
        assert info["available"] is False
        assert "docker" in (info["error"] or "").lower() or "docker" in info["type"]

    def test_docker_daemon_unreachable(self, monkeypatch):
        """docker CLI 在但 daemon 不通 (Windows npipe 错) → status=unreachable"""
        from common.backends.local_docker import LocalDockerBackend

        class FakeResult:
            returncode = 1
            stderr = "error during connect: ... pipe/dockerDesktopLinuxEngine"
            stdout = ""

        monkeypatch.setattr(subprocess, "run",
                            lambda *a, **k: FakeResult())
        b = LocalDockerBackend()
        info = b.info()
        assert info["status"] == "unreachable"
        assert info["action_needed"] == "start_docker"

    def test_container_not_running(self, monkeypatch):
        """daemon 通 + 容器没跑 → status=stopped, action_needed=start_container"""
        from common.backends.local_docker import LocalDockerBackend

        class FakeResult:
            returncode = 0
            stdout = ""  # 没有任何容器
            stderr = ""

        monkeypatch.setattr(subprocess, "run",
                            lambda *a, **k: FakeResult())
        b = LocalDockerBackend()
        info = b.info()
        assert info["status"] == "stopped"
        assert info["action_needed"] == "start_container"
        assert info["container_running"] is False


class TestLocalDockerStart:
    def test_docker_missing(self, monkeypatch):
        from common.backends.local_docker import LocalDockerBackend

        def fake_run(*args, **kwargs):
            raise FileNotFoundError("docker missing")

        monkeypatch.setattr(subprocess, "run", fake_run)
        b = LocalDockerBackend()
        r = b.start()
        assert r["ok"] is False
        assert r["stage"] == "docker_missing"

    def test_daemon_unreachable(self, monkeypatch):
        from common.backends.local_docker import LocalDockerBackend

        class FakeResult:
            returncode = 1
            stderr = "pipe/dockerDesktopLinuxEngine not found"
            stdout = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: FakeResult())
        b = LocalDockerBackend()
        r = b.start()
        assert r["ok"] is False
        assert r["stage"] == "daemon_unreachable"


# ---- LocalDocker: 重新导出 (向后兼容) ----

class TestDockerEnvReExport:
    def test_module_level_functions_still_importable(self):
        """workbench/backend/app/docker_env.py 旧 API 全部保留。"""
        from workbench.backend.app import docker_env
        assert callable(docker_env.docker_info)
        assert callable(docker_env.lmp_process_count)
        assert callable(docker_env.kill_lmp_processes)
        assert callable(docker_env.container_metrics)
        assert callable(docker_env.start_container)
        assert callable(docker_env.container_fingerprint)


# ---- RemoteHPC: 骨架 ----

class TestRemoteHPC:
    def test_unconfigured_returns_configure_action(self):
        from common.backends.remote_hpc import RemoteHPCBackend
        b = RemoteHPCBackend()  # 全空
        info = b.info()
        assert info["status"] == "unconfigured"
        assert info["action_needed"] == "configure"
        assert info["available"] is False
        assert "ssh_host" in info["error"]
        assert "ssh_user" in info["error"]

    def test_configured_ssh_unreachable(self, monkeypatch):
        """ssh 命令不存在 / 超时 → status=unreachable"""
        from common.backends.remote_hpc import RemoteHPCBackend

        def fake_run(*args, **kwargs):
            raise FileNotFoundError("ssh not found")

        monkeypatch.setattr(subprocess, "run", fake_run)
        b = RemoteHPCBackend(ssh_host="h.univ.edu", ssh_user="alice")
        info = b.info()
        assert info["status"] == "unreachable"
        assert info["available"] is False

    def test_configured_ssh_ok(self, monkeypatch):
        """ssh 通了 → status=configured, available=True"""
        from common.backends.remote_hpc import RemoteHPCBackend

        class FakeResult:
            returncode = 0
            stdout = "ok\n"
            stderr = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: FakeResult())
        b = RemoteHPCBackend(ssh_host="h.univ.edu", ssh_user="alice")
        info = b.info()
        assert info["status"] == "configured"
        assert info["available"] is True
        assert info["action_needed"] == "none"

    def test_start_is_no_op(self, monkeypatch):
        """HPC 后端没有"启动"概念 — 配置好后 start() 返回 ok=True, stage=no_op"""
        from common.backends.remote_hpc import RemoteHPCBackend

        class FakeResult:
            returncode = 0
            stdout = "ok\n"
            stderr = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: FakeResult())
        b = RemoteHPCBackend(ssh_host="h", ssh_user="u")
        r = b.start()
        assert r["ok"] is True
        assert r["stage"] == "no_op"

    def test_render_sbatch_script(self):
        """string.Template 渲染: $script / $omp / $workdir / $modules 正确替换。"""
        from common.backends.remote_hpc import RemoteHPCBackend
        b = RemoteHPCBackend(ssh_host="h", ssh_user="u",
                              hpc_modules=["openmpi/4.1", "lammps/20240328"])
        out = b.render_sbatch_script("/home/alice/lammps/jobs/abc", "in.lmp",
                                       omp_threads=8)
        assert "#SBATCH --job-name=lammps-in.lmp" in out
        assert "#SBATCH --cpus-per-task=8" in out
        assert "module load openmpi/4.1" in out
        assert "module load lammps/20240328" in out
        assert 'cd "/home/alice/lammps/jobs/abc"' in out
        assert "mpirun -np 1 /usr/bin/lmp_mpi -in \"in.lmp\"" in out

    def test_ssh_cmd_format(self):
        """_ssh_cmd 拼出 BatchMode + ConnectTimeout, 避免交互卡死。"""
        from common.backends.remote_hpc import RemoteHPCBackend
        b = RemoteHPCBackend(ssh_host="h.univ.edu", ssh_user="alice",
                              ssh_key_path="/home/alice/.ssh/id_rsa")
        cmd = b._ssh_cmd("echo ok")
        assert "-o" in cmd and "BatchMode=yes" in cmd
        assert "-o" in cmd and "ConnectTimeout=5" in cmd
        assert "-i" in cmd and "/home/alice/.ssh/id_rsa" in cmd
        assert cmd[-2] == "alice@h.univ.edu"
        assert cmd[-1] == "echo ok"

    def test_run_lmp_command_ssh_sbatch(self):
        """run_lmp_command 拼出 ssh + cd + sbatch 链路。"""
        from common.backends.remote_hpc import RemoteHPCBackend
        b = RemoteHPCBackend(ssh_host="h.univ.edu", ssh_user="alice")
        cmd = b.run_lmp_command("/home/alice/lammps/jobs/abc", "in.lmp",
                                  omp_threads=4)
        assert cmd[0] == "ssh"
        assert "alice@h.univ.edu" in cmd
        remote = cmd[-1]
        assert "cd" in remote and "/home/alice/lammps/jobs/abc" in remote
        assert "sbatch run.sh" in remote


# ---- workbench/backend/app/routers/system.py 路由 (基础) ----

class TestBackendRoutes:
    """路由层仅验证 GET /api/backend 与 GET /api/backend/list 返回 200 + 合理结构。
    PUT/POST 测试因需要 FastAPI app 启动, 留给集成测试 (单测重点是 Backend 抽象)。"""

    def test_backend_get_returns_config_and_info(self, backend_cfg_dir):
        # backend.json 不存在 → 默认 local_docker
        from common.backends import get_backend, get_backend_config
        # 不通过 HTTP (避免启动 FastAPI), 直接验证返回结构
        cfg = get_backend_config()
        info = get_backend().info()
        assert "type" in cfg
        assert info["type"] == "local_docker"

    def test_backend_list_includes_both(self):
        from common.backends import list_backends
        # local_docker 在 docker 不通时会报 unavailable; remote_hpc 无配置也是 unconfigured
        rows = list_backends()
        types = {r["type"] for r in rows}
        assert "local_docker" in types
        assert "remote_hpc" in types
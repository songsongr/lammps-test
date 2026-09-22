"""RemoteHPCBackend — 远程 HPC (sbatch) 后端骨架 (v1.8.5)。

设计:
- 用 ssh + rsync + sbatch 完成「暂存-运行-回收」(与 LocalDocker 同语义, 但 100% 远程)
- 不引入 paramiko: 一律 subprocess + ssh CLI (跨平台, 与 Git Bash/PowerShell 兼容);
  v1.8.6+ 可选 paramiko 加速
- 拼出的命令是 `ssh -o BatchMode=yes user@host "cd <workdir> && sbatch run.sh"` 这种

配置 (持久化到 workbench/data/backend.json):
  ssh_host:        str (e.g. "hpc.univ.edu")
  ssh_user:        str (e.g. "alice")
  ssh_key_path:    str | None (id_rsa 绝对路径; None = ssh-agent / 默认 key)
  ssh_port:        int (默认 22)
  hpc_workdir:     str (远程提交根目录, e.g. "/home/alice/lammps")
  hpc_sbatch_template: str (sbatch 脚本模板, string.Template 语法; 必须含 $script 变量)
  hpc_modules:     list[str] (load 列表, e.g. ["openmpi/4.1", "lammps/20240328"])

状态机:
  status:        "configured" | "unconfigured" | "unreachable" | "running"
  action_needed: "none" | "no_op" | "configure" | "unavailable"
  available:     bool
"""
from __future__ import annotations

import os
import shlex
import string
import subprocess
from typing import Any

from .base import BackendInfo, BackendStartResult, register_backend

DEFAULT_SBATCH_TEMPLATE = """#!/bin/bash
#SBATCH --job-name=lammps-$script
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=$omp
#SBATCH --time=01:00:00
#SBATCH --output=$script.out
#SBATCH --error=$script.err
set -e
$modules
cd "$workdir"
mpirun -np 1 /usr/bin/lmp_mpi -in "$script"
"""


class RemoteHPCBackend:
    name: str = "remote_hpc"
    label: str = "Remote HPC (sbatch)"

    def __init__(self,
                 ssh_host: str | None = None,
                 ssh_user: str | None = None,
                 ssh_key_path: str | None = None,
                 ssh_port: int = 22,
                 hpc_workdir: str | None = None,
                 hpc_sbatch_template: str | None = None,
                 hpc_modules: list[str] | None = None) -> None:
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_key_path = ssh_key_path
        self.ssh_port = ssh_port
        self.hpc_workdir = hpc_workdir or "~/lammps"
        self.hpc_sbatch_template = hpc_sbatch_template or DEFAULT_SBATCH_TEMPLATE
        self.hpc_modules = hpc_modules or []

    # ---- 配置完备性 ----

    def is_configured(self) -> bool:
        return bool(self.ssh_host and self.ssh_user)

    def _missing_fields(self) -> list[str]:
        missing = []
        if not self.ssh_host:
            missing.append("ssh_host")
        if not self.ssh_user:
            missing.append("ssh_user")
        return missing

    # ---- Backend 协议 ----

    def info(self) -> BackendInfo:
        info: BackendInfo = BackendInfo(
            type="remote_hpc",
            name="Remote HPC (sbatch)",
            available=False,
            ssh_host=self.ssh_host,
            ssh_user=self.ssh_user,
            hpc_workdir=self.hpc_workdir,
            status="unconfigured",
            action_needed="configure",
            details={},
        )
        if not self.is_configured():
            info["error"] = f"HPC 后端未配置: 缺少 {', '.join(self._missing_fields())}"
            return info
        # 连通性探测: ssh -o BatchMode=yes -o ConnectTimeout=5 user@host "echo ok"
        try:
            r = subprocess.run(
                self._ssh_cmd('echo ok'),
                capture_output=True, text=True, timeout=8,
            )
        except FileNotFoundError:
            info["error"] = "未找到 ssh 命令"
            info["status"] = "unreachable"
            info["action_needed"] = "unavailable"
            return info
        except subprocess.TimeoutExpired:
            info["error"] = "ssh 连接超时 (5s)"
            info["status"] = "unreachable"
            info["action_needed"] = "none"  # 用户可重试
            return info
        if r.returncode != 0:
            info["error"] = (r.stderr or r.stdout or "ssh 失败").strip()[:200]
            info["status"] = "unreachable"
            info["action_needed"] = "none"
            return info
        info["available"] = True
        info["status"] = "configured"
        info["action_needed"] = "none"
        info["details"] = {"probe_stdout": r.stdout.strip()[:120]}
        return info

    def stage_dependencies(self, project_dir: str, script: str,
                           ws_host: str, *, skip_script: bool = False) -> list[str]:
        """暂存: rsync 本地工作区 ws_host → 远程 hpc_workdir/jobs/<ws_id_basename>/。

        ws_host 是本地路径 (工作台给的 staging 目录); 我们从 ws_host 推导远程目的
        (basename = job_id), 这样跟 LocalDocker 的"按 job_id 隔离"语义对齐。
        依赖闭包解析走 LocalDocker 同套逻辑 (collect_deps) — 复用避免漂移。
        """
        import shutil
        from common.runner import collect_deps

        os.makedirs(ws_host, exist_ok=True)
        deps, missing = collect_deps(script, project_dir)
        import glob
        copies = ([] if skip_script else [script]) + deps
        for p in glob.glob(os.path.join(project_dir, "*.data")):
            name = os.path.basename(p)
            if name not in copies:
                copies.append(name)
        for rel in copies:
            shutil.copy2(os.path.join(project_dir, rel), os.path.join(ws_host, rel))

        # 同步到远程 (rsync 必须可用)
        ws_basename = os.path.basename(ws_host.rstrip(os.sep))
        remote_dest = f"{self.ssh_user}@{self.ssh_host}:{self.hpc_workdir.rstrip('/')}/jobs/{ws_basename}"
        rsync_cmd = ["rsync", "-az", "--delete", ws_host + os.sep, remote_dest]
        try:
            r = subprocess.run(rsync_cmd, capture_output=True, text=True, timeout=60)
            if r.returncode != 0:
                missing.append(f"__rsync_failed__:{r.stderr.strip()[:120]}")
        except FileNotFoundError:
            missing.append("__rsync_missing__:未找到 rsync 命令")
        return missing

    def run_lmp_command(self, ws_backend: str, script: str,
                        omp_threads: int = 8) -> list[str]:
        """拼装 ssh + sbatch 命令:
        `ssh user@host "cd <ws_backend> && sbatch run_<script>.sh"`

        sbatch 脚本经 string.Template 渲染写到 ws_backend 的工作区后,
        通过 ssh 触发提交; 命令本身只生成拼好的 ssh 命令, sbatch 脚本由
        调用方通过 stage_dependencies 后的额外步骤写入 (见 _write_sbatch)。
        简化: 这里直接 ssh 触发渲染后的脚本 (run.sh 名字固定)。
        """
        # 工作区内的 sbatch 脚本名 (固定为 run.sh, 避免字符转义)
        sbatch_script = "run.sh"
        sbatch_path = os.path.join(ws_backend.replace(self.hpc_workdir, "").lstrip("/"),
                                   sbatch_script)
        remote_workdir = ws_backend
        # 拼接远程命令 — sbatch 输出 job id, 写到 .jobid
        remote_cmd = (
            f"cd {shlex.quote(remote_workdir)} && "
            f"chmod +x {shlex.quote(sbatch_script)} && "
            f"sbatch {shlex.quote(sbatch_script)} | tee {shlex.quote(sbatch_script)}.jobid"
        )
        ssh = self._ssh_cmd(remote_cmd)
        # 让 Popen 通过 shell=False 仍能传多词 ssh 命令 — ssh 自身接受参数列表
        # 我们把 remote_cmd 合并为单个字符串 (ssh 把它当 shell 命令传给远端)
        ssh[-1] = remote_cmd
        return ssh

    def render_sbatch_script(self, ws_backend: str, script: str,
                             omp_threads: int = 8) -> str:
        """把 sbatch 模板渲染成可写文件内容 (供 stage_dependencies 后调用方写入)。"""
        tpl = string.Template(self.hpc_sbatch_template)
        modules = "\n".join(f"module load {m}" for m in self.hpc_modules) or "true"
        return tpl.safe_substitute(
            script=script,
            omp=omp_threads,
            workdir=ws_backend,
            modules=modules,
        )

    def lmp_process_count(self) -> int | None:
        """远程 HPC 上 LMP 跑在 compute node, 工作台拿不到精确计数;
        用 squeue -u <user> 近似 = 用户当前排队/运行任务数 (含挂起的)。
        返回 None 当探测失败。
        """
        if not self.is_configured():
            return None
        try:
            r = subprocess.run(
                self._ssh_cmd(f"squeue -u {shlex.quote(self.ssh_user)} -h | wc -l"),
                capture_output=True, text=True, timeout=8,
            )
        except Exception:
            return None
        if r.returncode != 0:
            return None
        try:
            return int(r.stdout.strip() or 0)
        except ValueError:
            return None

    def fingerprint(self) -> dict | None:
        """远程环境指纹: module list + lmp_mpi -h 首行。
        拿不到返回 None 不阻塞。"""
        if not self.is_configured():
            return None
        try:
            r = subprocess.run(
                self._ssh_cmd("module list 2>&1 | head -20; echo ---; /usr/bin/lmp_mpi -h 2>&1 | head -3"),
                capture_output=True, text=True, timeout=15,
            )
        except Exception:
            return None
        if r.returncode != 0:
            return None
        text = r.stdout.strip()
        version = None
        for line in text.splitlines():
            if line.strip().startswith("---"):
                continue
            if "Large-scale" in line or "LAMMPS" in line:
                version = line.strip()[:120]
                break
        return {
            "remote": f"{self.ssh_user}@{self.ssh_host}",
            "module_list": [l for l in text.splitlines()
                            if l.strip().startswith("Currently loaded") or "\t" in l][:10],
            "lmp_version": version,
        }

    def start(self) -> BackendStartResult:
        """HPC 后端没有"启动"概念 — 返回 no_op 提示用户这是任务提交模式。"""
        if not self.is_configured():
            return BackendStartResult(
                ok=False, stage="unconfigured",
                message=f"HPC 后端未配置: 缺少 {', '.join(self._missing_fields())}",
                hint_url=None,
            )
        # 顺便做一次连通性探活
        info = self.info()
        if info["status"] == "configured":
            return BackendStartResult(
                ok=True, stage="no_op",
                message="无需启动, HPC 后端是任务提交模式 (sbatch)",
                hint_url=None,
            )
        return BackendStartResult(
            ok=False, stage="unreachable",
            message=info.get("error", "ssh 不通"),
            hint_url=None,
        )

    # ---- 内部 ----

    def _ssh_cmd(self, remote_cmd: str) -> list[str]:
        """构造 ssh 命令 argv 列表 (跨平台; 始终 BatchMode=yes 避免交互卡死)。"""
        cmd = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5",
               "-p", str(self.ssh_port)]
        if self.ssh_key_path:
            cmd.extend(["-i", self.ssh_key_path])
        cmd.append(f"{self.ssh_user}@{self.ssh_host}")
        cmd.append(remote_cmd)
        return cmd


register_backend(RemoteHPCBackend.name, RemoteHPCBackend)
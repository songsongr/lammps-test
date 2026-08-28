"""暂存-运行-回收统一执行契约 — CLI (entrypoints) 与 workbench (job_manager) 共用。

staging: 把 .lmp + 依赖闭包 (include/read_data/read_restart + 项目顶层 *.data)
         拷入数据工作区 lammps-data-docker/jobs/<ws_id>/ (= 容器 /data/jobs/<ws_id>/)
command: docker exec -w /data/jobs/<ws_id> lammpsd lmp_mpi -sf omp -pk omp N -in <容器内绝对路径>
执行循环由调用方实现 (CLI 同步流式 / workbench 异步流式), 两者共享同一契约与取消语义。
"""
from __future__ import annotations

import os
import re

CONTAINER_NAME = "lammpsd"
LAMMPS_EXE = "/usr/bin/lmp_mpi"
CONTAINER_DATA_DIR = "/data"

_DEP_PAT = re.compile(r"^\s*(?:include|read_data|read_restart)\s+(\S+)", re.M)
_SCAN_SKIP_EXT = {".lammpstrj", ".dump", ".restart", ".png", ".jpg", ".jpeg",
                  ".xlsx", ".zip", ".gz", ".pdf"}
_MAX_SCAN_BYTES = 2_000_000
_MAX_DEP_DEPTH = 10


def workspace_host(data_host_dir: str, ws_id: str) -> str:
    """任务工作区 (宿主机视角): 数据目录下按工作区 id 隔离。"""
    import os
    return os.path.join(data_host_dir, "jobs", ws_id)


def workspace_container(ws_id: str) -> str:
    return f"{CONTAINER_DATA_DIR}/jobs/{ws_id}"


def collect_deps(script_name: str, project_dir: str) -> tuple[list[str], list[str]]:
    """解析脚本的 include/read_data/read_restart 引用闭包。

    返回 (项目目录内存在且需暂存的相对路径, 引用了但不存在的相对路径)。
    仅扫描小文本文件; 引用按项目目录扁平解析 (v1 不支持子目录相对引用)。
    """
    present: list[str] = []
    missing: list[str] = []
    seen: set[str] = {script_name}
    queue: list[str] = [script_name]
    depth = 0
    while queue and depth < _MAX_DEP_DEPTH:
        rel = queue.pop(0)
        depth += 1
        path = os.path.join(project_dir, rel)
        if not os.path.isfile(path) or os.path.getsize(path) > _MAX_SCAN_BYTES:
            continue
        if os.path.splitext(path)[1].lower() in _SCAN_SKIP_EXT:
            continue
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        for ref in _DEP_PAT.findall(text):
            ref = os.path.normpath(ref)
            if ref in seen:
                continue
            seen.add(ref)
            if os.path.isfile(os.path.join(project_dir, ref)):
                present.append(ref)
                queue.append(ref)  # 传递闭包: 依赖的依赖
            elif ref not in missing:
                missing.append(ref)
    return present, missing


def stage_dependencies(project_dir: str, script: str, ws_host: str) -> list[str]:
    """把脚本 + 依赖闭包 + 顶层 *.data 暂存到工作区, 返回缺失依赖列表。

    调用方负责创建目录与向用户呈现缺失告警。
    """
    import glob
    import shutil

    os.makedirs(ws_host, exist_ok=True)
    deps, missing = collect_deps(script, project_dir)
    copies = [script, *deps]
    for p in glob.glob(os.path.join(project_dir, "*.data")):
        name = os.path.basename(p)
        if name not in copies:
            copies.append(name)
    for rel in copies:
        shutil.copy2(os.path.join(project_dir, rel), os.path.join(ws_host, rel))
    return missing


def lmp_command(ws_container: str, script: str, omp_threads: int = 8) -> list[str]:
    """LAMMPS 容器命令 — -in 用容器内绝对路径, 任务标识进入命令行 (精确取消的依据)。"""
    return [
        "docker", "exec", "-w", ws_container, CONTAINER_NAME,
        LAMMPS_EXE, "-sf", "omp", "-pk", "omp", str(omp_threads),
        "-in", f"{ws_container}/{script}",
    ]


def run_cli(project_dir: str, script: str, omp_threads: int = 8) -> int:
    """CLI 同步执行: 暂存 → docker exec → 输出流式透传到本进程 stdout。

    与工作台同账本: 任务写入工作台任务库 (source=cli, 失败静默降级不影响 CLI 本身),
    输出 tee 到 workbench/data/jobs/<id>.log (详情页可回放)。
    """
    import subprocess
    import sys
    import uuid
    from datetime import datetime

    ws_id = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
    # 数据目录: 项目根下的 lammps-data-docker (与 workbench 同一约定)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_host = os.path.join(repo_root, "lammps-data-docker")
    ws_host = workspace_host(data_host, ws_id)
    missing = stage_dependencies(project_dir, script, ws_host)
    for ref in missing:
        print(f"[runner] 警告: 脚本引用的依赖不存在, 未暂存: {ref}", file=sys.stderr)
    print(f"[runner] 工作区: {ws_host}", file=sys.stderr)

    job_id = ws_id.replace("-", "")[:16]
    record = _cli_record(job_id, repo_root, project_dir, script, ws_host)
    log_file = None
    if record:
        try:
            log_file = open(record["_log_path"], "w", encoding="utf-8", errors="replace")
        except OSError:
            log_file = None

    cmd = lmp_command(workspace_container(ws_id), script, omp_threads)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert proc.stdout is not None
    for raw in proc.stdout:
        line = raw.decode("utf-8", "replace")
        sys.stdout.write(line)
        sys.stdout.flush()
        if log_file:
            try:
                log_file.write(line)
                log_file.flush()
            except OSError:
                pass
    code = proc.wait()
    if log_file:
        log_file.close()
    _cli_finish(job_id, code)
    return code


def _cli_record(job_id: str, repo_root: str, project_dir: str,
                script: str, ws_host: str) -> dict | None:
    """把 CLI 任务登记进工作台任务库 (source=cli); store 不可用时静默跳过。"""
    import json
    from datetime import datetime

    try:
        from workbench.backend.app import store
        from workbench.backend.app.config import JOBS_LOG_DIR

        store.init()
        log_path = os.path.join(JOBS_LOG_DIR, f"{job_id}.log")
        fingerprint = {}
        sys_path = os.path.join(project_dir, "system.json")
        if os.path.isfile(sys_path):
            import hashlib
            with open(sys_path, "rb") as f:
                fingerprint["system_sha"] = hashlib.sha256(f.read()).hexdigest()[:16]
        job = {
            "id": job_id,
            "project_id": os.path.basename(os.path.normpath(project_dir)),
            "project_name": os.path.basename(os.path.normpath(project_dir)),
            "script": script,
            "kind": "lmp",
            "command": f"uv run run-sim (cli) {script}",
            "status": "running",
            "exit_code": None,
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "started_at": datetime.now().isoformat(timespec="seconds"),
            "finished_at": None,
            "log_path": log_path,
            "workspace": ws_host,
            "omp_threads": 8,
            "fingerprint": json.dumps(fingerprint, ensure_ascii=False) if fingerprint else None,
            "source": "cli",
        }
        store.insert(job)
        job["_log_path"] = log_path
        return job
    except Exception:
        return None


def _cli_finish(job_id: str, code: int) -> None:
    """CLI 任务终态回写 (静默降级)。"""
    try:
        from datetime import datetime

        from workbench.backend.app import store

        store.update(job_id, status="completed" if code == 0 else "failed",
                     exit_code=code, finished_at=datetime.now().isoformat(timespec="seconds"))
    except Exception:
        pass


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) < 2:
        print("用法: python -m common.runner <project_dir> <script> [--omp N]", file=sys.stderr)
        raise SystemExit(2)
    omp = 8
    if "--omp" in args:
        i = args.index("--omp")
        omp = int(args[i + 1])
        args = args[:i] + args[i + 2 :]
    raise SystemExit(run_cli(args[0], args[1], omp))

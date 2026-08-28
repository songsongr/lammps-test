"""Docker 环境探测: docker 可用性 + lammpsd 容器状态与 /data 挂载校验。"""
import os
import subprocess

from .config import CONTAINER_DATA_DIR, CONTAINER_NAME, LAMMPS_DATA_HOST_DIR


def docker_info() -> dict:
    """同步调用 docker (约几百 ms), 调用方应放线程池/缓存结果。"""
    info: dict = {
        "available": False,
        "container_running": False,
        "container_status": None,
        "image": None,
        "error": None,
        "data_mount_host": None,
        "data_mount_ok": False,
    }
    try:
        r = subprocess.run(
            ["docker", "ps", "--filter", f"name={CONTAINER_NAME}",
             "--format", "{{.Names}}|{{.Status}}|{{.Image}}"],
            capture_output=True, text=True, timeout=8,
        )
    except FileNotFoundError:
        info["error"] = "未找到 docker 命令"
        return info
    except subprocess.TimeoutExpired:
        info["error"] = "docker 命令超时"
        return info

    if r.returncode != 0:
        info["error"] = (r.stderr or "docker 命令失败").strip()
        return info

    info["available"] = True
    for line in r.stdout.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0] == CONTAINER_NAME:
            info["container_running"] = True
            info["container_status"] = parts[1]
            info["image"] = parts[2]
    if not info["container_running"]:
        info["error"] = f"容器 {CONTAINER_NAME} 未运行"
        return info

    # 校验 /data 挂载源是否为预期的数据目录
    expected = os.path.normcase(os.path.normpath(LAMMPS_DATA_HOST_DIR))
    try:
        ins = subprocess.run(
            ["docker", "inspect", CONTAINER_NAME,
             "--format", "{{range .Mounts}}{{.Source}}|{{.Destination}};{{end}}"],
            capture_output=True, text=True, timeout=8,
        )
        for pair in ins.stdout.split(";"):
            parts = pair.split("|")
            if len(parts) == 2 and parts[1].rstrip("/") == CONTAINER_DATA_DIR:
                host = parts[0]
                info["data_mount_host"] = host
                info["data_mount_ok"] = os.path.normcase(os.path.normpath(host)) == expected
    except Exception:
        pass
    if not info["data_mount_ok"]:
        info["error"] = (info["error"] or "") or f"/data 未挂载到预期的数据目录 {LAMMPS_DATA_HOST_DIR}"

    # 容器内真实 LAMMPS 进程数 (孤儿进程探测: 与任务记账无关的地面真相)
    info["lmp_processes"] = lmp_process_count()
    return info


def lmp_process_count() -> int | None:
    """容器内 lmp_mpi 进程数; 探测失败返回 None (未知, 不猜 0)。"""
    try:
        pg = subprocess.run(
            ["docker", "exec", CONTAINER_NAME, "pgrep", "-c", "-f", "lmp_mpi"],
            capture_output=True, text=True, timeout=8,
        )
    except Exception:
        return None
    if pg.returncode == 0:
        try:
            return int(pg.stdout.strip() or 0)
        except ValueError:
            return None
    if pg.returncode == 1:  # pgrep: 无匹配
        return 0
    return None


def kill_lmp_processes() -> int | None:
    """清理容器内全部 lmp_mpi 进程 (工作台受控退出前的孤儿清扫); 返回清理后残余数。"""
    try:
        subprocess.run(
            ["docker", "exec", CONTAINER_NAME, "pkill", "-f", "lmp_mpi"],
            capture_output=True, timeout=8,
        )
    except Exception:
        pass
    return lmp_process_count()


# ---- 容器环境指纹 (任务可比性: 镜像 ID + LAMMPS 版本; 进程内 TTL 缓存) ----
_fp_cache: dict = {"t": 0.0, "value": None}
_FP_TTL = 600.0  # 秒


def container_fingerprint() -> dict | None:
    """镜像 ID + LAMMPS 版本 (发任务时记录; 10 分钟缓存, 拿不到返回 None 不阻塞)。"""
    import time
    now = time.time()
    if _fp_cache["value"] is not None and now - _fp_cache["t"] < _FP_TTL:
        return _fp_cache["value"]
    fp: dict = {"image_id": None, "lmp_version": None}
    try:
        ins = subprocess.run(
            ["docker", "inspect", CONTAINER_NAME,
             "--format", "{{.Image}}|{{.Config.Image}}"],
            capture_output=True, text=True, timeout=8,
        )
        if ins.returncode == 0 and "|" in ins.stdout:
            image_id, image_name = ins.stdout.strip().split("|", 1)
            fp["image_id"] = image_id[:19]  # sha256:12a3... 截短可读
            fp["image"] = image_name
    except Exception:
        pass
    try:
        ver = subprocess.run(
            ["docker", "exec", CONTAINER_NAME, "/usr/bin/lmp_mpi", "-h"],
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

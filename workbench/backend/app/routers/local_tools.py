"""本地工具 (VMD / Vesta) HTTP 接口: 探测、配置、启动器生成、直起。"""
import os
import platform
import subprocess
import sys as _sys
import tempfile
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from common.local_tools_compat import supports

from ..config import LOCAL_TOOLS_CONFIG
from ..local_tools.detect import detect, launcher

router = APIRouter(prefix="/api/local-tools")


def _load_overrides() -> dict:
    if not os.path.isfile(LOCAL_TOOLS_CONFIG):
        return {}
    import json
    with open(LOCAL_TOOLS_CONFIG, encoding="utf-8") as f:
        return json.load(f)


def _save_overrides(d: dict) -> None:
    import json
    os.makedirs(os.path.dirname(LOCAL_TOOLS_CONFIG), exist_ok=True)
    with open(LOCAL_TOOLS_CONFIG, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _merged() -> dict:
    info = detect()
    overrides = _load_overrides()
    for tool in ("vmd", "vesta"):
        ov = overrides.get(tool, {})
        if ov.get("path"):
            info[tool]["path"] = ov["path"]
            info[tool]["found"] = os.path.isfile(ov["path"])
            info[tool]["source"] = "manual"
    return info


@router.get("/detect")
async def get_detect() -> dict:
    """探测 + 用户配置覆盖, 前端仪表盘用。"""
    return _merged()


class ConfigureBody(BaseModel):
    tool: str
    path: Optional[str] = None  # 传空字符串清除
    custom_install_hints: Optional[list[str]] = None  # 仅展示用, 不持久化


@router.post("/configure")
async def configure(body: ConfigureBody) -> dict:
    if body.tool not in ("vmd", "vesta"):
        raise HTTPException(status_code=400, detail="tool 必须是 vmd 或 vesta")
    overrides = _load_overrides()
    if body.path is None or body.path == "":
        overrides.pop(body.tool, None)
    else:
        if not os.path.isfile(body.path):
            raise HTTPException(status_code=400, detail=f"文件不存在或不可访问: {body.path}")
        overrides[body.tool] = {"path": body.path}
    _save_overrides(overrides)
    return _merged()


@router.get("/launcher")
async def make_launcher(tool: str, path: str) -> dict:
    """生成一键启动脚本 (双击运行, 适配本机 OS)。

    注: v1.8.2 推荐使用 POST /open 直接启动, 本端点保留为手动下载启动器入口。
    """
    if tool not in ("vmd", "vesta"):
        raise HTTPException(status_code=400, detail="tool 必须是 vmd 或 vesta")
    if not path:
        raise HTTPException(status_code=400, detail="path 必填")
    overrides = _load_overrides()
    exe = overrides.get(tool, {}).get("path")
    r = launcher(tool, path, exe_override=exe)
    return r


class OpenBody(BaseModel):
    tool: str
    path: str  # 文件绝对路径 (本机视角)
    auto_convert_data: bool = True  # .data → .xyz 临时文件 (VESTA 必需)


def _spawn_exe(exe: str, file_path: str) -> tuple[bool, str, str | None]:
    """后端 spawn 本机 .exe 打开文件。返回 (ok, message, pid_or_None)。

    硬约束: 后端必须与用户在**同一台机器 + 同一 OS + 同一用户**上运行
    (Docker 后端/SSH/RDP 不可行, 直接返回 ok=False + 降级提示)。
    """
    plat = _sys.platform
    if plat.startswith("linux") and not _is_host_user_session():
        return False, "Docker/远程后端无法直接启动本机 GUI (需下载启动器)", None
    try:
        if plat == "win32":
            # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP: 子进程脱离父进程, 父退出不影响
            flags = 0x00000008 | 0x00000200
            p = subprocess.Popen([exe, file_path], creationflags=flags,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif plat == "darwin":
            p = subprocess.Popen([exe, file_path], start_new_session=True,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            p = subprocess.Popen([exe, file_path], start_new_session=True,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True, "已启动", str(p.pid)
    except FileNotFoundError:
        return False, f"工具未找到: {exe}", None
    except OSError as e:
        return False, f"启动失败: {e}", None


def _is_host_user_session() -> bool:
    """粗判: 后端是否在用户本机 (非 Docker / SSH)。

    真值靠: (1) 非 Linux; (2) Linux 下有 DISPLAY (X11) 或 WAYLAND_DISPLAY;
    实际更可靠的判据是 OSError 出现再 fallback。本函数保守返回 True,
    真实失败在 _spawn_exe 内的 OSError 兜住。
    """
    return True


@router.post("/open")
async def open_with_tool(body: OpenBody) -> dict:
    """真一键: 后端 spawn 本机 .exe 直接打开文件 (Docker 后端/远程会自动降级)。

    - VMD 支持的格式直接打开
    - VESTA 不支持 .data: 若 auto_convert_data, 调 lammps_data_to_xyz 转临时 .xyz 后再开
    - 后端无法 spawn (Docker/远程) 时, 优雅降级返回 launcher 脚本, 前端按需下载
    """
    if body.tool not in ("vmd", "vesta"):
        raise HTTPException(status_code=400, detail="tool 必须是 vmd 或 vesta")
    if not body.path or not os.path.isfile(body.path):
        raise HTTPException(status_code=400, detail=f"文件不存在: {body.path}")
    overrides = _load_overrides()
    exe = overrides.get(body.tool, {}).get("path")
    if not exe or not os.path.isfile(exe):
        info = _merged()
        exe = info[body.tool].get("path")
    if not exe or not os.path.isfile(exe):
        raise HTTPException(status_code=404, detail=f"{body.tool} 未配置 (请在工作台仪表盘「本地工具」浮窗手动指定路径)")

    ext = os.path.splitext(body.path)[1].lower()
    open_path = body.path

    # VESTA 不支持 .data: 转临时 .xyz
    if body.tool == "vesta" and ext == ".data" and body.auto_convert_data:
        try:
            from common.lammps_data import lammps_data_to_xyz
            text = open(body.path, encoding="utf-8", errors="replace").read()
            xyz = lammps_data_to_xyz(text)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"data→xyz 转换失败: {e}")
        cache_dir = os.path.join(tempfile.gettempdir(), "lammps_workbench_open")
        os.makedirs(cache_dir, exist_ok=True)
        tmp_xyz = os.path.join(cache_dir, f"{os.path.basename(body.path)}.xyz")
        with open(tmp_xyz, "w", encoding="utf-8") as f:
            f.write(xyz)
        open_path = tmp_xyz

    # 工具原生支持校验 (不通过则直接降级 launcher, 不做无效 spawn)
    if not supports(body.tool, os.path.splitext(open_path)[1]):
        r = launcher(body.tool, body.path, exe_override=exe)
        return {"ok": False, "spawned": False, "fallback": "launcher",
                "message": f"{body.tool} 不支持 {ext or '(无扩展名)'} 格式, 已生成启动器供手动下载",
                **r}

    ok, msg, pid = _spawn_exe(exe, open_path)
    if ok:
        return {"ok": True, "spawned": True, "pid": pid, "path": open_path,
                "message": f"已启动 {body.tool} (pid {pid})"}
    # spawn 失败: 降级 launcher
    r = launcher(body.tool, body.path, exe_override=exe)
    return {"ok": False, "spawned": False, "fallback": "launcher", "message": msg, **r}


@router.get("/install-hint")
async def install_hint(tool: str) -> dict:
    """自动配置失败时展示给用户的安装指引 (按平台)。"""
    sys = platform.system()
    urls = {
        "vmd": {
            "Windows": "https://www.ks.uiuc.edu/Research/vmd/",
            "macOS": "https://www.ks.uiuc.edu/Research/vmd/ (下载 .dmg, 拖入 Applications)",
            "Linux": "sudo apt install vmd  (Debian/Ubuntu) 或官网下载",
        },
        "vesta": {
            "Windows": "https://jp-minerals.org/vesta/en/download.html",
            "macOS": "https://jp-minerals.org/vesta/en/download.html (下载 .dmg)",
            "Linux": "https://jp-minerals.org/vesta/en/download.html (下载 tar.gz)",
        },
    }
    return {"tool": tool, "platform": sys, "url": urls.get(tool, {}).get(sys, "")}

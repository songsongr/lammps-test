"""本地工具 (VMD / Vesta) HTTP 接口: 探测、配置、启动器生成。"""
import os
import platform
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

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
    """生成一键启动脚本 (双击运行, 适配本机 OS)。"""
    if tool not in ("vmd", "vesta"):
        raise HTTPException(status_code=400, detail="tool 必须是 vmd 或 vesta")
    if not path:
        raise HTTPException(status_code=400, detail="path 必填")
    overrides = _load_overrides()
    exe = overrides.get(tool, {}).get("path")
    r = launcher(tool, path, exe_override=exe)
    return r


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

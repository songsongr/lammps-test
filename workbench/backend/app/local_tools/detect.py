"""本地工具自动探测 (VMD / Vesta) — 纯函数, 前后端 / CLI 共用。

策略: 在常见安装路径中快速比对 (os.path.isfile), 不调用外部命令以免阻塞。
返回结构化结果供 UI 决策:
  found: bool         # 是否找到
  path:  str | None   # 可执行文件绝对路径
  version_hint: str | None  # 来自路径的版本片段 (如 vmd 2.0 → "2.0"), 仅展示用
  source: str         # "known" | "fallback" | "env" | None
"""
import os
import platform
import re

_SYSTEM = platform.system()  # "Windows" / "Darwin" / "Linux"


def _common_paths_vmd() -> list[str]:
    if _SYSTEM == "Windows":
        return [
            r"C:\Program Files\VMD\vmd.exe",
            r"C:\Program Files (x86)\VMD\vmd.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\VMD\vmd.exe"),
        ]
    if _SYSTEM == "Darwin":
        return ["/Applications/VMD.app/Contents/vmd/vmd",
                "/Applications/VMD.app/Contents/MacOS/startup.app"]
    return [
        "/usr/local/bin/vmd",
        "/usr/bin/vmd",
        os.path.expanduser("~/bin/vmd"),
    ]


def _common_paths_vesta() -> list[str]:
    if _SYSTEM == "Windows":
        return [
            r"C:\Program Files\Vesta\VESTA.exe",
            r"C:\Program Files\Vesta-win64\VESTA.exe",
            r"C:\Program Files (x86)\Vesta\VESTA.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\Vesta\VESTA.exe"),
        ]
    if _SYSTEM == "Darwin":
        return ["/Applications/Vesta.app/Contents/MacOS/Vesta",
                "/Applications/VESTA.app/Contents/MacOS/Vesta"]
    return [
        "/usr/local/bin/vesta",
        "/usr/bin/vesta",
        os.path.expanduser("~/bin/vesta"),
    ]


def _search(env_var: str, paths: list[str]) -> tuple[str | None, str]:
    """返回 (path, source); source ∈ {"env","known","fallback",""}."""
    p = os.environ.get(env_var, "").strip()
    if p and os.path.isfile(p):
        return p, "env"
    for cand in paths:
        if os.path.isfile(cand):
            return cand, "known"
    return None, "fallback"


def _version_hint(path: str) -> str | None:
    """从路径里抓版本号, 仅作展示。"""
    if not path:
        return None
    base = os.path.basename(os.path.dirname(path))
    m = re.search(r"(\d+(?:\.\d+){0,2})", base)
    return m.group(1) if m else None


def detect() -> dict:
    """同时探测 VMD / Vesta, 一次返回。"""
    vmd_path, vmd_src = _search("VMD_EXE", _common_paths_vmd())
    vesta_path, vesta_src = _search("VESTA_EXE", _common_paths_vesta())
    return {
        "platform": _SYSTEM,
        "vmd": {
            "found": vmd_path is not None,
            "path": vmd_path,
            "version_hint": _version_hint(vmd_path) if vmd_path else None,
            "source": vmd_src if vmd_path else None,
        },
        "vesta": {
            "found": vesta_path is not None,
            "path": vesta_path,
            "version_hint": _version_hint(vesta_path) if vesta_path else None,
            "source": vesta_src if vesta_path else None,
        },
    }


def launcher(tool: str, file_path: str, exe_override: str | None = None) -> dict:
    """生成一键启动脚本 (小文件, 用户双击即可, 无需配置 PATH / 防火墙)。

    返回 {filename, content}; filename 含平台后缀, content 是可直接保存运行的脚本。
    exe_override: 用户在手动配置浮窗里填的路径, 优先生效 (用于自动检测失败时的兜底)。
    """
    info = detect()
    conf = info["vesta"] if tool == "vesta" else info["vmd"]
    exe = exe_override or conf["path"]
    if _SYSTEM == "Windows":
        # .bat: start "" 让 GUI 进程脱离父进程, 失败时弹出窗口让用户看到错误
        body = (
            f"@echo off\r\n"
            f"setlocal\r\n"
            f"if exist \"{exe}\" (\r\n"
            f"  start \"\" \"{exe}\" \"{file_path}\"\r\n"
            f") else (\r\n"
            f"  echo 工具未找到: {exe}\r\n"
            f"  echo 请在工作台仪表盘「本地工具」浮窗里重新配置路径后重试。\r\n"
            f"  pause\r\n"
            f")\r\n"
        )
        return {"filename": f"open-{tool}.bat", "content": body, "exe": exe, "found": bool(exe)}
    if _SYSTEM == "Darwin":
        body = f'#!/usr/bin/env bash\n[ -f "{exe}" ] && open -a "{exe}" --args "{file_path}" 2>/dev/null \\\n   || open -a "{exe}" "{file_path}"\n'
        return {"filename": f"open-{tool}.command", "content": body, "exe": exe, "found": bool(exe)}
    body = f'#!/usr/bin/env bash\n[ -x "{exe}" ] && "{exe}" "{file_path}" &\n'
    return {"filename": f"open-{tool}.sh", "content": body, "exe": exe, "found": bool(exe)}

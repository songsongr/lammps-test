"""全局配置: 路径、容器参数、项目注册 (约定优于配置, 纯扫描)。

项目注册: 任何含 project.json 的项目目录即被自动注册 —
内置项目 (BUILTIN_DIRS, manifest 带 builtin: true) 与用户项目 (projects/) 同一机制,
新增/删除项目零代码改动、零重启 (每次 get_projects() 实时扫描)。
"""
import json
import os

# 项目根 = workbench/backend/app 的上三级
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# 运行时数据 (SQLite 任务库 + 任务日志), 已 gitignore
DATA_DIR = os.path.join(ROOT, "workbench", "data")
JOBS_LOG_DIR = os.path.join(DATA_DIR, "jobs")
DB_PATH = os.path.join(DATA_DIR, "workbench.db")

# Docker / LAMMPS 参数 (执行契约见 common/runner.py)
CONTAINER_NAME = "lammpsd"

# 容器 /data 挂载 = 独立数据目录 (不挂项目根); LAMMPS 任务采用「暂存-运行-回收」:
# 每个任务在数据目录下建独立工作区 jobs/<id>/, 宿主机侧直接拷入脚本与依赖,
# 容器内 -w /data/jobs/<id> 运行, 产物天然留在宿主机工作区中。
LAMMPS_DATA_HOST_DIR = os.path.join(ROOT, "lammps-data-docker")
CONTAINER_DATA_DIR = "/data"  # 须与 lammpsd 容器实际挂载一致 (health 接口会校验)

# 任务工作区保留天数 (终态任务超期后由后台 sweeper 清理; 0 = 不清理)
WORKSPACE_RETENTION_DAYS = 14

# 前端构建产物目录 (存在时由后端静态托管)
FRONTEND_DIST = os.path.join(ROOT, "workbench", "frontend", "dist")

# 本地工具配置 (VMD / Vesta 路径) — 用户在仪表盘浮窗手动填后持久化, 优先生效
LOCAL_TOOLS_CONFIG = os.path.join(DATA_DIR, "local_tools.json")

# 内置项目目录 (相对 ROOT, 可含子路径; project.json 带 builtin: true;
# 与用户 projects/ 同一注册机制)。内置项目统一收在 systems/ 下。
BUILTIN_DIRS = ("systems/strontium_adsorption", "systems/Montmorillonite-test", "systems/demos")
USER_PROJECTS_DIR = os.path.join(ROOT, "projects")


def _load_manifest(abs_dir: str) -> dict | None:
    path = os.path.join(abs_dir, "project.json")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def get_projects() -> list[dict]:
    """扫描注册全部项目: 内置目录 + projects/ 用户目录, 实时无缓存。"""
    projects: list[dict] = []
    seen_dirs: set[str] = set()

    scan_dirs: list[tuple[str, bool]] = [(d, True) for d in BUILTIN_DIRS]
    if os.path.isdir(USER_PROJECTS_DIR):
        scan_dirs += [(d, False) for d in sorted(os.listdir(USER_PROJECTS_DIR))
                      if os.path.isdir(os.path.join(USER_PROJECTS_DIR, d))]

    for d, is_builtin in scan_dirs:
        if d in seen_dirs:
            continue
        seen_dirs.add(d)
        base = os.path.basename(os.path.normpath(d))  # id 取末段 (与子目录布局解耦)
        abs_dir = os.path.join(ROOT, d) if is_builtin else os.path.join(USER_PROJECTS_DIR, d)
        rel_dir = d if is_builtin else f"projects/{d}"
        manifest = _load_manifest(abs_dir)
        if manifest is None:
            if is_builtin:
                # 内置目录缺 manifest 时兜底注册 (健壮性优先)
                projects.append({"id": base, "name": base, "dir": rel_dir,
                                 "description": "", "builtin": True})
            elif os.listdir(abs_dir):
                # 手动直建目录兜底注册: 文件夹即项目, 无需向导。
                # 以目录名注册并带 unregistered 标记 (前端角标引导补 project.json);
                # 空目录忽略 (避免随手 mkdir 产生噪音卡片)。
                projects.append({"id": base, "name": base, "dir": rel_dir, "description": "",
                                 "builtin": False, "unregistered": True})
            continue
        projects.append({
            "id": manifest.get("id", d),
            "name": manifest.get("name", d),
            "dir": rel_dir,
            "description": manifest.get("description", ""),
            "builtin": bool(manifest.get("builtin", is_builtin)),
        })
    return projects

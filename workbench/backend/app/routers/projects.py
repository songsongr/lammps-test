"""项目路由: 浏览 / 新建 (向导) / 体系配置读写 / 方法渲染 / 文件保存。"""
import hashlib
import json
import os
import re
import shutil
from datetime import datetime

from fastapi import APIRouter, HTTPException

from common import system_config
from common.lammps_lint import lint_lammps_input

from ..config import INBOX_DIR_NAME, ROOT, USER_PROJECTS_DIR, get_projects
from ..schemas import FileSaveRequest, ProjectCreate, RenderRequest, ScanRequest
from ..template_render import (get_method, list_methods, render_run_lmp,
                               sha256_text, write_if_changed)

router = APIRouter(prefix="/api")

_SCRIPT_EXTS = (".lmp", ".py")

_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_\-]{0,62}$")  # 复用同一 id 规则


def _project_or_404(project_id: str) -> tuple[dict, str]:
    project = next((p for p in get_projects() if p["id"] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="项目不存在")
    return project, os.path.join(ROOT, project["dir"])


def _load_project_meta(abs_dir: str) -> dict | None:
    path = os.path.join(abs_dir, "project.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _save_project_meta(abs_dir: str, meta: dict) -> None:
    with open(os.path.join(abs_dir, "project.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        f.write("\n")


# ---- 浏览 ----

@router.get("/projects")
async def list_projects() -> list[dict]:
    out = []
    for p in get_projects():
        abs_dir = os.path.join(ROOT, p["dir"])
        scripts = []
        if os.path.isdir(abs_dir):
            for name in sorted(os.listdir(abs_dir)):
                path = os.path.join(abs_dir, name)
                if not os.path.isfile(path):
                    continue
                ext = os.path.splitext(name)[1].lower()
                if ext == ".lmp":
                    kind = "lmp"
                elif ext == ".py":
                    kind = "python"
                else:
                    continue
                st = os.stat(path)
                scripts.append({
                    "name": name,
                    "kind": kind,
                    "size": st.st_size,
                    "mtime": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
                })
        out.append({
            "id": p["id"],
            "name": p["name"],
            "dir": p["dir"],
            "description": p["description"],
            "builtin": p.get("builtin", False),
            "unregistered": p.get("unregistered", False),
            "has_system": os.path.isfile(os.path.join(abs_dir, "system.json")),
            "scripts": scripts,
        })
    return out


# ---- 模板 (新建向导) ----

@router.get("/templates")
async def list_templates() -> dict:
    return {
        "system_profiles": [
            {"id": pid, **schema} for pid, schema in system_config.PROFILE_SCHEMAS.items()
        ],
        "methods": list_methods(),
        "water_models": list(system_config.WATER_PRESETS),
    }


# ---- 新建项目 ----

@router.post("/projects", status_code=201)
async def create_project(body: ProjectCreate) -> dict:
    user_dir = os.path.join(USER_PROJECTS_DIR, body.id)
    if os.path.exists(user_dir):
        raise HTTPException(status_code=409, detail=f"项目 ID 已存在: {body.id}")

    try:
        cfg = system_config.default_system(body.profile, body.water_model, body.system_overrides)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    errors = system_config.validate(cfg)
    if errors:
        raise HTTPException(status_code=400, detail="体系配置校验失败: " + "; ".join(errors))
    try:
        get_method(body.method_id)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

    os.makedirs(user_dir, exist_ok=True)
    meta = {
        "id": body.id,
        "name": body.name,
        "description": body.description,
        "profile": body.profile,
        "method_id": body.method_id,
        "method_params": body.method_params,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "rendered_sha": None,
    }
    _save_project_meta(user_dir, meta)
    system_config.save(os.path.join(user_dir, "system.json"), cfg)

    text = render_run_lmp(cfg, body.method_id, body.method_params)
    with open(os.path.join(user_dir, "run.lmp"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    meta["rendered_sha"] = sha256_text(text)
    _save_project_meta(user_dir, meta)

    return {"id": body.id, "dir": f"projects/{body.id}", "name": body.name,
            "system": cfg, "run_lmp": "run.lmp"}


def _file_sha(path: str) -> str | None:
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def compute_consistency(abs_dir: str, meta: dict) -> dict:
    """体系一致性链 (ANL「就绪检查表」思想的确定性落地):
    built_state: built=构建产物与当前参数一致 / stale=参数已改未重建 / never=从未构建
    script_state: sync=脚本与渲染指纹一致 / hand_edited=脚本被手改 / missing=未渲染
    """
    system_sha = _file_sha(os.path.join(abs_dir, "system.json"))
    if system_sha is None:
        return {}
    built_sha = meta.get("built_system_sha")
    rendered_sha = meta.get("rendered_sha")
    run_lmp_sha = _file_sha(os.path.join(abs_dir, "run.lmp"))
    built_state = ("built" if built_sha == system_sha
                   else "stale" if built_sha else "never")
    if run_lmp_sha is None:
        script_state = "missing"  # 无脚本 (无论是否渲染过都不能算 sync)
    else:
        script_state = "sync" if rendered_sha == run_lmp_sha else "hand_edited"
    return {"system_sha": system_sha, "built_system_sha": built_sha,
            "run_lmp_sha": run_lmp_sha, "rendered_sha": rendered_sha,
            "built_state": built_state, "script_state": script_state}


# ---- 体系配置 (单一真相源) ----

@router.get("/projects/{project_id}/system")
async def get_system(project_id: str) -> dict:
    _, abs_dir = _project_or_404(project_id)
    path = os.path.join(abs_dir, "system.json")
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="该项目无体系配置 (内置教学项目或未迁移)")
    cfg = system_config.load(path)
    meta = _load_project_meta(abs_dir) or {}
    consistency = compute_consistency(abs_dir, meta)
    return {"config": cfg, "errors": system_config.validate(cfg), "consistency": consistency,
            "meta": {"method_id": meta.get("method_id"), "method_params": meta.get("method_params", {})}}


@router.put("/projects/{project_id}/system")
async def put_system(project_id: str, body: dict) -> dict:
    project, abs_dir = _project_or_404(project_id)
    path = os.path.join(abs_dir, "system.json")
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="该项目无体系配置")
    errors = system_config.validate(body)
    if errors:
        raise HTTPException(status_code=400, detail="校验失败: " + "; ".join(errors))
    system_config.save(path, body)
    return {"saved": True, "note": "参数已保存; 需运行「重建体系」生成新 system.data, "
                                   "再「重新渲染」同步 run.lmp 的力场段落"}


# ---- 方法渲染 (system.json + 方法参数 → 脚本) ----

@router.post("/projects/{project_id}/render")
async def render_project(project_id: str, body: RenderRequest) -> dict:
    project, abs_dir = _project_or_404(project_id)
    meta = _load_project_meta(abs_dir) or {}
    method_id = body.method_id or meta.get("method_id", "nvt_production")
    params = body.params or meta.get("method_params", {})

    cfg_path = os.path.join(abs_dir, "system.json")
    if not os.path.isfile(cfg_path):
        raise HTTPException(status_code=404, detail="该项目无体系配置, 无法渲染")
    cfg = system_config.load(cfg_path)
    text = render_run_lmp(cfg, method_id, params)

    # 渲染产物统一为 run.lmp; rendered_sha 门控手改覆盖 (内置项目手写脚本已归档)
    out_path = os.path.join(abs_dir, "run.lmp")
    check = write_if_changed(out_path, text, meta.get("rendered_sha"))
    manual_edits = check["manual_edits"]
    if manual_edits and not body.force:
        raise HTTPException(status_code=409, detail="检测到 run.lmp 被手改过; 确认覆盖请传 force=true")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    meta["rendered_sha"] = sha256_text(text)
    _save_project_meta(abs_dir, meta)
    lint = lint_lammps_input(text, abs_dir)  # 渲染产物防御性 lint (模板异常兜底)
    return {"file": "run.lmp", "manual_edits_detected": manual_edits,
            "bytes": len(text.encode("utf-8")), "lint": lint}


@router.post("/projects/{project_id}/scan", status_code=201)
async def scan_project(project_id: str, body: ScanRequest) -> dict:
    """参数扫描: 对每个参数值渲染脚本副本并发起 LAMMPS 任务 (项目目录文件不动)。

    值只写入各任务工作区的脚本副本; 任务经队列串行执行, batch id 供列表过滤与对比。
    """
    from ..job_manager import manager

    project, abs_dir = _project_or_404(project_id)
    meta = _load_project_meta(abs_dir) or {}
    cfg_path = os.path.join(abs_dir, "system.json")
    if not os.path.isfile(cfg_path):
        raise HTTPException(status_code=404, detail="该项目无体系配置, 无法渲染扫描脚本")
    if not body.values:
        raise HTTPException(status_code=400, detail="values 不能为空")
    if len(body.values) > 20:
        raise HTTPException(status_code=400, detail="单次扫描最多 20 个值")

    cfg = system_config.load(cfg_path)
    method_id = meta.get("method_id", "nvt_production")
    from common.lammps_lint import lint_lammps_input
    try:
        method = get_method(method_id)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    known = {f["key"].split(".")[-1]: f["key"] for f in method["params"]}
    if body.param_key not in known:
        raise HTTPException(status_code=400,
                            detail=f"未知方法参数 {body.param_key}; 可选: {', '.join(sorted(known))}")

    base_params = dict(meta.get("method_params", {}))
    batch = "scan-" + datetime.now().strftime("%H%M%S") + "-" + os.urandom(2).hex()
    jobs = []
    for v in body.values:
        params = {**base_params, body.param_key: v}
        text = render_run_lmp(cfg, method_id, params)
        lint = lint_lammps_input(text, abs_dir)  # 与 create_job 同一拦截门
        if lint["errors"]:
            raise HTTPException(status_code=400,
                                detail=f"扫描值 {v} 渲染脚本未通过 lint: " + "; ".join(lint["errors"]))
        job = await manager.start(project_id, "run.lmp", "lmp",
                                  body.omp_threads, script_text=text, batch=batch)
        try:
            from .. import store as _store
            fp = json.loads(job.get("fingerprint") or "{}")
            fp["scan"] = {body.param_key: v}
            _store.update(job["id"], fingerprint=json.dumps(fp, ensure_ascii=False))
        except Exception:
            pass
        jobs.append({"id": job["id"], "value": v, "status": job["status"]})
    return {"batch": batch, "param": body.param_key, "values": body.values, "jobs": jobs}


# ---- 历史研究迁移暂存 (projects/_inbox/<id>/) ----

def _inbox_root() -> str:
    return os.path.join(USER_PROJECTS_DIR, INBOX_DIR_NAME)


def _inbox_dir_or_404(inbox_id: str) -> str:
    if not _ID_RE.match(inbox_id):
        raise HTTPException(status_code=400, detail=f"非法暂存目录 id: {inbox_id}")
    abs_dir = os.path.join(_inbox_root(), inbox_id)
    if not os.path.isdir(abs_dir):
        raise HTTPException(status_code=404,
                            detail=f"暂存目录不存在: projects/{INBOX_DIR_NAME}/{inbox_id}")
    return abs_dir


@router.get("/projects/inbox")
async def list_inbox() -> dict:
    """列出迁移暂存区待入库条目 (agent 按「手动创建指南」迁入的副本)。

    正式项目库 (get_projects) 扫描时跳过 _inbox, 暂存产物不会混入项目列表;
    用户在此审阅 → 确认入库 (move + 注册) 或丢弃 (仅删副本, 旧路径不动)。
    """
    root = _inbox_root()
    registered_ids = {p["id"] for p in get_projects()}
    items = []
    if os.path.isdir(root):
        for name in sorted(os.listdir(root)):
            abs_dir = os.path.join(root, name)
            if not os.path.isdir(abs_dir) or name.startswith("."):
                continue
            meta = _load_project_meta(abs_dir) or {}
            files = []
            total = 0
            for fn in sorted(os.listdir(abs_dir)):
                fp = os.path.join(abs_dir, fn)
                if os.path.isfile(fp):
                    st = os.stat(fp)
                    total += st.st_size
                    files.append({"name": fn, "size": st.st_size})
            target_id = str(meta.get("id") or name)
            items.append({
                "id": name,
                "name": meta.get("name") or name,
                "description": meta.get("description") or "",
                "has_manifest": bool(meta),
                "has_migration_manifest":
                    os.path.isfile(os.path.join(abs_dir, "migration_manifest.md")),
                "files": files,
                "file_count": len(files),
                "total_bytes": total,
                "target_id": target_id,
                "target_conflict": target_id in registered_ids,
                "mtime": datetime.fromtimestamp(os.stat(abs_dir).st_mtime).isoformat(timespec="seconds"),
            })
    return {"dir": f"projects/{INBOX_DIR_NAME}", "items": items}


@router.post("/projects/inbox/{inbox_id}/confirm", status_code=201)
async def confirm_inbox(inbox_id: str) -> dict:
    """确认入库: 暂存目录整体移动为 projects/<target_id>/, 进入正常自动注册。

    - manifest 缺失时补最小 manifest (与兜底注册哲学一致);
    - 目标已存在 → 409, 不做任何合并 (防覆盖既有项目);
    - 不通过此入口则暂存目录永远不会进入项目列表。
    """
    abs_dir = _inbox_dir_or_404(inbox_id)
    meta = _load_project_meta(abs_dir) or {}
    manifest_backfilled = not meta
    target_id = str(meta.get("id") or inbox_id)
    if not _ID_RE.match(target_id):
        raise HTTPException(
            status_code=400,
            detail=f"manifest id 不合法: {target_id} (字母数字开头, ≤63 位字母/数字/_/-)")
    target = os.path.join(USER_PROJECTS_DIR, target_id)
    if os.path.exists(target):
        raise HTTPException(status_code=409,
                            detail=f"目标项目已存在: projects/{target_id}; "
                                   f"请改暂存 manifest 的 id 后再确认入库")
    if manifest_backfilled:
        meta = {"id": target_id, "name": target_id,
                "description": "历史研究迁移入库 (自动补最小 manifest)"}
    meta["id"] = target_id
    meta.setdefault("name", target_id)
    meta["migrated_at"] = datetime.now().isoformat(timespec="seconds")
    _save_project_meta(abs_dir, meta)
    os.makedirs(USER_PROJECTS_DIR, exist_ok=True)
    shutil.move(abs_dir, target)
    return {"confirmed": True, "id": target_id, "dir": f"projects/{target_id}",
            "manifest_backfilled": manifest_backfilled}


@router.delete("/projects/inbox/{inbox_id}")
async def discard_inbox(inbox_id: str) -> dict:
    """丢弃暂存副本: 仅删除工作台内 _inbox 副本, 用户旧路径文件不受影响。"""
    abs_dir = _inbox_dir_or_404(inbox_id)
    shutil.rmtree(abs_dir, ignore_errors=True)
    return {"discarded": True, "id": inbox_id}


@router.delete("/projects/{project_id}")
async def delete_project(project_id: str) -> dict:
    """删除用户自建项目目录 (内置项目不可删)。"""
    project, abs_dir = _project_or_404(project_id)
    if project.get("builtin", False):
        raise HTTPException(status_code=403, detail="内置项目不可删除")
    if not os.path.abspath(abs_dir).startswith(os.path.abspath(USER_PROJECTS_DIR)):
        raise HTTPException(status_code=403, detail="仅允许删除 projects/ 目录下的自建项目")
    shutil.rmtree(abs_dir, ignore_errors=True)
    return {"deleted": True, "id": project_id}


@router.get("/projects/{project_id}/system-data")
async def get_system_data(project_id: str) -> dict:
    """返回项目 system.data 文本与绝对路径 (3D 预览专用; 体积上限 32 MB)。"""
    project, abs_dir = _project_or_404(project_id)
    path = os.path.join(abs_dir, "system.data")
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="该项目暂无 system.data, 请先「重建体系」")
    size = os.path.getsize(path)
    if size > 32 * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"system.data 过大 ({size} 字节), 浏览器预览不适用")
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    xyz = None
    xyz_error = None
    try:
        from common.lammps_data import lammps_data_to_xyz
        xyz = lammps_data_to_xyz(text)
    except Exception as e:  # 结构特殊/赝品质量 — 前端显式提示而非静默渲染垃圾
        xyz_error = str(e)
    return {"path": path, "bytes": size, "text": text, "xyz": xyz, "xyz_error": xyz_error}


# ---- 文件保存 (在线编辑) ----

@router.put("/projects/{project_id}/files/{name}")
async def save_file(project_id: str, name: str, body: FileSaveRequest) -> dict:
    _, abs_dir = _project_or_404(project_id)
    if os.path.basename(name) != name or os.path.splitext(name)[1].lower() not in _SCRIPT_EXTS:
        raise HTTPException(status_code=400, detail="仅允许保存项目目录下的 .lmp / .py 文件")
    path = os.path.join(abs_dir, name)
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="文件不存在 (仅支持编辑既有文件)")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body.content)
    return {"saved": True, "file": name, "bytes": len(body.content.encode("utf-8"))}

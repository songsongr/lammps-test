"""项目路由: 浏览 / 新建 (向导) / 体系配置读写 / 方法渲染 / 文件保存。"""
import hashlib
import json
import os
import shutil
from datetime import datetime

from fastapi import APIRouter, HTTPException

from common import system_config
from common.lammps_lint import lint_lammps_input

from ..config import ROOT, USER_PROJECTS_DIR, get_projects
from ..schemas import FileSaveRequest, ProjectCreate, RenderRequest
from ..template_render import (get_method, list_methods, render_run_lmp,
                               sha256_text, write_if_changed)

router = APIRouter(prefix="/api")

_SCRIPT_EXTS = (".lmp", ".py")


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
    consistency = compute_consistency(abs_dir, _load_project_meta(abs_dir) or {})
    return {"config": cfg, "errors": system_config.validate(cfg), "consistency": consistency}


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
    return {"path": path, "bytes": size, "text": text}


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

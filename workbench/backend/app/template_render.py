"""方法模板渲染: system.json + 方法参数 → run.lmp (Jinja2)。

pair_coeff / 类型分组从 system.json 推导 — 力场单一真相源,
消灭 build 脚本与 .lmp 的双源漂移。
"""
import hashlib
import json
import os

import jinja2

TEMPLATES_DIR = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates"))


def list_methods() -> list[dict]:
    out: list[dict] = []
    methods_dir = os.path.join(TEMPLATES_DIR, "methods")
    for name in sorted(os.listdir(methods_dir)):
        mj = os.path.join(methods_dir, name, "method.json")
        if os.path.isfile(mj):
            with open(mj, encoding="utf-8") as f:
                out.append(json.load(f))
    return out


def get_method(method_id: str) -> dict:
    for m in list_methods():
        if m["id"] == method_id:
            return m
    raise KeyError(f"未知方法模板: {method_id}")


def _derive_types(system: dict) -> dict:
    """从体系类型表推导模板上下文: 表面(可选)/水/离子。"""
    types = system["atom_types"]
    surf = next((t for t in types if t["name"] == "Surf"), None)
    ow = next(t for t in types if t["name"] == "Ow")
    hw = next(t for t in types if t["name"] == "Hw")
    ions = [t for t in types if t["name"] not in ("Surf", "Ow", "Hw")]
    return {
        "surf_id": surf["id"] if surf else None,
        "surf_name": surf["name"] if surf else None,
        "ow_id": ow["id"],
        "hw_id": hw["id"],
        "ion_types": ions,
    }


def render_run_lmp(system: dict, method_id: str, params: dict | None = None) -> str:
    method = get_method(method_id)
    merged = {p["key"]: p["default"] for p in method.get("params", [])}
    merged.update(params or {})
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
        trim_blocks=True, lstrip_blocks=True,
    )
    tmpl = env.get_template(f"methods/{method_id}/run.lmp.j2")
    return tmpl.render(system=system, method_id=method_id, params=merged,
                       **_derive_types(system))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_if_changed(path: str, text: str, stored_sha: str | None) -> dict:
    """写入渲染产物; 检测手改 (现文件哈希 ≠ 上次渲染记录) → 返回提示, 由调用方决定 force。"""
    manual_edits = False
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            current = f.read()
        if stored_sha is not None and sha256_text(current) != stored_sha:
            manual_edits = True
    return {"manual_edits": manual_edits, "sha": sha256_text(text)}

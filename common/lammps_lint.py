"""LAMMPS 输入脚本确定性 lint — 发车前静态检查 (借鉴 chatmaterials/lammps-workflows
的 check 思想与 ANL LAMMPS-Agents 的"输入评审"思想, 用代码强制而非提示词自律)。

纯函数、零依赖 (不 import workbench), CLI 与工作台同源可用。
返回 {errors, warnings}: errors 阻止发车, warnings 放行仅提示。
"""
import os
import re

# 占位符标记 (力场未填/骨架未完成的典型残留); 大小写不敏感
_PLACEHOLDER_PAT = re.compile(r"replace-with|placeholder|tbd\b|todo\b|fixme\b", re.IGNORECASE)
# 旧挂载约定残留: /data/<项目>/... 绝对路径 (2026-08-28 起必须用相对路径)
_LEGACY_MOUNT_PAT = re.compile(r"^\s*\S*/data/", )
# 引用依赖的命令
_REF_PAT = re.compile(r"\b(read_data|include|read_restart)\s+(\S+)")
_UNIT_KW = ("real", "metal", "si", "cgs", "electron", "micro", "nano", "lj")


def lint_lammps_input(text: str, project_dir: str | None = None) -> dict:
    """静态检查输入脚本。project_dir 提供时校验引用文件存在性。"""
    errors: list[str] = []
    warnings: list[str] = []
    has_units = has_pair_style = has_run = False

    for lineno, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        is_comment = stripped.startswith("#")
        code = stripped.split("#", 1)[0].strip()
        low = raw.lower()

        if _PLACEHOLDER_PAT.search(raw):
            (warnings if is_comment else errors).append(
                f"L{lineno}: 疑似占位符残留 «{stripped[:60]}» — 力场/参数未填写完成")
        if not is_comment and code:
            if _LEGACY_MOUNT_PAT.match(code):
                warnings.append(
                    f"L{lineno}: 出现 /data/ 绝对路径 — 旧挂载约定已废弃, 请改用相对路径")
            first = code.split()[0]
            if first == "units":
                has_units = True
                unit = code.split()[1] if len(code.split()) > 1 else ""
                if unit.lower() not in _UNIT_KW:
                    errors.append(f"L{lineno}: units 值 «{unit}» 不合法")
            if first == "pair_style":
                has_pair_style = True
            if first in ("run", "minimize"):
                has_run = True
                if first == "run":
                    try:
                        steps = int(code.split()[1])
                        if steps <= 0:
                            warnings.append(f"L{lineno}: run 0 — 仅评估 thermo, 无实际模拟")
                    except (IndexError, ValueError):
                        errors.append(f"L{lineno}: run 步数缺失或非整数")

        for m in _REF_PAT.finditer(code):
            ref = m.group(2).strip('"\'')
            if ref.startswith("/data/"):
                warnings.append(f"L{lineno}: {m.group(1)} 引用 /data/ 绝对路径 — 旧挂载约定已废弃")
            elif project_dir and not os.path.isfile(os.path.join(project_dir, ref)):
                errors.append(
                    f"L{lineno}: {m.group(1)} 引用的文件 «{ref}» 在项目目录中不存在")

    if not has_units:
        errors.append("缺少 units 命令 — 缺省为 lj 单位, 对真实体系是静默的科学错误")
    if not has_pair_style:
        errors.append("缺少 pair_style 命令 — 无相互作用定义")
    if not has_run:
        errors.append("缺少 run / minimize — 脚本不会执行任何模拟")

    return {"errors": errors, "warnings": warnings}

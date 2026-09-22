"""蒙脱石 CIF → 层间水体系构建器 (移植自 Montmorillonite-test/convert_cif.py)。

流程: 解析 CIF → 超胞 → CLAYFF 分型 + OH 加氢 → 层间水 (格点法) → 电中性修正 → data 文件。
算法与 RNG 消费顺序 (random: Ca 占位/格点洗牌; np.random: 水取向) 与原脚本一致, 同种子可复现。
CIF 绑定阈值 (OH 分数坐标 z 等) 由 system.json 的 cif_binding 块提供 — 换 CIF 需重新标定。
"""
from __future__ import annotations

import os

import numpy as np

from .base import BuildOutput, type_map
from ..water_builder import random_water_orientation

_FRAMEWORK_TYPES = (1, 2, 3, 5, 6)  # ob/obos/oh/st/ao


def _parse_cif(path: str) -> tuple[dict, list[dict]]:
    cell: dict = {}
    atoms_raw: list[dict] = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("_cell_length_a"):
            cell["a"] = float(line.split()[-1])
        elif line.startswith("_cell_length_b"):
            cell["b"] = float(line.split()[-1])
        elif line.startswith("_cell_length_c"):
            cell["c"] = float(line.split()[-1])
        if line.startswith("loop_"):
            i += 1
            keys = []
            while i < len(lines) and lines[i].strip().startswith("_"):
                keys.append(lines[i].strip())
                i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("_") \
                    and not lines[i].strip().startswith("loop_"):
                parts = lines[i].strip().split()
                if len(parts) >= 8:
                    atoms_raw.append({
                        "label": parts[0],
                        "occ": float(parts[1]),
                        "frac": (float(parts[2]), float(parts[3]), float(parts[4])),
                        "element": parts[7],
                    })
                i += 1
            continue
        i += 1
    if not all(k in cell for k in ("a", "b", "c")):
        raise ValueError(f"CIF 解析失败: 未找到完整晶胞参数 ({path})")
    return cell, atoms_raw


def _classify_o(z_frac: float, cell: dict, bind: dict, tids: dict) -> int:
    z = z_frac * cell["c"]
    is_oh = bind["oh_frac_z_min"] <= (z_frac % 1.0) <= bind["oh_frac_z_max"]
    if z < bind["z_ob_max"]:
        return tids["ob"]
    if z < bind["z_obos_max"]:
        return tids["obos"]
    if bind["z_oh_min"] <= z < bind["z_oh_max"]:
        return tids["oh"] if is_oh else tids["obos"]
    return tids["ob"]


def build(cfg: dict, rng, project_dir: str | None = None) -> BuildOutput:
    np.random.seed(cfg.get("seed", 42))  # 水取向用全局 np.random (与 convert_cif.py 一致)
    types = cfg["atom_types"]
    tmap = type_map(types)
    tids = {t["name"]: t["id"] for t in types}
    bind = cfg["cif_binding"]
    sup = cfg["supercell"]
    iw = cfg["interlayer_water"]

    # CIF 路径解析: 相对项目目录
    cif_path = cfg["cif_file"]
    if project_dir and not os.path.isabs(cif_path):
        cif_path = os.path.join(project_dir, cif_path)
    if not os.path.isfile(cif_path):
        raise ValueError(f"CIF 文件不存在: {cif_path} (请将其放入项目目录)")

    # ---- 1. 解析 CIF ----
    cell, atoms_raw = _parse_cif(cif_path)

    # ---- 2. 超胞 (Ca 按占据率随机保留) ----
    ca_positions = [a for a in atoms_raw if a["element"] == "Ca"]
    non_ca = [a for a in atoms_raw if a["element"] != "Ca"]
    super_atoms: list[dict] = []
    atom_id = 0
    for ix in range(sup["nx"]):
        for iy in range(sup["ny"]):
            for iz in range(sup["nz"]):
                shift = (ix / sup["nx"], iy / sup["ny"], iz / sup["nz"])
                for a in non_ca:
                    atom_id += 1
                    super_atoms.append({
                        "id": atom_id, "element": a["element"], "mol": 0, "charge": 0.0,
                        "frac": ((a["frac"][0] + shift[0]) / sup["nx"],
                                 (a["frac"][1] + shift[1]) / sup["ny"],
                                 (a["frac"][2] + shift[2]) / sup["nz"]),
                    })
                for a in ca_positions:
                    if rng.random() < a["occ"]:
                        atom_id += 1
                        super_atoms.append({
                            "id": atom_id, "element": "Ca", "mol": 0, "charge": 0.0,
                            "frac": ((a["frac"][0] + shift[0]) / sup["nx"],
                                     (a["frac"][1] + shift[1]) / sup["ny"],
                                     (a["frac"][2] + shift[2]) / sup["nz"]),
                        })
    super_cell = {"a": cell["a"] * sup["nx"], "b": cell["b"] * sup["ny"], "c": cell["c"] * sup["nz"]}

    # ---- 3. CLAYFF 分型 + OH 加氢 ----
    oh_oxygens = []
    for a in super_atoms:
        elem = a["element"]
        if elem == "Si":
            a["type"] = tids["st"]
        elif elem == "Al":
            a["type"] = tids["ao"]
        elif elem == "Ca":
            a["type"] = tids["ca"]
        elif elem == "O":
            a["type"] = _classify_o(a["frac"][2], super_cell, bind, tids)
        else:
            raise ValueError(f"未知元素: {elem} (label={a.get('label')})")
        a["charge"] = tmap[a["type"]]["charge"]
        if a["type"] == tids["oh"]:
            oh_oxygens.append(a)

    new_atoms = list(super_atoms)
    next_id = max(a["id"] for a in super_atoms) + 1
    oh_bond_pairs: list[tuple] = []  # (oh O id, ho id) — CLAYFF 羟基 O-H 键 (与水同键型)
    for oa in oh_oxygens:  # H 沿 +z 指向层间, 1.0 Å
        new_atoms.append({
            "id": next_id, "element": "H", "mol": 0,
            "type": tids["ho"], "charge": tmap[tids["ho"]]["charge"],
            "frac": (oa["frac"][0], oa["frac"][1], oa["frac"][2] + 1.0 / super_cell["c"]),
        })
        oh_bond_pairs.append((oa["id"], next_id))
        next_id += 1
    atoms = new_atoms

    # ---- 4. 层间水 (格点法, SPC/E) ----
    def frac_to_cart(f):
        return np.array([f[0] * super_cell["a"], f[1] * super_cell["b"], f[2] * super_cell["c"]])

    framework = [a for a in atoms if a["type"] in (*_FRAMEWORK_TYPES, tids["ca"], tids["ho"])]
    fw_positions = [frac_to_cart(a["frac"]) for a in framework]

    z_values = [a["frac"][2] * super_cell["c"] for a in atoms if a["type"] in _FRAMEWORK_TYPES]
    inter_z_min = (max(z_values) if z_values else 8.0) + 2.0
    inter_z_max = super_cell["c"] - 0.5

    next_id = max(a["id"] for a in atoms) + 1
    next_mol = 1
    water_os: list[np.ndarray] = []
    water_mols: list[tuple] = []

    nx_grid = max(1, int(super_cell["a"] / iw["grid_xy"]))
    ny_grid = max(1, int(super_cell["b"] / iw["grid_xy"]))
    nz_grid = max(1, int((inter_z_max - inter_z_min) / iw["grid_z"]))
    x_pos = [(i + 0.5) * super_cell["a"] / nx_grid for i in range(nx_grid)]
    y_pos = [(j + 0.5) * super_cell["b"] / ny_grid for j in range(ny_grid)]
    z_pos = [inter_z_min + (k + 0.5) * (inter_z_max - inter_z_min) / nz_grid for k in range(nz_grid)]

    placed = 0
    grid_order = [(ix, iy, iz) for ix in range(nx_grid) for iy in range(ny_grid) for iz in range(nz_grid)]
    rng.shuffle(grid_order)

    for ix, iy, iz in grid_order:
        if placed >= iw["target"]:
            break
        o_pos = np.array([x_pos[ix], y_pos[iy], z_pos[iz]])
        if any(np.linalg.norm(o_pos - fw) < iw["min_dist_o_fw"] for fw in fw_positions):
            continue
        if any(np.linalg.norm(o_pos - wo) < iw["grid_xy"] for wo in water_os):
            continue
        h_rot = random_water_orientation()  # np.random 全局流 (构建入口已 seed)
        h1_pos, h2_pos = o_pos + h_rot[0], o_pos + h_rot[1]
        h_too_close = False
        for hpos in (h1_pos, h2_pos):
            if any(np.linalg.norm(hpos - fw) < iw["min_dist_h_fw"] for fw in fw_positions):
                h_too_close = True
                break
        if h_too_close:
            continue
        if not (0 < h1_pos[0] < super_cell["a"] and 0 < h1_pos[1] < super_cell["b"] and 0 < h1_pos[2] < super_cell["c"]):
            continue
        if not (0 < h2_pos[0] < super_cell["a"] and 0 < h2_pos[1] < super_cell["b"] and 0 < h2_pos[2] < super_cell["c"]):
            continue

        def to_frac(p):
            return tuple(f % 1.0 for f in (p[0] / super_cell["a"], p[1] / super_cell["b"], p[2] / super_cell["c"]))

        atoms.append({"id": next_id, "mol": next_mol, "type": tids["ow"],
                      "charge": tmap[tids["ow"]]["charge"], "frac": to_frac(o_pos)})
        atoms.append({"id": next_id + 1, "mol": next_mol, "type": tids["hw"],
                      "charge": tmap[tids["hw"]]["charge"], "frac": to_frac(h1_pos)})
        atoms.append({"id": next_id + 2, "mol": next_mol, "type": tids["hw"],
                      "charge": tmap[tids["hw"]]["charge"], "frac": to_frac(h2_pos)})
        water_os.append(o_pos)
        water_mols.append((atoms[-3], atoms[-2], atoms[-1]))
        next_id += 3
        next_mol += 1
        placed += 1

    # ---- 5. 电中性修正 (均匀偏移骨架 O) ----
    warnings: list[str] = []
    total_q = sum(a["charge"] for a in atoms)
    if abs(total_q) >= 1e-6:
        fw_o = [a for a in atoms if a["type"] in (tids["ob"], tids["obos"], tids["oh"])]
        shift = -total_q / len(fw_o)
        for a in fw_o:
            a["charge"] += shift
        warnings.append(f"电中性修正: 骨架 O 电荷均匀偏移 {shift:+.6f} (e)")
        total_q = sum(a["charge"] for a in atoms)

    # ---- 输出 ----
    out_atoms = []
    for a in atoms:
        cart = frac_to_cart(a["frac"])
        out_atoms.append((a["id"], a["type"], a["mol"], a["charge"],
                          float(cart[0]), float(cart[1]), float(cart[2])))

    bonds: list[tuple] = []
    angles: list[tuple] = []
    # 羟基 O-H 键 (CLAYFF: 与水同一谐振子键型 554.13 kcal/mol/A^2, r0=1.0)。
    # 缺此键时 ho 是无约束点电荷 (eps=0), minimize 会库仑坍缩进 O (PE -> -1e17)。
    hid = 1
    for oid, ho_id in oh_bond_pairs:
        bonds.append((hid, 1, oid, ho_id))
        hid += 1
    for k, (wo, wh1, wh2) in enumerate(water_mols, start=1):
        bonds.append((hid + 2 * k - 2, 1, wo["id"], wh1["id"]))
        bonds.append((hid + 2 * k - 1, 1, wo["id"], wh2["id"]))
        angles.append((k, 1, wh1["id"], wo["id"], wh2["id"]))

    for t in types:
        if t.get("warning"):
            warnings.append(f"{t['name']}: {t['warning']}")

    return BuildOutput(
        title=cfg.get("title", "Montmorillonite with interlayer water"),
        box=(0.0, super_cell["a"], 0.0, super_cell["b"], 0.0, super_cell["c"]),
        atom_types=types,
        atoms=out_atoms,
        bonds=bonds,
        angles=angles,
        warnings=warnings,
    )

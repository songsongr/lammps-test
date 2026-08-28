"""带电表面 + 水层 + 离子 体系构建器 (移植自 strontium_adsorption/build_system.py)。

算法与 RNG 调用顺序与原脚本逐行一致, 同种子可复现旧产物;
区别仅在于: 参数全部来自 system.json (不再硬编码)。
"""
from __future__ import annotations

import math

from .. import system_config
from .base import BuildOutput, place_water, type_map, water_geometry


def build(cfg: dict, rng, project_dir: str | None = None) -> BuildOutput:
    types = cfg["atom_types"]
    tmap = type_map(types)
    tids = {t["name"]: t["id"] for t in types}
    geo = cfg["geometry"]
    ions = cfg["ions"]

    # ---- 表面 ----
    a = geo["surface"]["a"]
    nx, ny = geo["surface"]["nx"], geo["surface"]["ny"]
    layers = geo["surface"]["layers"]
    occupancy = geo["surface"]["occupancy"]
    surf_type = tids["Surf"]
    ow_type, hw_type = tids["Ow"], tids["Hw"]
    surf_charge = tmap[surf_type]["charge"]

    surf_atoms: list[tuple] = []
    aid = 0
    for iz in range(layers):
        for iy in range(ny):
            for ix in range(nx):
                x = ix * a + (iz % 2) * a / 2
                y = iy * a + (iz % 2) * a / 2
                z = iz * a
                # 占位筛选: 原脚本 occupancy=0.5 时等价于 (ix+iy+iz)%2==0 菱形图案
                if occupancy == 0.5:
                    keep = (ix + iy + iz) % 2 == 0
                else:
                    keep = rng.random() < occupancy
                if keep:
                    aid += 1
                    surf_atoms.append((aid, surf_type, 0, surf_charge, x, y, z))

    # ---- 盒子 ----
    xs, ys = nx * a, ny * a
    water = geo["water"]
    vacuum = geo["vacuum"]
    z_max_surf = max(s[5] for s in surf_atoms) + 1.0
    zlo = -1.0
    zhi = water["z_start"] + water["thickness"] + vacuum
    box = (0.0, xs, 0.0, ys, zlo, zhi)

    # ---- 加水 (网格 + 与表面最小距离 + 随机取向) ----
    sp = water["grid"]
    nwx = max(1, int(xs / sp))
    nwy = max(1, int(ys / sp))
    nwz = max(1, int(water["thickness"] / sp))
    oh_dist, angle_half = water_geometry(cfg)

    q_ow = tmap[ow_type]["charge"]
    q_hw = tmap[hw_type]["charge"]
    min_d2_surf = water["min_dist_surface"] ** 2
    surf_positions = [(s[4], s[5], s[6]) for s in surf_atoms]

    water_atoms: list[tuple] = []
    water_mols = 0
    for iz in range(nwz):
        for iy in range(nwy):
            for ix in range(nwx):
                cx = (ix + 0.5) * sp
                cy = (iy + 0.5) * sp
                cz = water["z_start"] + (iz + 0.5) * sp
                too_close = False
                for sx, sy, sz in surf_positions:
                    dx, dy, dz = cx - sx, cy - sy, cz - sz
                    if dx * dx + dy * dy + dz * dz < min_d2_surf:
                        too_close = True
                        break
                if too_close:
                    continue
                aid += 1
                place_water(water_atoms, rng, aid, ow_type, hw_type, q_ow, q_hw,
                            cx, cy, cz, oh_dist, angle_half, water_mols + 1)
                aid += 2
                water_mols += 1

    # ---- 离子 (替换水分子) ----
    water_vol_l = xs * ys * water["thickness"] * 1e-27
    na = 6.022e23
    id_cation, id_anion = system_config.ion_type_ids(cfg)
    n_cation = max(1, int(ions["conc_mol"] * water_vol_l * na)) + ions["extra_sr"]
    n_anion = (n_cation - ions["extra_sr"]) * 2

    n_remove = n_cation + n_anion
    if n_remove > water_mols:
        raise ValueError(f"离子数 ({n_remove}) 超过水分子数 ({water_mols}), 请降低浓度或加大水层")
    indices = list(range(water_mols))
    rng.shuffle(indices)
    remove_set = set(indices[:n_remove])

    kept_atoms: list[tuple] = []
    removed_positions: list[tuple] = []
    for i in range(water_mols):
        if i in remove_set:
            ox = water_atoms[i * 3][4]
            oy = water_atoms[i * 3][5]
            oz = water_atoms[i * 3][6]
            removed_positions.append((ox, oy, oz))
        else:
            kept_atoms.extend(water_atoms[i * 3:i * 3 + 3])

    ion_atoms: list[tuple] = []
    n_surf = len(surf_atoms)
    for k, (ix, iy, iz) in enumerate(removed_positions):
        itype = id_cation if k < n_cation else id_anion
        aid = n_surf + len(kept_atoms) + k + 1
        ion_atoms.append((aid, itype, 0, tmap[itype]["charge"], ix, iy, iz))

    all_atoms = surf_atoms + kept_atoms + ion_atoms
    all_atoms = [(i + 1, t, m, q, x, y, z)
                 for i, (_, t, m, q, x, y, z) in enumerate(all_atoms)]
    n_kept = water_mols - n_remove

    # ---- 键/角 (水分子连续排布, id = n_surf + k*3 + 1) ----
    bonds = []
    angles = []
    for k in range(n_kept):
        oid = n_surf + k * 3 + 1
        for h in (1, 2):
            bonds.append((len(bonds) + 1, 1, oid, oid + h))
        angles.append((k + 1, 1, oid + 1, oid, oid + 2))

    total_charge = sum(tmap[t]["charge"] for _, t, *_ in all_atoms)
    warnings = [f"{t['name']}: {t['warning']}" for t in types if t.get("warning")]
    if abs(total_charge) > 1e-6:
        warnings.append(f"总电荷 {total_charge:.4f} 非零 (表面电荷由离子平衡, 数值漂移为舍入)")

    return BuildOutput(
        title=cfg.get("title", "Charged surface + water + salt"),
        box=box,
        atom_types=types,
        atoms=all_atoms,
        bonds=bonds,
        angles=angles,
        warnings=warnings,
    )

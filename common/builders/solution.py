"""均相溶液体系构建器: 纯水盒子 + 盐离子 (无表面)。

参数来自 system.json (profile=solution):
geometry.box{x,y,z}, geometry.water.grid, ions.conc_mol, atom_types (Ow/Hw/阳/阴)。
"""
from __future__ import annotations

from .. import system_config
from .base import BuildOutput, place_water, type_map, water_geometry


def build(cfg: dict, rng, project_dir: str | None = None) -> BuildOutput:
    types = cfg["atom_types"]
    tmap = type_map(types)
    tids = {t["name"]: t["id"] for t in types}
    ow_type, hw_type = tids["Ow"], tids["Hw"]
    geo = cfg["geometry"]
    ions = cfg["ions"]

    bx, by, bz = geo["box"]["x"], geo["box"]["y"], geo["box"]["z"]
    sp = geo["water"]["grid"]
    oh_dist, angle_half = water_geometry(cfg)

    q_ow = tmap[ow_type]["charge"]
    q_hw = tmap[hw_type]["charge"]
    id_cation, id_anion = system_config.ion_type_ids(cfg)

    nwx = max(1, int(bx / sp))
    nwy = max(1, int(by / sp))
    nwz = max(1, int(bz / sp))

    atoms: list[tuple] = []
    water_mols = 0
    for iz in range(nwz):
        for iy in range(nwy):
            for ix in range(nwx):
                aid = water_mols * 3 + 1
                place_water(atoms, rng, aid, ow_type, hw_type, q_ow, q_hw,
                            (ix + 0.5) * sp, (iy + 0.5) * sp, (iz + 0.5) * sp,
                            oh_dist, angle_half, water_mols + 1)
                water_mols += 1

    water_vol_l = bx * by * bz * 1e-27
    na = 6.022e23
    n_cation = max(1, int(ions["conc_mol"] * water_vol_l * na))
    n_anion = n_cation * 2

    n_remove = n_cation + n_anion
    if n_remove > water_mols:
        raise ValueError(f"离子数 ({n_remove}) 超过水分子数 ({water_mols}), 请降低浓度或加大盒子")
    indices = list(range(water_mols))
    rng.shuffle(indices)
    remove_set = set(indices[:n_remove])

    kept: list[tuple] = []
    removed_positions: list[tuple] = []
    for i in range(water_mols):
        if i in remove_set:
            removed_positions.append((atoms[i * 3][4], atoms[i * 3][5], atoms[i * 3][6]))
        else:
            kept.extend(atoms[i * 3:i * 3 + 3])

    ion_atoms = []
    for k, (x, y, z) in enumerate(removed_positions):
        itype = id_cation if k < n_cation else id_anion
        ion_atoms.append((len(kept) + k + 1, itype, 0, tmap[itype]["charge"], x, y, z))

    all_atoms = [(i + 1, t, m, q, x, y, z)
                 for i, (_, t, m, q, x, y, z) in enumerate(kept + ion_atoms)]
    n_kept = water_mols - n_remove

    bonds = []
    angles = []
    for k in range(n_kept):
        oid = k * 3 + 1
        for h in (1, 2):
            bonds.append((len(bonds) + 1, 1, oid, oid + h))
        angles.append((k + 1, 1, oid + 1, oid, oid + 2))

    total_charge = sum(t["charge"] for t in [tmap[t] for _, t, *_ in all_atoms])
    warnings = [f"{t['name']}: {t['warning']}" for t in types if t.get("warning")]

    return BuildOutput(
        title=cfg.get("title", "Homogeneous solution"),
        box=(0.0, bx, 0.0, by, 0.0, bz),
        atom_types=types,
        atoms=all_atoms,
        bonds=bonds,
        angles=angles,
        warnings=warnings,
    )

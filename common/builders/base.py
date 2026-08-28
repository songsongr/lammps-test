"""体系构建器: 从 system.json 确定性构建 LAMMPS data 文件。

每个 profile 一个 build(cfg, rng) 函数, 返回 BuildOutput;
base 提供公共写入器与报告。移植自 build_system.py 的算法保持
RNG 调用顺序一致, 同种子可逐字节复现旧产物 (标题/注释除外)。
"""
from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass, field

import numpy as np

from .. import system_config


@dataclass
class BuildOutput:
    title: str
    box: tuple[float, float, float, float, float, float]  # xlo xhi ylo yhi zlo zhi
    atom_types: list[dict]
    atoms: list[tuple]  # (id, type, mol_id, charge, x, y, z)
    bonds: list[tuple]  # (id, btype, a1, a2)
    angles: list[tuple]  # (id, atype, a1, a2, a3)
    warnings: list[str] = field(default_factory=list)
    header_comments: list[str] = field(default_factory=list)  # 写在标题后的注释行

    def type_counts(self) -> dict[int, int]:
        counts: dict[int, int] = {}
        for _, t, *_ in self.atoms:
            counts[t] = counts.get(t, 0) + 1
        return counts

    def total_charge(self) -> float:
        return sum(a[3] for a in self.atoms)


def write_data(path: str, out: BuildOutput) -> None:
    """写 LAMMPS data 文件 (格式与 build_system.py 产物一致)。"""
    n_bonds = len(out.bonds)
    n_angles = len(out.angles)
    xlo, xhi, ylo, yhi, zlo, zhi = out.box
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{out.title}\n")
        for comment in out.header_comments:
            f.write(f"{comment}\n")
        f.write("\n")
        f.write(f"{len(out.atoms)} atoms\n")
        f.write(f"{n_bonds} bonds\n")
        f.write(f"{n_angles} angles\n\n")
        f.write(f"{len(out.atom_types)} atom types\n")
        f.write("1 bond types\n")
        f.write("1 angle types\n\n")
        f.write(f"{xlo:.6f} {xhi:.6f} xlo xhi\n")
        f.write(f"{ylo:.6f} {yhi:.6f} ylo yhi\n")
        f.write(f"{zlo:.6f} {zhi:.6f} zlo zhi\n\n")
        f.write("Masses\n\n")
        for t in out.atom_types:
            f.write(f"{t['id']} {t['mass']:.4f}  # {t['name']}\n")
        f.write("\nAtoms\n\n")
        for aid, atype, mol, chg, x, y, z in out.atoms:
            f.write(f"{aid} {mol} {atype} {chg:.6f} {x:.6f} {y:.6f} {z:.6f}\n")
        f.write("\nBonds\n\n")
        for bid, bt, a1, a2 in out.bonds:
            f.write(f"{bid} {bt} {a1} {a2}\n")
        f.write("\nAngles\n\n")
        for angle_id, at, a1, a2, a3 in out.angles:
            f.write(f"{angle_id} {at} {a1} {a2} {a3}\n")


def type_map(atom_types: list[dict]) -> dict[int, dict]:
    return {t["id"]: t for t in atom_types}


def place_water(out_atoms: list[tuple], rng, oid: int, atype_o: int, atype_h: int,
                q_o: float, q_h: float, cx: float, cy: float, cz: float,
                oh_dist: float, angle_half: float, mol_id: int) -> None:
    """放一个随机取向水分子 (O + 2H), 与 build_system.py 的双轴旋转逐行一致。"""
    theta = rng.uniform(0, 2 * math.pi)
    phi = rng.uniform(0, math.pi)
    h_local_x = oh_dist * math.sin(angle_half)
    h_local_y = oh_dist * math.cos(angle_half)
    out_atoms.append((oid, atype_o, mol_id, q_o, cx, cy, cz))
    out_atoms.append((oid + 1, atype_h, mol_id, q_h,
                      cx + h_local_x * math.cos(theta),
                      cy + h_local_x * math.sin(theta) * math.cos(phi) + h_local_y * math.sin(phi),
                      cz + h_local_x * math.sin(theta) * math.sin(phi) - h_local_y * math.cos(phi)))
    out_atoms.append((oid + 2, atype_h, mol_id, q_h,
                      cx - h_local_x * math.cos(theta),
                      cy - h_local_x * math.sin(theta) * math.cos(phi) + h_local_y * math.sin(phi),
                      cz - h_local_x * math.sin(theta) * math.sin(phi) - h_local_y * math.cos(phi)))


def water_geometry(cfg: dict) -> tuple[float, float]:
    """(oh_dist, angle_half_rad) — 从水模型预设取水分子几何。"""
    preset = system_config.WATER_PRESETS[cfg["water_model"]]
    return preset["oh_dist"], math.radians(preset["hoh_angle"] / 2)


def profile_registry() -> dict[str, callable]:
    from . import clay_cif, solution, surface_adsorption
    return {
        "surface_adsorption": surface_adsorption.build,
        "solution": solution.build,
        "clay_cif": clay_cif.build,
    }


def run_build(project_dir: str) -> dict:
    """加载 <project_dir>/system.json → 构建 → 写 system.data + build_report.json。

    返回报告 dict; 校验失败抛 ValueError。
    """
    cfg_path = os.path.join(project_dir, "system.json")
    cfg = system_config.load(cfg_path)
    errors = system_config.validate(cfg)
    if errors:
        raise ValueError("体系配置校验失败:\n- " + "\n- ".join(errors))

    import random

    rng = random.Random(cfg.get("seed", 42))
    if cfg["profile"] == "clay_cif":
        np.random.seed(cfg.get("seed", 42))  # 水取向用全局 np.random (与 convert_cif 一致)
    build_fn = profile_registry()[cfg["profile"]]
    out = build_fn(cfg, rng, project_dir=project_dir)

    data_path = os.path.join(project_dir, "system.data")
    write_data(data_path, out)

    report = {
        "profile": cfg["profile"],
        "n_atoms": len(out.atoms),
        "type_counts": {str(k): v for k, v in sorted(out.type_counts().items())},
        "n_bonds": len(out.bonds),
        "n_angles": len(out.angles),
        "total_charge": round(out.total_charge(), 4),
        "box": list(out.box),
        "warnings": out.warnings,
    }
    with open(os.path.join(project_dir, "build_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return report

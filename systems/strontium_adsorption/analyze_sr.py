#!/usr/bin/env python3
"""
Analyze prod.lammpstrj — Sr2+ / Cl- z-direction distribution

Output (按离子类型, name 前缀 sr/cl):
  1. {name}_z_distribution.txt  — 该离子 z 坐标 per frame
  2. {name}_z_histogram.txt      — z 密度直方图数据
  3. {name}_z_histogram.png      — z 密度直方图
  4. Terminal summary            — 表面 vs 本体浓度与富集比

Cl⁻ 物理预期: 带负电表面排斥 Cl⁻, 近表面浓度低于本体 (富集比 < 1),
             与 Sr²⁺ 的富集行为相反, 可作对照验证力场与表面电荷设置。
"""
import sys, os, math

import numpy as np

# ---- 项目根加入 sys.path 以便 import 公共库 common/ ----
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common.traj_parser import parse_lammpstrj

# ---- paths: relative to this script (Windows local via uv run) ----
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TRAJ_FILE   = os.path.join(SCRIPT_DIR, "prod.lammpstrj")

# ---- parameters: 体系相关值从 system.json 读取 (单一真相源); 方法参数仍为常量 ----
import json

with open(os.path.join(SCRIPT_DIR, "system.json"), encoding="utf-8") as _f:
    _system = json.load(_f)
_geo = _system.get("geometry", {})
_tids = {t["name"]: t["id"] for t in _system.get("atom_types", [])}

SURFACE_Z_MAX  = _geo.get("water", {}).get("z_start", 6.0)   # 表面原子最大 z (= 水面起始, Å)
SURFACE_REGION = SURFACE_Z_MAX + 10.0  # "near-surface" region: z < SURFACE_REGION
BULK_START     = 30.0    # "bulk water" starts at this z
BIN_WIDTH      = 1.0     # histogram bin width (Angstrom)
VACUUM_LAYER   = _geo.get("vacuum", 40.0)  # vacuum thickness subtracted from top (Angstrom)
TIMESTEP_FS    = 2.0     # 生产步长 (方法参数; nvt_production 模板默认 2.0 fs)

# ---- 离子规格: type -> 输出文件前缀与标签 (类型 id 来自 system.json) ----
ION_SPECS = [
    {"type": _tids.get("Sr", 4), "name": "sr", "label": "Sr2+"},
    {"type": _tids.get("Cl", 5), "name": "cl", "label": "Cl-"},
]

# ---- handle Windows GBK console ----
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ============================================================
# Part 1: Parse trajectory (通用解析器 common.traj_parser)
# ============================================================
print(f"Reading: {TRAJ_FILE}")

frames_raw = parse_lammpstrj(TRAJ_FILE)
n_frames = len(frames_raw)
if n_frames == 0:
    print("error: 轨迹为空或格式无法解析")
    sys.exit(1)

box_xlo, box_xhi, box_ylo, box_yhi, box_zlo, box_zhi = frames_raw[0]["box"]
timesteps = [fr["timestep"] for fr in frames_raw]

# 每种离子类型提取 z 坐标: frames_by_type[itype] = [[z1, z2, ...], ...]
frames_by_type = {}
for spec in ION_SPECS:
    itype = spec["type"]
    frames_by_type[itype] = [
        [a["z"] for a in fr["atoms"] if a["type"] == itype] for fr in frames_raw
    ]

print(f"Box z:  {box_zlo:.1f} to {box_zhi:.1f} A  ({n_frames} frames)")
for spec in ION_SPECS:
    itype = spec["type"]
    n_ion = len(frames_by_type[itype][0]) if n_frames else 0
    print(f"  {spec['label']:>4s} (type {itype}): {n_ion} per frame")

# ============================================================
# Part 2-5: 对每种离子输出坐标 / 直方图 / 分区分析 / 绘图
# ============================================================
hist_lo = math.floor(box_zlo) if box_zlo else -1.0
hist_hi = math.ceil(box_zhi)  if box_zhi else 116.0
n_bins  = int((hist_hi - hist_lo) / BIN_WIDTH)

xy_area = (box_xhi - box_xlo) * (box_yhi - box_ylo) if box_xhi else 900.0
NA = 6.022e23
water_top = box_zhi - VACUUM_LAYER   # 水层顶, 减去真空层

for spec in ION_SPECS:
    itype  = spec["type"]
    name   = spec["name"]
    label  = spec["label"]
    frames = frames_by_type[itype]
    n_ion  = len(frames[0]) if n_frames else 0

    if n_ion == 0:
        print(f"\n[{label}] 轨迹中无 type {itype} 原子, 跳过")
        continue

    out_coords = os.path.join(SCRIPT_DIR, f"{name}_z_distribution.txt")
    out_hist   = os.path.join(SCRIPT_DIR, f"{name}_z_histogram.txt")
    out_png    = os.path.join(SCRIPT_DIR, f"{name}_z_histogram.png")

    print(f"\n{'=' * 60}")
    print(f"  [{label}] 分析")
    print(f"{'=' * 60}")

    # ---- Part 2: 输出逐帧坐标 ----
    with open(out_coords, "w", encoding="utf-8") as f:
        f.write(f"# {label} z coordinates per frame\n")
        f.write(f"# {n_frames} frames, {n_ion} {label} per frame\n")
        f.write(f"# Box z: {box_zlo:.1f} to {box_zhi:.1f} A\n")
        f.write(f"# Columns: frame_idx ion_idx z\n\n")
        for i, zs in enumerate(frames):
            for j, z in enumerate(zs):
                f.write(f"{i} {j} {z:.6f}\n")
    print(f"Writing: {out_coords}")

    # ---- Part 3: z 密度直方图 (numpy.histogram) ----
    all_z = np.array([z for zs in frames for z in zs], dtype=float)
    counts, edges = np.histogram(all_z, bins=n_bins, range=(hist_lo, hist_hi))

    vol_per_bin = xy_area * BIN_WIDTH  # A^3
    with open(out_hist, "w", encoding="utf-8") as f:
        f.write(f"# {label} z-density histogram\n")
        f.write(f"# {n_frames} frames, {all_z.size} total {label} positions\n")
        f.write(f"# Bin width: {BIN_WIDTH} A\n")
        f.write(f"# Columns: z_center(A)  total_count  density(per_A_per_frame)  conc(mol/L)\n\n")
        for i in range(n_bins):
            z_lo   = hist_lo + i * BIN_WIDTH
            z_hi   = z_lo + BIN_WIDTH
            count  = counts[i]
            density = count / (n_frames * BIN_WIDTH)
            avg_per_frame = count / n_frames
            conc = avg_per_frame / (NA * vol_per_bin * 1e-27) if vol_per_bin > 0 else 0
            z_center = (z_lo + z_hi) / 2
            f.write(f"{z_center:.2f} {count} {density:.6f} {conc:.6f}\n")
    print(f"Writing: {out_hist}")

    # ---- Part 4: 分区分析 ----
    near_surface_z = all_z[all_z < SURFACE_REGION]
    bulk_z         = all_z[all_z > BULK_START]
    middle_z       = all_z[(all_z >= SURFACE_REGION) & (all_z <= BULK_START)]

    near_vol   = xy_area * (SURFACE_REGION - box_zlo)
    bulk_vol   = xy_area * max(0, water_top - BULK_START)
    middle_vol = xy_area * (BULK_START - SURFACE_REGION)

    near_avg   = near_surface_z.size / n_frames
    bulk_avg   = bulk_z.size         / n_frames
    middle_avg = middle_z.size       / n_frames

    def to_mol_L(count, vol):
        return count / (NA * vol * 1e-27) if vol > 0 else 0

    near_conc   = to_mol_L(near_avg,   near_vol)
    bulk_conc   = to_mol_L(bulk_avg,   bulk_vol)
    middle_conc = to_mol_L(middle_avg, middle_vol)

    print(f"  {'Region':<22} {'z range (A)':<16} {'Avg':<10} {'Conc (mol/L)':<14}")
    print(f"  {'-'*22} {'-'*16} {'-'*10} {'-'*14}")
    print(f"  {'Near-surface':<22} {f'{box_zlo:.1f} - {SURFACE_REGION:.1f}':<16} {near_avg:<10.2f} {near_conc:<14.4f}")
    print(f"  {'Transition':<22} {f'{SURFACE_REGION:.1f} - {BULK_START:.1f}':<16} {middle_avg:<10.2f} {middle_conc:<14.4f}")
    print(f"  {'Bulk water':<22} {f'{BULK_START:.1f} - {water_top:.1f}':<16} {bulk_avg:<10.2f} {bulk_conc:<14.4f}")

    ratio = near_conc / bulk_conc if bulk_conc > 0 else float('inf')
    print(f"\n  Near-surface / Bulk concentration ratio: {ratio:.2f}")
    if ratio > 1.5:
        print(f"  => {label} enriched near the surface (ratio > 1)")
    elif ratio > 0.8:
        print(f"  => {label} roughly uniform (ratio ~ 1)")
    else:
        print(f"  => {label} depleted near surface, more in bulk (ratio < 1)")

    # ---- Part 5: 绘图 ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        z_centers = []
        concentrations = []
        with open(out_hist, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                parts = line.strip().split()
                if len(parts) >= 4:
                    z_centers.append(float(parts[0]))
                    concentrations.append(float(parts[3]))

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.axvspan(box_zlo, SURFACE_REGION, color="gold", alpha=0.12,
                   label=f"Near-surface (z < {SURFACE_REGION:.0f} A)")
        ax.axvspan(SURFACE_REGION, BULK_START, color="gray", alpha=0.07,
                   label=f"Transition ({SURFACE_REGION:.0f} - {BULK_START:.0f} A)")
        ax.axvspan(BULK_START, water_top, color="skyblue", alpha=0.10,
                   label=f"Bulk water ({BULK_START:.0f} - {water_top:.0f} A)")

        ax.bar(z_centers, concentrations, width=BIN_WIDTH, color="crimson",
               edgecolor="white", linewidth=0.3, alpha=0.85)

        ax.axvline(x=SURFACE_Z_MAX, color="chocolate", linestyle="--",
                   linewidth=1.2, alpha=0.7, label=f"Surface top (z={SURFACE_Z_MAX:.0f} A)")
        ax.axvline(x=water_top, color="green", linestyle=":",
                   linewidth=1.0, alpha=0.6, label=f"Water surface (z={water_top:.0f} A)")

        ax.set_xlabel("z (Angstrom)", fontsize=12)
        ax.set_ylabel(f"{label} concentration (mol/L)", fontsize=12)
        ax.set_title(f"{label} z-direction distribution in charged-surface system", fontsize=13)
        ax.set_xlim(box_zlo, box_zhi)
        ax.legend(fontsize=9, framealpha=0.9)
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        fig.savefig(out_png, dpi=200)
        plt.close(fig)
        print(f"  saved: {out_png}")
    except ImportError:
        print("  (matplotlib not available, skipping plot)")
    except Exception as e:
        print(f"  (plot failed: {e})")

# ============================================================
# 体系与时间信息 (打印一次)
# ============================================================
print()
print("=" * 60)
print("  Simulation summary")
print("=" * 60)
print(f"  Box z range:      {box_zlo:.1f} - {box_zhi:.1f} A")
print(f"  Water layer:      ~6.0 - ~{water_top:.0f} A  (water ~70 A + vacuum ~{VACUUM_LAYER:.0f} A)")
print(f"  Trajectory frames: {n_frames}")
if len(timesteps) >= 2:
    dump_dt = (timesteps[-1] - timesteps[0]) / (n_frames - 1)
    sim_steps = timesteps[-1] - timesteps[0]
    print(f"  Production steps: {sim_steps}  (first_ts={timesteps[0]}, last_ts={timesteps[-1]})")
    if dump_dt > 1:
        print(f"  Production time:  {sim_steps * 2.0:.0f} fs = {sim_steps * 2.0 / 1000:.1f} ps  (timestep=2.0 fs)")
    else:
        print(f"  Production time:  {sim_steps:.0f} fs = {sim_steps / 1000:.1f} ps")
else:
    print(f"  Frames: {n_frames}  (no timestep info for duration)")
print("=" * 60)

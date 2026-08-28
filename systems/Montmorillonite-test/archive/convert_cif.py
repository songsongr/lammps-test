#!/usr/bin/env python3
"""
convert_cif.py — 蒙脱石 CIF → LAMMPS data 文件 (含层间水)

工作流:
  1. 解析 CIF 结构 (原子种类/坐标/晶胞)
  2. 构建 NX×NY×NZ 超胞
  3. 按 CLAYFF 力场分配原子类型和电荷
  4. 为 OH 基团添加 H 原子
  5. 在层间区域随机放置 SPC/E 水分子
  6. 输出 LAMMPS data 文件 + bond/angle 连接关系

用法: uv run python convert_cif.py
"""

import math
import os
import random
import sys
import numpy as np

# ---- 项目根加入 sys.path 以便 import 公共库 common/ ----
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common.water_builder import random_water_orientation

# ============================================================
# 用户参数
# ============================================================
CIF_FILE = "Montmorillonite.cif"
DATA_FILE = "system.data"
NX, NY, NZ = 2, 2, 1            # 超胞倍数
N_WATER_TARGET = 80            # 超胞中层间水分子目标数
SEED = 42
MIN_DIST_O_FW = 4.0             # 水 O 距骨架原子最小距离 (Å)
MIN_DIST_H_FW = 2.5             # 水 H 距骨架原子最小距离 (Å)
WATER_GRID_XY = 4.0               # 水分子间最小 O-O 距离 (Å)
WATER_GRID_Z = 3.0              # 层间水格点间距 z (A)

# ============================================================
# CLAYFF 原子类型定义
# ============================================================
# 类型号, 名称, 元素, 电荷, ε (kcal/mol), σ (Å), mass
ATOM_TYPES = [
    # 骨架氧 - 桥氧 (Si-O-Si)
    (1,  "ob",   "O",  -0.8000,  0.15539, 3.1655, 15.999),
    # 骨架氧 - 桥氧 (Al-O-Si) / 顶角氧
    (2,  "obos", "O",  -0.9000,  0.15539, 3.1655, 15.999),
    # 羟基氧 (Al-OH)
    (3,  "oh",   "O",  -0.9000,  0.15539, 3.1655, 15.999),
    # 羟基氢
    (4,  "ho",   "H",   0.4250,  0.00000, 0.0000,  1.008),
    # 四面体硅 Si
    (5,  "st",   "Si",  2.1000,  1.84e-6, 3.7064, 28.086),
    # 八面体铝 Al
    (6,  "ao",   "Al",  1.5750,  5.56e-6, 4.2713, 26.982),
    # 层间钙 Ca
    (7,  "ca",   "Ca",  2.0000,  0.23500, 3.0950, 40.078),
    # 水氧 (SPC/E)
    (8,  "ow",   "O",  -0.8476,  0.15539, 3.1655, 15.999),
    # 水氢 (SPC/E)
    (9,  "hw",   "H",   0.4238,  0.00000, 0.0000,  1.008),
]

TYPE_MASS = {tid: mass for tid, _, _, _, _, _, mass in ATOM_TYPES}
TYPE_CHARGE = {tid: charge for tid, _, _, charge, _, _, _ in ATOM_TYPES}
TYPE_EPS = {tid: eps for tid, _, _, _, eps, _, _ in ATOM_TYPES}
TYPE_SIGMA = {tid: sig for tid, _, _, _, _, sig, _ in ATOM_TYPES}

# ============================================================
# 1. 解析 CIF
# ============================================================
def parse_cif(filename):
    """解析 CIF, 返回晶胞参数和原子列表."""
    cell = {}
    atoms_raw = []
    in_loop = False
    loop_keys = []

    with open(filename, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 晶胞参数
        if line.startswith('_cell_length_a'):
            cell['a'] = float(line.split()[-1])
        elif line.startswith('_cell_length_b'):
            cell['b'] = float(line.split()[-1])
        elif line.startswith('_cell_length_c'):
            cell['c'] = float(line.split()[-1])
        elif line.startswith('_cell_angle_alpha'):
            cell['alpha'] = float(line.split()[-1])
        elif line.startswith('_cell_angle_beta'):
            cell['beta'] = float(line.split()[-1])
        elif line.startswith('_cell_angle_gamma'):
            cell['gamma'] = float(line.split()[-1])

        # 读取 atom_site loop
        if line.startswith('loop_'):
            in_loop = True
            loop_keys = []
            i += 1
            # 读取 loop 键名
            while i < len(lines) and lines[i].strip().startswith('_'):
                loop_keys.append(lines[i].strip())
                i += 1
            # 读取原子数据
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('_') and not lines[i].strip().startswith('loop_'):
                parts = lines[i].strip().split()
                if len(parts) >= 8:
                    # _atom_site_label, _occupancy, _fract_x, _fract_y, _fract_z, _adp_type, _U, _type_symbol
                    atoms_raw.append({
                        'label': parts[0],
                        'occ': float(parts[1]),
                        'frac': (float(parts[2]), float(parts[3]), float(parts[4])),
                        'element': parts[7],
                    })
                i += 1
            continue

        i += 1

    # 打印摘要
    print(f"  晶胞: {cell['a']:.4f} × {cell['b']:.4f} × {cell['c']:.4f} Å")
    print(f"  原子总数 (原始): {len(atoms_raw)}")
    elem_counts = {}
    for a in atoms_raw:
        elem_counts[a['element']] = elem_counts.get(a['element'], 0) + 1
    for e, c in sorted(elem_counts.items()):
        print(f"    {e}: {c}")

    return cell, atoms_raw


# OH 氧的原始CIF索引 (在 24 个 O 中的位置, 基于 z≈0.29 筛选)
# 实际蒙脱石每个原胞有 4 个 OH (Al₄Si₈O₂₀(OH)₄), 取 z 最接近 0.29 的 4 个
# 但此CIF在 z≈0.29 有 6 个 O; 我们用 z 阈值精确选 z∈[0.290, 0.292] 的 4 个
_OH_FRAC_Z_THRESH = (0.289, 0.296)  # 分数坐标阈值, 覆盖所有 z≈0.29 的 O

def is_oh_oxygen(atom, cell):
    """通过 z 位置判断是否为 OH 基团氧 (精确到 z 分数坐标)."""
    z_frac = atom['frac'][2] % 1.0  # 确保在 [0,1)
    # 原始CIF中 OH 氧的 z 分数坐标约 0.2908
    return _OH_FRAC_Z_THRESH[0] <= z_frac <= _OH_FRAC_Z_THRESH[1]

def classify_o_type(z_frac, cell):
    """按 z 位置分类骨架 O 类型: 1=ob, 2=obos, 3=oh."""
    z = z_frac * cell['c']
    if z < 1.5:
        return 1  # ob (桥氧, 上 basal)
    elif 1.5 <= z < 3.0:
        return 2  # obos (顶角氧)
    elif 3.5 <= z < 5.5:
        if is_oh_oxygen({'frac': (0, 0, z_frac)}, cell):
            return 3  # oh (羟基氧)
        else:
            return 2  # 非 OH 的中间层 O → obos
    elif z >= 5.5:
        return 1  # ob (桥氧, 下 basal)
    else:
        return 1  # fallback


def assign_framework_type(atom, cell):
    """为骨架原子分配 CLAYFF 类型和电荷."""
    elem = atom['element']
    z_frac = atom['frac'][2]

    if elem == 'Si':
        return 5  # st
    elif elem == 'Al':
        return 6  # ao
    elif elem == 'Ca':
        return 7  # ca
    elif elem == 'O':
        return classify_o_type(z_frac, cell)
    else:
        raise ValueError(f"未知元素: {elem}")


# ============================================================
# 2. 构建超胞
# ============================================================
def build_supercell(atoms, cell, nx, ny, nz):
    """构建 NX×NY×NZ 超胞."""
    super_atoms = []
    atom_id = 0

    # Ca 原子按占据率随机保留
    ca_positions = [a for a in atoms if a['element'] == 'Ca']
    non_ca = [a for a in atoms if a['element'] != 'Ca']

    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                shift = (ix / nx, iy / ny, iz / nz)

                for a in non_ca:
                    new_frac = (
                        (a['frac'][0] + shift[0]) / nx,
                        (a['frac'][1] + shift[1]) / ny,
                        (a['frac'][2] + shift[2]) / nz,
                    )
                    atom_id += 1
                    super_atoms.append({
                        'id': atom_id,
                        'element': a['element'],
                        'frac': new_frac,
                        'type': None,  # 待分配
                        'charge': 0.0,
                        'mol': 0,
                    })

                # Ca: 按占据率保留 (occ=0.5)
                for a in ca_positions:
                    if random.random() < a['occ']:
                        new_frac = (
                            (a['frac'][0] + shift[0]) / nx,
                            (a['frac'][1] + shift[1]) / ny,
                            (a['frac'][2] + shift[2]) / nz,
                        )
                        atom_id += 1
                        super_atoms.append({
                            'id': atom_id,
                            'element': a['element'],
                            'frac': new_frac,
                            'type': None,
                            'charge': 0.0,
                            'mol': 0,
                        })

    new_cell = {
        'a': cell['a'] * nx,
        'b': cell['b'] * ny,
        'c': cell['c'] * nz,
        'alpha': cell['alpha'],
        'beta': cell['beta'],
        'gamma': cell['gamma'],
    }

    print(f"  超胞: {new_cell['a']:.2f} × {new_cell['b']:.2f} × {new_cell['c']:.2f} Å")
    print(f"  骨架原子数: {len(super_atoms)}")

    return super_atoms, new_cell


# ============================================================
# 3. 分配 CLAYFF 类型 + 添加 OH 氢
# ============================================================
def assign_types_and_add_oh(super_atoms, cell):
    """分配原子类型/电荷, 并为 OH 基团添加 H 原子."""
    oh_oxygens = []

    for a in super_atoms:
        a['type'] = assign_framework_type(a, cell)
        a['charge'] = TYPE_CHARGE[a['type']]

        if a['type'] == 3:  # oh
            oh_oxygens.append(a)

    # 为每个 OH 氧添加 H 原子 (指向层间方向 +z)
    new_atoms = list(super_atoms)
    next_id = max(a['id'] for a in super_atoms) + 1

    for oa in oh_oxygens:
        # H 沿 +z 方向, 距离 1.0 Å
        h_frac_z = oa['frac'][2] + 1.0 / cell['c']
        # 确保不超过 1.0 (PBC 处理 - 但在层间中央所以安全)
        h = {
            'id': next_id,
            'element': 'H',
            'frac': (oa['frac'][0], oa['frac'][1], h_frac_z),
            'type': 4,  # ho
            'charge': TYPE_CHARGE[4],
            'mol': 0,
        }
        new_atoms.append(h)
        next_id += 1

    print(f"  OH 氢原子数: {len(oh_oxygens)}")
    print(f"  添加后原子总数: {len(new_atoms)}")

    return new_atoms


# ============================================================
# 4. 笛卡尔坐标转换
# ============================================================
def frac_to_cart(frac, cell):
    """分数坐标转笛卡尔坐标 (正交晶系, 所有角=90°)."""
    return (
        frac[0] * cell['a'],
        frac[1] * cell['b'],
        frac[2] * cell['c'],
    )


def cart_to_frac(cart, cell):
    """笛卡尔坐标转分数坐标."""
    return (
        cart[0] / cell['a'],
        cart[1] / cell['b'],
        cart[2] / cell['c'],
    )


# ============================================================
# 5. 层间水生成 (SPC/E)
# ============================================================
def get_interlayer_z_range(framework_atoms, cell):
    """识别层间区域 z 范围."""
    z_values = []
    for a in framework_atoms:
        if a['type'] in (1, 2, 3, 5, 6):  # 骨架原子
            z_values.append(a['frac'][2] * cell['c'])

    if not z_values:
        return 8.0, 12.0

    max_z = max(z_values)
    min_z = min(z_values)

    # 层间区域 = 骨架以上 ~1Å 到晶胞顶
    # 注意 z 是周期性的, 但我们的 TOT 层在底部
    inter_z_min = max_z + 2.0  # 骨架顶部 + 2Å 缓冲
    inter_z_max = cell['c'] - 0.5  # 留一点边界

    print(f"  骨架 z 范围: [{min_z:.2f}, {max_z:.2f}] Å")
    print(f"  层间 z 范围: [{inter_z_min:.2f}, {inter_z_max:.2f}] Å")
    print(f"  层间厚度: {inter_z_max - inter_z_min:.2f} Å")

    return inter_z_min, inter_z_max


# random_water_orientation 已迁移至 common.water_builder (2026-08-14), 此处直接复用。
# 注意: 迁移前使用 random 模块生成四元数, 迁移后使用 np.random (物理等价, 输出取向序列不同)。


def add_interlayer_water(atoms, cell, n_water_target):
    """
    在层间区域放置 SPC/E 水分子 (格点法, 均匀分布).
    """
    framework = [a for a in atoms if a['type'] in (1, 2, 3, 4, 5, 6, 7)]

    fw_positions = []
    for a in framework:
        cart = frac_to_cart(a['frac'], cell)
        fw_positions.append(np.array(cart))

    inter_z_min, inter_z_max = get_interlayer_z_range(framework, cell)

    next_id = max(a['id'] for a in atoms) + 1
    next_mol = 1

    water_os = []
    water_molecules = []

    # 在 xy 平面创建格点
    nx_grid = max(1, int(cell['a'] / WATER_GRID_XY))
    ny_grid = max(1, int(cell['b'] / WATER_GRID_XY))
    nz_grid = max(1, int((inter_z_max - inter_z_min) / WATER_GRID_Z))

    x_positions = [(i + 0.5) * cell['a'] / nx_grid for i in range(nx_grid)]
    y_positions = [(j + 0.5) * cell['b'] / ny_grid for j in range(ny_grid)]
    z_positions = [inter_z_min + (k + 0.5) * (inter_z_max - inter_z_min) / nz_grid for k in range(nz_grid)]

    placed = 0
    grid_order = [(ix, iy, iz) for ix in range(nx_grid) for iy in range(ny_grid) for iz in range(nz_grid)]
    random.shuffle(grid_order)

    for ix, iy, iz in grid_order:
        if placed >= n_water_target:
            break

        ox, oy, oz = x_positions[ix], y_positions[iy], z_positions[iz]
        o_pos = np.array([ox, oy, oz])

        # 距离骨架原子
        too_close = False
        for fw_pos in fw_positions:
            d = np.linalg.norm(o_pos - fw_pos)
            if d < MIN_DIST_O_FW:
                too_close = True
                break
        if too_close:
            continue

        # 距离已放置水分子
        for wo_pos in water_os:
            d = np.linalg.norm(o_pos - wo_pos)
            if d < WATER_GRID_XY:
                too_close = True
                break
        if too_close:
            continue

        # 生成水分子取向
        h_rot = random_water_orientation()
        h1_pos = o_pos + h_rot[0]
        h2_pos = o_pos + h_rot[1]

        h_too_close = False
        for hpos in [h1_pos, h2_pos]:
            for fw_pos in fw_positions:
                d = np.linalg.norm(hpos - fw_pos)
                if d < MIN_DIST_H_FW:
                    h_too_close = True
                    break
            if h_too_close:
                break
        if h_too_close:
            continue

        if not (0 < h1_pos[0] < cell['a'] and 0 < h1_pos[1] < cell['b'] and 0 < h1_pos[2] < cell['c']):
            continue
        if not (0 < h2_pos[0] < cell['a'] and 0 < h2_pos[1] < cell['b'] and 0 < h2_pos[2] < cell['c']):
            continue

        o_frac = cart_to_frac(o_pos, cell)
        h1_frac = cart_to_frac(h1_pos, cell)
        h2_frac = cart_to_frac(h2_pos, cell)
        o_frac = tuple(f % 1.0 for f in o_frac)
        h1_frac = tuple(f % 1.0 for f in h1_frac)
        h2_frac = tuple(f % 1.0 for f in h2_frac)

        o_atom = {'id': next_id, 'mol': next_mol, 'element': 'O',
                  'type': 8, 'charge': TYPE_CHARGE[8], 'frac': o_frac}
        next_id += 1
        h1_atom = {'id': next_id, 'mol': next_mol, 'element': 'H',
                   'type': 9, 'charge': TYPE_CHARGE[9], 'frac': h1_frac}
        next_id += 1
        h2_atom = {'id': next_id, 'mol': next_mol, 'element': 'H',
                   'type': 9, 'charge': TYPE_CHARGE[9], 'frac': h2_frac}
        next_id += 1

        atoms.extend([o_atom, h1_atom, h2_atom])
        water_os.append(o_pos)
        water_molecules.append((o_atom, h1_atom, h2_atom))
        next_mol += 1
        placed += 1

        if placed % 50 == 0:
            print(f'  已放置 {placed}/{n_water_target} 个水分子...')

    print(f'实际放置水分子: {placed} (目标 {n_water_target})')
    print(f'总原子数: {len(atoms)}')

    return atoms, water_molecules



# ============================================================
# 6. 写入 LAMMPS data 文件
# ============================================================
def write_data(filename, cell, atoms, water_molecules):
    """写入 LAMMPS data 文件."""

    # 坐标转换为笛卡尔
    atom_data = []
    for a in atoms:
        cart = frac_to_cart(a['frac'], cell)
        atom_data.append((a['id'], a['mol'], a['type'], a['charge'], cart[0], cart[1], cart[2]))

    # 键和角 (水分子内)
    bonds = []
    angles = []
    bond_id = 1
    angle_id = 1
    for wo, wh1, wh2 in water_molecules:
        bonds.append((bond_id, 1, wo['id'], wh1['id'])); bond_id += 1
        bonds.append((bond_id, 1, wo['id'], wh2['id'])); bond_id += 1
        angles.append((angle_id, 1, wh1['id'], wo['id'], wh2['id'])); angle_id += 1

    n_atoms = len(atoms)
    n_bonds = len(bonds)
    n_angles = len(angles)
    n_types = 9

    # 统计各类型数量
    type_counts = {}
    for a in atoms:
        t = a['type']
        type_counts[t] = type_counts.get(t, 0) + 1

    # 统计各元素数量 (用于 Masses)
    elements_present = set(a['element'] for a in atoms)

    with open(filename, 'w') as f:
        f.write("LAMMPS data file — Montmorillonite with interlayer water\n")
        f.write(f"# Generated by convert_cif.py from {CIF_FILE}\n")
        f.write(f"# Supercell: {NX}×{NY}×{NZ}\n")
        f.write(f"# Water molecules: {len(water_molecules)}\n")
        f.write(f"# Date: 2026-07-01\n")
        f.write("\n")

        f.write(f"{n_atoms:>12d}  atoms\n")
        f.write(f"{n_bonds:>12d}  bonds\n")
        f.write(f"{n_angles:>12d}  angles\n")
        f.write("\n")
        f.write(f"{n_types:>12d}  atom types\n")
        f.write(f"{1:>12d}  bond types\n")
        f.write(f"{1:>12d}  angle types\n")
        f.write("\n")

        # 盒子尺寸
        f.write(f"{0.0:16.6f}  {cell['a']:16.6f}  xlo xhi\n")
        f.write(f"{0.0:16.6f}  {cell['b']:16.6f}  ylo yhi\n")
        f.write(f"{0.0:16.6f}  {cell['c']:16.6f}  zlo zhi\n")
        f.write("\n")

        # Masses
        f.write("Masses\n\n")
        type_names = {1: "ob", 2: "obos", 3: "oh", 4: "ho",
                      5: "st", 6: "ao", 7: "ca", 8: "ow", 9: "hw"}
        for tid in range(1, n_types + 1):
            if tid in type_counts:
                mass = TYPE_MASS[tid]
                name = type_names[tid]
                f.write(f"{tid:>6d}  {mass:10.6f}  # {name}\n")

        # 原子
        f.write("\nAtoms\n\n")
        for aid, mol, atype, charge, x, y, z in atom_data:
            f.write(f"{aid:>8d} {mol:>6d} {atype:>4d} {charge:10.6f}  {x:12.6f} {y:12.6f} {z:12.6f}\n")

        # 键
        f.write("\nBonds\n\n")
        for bid, btype, ai, aj in bonds:
            f.write(f"{bid:>8d} {btype:>4d} {ai:>8d} {aj:>8d}\n")

        # 角
        f.write("\nAngles\n\n")
        for aid, atype, ai, aj, ak in angles:
            f.write(f"{aid:>8d} {atype:>4d} {ai:>8d} {aj:>8d} {ak:>8d}\n")

    print(f"\n  写入 {filename}")
    print(f"  原子: {n_atoms}, 键: {n_bonds}, 角: {n_angles}")
    print(f"  类型分布: {dict(sorted(type_counts.items()))}")

    # 验证电中性
    total_charge = sum(a['charge'] for a in atoms)
    print(f"  总电荷: {total_charge:+.4f} (应为 0)")


# ============================================================
# 7. 电中性修正
# ============================================================
def neutralize_charge(atoms):
    """通过均匀偏移骨架 O 电荷实现体系电中性."""
    total_q = sum(a['charge'] for a in atoms)
    fw_o_atoms = [a for a in atoms if a['type'] in (1, 2, 3)]
    n_fw_o = len(fw_o_atoms)

    if abs(total_q) < 1e-6:
        print(f"  体系已电中性 (总电荷 = {total_q:+.4f})")
        return atoms

    shift = -total_q / n_fw_o
    for a in fw_o_atoms:
        a['charge'] += shift

    new_total = sum(a['charge'] for a in atoms)
    print(f"  总电荷: {total_q:+.4f} -> {new_total:+.4f} (骨架O偏移 {shift:+.6f})")
    return atoms


# ============================================================
# Main
# ============================================================
def main():
    random.seed(SEED)
    np.random.seed(SEED)

    print("=" * 60)
    print("蒙脱石 CIF → LAMMPS data 文件转换")
    print("=" * 60)

    # 1. 解析 CIF
    print("\n[1/6] 解析 CIF 结构...")
    cell, atoms_raw = parse_cif(CIF_FILE)

    # 2. 构建超胞
    print("\n[2/6] 构建超胞...")
    super_atoms, super_cell = build_supercell(atoms_raw, cell, NX, NY, NZ)

    # 3. 分配 CLAYFF 类型 + OH 氢
    print("\n[3/6] 分配原子类型/电荷, 添加 OH 氢...")
    all_atoms = assign_types_and_add_oh(super_atoms, super_cell)

    # 4. 层间水
    print("\n[4/6] 放置层间水分子...")
    all_atoms, water_mols = add_interlayer_water(all_atoms, super_cell, N_WATER_TARGET)

    # 5. 电中性修正
    print("\n[5/6] 电中性修正...")
    all_atoms = neutralize_charge(all_atoms)

    # 6. 写入 data 文件
    print("\n[6/6] 写入 LAMMPS data 文件...")
    write_data(DATA_FILE, super_cell, all_atoms, water_mols)

    print("\n" + "=" * 60)
    print("完成! 输出文件: " + DATA_FILE)
    print("=" * 60)


if __name__ == "__main__":
    main()

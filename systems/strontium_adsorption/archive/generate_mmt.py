#!/usr/bin/env python3
"""
蒙脱石(001)表面 + 水溶液 + SrCl2 体系生成器
输出 LAMMPS data file
"""

import math
import random
random.seed(42)

# ============================================================
# 1. 参数设置
# ============================================================

# 蒙脱石单元 (近似正交晶系)
a0 = 5.23   # Å
b0 = 9.06   # Å
c_layer = 6.56   # TOT 层厚度 (Å)

# 超胞大小
nx, ny = 4, 2   # 4×2 超胞 (约 20.9×18.1 Å)
n_layers = 1    # TOT 层数

# 水层厚度 (Å) - 约 30 Å 水层
water_thickness = 30.0

# SrCl2 浓度 (mol/L)
conc = 0.25

# ============================================================
# 2. CLAYFF 原子类型定义
# ============================================================

# atom_type: (name, charge, mass)
atom_data = {
    1: ("Si",  1.200, 28.0855),   # 四面体 Si
    2: ("Al",  1.575, 26.9815),   # 八面体 Al
    3: ("O",  -0.950, 15.9994),   # 桥氧
    4: ("Oh", -0.950, 15.9994),   # 羟基氧
    5: ("Ho",  0.425,  1.0079),   # 羟基氢
    6: ("Ow", -0.820, 15.9994),   # 水氧 (SPC/E)
    7: ("Hw",  0.410,  1.0079),   # 水氢
    8: ("Sr",  2.000, 87.6200),   # Sr²⁺
    9: ("Cl", -1.000, 35.4530),   # Cl⁻
}

# ============================================================
# 3. 蒙脱石 TOT 层结构 (正交近似)
# ============================================================

# 原子在单元内的分数坐标 (基于文献典型值)
# 坐标范围: (0-1) × a0, (0-1) × b0
# z 坐标相对于层中心 (Å)

def generate_mmt_cell():
    """生成一个 MMT 单元的所有原子（正交近似）"""
    atoms = []
    aid = 0
    # z-offset: 各原子层相对于层中心的 z 高度 (Å)

    # ---- 下层四面体片 (倒置) ----
    # 桥氧 (底面)
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 3, ix*a0, iy*b0, -3.28))
    # Si
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 1, (ix+0.5)*a0*0.5, (iy+0.5)*b0*0.5, -2.40))
    # 顶氧（连接八面体）
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 3, ix*a0*0.5+0.25*a0, iy*b0*0.5+0.25*b0, -1.30))

    # ---- 八面体片 ----
    # Al
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 2, (ix+0.5)*a0*0.5, (iy+0.5)*b0*0.5, 0.00))
    # OH
    aid += 1
    atoms.append((aid, 4, 0.25*a0, 0.25*b0, 0.65))
    aid += 1
    atoms.append((aid, 5, 0.25*a0, 0.25*b0, 1.25))
    aid += 1
    atoms.append((aid, 4, 0.75*a0, 0.75*b0, 0.65))
    aid += 1
    atoms.append((aid, 5, 0.75*a0, 0.75*b0, 1.25))

    # ---- 上层四面体片 ----
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 3, ix*a0*0.5+0.25*a0, iy*b0*0.5+0.25*b0, 1.30))
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 1, (ix+0.5)*a0*0.5, (iy+0.5)*b0*0.5, 2.40))
    for iy in range(2):
        for ix in range(2):
            aid += 1
            atoms.append((aid, 3, ix*a0, iy*b0, 3.28))

    return atoms

# ============================================================
# 4. 构建超胞并写入 LAMMPS data
# ============================================================

def write_data():
    cell_a = a0
    cell_b = b0

    # 盒子尺寸
    xlo, xhi = 0.0, nx * cell_a
    ylo, yhi = 0.0, ny * cell_b
    zlo = -c_layer / 2 - 2.0   # 底部留空
    zhi = c_layer / 2 + water_thickness + 5.0  # 顶部水层 + 真空

    # 生成蒙脱石原子
    mmt_cell = generate_mmt_cell()

    # 扩展为超胞
    all_atoms = []
    for ix in range(nx):
        for iy in range(ny):
            offset_x = ix * cell_a
            offset_y = iy * cell_b
            for aid, atype, x, y, z in mmt_cell:
                all_atoms.append((len(all_atoms)+1, atype,
                                 x + offset_x, y + offset_y, z))

    n_mmt_atoms = len(all_atoms)
    print(f"蒙脱石原子数: {n_mmt_atoms}", file=__import__('sys').stderr)

    # ---- 加入水分子 ----
    # SPC/E 水分子几何
    ow_pos = (0.0, 0.0, 0.0)
    hw1_pos = (0.8165, 0.5774, 0.0)  # Å
    hw2_pos = (-0.8165, 0.5774, 0.0)
    oh_dist = 1.0  # O-H 距离 (Å)
    hoh_angle = 109.47  # 度

    # 计算 H 位置
    rad = math.radians(hoh_angle/2)
    hx = oh_dist * math.sin(rad)
    hy = oh_dist * math.cos(rad)

    water_ox = 0.0
    water_oy = 0.0
    water_oz = 0.0
    h1 = (hx, hy, 0.0)
    h2 = (-hx, hy, 0.0)

    # 水分子网格 - 密度 ~1 g/cm³
    nw_cells_x = int(nx * cell_a / 3.0)
    nw_cells_y = int(ny * cell_b / 3.0)
    nw_cells_z = int(water_thickness / 3.0)
    water_spacing_x = (nx * cell_a) / nw_cells_x
    water_spacing_y = (ny * cell_b) / nw_cells_y
    water_spacing_z = water_thickness / nw_cells_z

    water_z_start = c_layer / 2 + 1.0  # 从表面上方开始放水

    water_atoms = []
    for iz in range(nw_cells_z):
        for iy in range(nw_cells_y):
            for ix in range(nw_cells_x):
                # 加一点随机扰动避免晶格排列
                jx = ix * water_spacing_x + water_spacing_x/2 + random.uniform(-0.1, 0.1)
                jy = iy * water_spacing_y + water_spacing_y/2 + random.uniform(-0.1, 0.1)
                jz = iz * water_spacing_z + water_spacing_z/2 + water_z_start + random.uniform(-0.1, 0.1)

                # 随机旋转 (简化: 绕三个轴随机旋转)
                theta = random.uniform(0, 2*math.pi)
                phi = random.uniform(0, 2*math.pi)
                psi = random.uniform(0, 2*math.pi)

                cos_t = math.cos(theta)
                sin_t = math.sin(theta)
                cos_p = math.cos(phi)
                sin_p = math.sin(phi)

                # 旋转后的 H 位置
                h1x = h1[0]*cos_t - h1[1]*sin_t
                h1y = h1[0]*sin_t + h1[1]*cos_t
                h1z = h1[1]*sin_p

                h2x = h2[0]*cos_t - h2[1]*sin_t
                h2y = h2[0]*sin_t + h2[1]*cos_t
                h2z = h2[1]*sin_p

                oid = len(all_atoms) + len(water_atoms) + 1
                water_atoms.append((oid, 6, jx, jy, jz))
                water_atoms.append((oid+1, 7, jx+h1x, jy+h1y, jz+h1z))
                water_atoms.append((oid+2, 7, jx+h2x, jy+h2y, jz+h2z))

    n_water_atoms = len(water_atoms)
    n_water_mols = n_water_atoms // 3
    print(f"水分子数: {n_water_mols}", file=__import__('sys').stderr)

    # ---- 加入 SrCl2 离子 ----
    # 0.25 mol/L → 计算所需离子数
    # 体积 = 水层体积 (Å³)
    water_vol = nx * cell_a * ny * cell_b * water_thickness  # Å³
    water_vol_l = water_vol * 1e-27  # 转换为 L
    avogadro = 6.022e23

    # n = C × V × NA
    n_Sr = int(conc * water_vol_l * avogadro)
    n_Cl = n_Sr * 2

    # 放置离子: 在水分子的间隙中随机放置
    ion_atoms = []

    # 收集所有水分子的位置
    water_oxy_positions = [(aid, x, y, z) for aid, atype, x, y, z in water_atoms if atype == 6]

    # 选择远离已放置离子的位置
    placed_ions = []
    min_ion_dist = 3.0  # Å

    for _ in range(n_Sr + n_Cl):
        attempts = 0
        while attempts < 200:
            idx = random.randint(0, len(water_oxy_positions)-1)
            _, wx, wy, wz = water_oxy_positions[idx]
            # 略高于表面
            if wz < water_z_start + 2.0:
                attempts += 1
                continue
            # 检查与其他离子的距离
            too_close = False
            for _, px, py, pz in placed_ions:
                dx = wx - px
                dy = wy - py
                dz = wz - pz
                if math.sqrt(dx*dx + dy*dy + dz*dz) < min_ion_dist:
                    too_close = True
                    break
            if not too_close:
                break
            attempts += 1

        # 确定是 Sr 还是 Cl
        if len(ion_atoms) < n_Sr:
            itype = 8  # Sr²⁺
        else:
            itype = 9  # Cl⁻

        aid = len(all_atoms) + len(water_atoms) + len(ion_atoms) + 1
        ion_atoms.append((aid, itype, wx, wy, wz))
        placed_ions.append((aid, wx, wy, wz))

    print(f"Sr²⁺ 离子数: {n_Sr}, Cl⁻ 离子数: {n_Cl}", file=__import__('sys').stderr)

    # ---- 写入 LAMMPS data file ----
    total_atoms = len(all_atoms) + len(water_atoms) + len(ion_atoms)
    total_bonds = n_water_mols * 2  # O-H bonds per water
    total_angles = n_water_mols * 1  # H-O-H angle per water

    with open("/data/strontium_adsorption/mmt_system.data", "w") as f:
        f.write("SrCl2-Montmorillonite system (generated)\n\n")
        f.write(f"{total_atoms} atoms\n")
        f.write(f"{total_bonds} bonds\n")
        f.write(f"{total_angles} angles\n\n")
        f.write("9 atom types\n")
        f.write("2 bond types\n")
        f.write("1 angle types\n\n")

        f.write(f"{xlo:.6f} {xhi:.6f} xlo xhi\n")
        f.write(f"{ylo:.6f} {yhi:.6f} ylo yhi\n")
        f.write(f"{zlo:.6f} {zhi:.6f} zlo zhi\n\n")

        f.write("Masses\n\n")
        for tid in range(1, 10):
            name, charge, mass = atom_data[tid]
            f.write(f"{tid} {mass:.4f} # {name}\n")

        f.write("\nAtoms\n\n")
        for aid, atype, x, y, z in all_atoms + water_atoms + ion_atoms:
            name, charge, mass = atom_data[atype]
            f.write(f"{aid} 1 {atype} {charge:.6f} {x:.6f} {y:.6f} {z:.6f}\n")

        f.write("\nBonds\n\n")
        bid = 0
        for i in range(n_water_mols):
            # O-H bonds (type 1 = harmonic O-H)
            bid += 1
            oid = len(all_atoms) + i*3 + 1
            hid1 = oid + 1
            hid2 = oid + 2
            f.write(f"{bid} 1 {oid} {hid1}\n")
            bid += 1
            f.write(f"{bid} 1 {oid} {hid2}\n")

        f.write("\nAngles\n\n")
        aidx = 0
        for i in range(n_water_mols):
            aidx += 1
            oid = len(all_atoms) + i*3 + 1
            hid1 = oid + 1
            hid2 = oid + 2
            f.write(f"{aidx} 1 {hid1} {oid} {hid2}\n")

        f.write("\n")

    print(f"\n数据文件已生成: mmt_system.data", file=__import__('sys').stderr)
    print(f"总原子数: {total_atoms}", file=__import__('sys').stderr)
    print(f"水分子: {n_water_mols}", file=__import__('sys').stderr)
    print(f"Sr²⁺: {n_Sr}, Cl⁻: {n_Cl}", file=__import__('sys').stderr)
    print(f"离子浓度: {conc} mol/L (目标)", file=__import__('sys').stderr)
    return total_atoms, n_water_mols, n_Sr, n_Cl

if __name__ == "__main__":
    write_data()

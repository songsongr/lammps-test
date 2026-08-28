#!/usr/bin/env python3
"""
生成: 带电表面 + SPC/E 水 + SrCl2 体系
输出 LAMMPS data file (带键/角)
"""
import math, random, sys
random.seed(42)

# ========== 参数 ==========
a0 = 3.0                     # 表面晶格常数 (Å)
nx, ny = 8, 8               # 表面超胞
n_surf_layers = 3            # 表面层数
surf_z_bottom = 0.0          # 表面底部 z

water_density = 1.0          # g/cm³
water_thickness = 25.0       # Å
conc = 0.25                  # SrCl2 mol/L

# ========== 原子类型 ==========
# 1: Surf (表面), 2: Ow (水氧), 3: Hw (水氢), 4: Sr²⁺, 5: Cl⁻

# ========== 建表面 ==========
surf_atoms = []
aid = 0
for iz in range(n_surf_layers):
    for iy in range(ny):
        for ix in range(nx):
            x = (ix + (iz % 2) * 0.5 + (iy % 2) * 0.5) * a0
            y = (iy * 0.5 + (ix % 2) * 0.25) * a0
            # FCC-like positions
            if iz % 2 == 0:
                x = (ix + 0.5 * (iy % 2)) * a0
                y = iy * a0 * math.sqrt(3) / 2
            else:
                x = (ix + 0.5 + 0.5 * (iy % 2)) * a0
                y = (iy + 0.5) * a0 * math.sqrt(3) / 2
            z = surf_z_bottom + iz * 2.0
            aid += 1
            surf_atoms.append((aid, 1, x, y, z))

# 计算盒子尺寸
all_x = [a[2] for a in surf_atoms]
all_y = [a[3] for a in surf_atoms]
all_z = [a[4] for a in surf_atoms]
xlo, xhi = 0, max(all_x) + a0
ylo, yhi = 0, max(all_y) + a0 * 0.87
zlo = -2.0
zhi = max(all_z) + water_thickness + 5.0

print(f"盒子: x={xlo:.1f}-{xhi:.1f}, y={ylo:.1f}-{yhi:.1f}, z={zlo:.1f}-{zhi:.1f}", file=sys.stderr)

# ========== 加水 ==========
# SPC/E 水: O-H 1.0 Å, 键角 109.47°
oh_dist = 1.0
angle_half = math.radians(109.47 / 2)
hx_local = oh_dist * math.sin(angle_half)
hy_local = oh_dist * math.cos(angle_half)

# 水分子放置 - 确保不重叠
surf_max_z = max(all_z) + 1.5  # 水面起始高度
water_z_start = surf_max_z

# 放置网格
nw_x = int((xhi - xlo) / 3.1)
nw_y = int((yhi - ylo) / 3.1)
nw_z = int(water_thickness / 3.1)
wx_sp = (xhi - xlo) / nw_x
wy_sp = (yhi - ylo) / nw_y
wz_sp = water_thickness / nw_z

water_atoms = []
water_mols = 0

for iz in range(nw_z):
    for iy in range(nw_y):
        for ix in range(nw_x):
            # 水分子中心位置 + 随机扰动
            cx = ix * wx_sp + wx_sp/2 + random.uniform(-0.2, 0.2)
            cy = iy * wy_sp + wy_sp/2 + random.uniform(-0.2, 0.2)
            cz = iz * wz_sp + wz_sp/2 + water_z_start + random.uniform(-0.2, 0.2)

            # 随机旋转
            theta = random.uniform(0, 2*math.pi)
            phi = random.uniform(0, math.pi)

            # 旋转 H 原子
            h1x = hx_local * math.cos(theta) - hy_local * math.sin(theta)
            h1y = hx_local * math.sin(theta) + hy_local * math.cos(theta)
            h1z = 0.0
            h2x = -h1x
            h2y = -h1y
            h2z = 0.0

            # 绕 x 轴旋转 phi
            h1y, h1z = h1y*math.cos(phi) - h1z*math.sin(phi), h1y*math.sin(phi) + h1z*math.cos(phi)
            h2y, h2z = h2y*math.cos(phi) - h2z*math.sin(phi), h2y*math.sin(phi) + h2z*math.cos(phi)

            aid += 1
            water_atoms.append((aid, 2, cx, cy, cz))
            aid += 1
            water_atoms.append((aid, 3, cx+h1x, cy+h1y, cz+h1z))
            aid += 1
            water_atoms.append((aid, 3, cx+h2x, cy+h2y, cz+h2z))
            water_mols += 1

all_atoms = surf_atoms + water_atoms
n_water = water_mols

# ========== 加离子 ==========
water_vol = (xhi - xlo) * (yhi - ylo) * water_thickness  # Å³
water_vol_L = water_vol * 1e-27
n_sr = max(1, int(conc * water_vol_L * 6.022e23))
n_cl = n_sr * 2

# 收集水氧位置用于放置离子
water_oxy = [(a[0], a[2], a[3], a[4]) for a in water_atoms if a[1] == 2]
random.shuffle(water_oxy)

ion_types = [4] * n_sr + [5] * n_cl
ion_atoms = []
ion_idx = 0

for itype in ion_types:
    if ion_idx < len(water_oxy):
        _, wx, wy, wz = water_oxy[ion_idx]
        aid += 1
        ion_atoms.append((aid, itype, wx, wy, wz))
        ion_idx += 1

all_atoms = surf_atoms + water_atoms + ion_atoms
n_total = len(all_atoms)

print(f"表面原子: {len(surf_atoms)}", file=sys.stderr)
print(f"水分子: {n_water}", file=sys.stderr)
print(f"Sr²⁺: {n_sr}, Cl⁻: {n_cl}", file=sys.stderr)

# ========== 写 LAMMPS data ==========
total_bonds = n_water * 2
total_angles = n_water

with open("/data/strontium_adsorption/system.data", "w") as f:
    f.write(f"SrCl2 adsorption on charged surface\n\n")
    f.write(f"{n_total} atoms\n")
    f.write(f"{total_bonds} bonds\n")
    f.write(f"{total_angles} angles\n\n")
    f.write("5 atom types\n")
    f.write("1 bond types\n")
    f.write("1 angle types\n\n")
    f.write(f"{xlo:.6f} {xhi:.6f} xlo xhi\n")
    f.write(f"{ylo:.6f} {yhi:.6f} ylo yhi\n")
    f.write(f"{zlo:.6f} {zhi:.6f} zlo zhi\n\n")

    f.write("Masses\n\n")
    f.write("1 28.0855 # Surf\n")
    f.write("2 15.9994 # Ow\n")
    f.write("3 1.0079  # Hw\n")
    f.write("4 87.6200 # Sr\n")
    f.write("5 35.4530 # Cl\n\n")

    f.write("Atoms\n\n")
    charge_map = {1: -0.3, 2: -0.820, 3: 0.410, 4: 2.0, 5: -1.0}
    for aid, atype, x, y, z in all_atoms:
        mol_id = 1 if atype in (2, 3) else 0
        chg = charge_map[atype]
        f.write(f"{aid} {mol_id} {atype} {chg:.6f} {x:.6f} {y:.6f} {z:.6f}\n")

    f.write("\nBonds\n\n")
    bid = 0
    for i in range(n_water):
        oid = len(surf_atoms) + i*3 + 1
        h1 = oid + 1
        h2 = oid + 2
        bid += 1; f.write(f"{bid} 1 {oid} {h1}\n")
        bid += 1; f.write(f"{bid} 1 {oid} {h2}\n")

    f.write("\nAngles\n\n")
    for i in range(n_water):
        oid = len(surf_atoms) + i*3 + 1
        h1 = oid + 1
        h2 = oid + 2
        f.write(f"{i+1} 1 {h1} {oid} {h2}\n")

print(f"\n生成完成: {n_total} atoms, {n_water} waters, {n_sr} Sr²⁺, {n_cl} Cl⁻", file=sys.stderr)

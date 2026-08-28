#!/usr/bin/env python3
"""
生成: 带电黏土表面 + SPC/E 水 + 0.25 M SrCl2
输出: LAMMPS data file
"""
import math, os, random, sys
random.seed(42)

# ========== 物理参数 ==========
surf_charge = -0.12          # 单原子电荷 (100原子→-12, 模拟MMT层电荷)
water_z_start = 6.0          # 水面起始高度 (Å)
water_thickness = 70.0       # 水层厚度 (Å) - 足够区分表面和本体
conc = 0.25                  # SrCl2 浓度 mol/L
extra_sr = 6                 # 额外 Sr²⁺ 平衡 -12 表面电荷 (每个+2, 需6个)

# 晶格
a = 3.0                      # 表面晶格常数 (Å)
nx, ny = 10, 10             # 表面超胞
nlayers = 2                  # 表面层数

# ========== 原子类型定义 ==========
# 1=Surf  2=Ow  3=Hw  4=Sr  5=Cl
type_name = {1:"Surf", 2:"Ow", 3:"Hw", 4:"Sr", 5:"Cl"}
type_charge = {1: surf_charge, 2: -0.820, 3: 0.410, 4: 2.0, 5: -1.0}
type_mass = {1: 28.0855, 2: 15.9994, 3: 1.0079, 4: 87.6200, 5: 35.4530}

# LJ 参数 (real units: kcal/mol, Å)
# 结构: {type: (epsilon, sigma, 来源, 置信度)}
# 注意: 本字典为体系文档记录; 实际生效的 pair_coeff 在 run_final.lmp,
#       修改此处后需同步 run_final.lmp 保持一致。
type_lj = {
    1: (0.1554, 3.1655, "近似 CLAYFF O 参数", "中"),
    2: (0.1554, 3.1655, "SPC/E 水模型标准", "高"),
    3: (0.0, 1.0, "SPC/E 标准 (H 无 LJ)", "高"),
    4: (0.1, 3.0, "随手设定, 无文献", "低"),
    5: (0.1, 4.0, "随手设定, 无文献", "低"),
}

# ---- 文献建议值 (备用, 切换前请核对原始文献并同步 run_final.lmp) ----
# Cl⁻ (type 5, 推荐替换):
#   Joung & Cheatham, J. Phys. Chem. B 2008, 112, 9020 (针对 SPC/E 水优化)
#   ε = 0.1000 kcal/mol, σ = 4.045 Å
# Sr²⁺ (type 4, 待核对):
#   常见方案: Aqvist 1990 (SPC 水, 势形式不同需换算), Mamatkulov 2013,
#   Li-Song-Merz 2015 (12-6-4 模型); 数值随水模型而异, 建议按 SPC/E 选用
#   后替换 (work-log 指出当前 σ=3.0 可能偏小, 深吸附阱或为力场假象)
LJ_ION_REF = {
    "cl_jc_spce": (0.1000, 4.045),   # Cl⁻ Joung-Cheatham 2008 (SPC/E)
}

# SPC/E 水分子几何
oh_dist = 1.0
angle_half = math.radians(109.47 / 2)
h_local_x = oh_dist * math.sin(angle_half)
h_local_y = oh_dist * math.cos(angle_half)

# ========== 建表面 ==========
surf_atoms = []
aid = 0
for iz in range(nlayers):
    for iy in range(ny):
        for ix in range(nx):
            x = ix * a + (iz % 2) * a / 2
            y = iy * a + (iz % 2) * a / 2
            z = iz * a
            if (ix + iy + iz) % 2 == 0:  # 一半原子 (菱形图案)
                aid += 1
                surf_atoms.append((aid, 1, x, y, z))

# 盒子尺寸
xs = nx * a
ys = ny * a
z_max_surf = max(a[4] for a in surf_atoms) + 1.0
zlo = -1.0
zhi = water_z_start + water_thickness + 40.0  # 额外真空层防周期镜像干扰

print(f"盒子: x=0-{xs:.1f} y=0-{ys:.1f} z={zlo:.1f}-{zhi:.1f}", file=sys.stderr)

# ========== 加水 ==========
# 间隔 3.2 Å (≈ 1 g/cm³ SPC/E 密度)
sp = 3.2
nwx = max(1, int(xs / sp))
nwy = max(1, int(ys / sp))
nwz = max(1, int(water_thickness / sp))

water_atoms = []
water_mols = 0
min_d2_surf = 10.24       # 与表面最小间距 3.2²

# 表面原子位置
surf_positions = [(a[2], a[3], a[4]) for a in surf_atoms]

for iz in range(nwz):
    for iy in range(nwy):
        for ix in range(nwx):
            # 水分子中心 (不加随机扰动, 保持规则排列避免重叠)
            cx = (ix + 0.5) * sp
            cy = (iy + 0.5) * sp
            cz = water_z_start + (iz + 0.5) * sp

            # 安全检查: 与表面距离
            too_close = False
            for sx, sy, sz in surf_positions:
                dx, dy, dz = cx - sx, cy - sy, cz - sz
                if dx*dx + dy*dy + dz*dz < min_d2_surf:
                    too_close = True
                    break
            if too_close:
                continue

            # 随机旋转水分子
            theta = random.uniform(0, 2*math.pi)
            phi = random.uniform(0, math.pi)

            # O 原子
            aid += 1
            oid = aid
            water_atoms.append((aid, 2, cx, cy, cz))

            # H 原子 (绕 x 轴旋转 theta, 再绕 y 轴旋转 phi)
            h1x = h_local_x * math.cos(theta)
            h1y = h_local_x * math.sin(theta) * math.cos(phi) + h_local_y * math.sin(phi)
            h1z = h_local_x * math.sin(theta) * math.sin(phi) - h_local_y * math.cos(phi)

            h2x = -h_local_x * math.cos(theta)
            h2y = -h_local_x * math.sin(theta) * math.cos(phi) + h_local_y * math.sin(phi)
            h2z = -h_local_x * math.sin(theta) * math.sin(phi) - h_local_y * math.cos(phi)

            aid += 1
            water_atoms.append((aid, 3, cx+h1x, cy+h1y, cz+h1z))
            aid += 1
            water_atoms.append((aid, 3, cx+h2x, cy+h2y, cz+h2z))
            water_mols += 1

print(f"表面原子: {len(surf_atoms)}", file=sys.stderr)
print(f"水分子: {water_mols}", file=sys.stderr)

# ========== 加 Sr²⁺ 和 Cl⁻ (替换水分子) ==========
water_vol = xs * ys * water_thickness  # Å³
water_vol_L = water_vol * 1e-27
na = 6.022e23

n_sr = max(1, int(conc * water_vol_L * na)) + extra_sr
n_cl = (n_sr - extra_sr) * 2

# 取出部分水(3原子一组), 换为离子
n_remove = n_sr + n_cl
# 从所有水中选 n_remove 个分子
wat_indices = list(range(water_mols))
random.shuffle(wat_indices)
remove_set = set(wat_indices[:n_remove])

new_water_atoms = []
removed_o = []
for i in range(water_mols):
    if i in remove_set:
        # 记录氧位置, 不放水
        oid = len(surf_atoms) + i * 3 + 1
        _, _, ox, oy, oz = water_atoms[i * 3]  # O atom
        removed_o.append((ox, oy, oz))
        # 不添加这3个水原子
    else:
        for j in range(3):
            new_water_atoms.append(water_atoms[i * 3 + j])

# 在移除的水位置上放离子
ion_atoms = []
for k, (ix, iy, iz) in enumerate(removed_o):
    itype = 4 if k < n_sr else 5
    aid = len(surf_atoms) + len(new_water_atoms) + k + 1
    ion_atoms.append((aid, itype, ix, iy, iz))

water_atoms = new_water_atoms
water_mols = water_mols - n_remove

all_atoms = surf_atoms + water_atoms + ion_atoms
n_total = len(all_atoms)

# 重新编号原子
renumbered = []
for i, (_, atype, x, y, z) in enumerate(all_atoms):
    renumbered.append((i+1, atype, x, y, z))
all_atoms = renumbered

# 检查电中性
total_charge = sum(type_charge[t] for _, t, _, _, _ in all_atoms)
print(f"总电荷: {total_charge:.4f} (应为 0)", file=sys.stderr)
print(f"Sr²⁺: {n_sr}, Cl⁻: {n_cl}", file=sys.stderr)

# ========== 写入 LAMMPS data ==========
total_bonds = water_mols * 2
total_angles = water_mols

# 输出到脚本同目录 (容器内 /data/strontium_adsorption/, Windows 本地同目录)
fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "system.data")
with open(fname, "w") as f:
    f.write(f"Charged surface + SPC/E water + SrCl2\n\n")
    f.write(f"{n_total} atoms\n")
    f.write(f"{total_bonds} bonds\n")
    f.write(f"{total_angles} angles\n\n")
    f.write("5 atom types\n")
    f.write("1 bond types\n")
    f.write("1 angle types\n\n")

    f.write(f"{0:.6f} {xs:.6f} xlo xhi\n")
    f.write(f"{0:.6f} {ys:.6f} ylo yhi\n")
    f.write(f"{zlo:.6f} {zhi:.6f} zlo zhi\n\n")

    f.write("Masses\n\n")
    for t in range(1, 6):
        f.write(f"{t} {type_mass[t]:.4f}  # {type_name[t]}\n")

    f.write("\nAtoms\n\n")
    # 水面原子 (mol_id=0), 水分子 (mol_id=1..N)
    mol_id = 0
    next_is_o = True
    for aid, atype, x, y, z in all_atoms:
        if atype == 2:  # Ow, 新分子开始
            mol_id += 1
        if atype in (2, 3):  # 水分子
            chg = type_charge[atype]
            f.write(f"{aid} {mol_id} {atype} {chg:.6f} {x:.6f} {y:.6f} {z:.6f}\n")
        else:  # 表面或离子
            chg = type_charge[atype]
            f.write(f"{aid} 0 {atype} {chg:.6f} {x:.6f} {y:.6f} {z:.6f}\n")

    f.write("\nBonds\n\n")
    bid = 0
    for i in range(water_mols):
        oid = len(surf_atoms) + i * 3 + 1
        for h in [1, 2]:
            bid += 1
            f.write(f"{bid} 1 {oid} {oid+h}\n")

    f.write("\nAngles\n\n")
    for i in range(water_mols):
        oid = len(surf_atoms) + i * 3 + 1
        f.write(f"{i+1} 1 {oid+1} {oid} {oid+2}\n")

print(f"\n写入完成: {fname}", file=sys.stderr)
print(f"总原子: {n_total}, 水分子: {water_mols}, Sr: {n_sr}, Cl: {n_cl}", file=sys.stderr)

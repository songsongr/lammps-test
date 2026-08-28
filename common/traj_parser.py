"""
LAMMPS 轨迹文件 (.lammpstrj) 通用解析器。

用法:
    from common.traj_parser import parse_lammpstrj, atoms_of_type
    frames = parse_lammpstrj("prod.lammpstrj")
    # frames[i] = {"timestep": int,
    #              "box": (xlo, xhi, ylo, yhi, zlo, zhi),
    #              "atoms": [{"id":int, "type":int, "x":float, ...}, ...]}
    # 原子字段由 dump 的 ITEM: ATOMS 头动态确定 (id/type/x/y/z 等)

特性:
    - 自动解析 ITEM: ATOMS 头确定列名与顺序
    - 支持正交 (3 列) 与倾斜/非周期 (2 列) 盒边界
    - 数值字段自动转 int/float
"""
import os


def parse_lammpstrj(filename):
    """解析 lammpstrj 文件, 返回帧列表。"""
    frames = []
    with open(filename, "r") as f:
        lines = f.readlines()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()
        if line != "ITEM: TIMESTEP":
            i += 1
            continue

        timestep = int(lines[i + 1].strip())
        i += 2

        # ---- NUMBER OF ATOMS ----
        if not lines[i].strip().startswith("ITEM: NUMBER"):
            break
        natoms = int(lines[i + 1].strip())
        i += 2

        # ---- BOX BOUNDS ----
        if not lines[i].strip().startswith("ITEM: BOX"):
            break
        i += 1
        bounds = []
        for _ in range(3):
            parts = lines[i].strip().split()
            bounds.append((float(parts[0]), float(parts[1])))
            i += 1
        xlo, xhi = bounds[0]
        ylo, yhi = bounds[1]
        zlo, zhi = bounds[2]
        box = (xlo, xhi, ylo, yhi, zlo, zhi)

        # ---- ATOMS 头 ----
        while i < n and not lines[i].strip().startswith("ITEM: ATOMS"):
            i += 1
        if i >= n:
            break
        cols = lines[i].strip().split()[2:]   # 去掉 "ITEM:" 与 "ATOMS"
        i += 1

        # ---- 原子数据 ----
        atoms = []
        for _ in range(natoms):
            parts = lines[i].strip().split()
            i += 1
            if len(parts) != len(cols):
                continue
            atom = {}
            for col, val in zip(cols, parts):
                if col in ("id", "type", "mol", "ix", "iy", "iz"):
                    atom[col] = int(val)
                elif col in ("x", "y", "z", "xu", "yu", "zu",
                             "xs", "ys", "zs",
                             "vx", "vy", "vz", "fx", "fy", "fz", "q"):
                    atom[col] = float(val)
                else:
                    atom[col] = val
            atoms.append(atom)

        frames.append({"timestep": timestep, "box": box, "atoms": atoms})

    return frames


def atoms_of_type(frames, atom_type):
    """生成器: 逐帧产出指定 type 的原子坐标列表 [(x, y, z), ...]。"""
    for frame in frames:
        yield [(a["x"], a["y"], a["z"])
               for a in frame["atoms"] if a["type"] == atom_type]

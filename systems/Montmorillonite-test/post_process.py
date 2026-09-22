#!/usr/bin/env python3
"""
post_process.py — LAMMPS 模拟后处理: XLSX + 画图

输出:
  MSD.xlsx, RDF.xlsx  — Excel 数据表 (作业提交)
  msd.png, rdf.png    — 成果图

用法: uv run python post_process.py
"""

import os, sys
import numpy as np
import matplotlib.pyplot as plt

# ---- 项目根加入 sys.path 以便 import 公共库 common/ ----
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common.traj_parser import parse_lammpstrj
from common.rdf import compute_rdf

# ---- 路径约定: 输入输出均相对本脚本目录 (docs/workflows.md) ----
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
def _p(name: str) -> str:
    return os.path.join(SCRIPT_DIR, name)

# ---- handle Windows GBK console ----
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import openpyxl
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False
    print("[提示] openpyxl 未安装, 跳过 XLSX 输出")
    print("  安装: uv pip install openpyxl")

# ============================================================
# 1. 读取 MSD 数据
# ============================================================
print("=" * 60)
print("蒙脱石模拟后处理")
print("=" * 60)

print("\n[1/3] 读取 MSD 数据...")
data = np.loadtxt(_p("msd.dat"), skiprows=3)
time_fs = (data[:, 0] - data[0, 0]) * 0.5  # 步数→时间 (步长0.5fs)
msd_water = data[:, 1]
msd_Ca = data[:, 2]
msd_fw = data[:, 3]

print(f"  时间范围: {time_fs[0]:.0f} - {time_fs[-1]:.0f} fs ({time_fs[-1]/1000:.2f} ps)")
print(f"  水 MSD 范围: {msd_water[0]:.3f} - {msd_water[-1]:.3f} A^2")

# 计算扩散系数 D = slope / 6 (MSD vs time 的斜率/6)
mask = time_fs > 2000  # 取稳态段
if np.sum(mask) > 5:
    slope_w = np.polyfit(time_fs[mask], msd_water[mask], 1)[0]
    D_water = slope_w / 6.0 * 0.1  # A^2/fs -> cm^2/s
    print(f"  水扩散系数 D = {D_water:.2e} cm^2/s")
    print(f"  (水 MSD 斜率 = {slope_w:.4f} A^2/fs)")

# 写入 XLSX
if HAS_OPENPYXL:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "MSD"
    ws.append(["时间 (fs)", "时间 (ps)", "MSD_水 (A^2)", "MSD_Ca (A^2)", "MSD_骨架 (A^2)"])
    for i in range(len(time_fs)):
        ws.append([time_fs[i], time_fs[i]/1000, msd_water[i], msd_Ca[i], msd_fw[i]])
    wb.save(_p("MSD.xlsx"))
    print("  已写入 MSD.xlsx")

# ============================================================
# 2. 画 MSD 图
# ============================================================
print("\n[2/3] 画 MSD 图...")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(time_fs/1000, msd_water, "b-", label="H2O (water)", linewidth=2)
ax.plot(time_fs/1000, msd_Ca, "r-", label="Ca2+", linewidth=2)
ax.plot(time_fs/1000, msd_fw, "g-", label="Framework (Al/Si/O)", linewidth=2)

ax.set_xlabel("Time (ps)", fontsize=12)
ax.set_ylabel("MSD (A^2)", fontsize=12)
ax.set_title("Mean Square Displacement - Montmorillonite", fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(_p("msd_plot.png"), dpi=200)
print("  已保存 msd_plot.png")

# ============================================================
# 3. 从轨迹计算 RDF
# ============================================================
print("\n[3/3] 从轨迹计算 RDF...")

# parse_lammpstrj / compute_rdf 已迁移至 common (2026-08-14), 此处直接复用

# 解析轨迹
try:
    frames = parse_lammpstrj(_p("prod.lammpstrj"))
    print(f"  解析 {len(frames)} 帧轨迹")

    if len(frames) > 0:
        # 每隔 10 帧计算一次 RDF，然后平均
        stride = max(1, len(frames) // 50)
        selected = frames[::stride]
        print(f"  使用 {len(selected)} 帧计算 RDF (stride={stride})")

        # 准备 RDF 累加器
        dr = 0.1
        rmax = 10.0
        nbins = int(rmax / dr)
        rdf_owow = np.zeros(nbins)
        rdf_owca = np.zeros(nbins)
        rdf_caob = np.zeros(nbins)
        rdf_owob = np.zeros(nbins)
        count = 0

        for frame in selected:
            box = frame["box"]
            atoms = frame["atoms"]

            # 按类型分组
            type8 = [(a["x"], a["y"], a["z"]) for a in atoms if a["type"] == 8]
            type7 = [(a["x"], a["y"], a["z"]) for a in atoms if a["type"] == 7]
            type1 = [(a["x"], a["y"], a["z"]) for a in atoms if a["type"] in (1, 2, 3)]

            if count == 0:
                print(f"  每帧: Ow={len(type8)}, Ca={len(type7)}, Ob={len(type1)}")

            if len(type8) > 1:
                r_vals, rdf1 = compute_rdf(type8, type8, box, dr, rmax)
                rdf_owow += rdf1
            if len(type8) > 0 and len(type7) > 0:
                _, rdf2 = compute_rdf(type8, type7, box, dr, rmax)
                rdf_owca += rdf2
            if len(type7) > 0 and len(type1) > 0:
                _, rdf3 = compute_rdf(type7, type1, box, dr, rmax)
                rdf_caob += rdf3
            if len(type8) > 0 and len(type1) > 0:
                _, rdf4 = compute_rdf(type8, type1, box, dr, rmax)
                rdf_owob += rdf4

            count += 1

        if count > 0:
            rdf_owow /= count
            rdf_owca /= count
            rdf_caob /= count
            rdf_owob /= count

            # 写入 RDF XLSX
            if HAS_OPENPYXL:
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.title = "RDF"
                ws.append(["r (A)", "g_OwOw", "g_OwCa", "g_CaOb", "g_OwOb"])
                for i in range(nbins):
                    ws.append([r_vals[i], rdf_owow[i], rdf_owca[i], rdf_caob[i], rdf_owob[i]])
                wb.save(_p("RDF.xlsx"))
                print("  已写入 RDF.xlsx")

            # 画 RDF 图
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

            ax1.plot(r_vals, rdf_owow, "b-", label="Ow-Ow", linewidth=1.5)
            ax1.plot(r_vals, rdf_owca, "r-", label="Ow-Ca", linewidth=1.5)
            ax1.plot(r_vals, rdf_owob, "g-", label="Ow-Ob", linewidth=1.5)
            ax1.set_xlabel("r (A)", fontsize=12)
            ax1.set_ylabel("g(r)", fontsize=12)
            ax1.set_title("RDF - Water Interactions", fontsize=13)
            ax1.legend(fontsize=10)
            ax1.grid(True, alpha=0.3)
            ax1.set_xlim(1.5, 8.0)

            ax2.plot(r_vals, rdf_owca, "r-", label="Ow-Ca", linewidth=2)
            ax2.plot(r_vals, rdf_caob, "m-", label="Ca-Ob (framework)", linewidth=2)
            ax2.set_xlabel("r (A)", fontsize=12)
            ax2.set_ylabel("g(r)", fontsize=12)
            ax2.set_title("RDF - Ca2+ Interactions", fontsize=13)
            ax2.legend(fontsize=10)
            ax2.grid(True, alpha=0.3)
            ax2.set_xlim(1.5, 8.0)

            fig.tight_layout()
            fig.savefig(_p("rdf_plot.png"), dpi=200)
            print("  已保存 rdf_plot.png")
        else:
            print("  警告: 未找到可用帧")
    else:
        print("  警告: 轨迹为空")
except FileNotFoundError:
    print("  警告: prod.lammpstrj 未找到, 跳过 RDF 计算")
except Exception as e:
    print(f"  警告: RDF 计算出错: {e}")

print("\n" + "=" * 60)
print("后处理完成!")
print("  输出: MSD.xlsx, RDF.xlsx (若安装了openpyxl)")
print("        msd_plot.png, rdf_plot.png")
print("=" * 60)

# 蒙脱石层间水与 Ca²⁺ 动力学模拟

> 基于 CIF 晶体结构的蒙脱石模型，研究层间水和 Ca²⁺ 的动力学行为。
> 这是对"真实蒙脱石 TOT 层"方向（[docs/work-log.md](../docs/work-log.md) P3 待办）的初步尝试。

## 模拟目标

- 用真实蒙脱石晶格（而非均匀点电荷表面）建立 CLAYFF 力场模型
- 计算层间水与 Ca²⁺ 的**扩散系数**（MSD 线性拟合）
- 计算**径向分布函数**（RDF）：水-水、水-Ca²⁺、Ca²⁺-表面氧的配位结构

## 管线

```
Montmorillonite.cif ──convert_cif.py──▶ system.data ──01_run.lmp──▶ msd.dat / prod.lammpstrj
(VESTA/晶体库结构,    (2×2×1 超胞,        (平衡 50k 步 +           │
 Al2 Ca0.5 O12 Si4)    CLAYFF 类型/电荷,   生产 100k 步)            ▼
                       80 个 SPC/E 层间水)              post_process.py ──▶ MSD.xlsx, RDF.xlsx, *.png
```

## 文件说明

| 文件 | 说明 |
|------|------|
| `Montmorillonite.cif` | 源晶体结构（正交 a=20.72 b=35.92 c=15.0 Å, P1） |
| `9002779.vesta` | 同结构的 VESTA 格式文件（晶体库 ID 9002779） |
| `convert_cif.py` | CIF → LAMMPS data 转换：超胞、CLAYFF 类型/电荷、OH 加 H、随机放置 80 个 SPC/E 水、生成键/角连接 |
| `system.data` | LAMMPS 数据文件（convert_cif.py 的输出, 01_run.lmp 的输入） |
| `01_run.lmp` | 模拟脚本：阶段 1 平衡（NVE/limit + Langevin 300 K, 50000 步）+ 阶段 2 生产（compute msd + fix ave/time + dump, 100000 步） |
| `msd.dat` | LAMMPS 输出的 MSD 时间序列（水/Ca²⁺/骨架） |
| `prod.lammpstrj` | 生产阶段轨迹（每 200 步一帧, RDF 分析输入） |
| `post_process.py` | 后处理：MSD → 扩散系数（t>2000 fs 斜率拟合）+ RDF（Ow-Ow, Ow-Ca, Ca-Ob, Ow-Ob）→ XLSX/PNG |
| `MSD.xlsx` / `RDF.xlsx` | 处理后的数值结果 |
| `msd_plot.png` / `rdf_plot.png` | 结果图 |
| `log.lammps` | LAMMPS 热力学日志 |
| `equil.data` / `equil.lammpstrj` | 遗留文件（早期版本产物, 当前脚本不引用） |

> ℹ️ 扩散系数 D 由 `post_process.py` 打印到控制台（未单独存文件）。

## 体系与参数

- 力场: CLAYFF（类型: ob/obos/oh/ho/st/ao/Ca/Ow/Hw, 类型表与参数见 `convert_cif.py`）
- 超胞: 2×2×1
- 层间水: 80 个 SPC/E 分子（键 K=554.13 r₀=1.0 Å; 角 K=45.77 θ₀=109.47°）
- 边界: p p p; 静电: `lj/cut/coul/long 9.0 8.0` + `pppm 1e-4`
- 时间步长: 0.5 fs; 平衡 50000 步 + 生产 100000 步

## 常用命令

```powershell
# 1. 生成体系 (Windows 本地, 相对路径)
uv run python convert_cif.py

# 2. 运行模拟 (容器内, -w 指定工作目录使相对路径生效)
uv run run-mmt-sim   # 暂存-运行-回收 (common.runner); 手动等价见 docs/workflows.md

# 3. 分析 (MSD 扩散 + RDF → xlsx/png)
uv run python post_process.py
```

## 已知事项

- `rdf_owow.dat`（0 字节孤儿文件）已于 2026-08-14 删除，无脚本读写它
- `equil.data` / `equil.lammpstrj` 未被当前脚本引用，保留作存档
- 本模型为早期探索，模拟时长有限（0.5 fs 步长 × 15 万步 = 75 ps），扩散系数精度需更长模拟验证

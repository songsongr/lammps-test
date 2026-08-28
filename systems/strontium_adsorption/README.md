# SrCl2 在带电黏土表面吸附模拟

> 本 README 描述体系的**当前模型与使用方法**；历史运行结果、讨论结论、待办清单见
> [docs/work-log.md](../docs/work-log.md)，力场参数与可信度见 [docs/parameters.md](../docs/parameters.md)。

## 模拟目标

研究 Sr²⁺ 和 Cl⁻ 在带电黏土表面附近的吸附行为：

- 比较贴近表面 vs 本体水中的 Sr²⁺ 浓度差异
- 观察离子在表面的配位环境
- 为后续蒙脱石真实模型提供方法验证

## 当前模型

### 体系组成

| 组分 | 原子类型 | 说明 |
|------|----------|------|
| 带电表面 | type 1 (Surf) | 2层, 10×10 超胞, 每个原子电荷 -0.12, 固定不动 |
| SPC/E 水 | type 2 (Ow), type 3 (Hw) | ~70 Å 水层, 刚性模型 (harmonic bond + harmonic angle) |
| Sr²⁺ | type 4 (Sr) | 0.25 mol/L + 额外 6 个平衡表面电荷 |
| Cl⁻ | type 5 (Cl) | 由电中性条件确定数量 |

### 力场

| 相互作用 | 设置 |
|----------|------|
| 短程 LJ | lj/cut, 截断 8 Å, arithmetic 混合规则 |
| 长程静电 | PPPM, 精度 1e-4, 截断 9 Å |
| 水分子内 | harmonic bond (K=554.13, r₀=1.0 Å), harmonic angle (K=45.77, θ₀=109.47°) |
| 近邻排除 | special_bonds lj 0.0 0.0 0.5 coul 0.0 0.0 0.5 |
| 边界条件 | p p p (三个方向周期性, PPPM 要求) |

> ⚠️ 表面/离子 LJ 参数可信度有限，详见 [docs/parameters.md](../docs/parameters.md) 的"力场可信度批判"。

### 模拟流程 (run_final.lmp)

1. 读取 `system.data`
2. 冻结表面原子 (`fix setforce 0 0 0`)
3. 能量最小化 (CG, etol=1e-4, ftol=1e-6)
4. NVT 平衡 (300 K, Nosé-Hoover, 100000 步 × 2.0 fs = 200 ps, SHAKE 约束水分子)
5. 生产模拟 (50000 步 × 2.0 fs = 100 ps, 每 100 步输出轨迹)

## 文件说明

```text
systems/strontium_adsorption/
├── README.md              # 本文档
│
├── build_system.py        # 体系生成脚本 (Python)
│   ├── 生成表面晶格、水分子网格、随机替换部分水为离子
│   ├── 输出 system.data (原子坐标 + 键 + 角 + 盒子尺寸)
│   └── 关键参数: water_thickness=70, conc=0.25, a=3.0, nx=ny=10
│
├── system.data            # LAMMPS 数据文件 (由 build_system.py 生成)
│
├── run_final.lmp          # 正式 LAMMPS 输入脚本 ★
│   └── 所有 .lmp 文件的写作模板 — 分板块、每行注释、ASCII print
│
├── analyze_sr.py          # Sr²⁺ z 分布分析 (读取 prod.lammpstrj)
│   └── 输出 sr_z_histogram.txt/png, sr_z_distribution.txt
│
├── prod.lammpstrj         # 正式生产轨迹 (VMD 可读)
│
├── archive/               # 旧尝试 (早期脚本、废弃方案)
│   ├── generate_mmt.py
│   ├── gen_system_v2.py
│   ├── build_all.lmp
│   ├── run_simple.lmp
│   ├── run_v2.lmp
│   ├── run_sr_mmt.lmp
│   └── run_sr_mmt_v2.lmp
│
└── runs/                  # 运行产物 (日志、重启文件、中间轨迹)
    ├── log.lammps
    ├── out.log
    ├── equil_300k.restart
    ├── minimized.data
    ├── traj.dump
    ├── traj.lammpstrj
    └── sr_zprofile.dump
```

## 常用命令

### 生成体系

```powershell
uv run build-sr
# 体系参数真相源: system.json → 构建器 common/builders/surface_adsorption.py
# 输出: system.data + build_report.json (脚本同目录)
# (旧版 build_system.py 已归档于 archive/, 由新引擎取代且种子级等价)
```

### 运行模拟

```powershell
# 本地 Docker (-w 指定工作目录, .lmp 内用相对路径; -sf omp 为 OMP 加速, 线程数按机器调整)
uv run run-sr-sim   # 暂存-运行-回收 (common.runner 契约, 见 docs/workflows.md)

# 远程 (Tailscale + SSH)
uv run run-sr-sim   # 本地; 远程需远程机具备相同容器与数据目录约定
```

### 分析

```powershell
uv run python analyze_sr.py
```

### 查看轨迹 (VMD)

```powershell
& "C:\Program Files\VMD\vmd.exe" C:\Users\23653\Desktop\cc-proj\lammps-test\systems\strontium_adsorption\prod.lammpstrj
```

VMD 建议设置：

- 查看 Sr²⁺: `Graphics → Representations → Selected Atoms: type 4`
- 绘图方法: `VDW` 或 `CPK` (避免 Lines 产生周期边界假键)
- 查看水: `type 2 3`, 用 `Lines` 或 `Licorice`

## 已知局限

1. **模型是近似表面** — 非真实蒙脱石晶格，用均匀点电荷替代表面
2. **模拟长度太短** — 100 ps 生产远不够观察吸附平衡
   - 改进方向: 加 SHAKE 约束 → 步长提到 2 fs → 跑 1 ns（已完成 SHAKE 改造）
3. **没有压力耦合** — 纯 NVT，无 barostat
   - 水层密度可能偏离 1 g/cm³
4. **无表面弛豫** — 表面原子完全冻结，不允许表面响应离子吸附
5. **力场参数精度** — 表面 LJ 参数近似 CLAYFF，离子 LJ 参数需核对文献

## 下一步改进

待办清单（含优先级）已移至 [docs/work-log.md](../docs/work-log.md) 文末。
近期重点: **P0 OMP 加速改造** 与 **P0 校正 Sr/Cl LJ 参数**。

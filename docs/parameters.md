# 力场与参数体系

> **数值真相源 (2026-08-28 起)**: 力场参数的权威数值在各项目的 `system.json`
> （atom_types: 电荷/ε/σ + source + confidence + warning）。本文档是**人工可读对照表**，
> 若与 system.json 冲突以 system.json 为准。
> strontium 体系为历史混合体（SPC 电荷 + SPC/E 型 O-LJ），已如实记录并标注。

## 各体系力场对照

| 系统 | 力场 | 体系配置 (真相源) | 构建器 |
|------|------|------------------|--------|
| 简单吸附 (Ar/Cu) | `lj/cut` | —（自包含脚本） | `systems/demos/adsorption.lmp` |
| 带电表面+水+SrCl₂ | 历史混合 (SPC 电荷 + SPC/E 型 O-LJ) + 离子LJ | `systems/strontium_adsorption/system.json` | `common/builders/surface_adsorption.py` |
| 蒙脱石+层间水+Ca²⁺ | CLAYFF + SPC/E | `systems/Montmorillonite-test/system.json` | `common/builders/clay_cif.py` |

## 关键参数源（带电表面体系）

- **SPC/E 水几何**: 键长 1.0 Å, 键角 109.47°, 刚性模型（`bond_style harmonic` + `angle_style harmonic`，或用 SHAKE）
- **表面晶格**: 自定义点电荷表面或 CLAYFF 结构, `a0` = 3.0–5.23 Å
- **离子浓度**: 0.25 mol/L SrCl₂（~15 Sr²⁺ + 30 Cl⁻ @ 70 Å 水层）
- **长程静电**: `kspace_style pppm 1e-4`
- **键/角处理**: `special_bonds lj 0.0 0.0 0.5 coul 0.0 0.0 0.5`（SPC/E 水分子内静电排除）
- **截断半径**: Coulomb 9.0 Å (pair) + 8.0 Å (LJ) + PPPM 长程修正
- **温度**: NVT 300 K, Langevin 或 Nosé-Hoover (`fix nvt`)
- **混合规则**: arithmetic（`sigma_ij = (sigma_i + sigma_j)/2`, `epsilon_ij = sqrt(epsilon_i * epsilon_j)`）
- **蒙脱石原子类型与电荷**: CLAYFF 类型表见 `systems/Montmorillonite-test/convert_cif.py`

## 带电表面体系最终参数（run_final.lmp）

| 参数 | 值 | 说明 |
|------|------|------|
| 单位 | real | kcal/mol, Å, g/mol, fs, e, K, atm |
| atom_style | full | 含 molecule-ID 和 charge |
| 边界 | p p p | 三个方向周期（PPPM 要求） |
| 力场非键 | lj/cut/coul/long 9.0 8.0 | LJ 截断 8 Å, Coulomb 截断 9 Å |
| 长程静电 | pppm 1e-4 | PPPM 求解器 |
| LJ pair_coeff | 1(Surf): ε=0.1554 σ=3.1655 ← 抄 CLAYFF O | |
| | 2(Ow): ε=0.1553 σ=3.1660 ← SPC/E | |
| | 3(Hw): ε=0 σ=1.0 ← 无 LJ | |
| | 4(Sr): ε=0.1 σ=3.0 ← **随手设的, 无文献 (待核对)** | |
| | 5(Cl): ε=0.1 σ=4.0 ← **随手设的, 无文献 (待核对)** | |
| | 文献建议 4(Sr): Aqvist 1990 / Mamatkulov 2013 / Li-Song-Merz 2015, 数值随水模型而异, 未定 | |
| | 文献建议 5(Cl): JC 2008 SPC/E: ε=0.1000 σ=4.045 ← **推荐替换** | |
| 键 | harmonic, K=554.13, r₀=1.0 (SPC/E O-H) | |
| 角 | harmonic, K=45.77, θ₀=109.47 (SPC/E H-O-H) | |
| special_bonds | lj 0 0 0.5 coul 0 0 0.5 ← SPC/E 标准 | |
| SHAKE | fix fshake water shake 0.0001 20 100 b 1 a 1 | |
| 时间步长 | 2.0 fs（SHAKE 启用, 原 0.2 fs） | |
| NVT 步数 | 100000 (200 ps) | |
| 生产步数 | 50000 (100 ps) | |
| 轨迹输出 | dump every 100 步, 每帧 5137 原子 | |
| 冻结 | fix setforce 0 0 0 作用于 surf 组 | |
| 恒温 | fix nvt, Nose-Hoover, T=300 K, damping=100 fs | |

## 体系数据（system.data, 由 build_system.py 生成）

```
盒子尺寸: 30x30x117 A^3 (z: -1~116, 水层 ~70 + 真空 ~40)
表面: 10x10 超胞, 2 层, 100 原子, 菱形图案(50%占位), a=3.0
  层0: z=0.0, 偶数(ix+iy)格点有原子
  层1: z=3.0, x/y偏移1.5, 奇数(ix+iy)格点有原子
表面电荷: 每原子 -0.12 -> 总 -12
水: SPC/E, 网格间距 3.2 A, 从 z=6.0 开始 -> 第一个 O 在 z=7.6
离子: 0.25M SrCl2 (9 Sr + 18 Cl) + 6 额外 Sr 平衡表面电荷 = 15 Sr + 18 Cl
  离子替换水分子, 替换位置在 z≈7.6 以上
总原子数: 5137 (表面 100 + 水 ~5004 + Sr 15 + Cl 18)
总键数: 3336 (= 水分子数 x 2)
总角数: 1668 (= 水分子数)
```

## 蒙脱石体系参数（Montmorillonite-test）

- 力场: CLAYFF（ob, obos, oh, ho, st, ao, Ca, Ow, Hw 类型表见 `convert_cif.py`）
- 结构: `Montmorillonite.cif`（Al2 Ca0.5 O12 Si4, a=20.72 b=35.92 c=15.0 Å）→ 2×2×1 超胞
- 层间: 80 个 SPC/E 水分子随机放置
- 模拟: 平衡 50000 步（NVE/limit + Langevin 300 K, dt=0.5 fs）+ 生产 100000 步
- 分析: MSD（水/Ca²⁺/骨架扩散）+ RDF（Ow-Ow, Ow-Ca, Ca-Ob, Ow-Ob）

## 力场可信度批判（IMPORTANT）

当前带电表面体系的力场是**四不像拼装货**，各部分可信度：

| 组分 | 状态 | 可信度 |
|------|------|--------|
| SPC/E 水 | 完整正确参数 | 可信 |
| 表面 LJ | 只抄了 CLAYFF 的 O 参数, 无 Si/Al/Mg/OH 区分 | 不可信 |
| 表面电荷 | 均匀 -0.12/原子, 非蒙脱石真实取代分布 | 不可信 |
| Sr²⁺ LJ | epsilon=0.1, sigma=3.0 随手给的 | 不可信, 需查文献 |
| Cl⁻ LJ | epsilon=0.1, sigma=4.0 随手给的 | 不可信, 需查文献 |
| 交叉项 | arithmetic 混合规则, 非 CLAYFF 标准 | 需验证 |

> **2026-08-14 更新**: 已核对 Joung-Cheatham (JPCB 2008, 112, 9020) — Cl⁻(SPC/E) 为 ε=0.1000 kcal/mol, σ=4.045 Å（推荐替换当前值）;
> Sr²⁺ 无统一文献值（随水模型而异）, 候选 Aqvist 1990 / Mamatkulov 2013 / Li-Song-Merz 2015, 尚未定案。
> 上述文献建议值已记录于 `run_final.lmp` pair_coeff 注释与 `build_system.py` `LJ_ION_REF`, 替换前请核对原始文献。

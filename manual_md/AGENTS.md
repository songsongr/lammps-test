# LAMMPS 文档图谱

> 基于 LAMMPS 30 Mar 2026 版官方手册整理
> 共 958 个文档页面，14 MB

---

## 📖 用户指南 (User Guide)

### 1. 简介 (Introduction)
| 文件 | 内容 |
|------|------|
| `Intro_overview.md` | LAMMPS 概述 — 经典分子动力学模拟软件，支持原子/分子/聚合物/生物/固体/颗粒/粗粒化等系统 |
| `Manual_version.md` | 版本号含义说明 |
| `Intro_features.md` | LAMMPS 功能特性列表 |
| `Intro_nonfeatures.md` | LAMMPS 不适用的场景 |
| `Intro_portability.md` | 跨平台兼容性信息 |
| `Intro_opensource.md` | 开源许可 (GPLv2) |
| `Intro_authors.md` | 作者列表 |
| `Intro_citing.md` | 引用 LAMMPS 的方式 |
| `Intro_website.md` | 相关网站链接 |

### 2. 安装 LAMMPS (Install)
| 文件 | 内容 |
|------|------|
| `Install_linux.md` | Linux 可执行文件下载 |
| `Install_mac.md` | macOS 可执行文件下载 |
| `Install_windows.md` | Windows 可执行文件下载 |
| `Install_conda.md` | 通过 Conda 安装 |
| `Install_tarball.md` | 下载源码和文档压缩包 |
| `Install_git.md` | 通过 Git 下载源码 |

### 3. 编译 LAMMPS (Build)
| 文件 | 内容 |
|------|------|
| `Build_prerequisites.md` | 编译前提条件 |
| `Build_cmake.md` | 用 CMake 编译 |
| `Build_make.md` | 用传统 Make 编译 |
| `Build_link.md` | 作为库链接到其他代码 |
| `Build_basics.md` | 基本编译选项 |
| `Build_settings.md` | 可选编译设置 |
| `Build_package.md` | 包含包 (Package) 的编译 |
| `Build_extras.md` | 需要额外依赖的包（93K 大文件） |
| `Build_manual.md` | 构建文档 |
| `Build_windows.md` | Windows 编译说明 |
| `Build_diskspace.md` | 节省磁盘空间的技巧 |
| `Build_development.md` | 开发编译选项 |

### 4. 运行 LAMMPS (Run)
| 文件 | 内容 |
|------|------|
| `Run_basics.md` | 基础运行方式 — `lmp -in in.file`、`mpirun -np 4 lmp -in in.file` 等 |
| `Run_options.md` | 命令行选项 — `-in`, `-var`, `-partition`, `-echo`, `-screen`, `-log`, `-restart`, `-skiprun` 等 |
| `Run_output.md` | 屏幕和日志文件输出 |
| `Run_formats.md` | 文件格式说明 |
| `Run_windows.md` | Windows 上运行 LAMMPS |

### 5. 错误处理 (Errors)
| 文件 | 内容 |
|------|------|
| `Errors_common.md` | 常见误解和问题 |
| `Errors_details.md` | 错误和警告的详细说明 |
| `Errors_bugs.md` | 报告 bug 的方式 |
| `Errors_debug.md` | 调试崩溃和卡死 |
| `Errors_messages.md` | **错误信息大全**（186K 大文件） |
| `Errors_warnings.md` | 警告信息大全 |

### 6. 命令 (Commands) ⭐ 最核心章节
| 文件 | 内容 |
|------|------|
| `Commands_input.md` | 输入脚本的工作方式 — 逐行读取、立即执行 |
| `Commands_parse.md` | 解析规则 — 变量替换、多行输入、文件包含 |
| `Commands_structure.md` | 输入脚本的标准结构：初始化 → 定义 → 运行 |
| `Commands_category.md` | 按类别划分的命令列表 |
| `Commands_all.md` | **所有命令的完整列表及链接** |

#### 命令分类参考
| 文件 | 内容 |
|------|------|
| `fix.md` | fix 命令 |
| `compute.md` | compute 命令 |
| `pair_style.md` | pair_style 命令 |
| `pair_coeff.md` | pair_coeff 命令 |
| `dump.md` / `dump_image.md` / `dump_movie.md` | 输出/可视化命令 |
| `dump_modify.md` | dump 修改选项 |
| `run.md` | 运行模拟 |
| `minimize.md` | 能量最小化 |
| `velocity.md` | 速度初始化 |
| `thermo.md` / `thermo_style.md` | 热力学输出控制 |
| `neighbor.md` / `neigh_modify.md` | 近邻列表设置 |
| `timestep.md` | 时间步长 |
| `units.md` | 单位制 |
| `atom_style.md` | 原子类型 |
| `boundary.md` | 边界条件 |
| `region.md` | 区域定义 |
| `create_box.md` / `create_atoms.md` | 创建模拟盒子和原子 |
| `read_data.md` / `read_restart.md` | 读取数据/重启文件 |
| `write_data.md` / `write_restart.md` | 写入数据/重启文件 |
| `group.md` | 原子分组 |
| `variable.md` | **变量定义**（93K 大文件） |
| `include.md` | 包含子脚本 |
| `label.md` / `next.md` / `jump.md` | 循环和跳转 |
| `print.md` | 打印输出 |

**完整命令参考见** `Commands_all.md`

### 7. 加速性能 (Speed)
| 文件 | 内容 |
|------|------|
| `Speed_bench.md` | 基准测试 |
| `Speed_measure.md` | 性能测量 |
| `Speed_tips.md` | 通用加速技巧 |
| `Speed_packages.md` | 加速包 (KOKKOS, OPENMP, OPT, INTEL, GPU) |
| `Speed_compare.md` | 各加速包对比 |

### 8. 可选包 (Packages)
| 文件 | 内容 |
|------|------|
| `Packages_details.md` | **所有可选包的详细说明**（143K 大文件） |

### 9. 辅助工具 (Tools)
| 文件 | 内容 |
|------|------|
| `Tools.md` | 预处理、后处理、杂项工具列表 (55K) |

### 10. Howto 讨论
- **完整列表**见 `Howto.md` (6.8K)，包含：
  - 通用 howto（输入脚本技巧、并行性能、多模拟等）
  - 设置 howto（力场、边界条件、电荷等）
  - 分析 howto（扩散、RDF、MSD 等）
  - 力场 howto（EAM、Buckingham、CHARMM、AMBER 等）
  - 包相关 howto
  - 教程 howto

### 11. 示例脚本 (Examples)
| 文件 | 内容 |
|------|------|
| `Examples.md` | 所有示例脚本的索引（11K） |

---

## 🔧 程序员指南 (Programmer Guide)

| 文件 | 内容 |
|------|------|
| `Library.md` | C/Python/Fortran/C++ 四种语言 API 接口 (13K) |
| `Library_properties.md` | 库属性接口（98K） |
| `Python_overview.md` | Python 接口概述 |
| `Python_module.md` | **lammps Python 模块详细文档**（117K） |
| `Python_run.md` | 从 Python 运行 LAMMPS |
| `Python_ext.md` | 扩展 Python 接口 |
| `Python_call.md` | 从 LAMMPS 调用 Python |
| `Python_jupyter.md` | 在 Jupyter 中使用 LAMMPS |
| `Modify_overview.md` | 修改/扩展 LAMMPS 的概述 |
| `Modify_contribute.md` | 提交新功能 |
| `Modify_requirements.md` | 贡献代码的要求 |
| `Modify_style.md` | LAMMPS 编程风格 |
| `Modify_atom.md` / `Modify_pair.md` / `Modify_bond.md` | 各风格开发指南 |
| `Modify_compute.md` / `Modify_fix.md` / `Modify_dump.md` | Compute/Fix/Dump 开发 |
| `Developer_org.md` | 源码目录结构 |
| `Developer_code_design.md` | 代码设计 |
| `Developer_parallel.md` | 并行算法 |
| `Developer_flow.md` | 一个时间步的执行流程 |
| `Developer_write.md` | 编写新风格 |
| `Developer_utils.md` | **工具类和函数大全**（246K） |
| `Developer_updating.md` | 旧版代码更新指南 |
| `Developer_plugins.md` | 插件编写 |
| `Classes.md` | C++ 基类说明 |
| `Fortran.md`| **Fortran 接口**（220K） |

---

## 📚 命令参考 (Command Reference)

| 文件 | 内容 |
|------|------|
| `commands_list.md` | **所有命令列表** |
| `fixes.md` | **所有 Fix 风格列表**（22K） |
| `computes.md` | **所有 Compute 风格列表**（15K） |
| `pairs.md` | **所有 Pair 风格列表**（29K） |
| `bonds.md` | 所有 Bond 风格列表 |
| `angles.md` | 所有 Angle 风格列表 |
| `dihedrals.md` | 所有 Dihedral 风格列表 |
| `impropers.md` | 所有 Improper 风格列表 |
| `dumps.md` | 所有 Dump 风格列表 |
| `Bibliography.md` | 参考文献（60K） |
| `genindex.md` | **全文索引**（297K 最大文件） |

---

## ⭐ 常用力场文件速查

| 力场类型 | 文件 |
|---------|------|
| Lennard-Jones | `pair_lj.md` / `pair_lj_cut.md` / `pair_lj_smooth.md` |
| EAM (金属) | `pair_eam.md` |
| Morse | `pair_morse.md` |
| Buckingham | `pair_buck.md` |
| CHARMM | `pair_lj_charmm.md` / `pair_lj_charmm_coul_charmm.md` |
| AMBER | `pair_amber.md` |
| ReaxFF (反应力场) | `pair_reaxff.md` |
| AIREBO (碳/烃) | `pair_airebo.md` |
| Tersoff (半导体) | `pair_tersoff.md` |
| SNAP (机器学习) | `pair_snap.md` |
| Born-Mayer | `pair_born.md` |
| Granular (颗粒) | `pair_gran.md` |
| Brownian (布朗) | `pair_brownian.md` |

---

## ⭐ 常用 Fix 速查

| Fix | 用途 |
|-----|------|
| `fix_nve.md` | NVE 系综（微正则） |
| `fix_nvt.md` | NVT 系综（正则，恒温） |
| `fix_npt.md` | NPT 系综（恒温恒压） |
| `fix_langevin.md` | Langevin 恒温器 |
| `fix_berendsen.md` | Berendsen 恒温/恒压 |
| `fix_deform.md` | 形变（拉伸/压缩） |
| `fix_rigid.md` | 刚体 |
| `fix_move.md` | 原子运动控制 |
| `fix_spring.md` | 弹簧势 |
| `fix_gravity.md` | 重力 |
| `fix_heat.md` | 热流 |
| `fix_ave_time.md` | 时间平均 |
| `fix_ave_spatial.md` | 空间平均 |
| `fix_print.md` | 打印输出 |

---

## ⭐ 常用 Compute 速查

| Compute | 用途 |
|---------|------|
| `compute_temp.md` | 温度 |
| `compute_pressure.md` | 压力 |
| `compute_stress.md` | 应力 |
| `compute_ke.md` | 动能 |
| `compute_pe.md` | 势能 |
| `compute_msd.md` | 均方位移 |
| `compute_rdf.md` | 径向分布函数 |
| `compute_gyration.md` | 回转半径 |
| `compute_centro.md` | 中心对称参数 (CSP) |
| `compute_ackland.md` | Ackland 晶体结构分析 |
| `compute_entropy.md` | 局域熵 |
| `compute_smd.md` | 平滑原子数密度 |

---

## 🔗 相关文档关联

- **新手上路**: `Intro_overview.md` → `Run_basics.md` → `Commands_input.md` → `Commands_structure.md` → `Commands_category.md`
- **Docker 用法**: `Run_basics.md`（命令行参数 `-in`） + `Run_windows.md`
- **写第一个脚本**: `Commands_structure.md` + `Commands_category.md` + 具体 `pair_style.md` + `fix_nve.md`
- **分析结果**: `thermo.md` + `dump.md` + `compute_msd.md` + `compute_rdf.md`
- **加速**: `Speed_tips.md` + `Speed_packages.md` + `package.md`

---

> 📁 所有文件位于 `manual_md/` 目录下
> 🔍 可用 `grep/findstr` 搜索命令名或关键词
> 📄 PDF 原版：`Manual.pdf`

# LAMMPS 分子动力学项目 + 控制中心工作台

**LAMMPS molecular dynamics simulations with a web-based control workbench** (FastAPI + React)

LAMMPS 分子动力学模拟研究项目，配套一个 Web 控制中心工作台：任务编排、实时日志与
thermo 曲线、体系参数可视化配置，全部通过浏览器操作，无需手写 LAMMPS 输入脚本。

## 研究主线

| 项目 | 体系 | 分析内容 |
|------|------|----------|
| 带电黏土表面吸附 | SrCl₂ 水溶液 + 带电表面 | Sr²⁺/Cl⁻ 沿 z 向分布 |
| 蒙脱石层间动力学 | CLAYFF 力场层间水 + Ca²⁺ | MSD 扩散系数 + RDF 水合结构 |

## 核心理念：体系即数据

每个研究项目的体系参数（几何/组成/力场）以项目目录下的 `system.json` 为**单一真相源**：

```
system.json  →  uv run build-xx  →  system.data + 模板渲染 run.lmp  →  暂存-运行-回收  →  分析
```

- 力场参数带 source / confidence 标注，科学数值不一致只标注不擅改
- 手改渲染产物（如 `run.lmp`）会在下次渲染时被检测并要求确认
- LAMMPS 任务统一走暂存-运行-回收契约（CLI 与工作台同源），失败自动解析归档

## 快速开始

**前置条件**：[uv](https://docs.astral.sh/uv/)（Python ≥ 3.10）、Docker（LAMMPS 在容器
`lammpsd` 中运行，镜像 `lammps/lammps:latest`；容器创建与挂载约定见
[docs/environment.md](docs/environment.md)）

```bash
uv sync             # 创建虚拟环境并安装依赖

# 研究 A：SrCl₂ 表面吸附
uv run build-sr     # 体系构建 (system.json → system.data)
uv run run-sr-sim   # 运行模拟（暂存-运行-回收）
uv run analyze-sr   # Sr²⁺/Cl⁻ z 分布分析

# 研究 B：蒙脱石层间动力学
uv run build-mmt && uv run run-mmt-sim && uv run postprocess-mmt

# 控制中心工作台
uv run workbench    # → http://127.0.0.1:8000
```

测试：

```bash
uv run pytest tests/ -q    # 78 用例
```

## 仓库结构

```
├── AGENTS.md            # AI 代理协作规范（人类入口也从这里开始）
├── ARCHITECTURE.md      # 架构总览（双空间设计）
├── common/              # 共享引擎：构建器 / runner / 一键 CLI / 输入 lint
├── systems/             # 内置研究项目（system.json + 模板渲染脚本 + 分析）
├── projects/            # 用户自建项目（project.json 零代码注册）
├── workbench/           # 控制中心工作台（FastAPI + React）
├── lammps-data-docker/  # 容器 /data 数据目录（任务工作区，gitignore）
├── manual_md/           # LAMMPS 官方手册 Markdown 转档（索引: manual_md/README.md）
├── docs/                # 详细文档（入口: docs/README.md）
└── tests/               # pytest 单元测试
```

## 文档导航

| 文档 | 内容 |
|------|------|
| [docs/README.md](docs/README.md) | 文档总索引 |
| [ARCHITECTURE.md](ARCHITECTURE.md) | 架构总览 |
| [docs/environment.md](docs/environment.md) | 环境与工具链（Docker 挂载/uv/workbench/VMD） |
| [docs/workflows.md](docs/workflows.md) | 体系配置层、标准工作流、`.lmp` 写作规范 |
| [docs/parameters.md](docs/parameters.md) | 力场参数对照（数值真相源 = 各项目 system.json） |
| [workbench/README.md](workbench/README.md) | 控制中心工作台使用说明 |

## 许可证

尚未选定开源许可证（默认保留所有权利，计划补充）。

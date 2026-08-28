# AGENTS.md

> AI 编码代理（Claude Code / ZCode / Codex / Cursor 等）在本仓库工作的规范指引，
> 遵循 [AGENTS.md](https://agents.md) 开放约定。
> 人类快速入口：[docs/README.md](docs/README.md)；架构总览：[ARCHITECTURE.md](ARCHITECTURE.md)。

## 项目概述

LAMMPS 分子动力学模拟项目 + **控制中心工作台**（Web 操控层），两条研究主线：

1. **SrCl₂ 在带电黏土表面的吸附**（`systems/strontium_adsorption/`）— 水层 + 带电表面 + Sr²⁺/Cl⁻
2. **蒙脱石层间水与 Ca²⁺ 动力学**（`systems/Montmorillonite-test/`）— CLAYFF 力场，MSD 扩散 + RDF 水合结构

核心架构原则：**体系即数据** — 每个研究项目的体系参数单一真相源是项目目录下的
`system.json`（几何/组成/力场，力场参数带 source + confidence），构建引擎与脚本渲染都从它读取。

## 仓库布局

```
.
├── AGENTS.md                  # 本文件（agent 规范指引）
├── ARCHITECTURE.md            # 当前架构总览 (双空间设计)
├── docs/                      # 详细文档（入口: docs/README.md）
├── workbench/                 # 控制中心工作台 (FastAPI + React; README.md)
│   ├── backend/app/           # 任务管理/体系模板/失败解析/thermo (routers + job_manager)
│   ├── backend/templates/     # 方法模板 (nvt_production)
│   ├── frontend/              # React SPA (构建产物由后端托管)
│   └── data/                  # 运行时 (任务库/日志, gitignore)
├── common/                    # 共享引擎
│   ├── system_config.py       # system.json 模型/校验/水模型预设/向导 schema
│   ├── builders/              # 体系构建器 (surface_adsorption/solution/clay_cif)
│   ├── build.py               # python -m common.build <dir> 入口
│   ├── runner.py              # 暂存-运行-回收统一执行契约 (CLI/workbench 同源)
│   ├── entrypoints.py         # 一键 CLI (build-sr/run-sr-sim/...)
│   ├── spce_params.py         # SPC/E 常量 (数值源: system_config 预设)
│   └── rdf.py / traj_parser.py / water_builder.py
├── systems/                   # 内置项目 (BUILTIN_DIRS 注册; "体系即数据" 研究/教学项目)
│   ├── strontium_adsorption/  # 研究 A: 带电表面吸附
│   │   ├── system.json        # 体系参数单一真相源
│   │   ├── run.lmp            # 模板渲染产物 (历史手写版在 archive/)
│   │   ├── analyze_sr.py      # z 分布分析 (参数读 system.json)
│   │   └── archive/ runs/     # 历史脚本 / 运行产物
│   ├── Montmorillonite-test/  # 研究 B: 蒙脱石层间动力学
│   │   ├── system.json        # 体系参数真相源 (clay_cif profile)
│   │   ├── 01_run.lmp         # 手写两段弛豫 (力场与 system.json 核对一致)
│   │   └── post_process.py archive/
│   └── demos/                 # 教学/环境验证 (自包含脚本, 无体系数据层)
├── projects/                  # 用户自建项目 (project.json 自动注册)
├── lammps-data-docker/        # 容器 /data 数据目录 (任务工作区, gitignore)
├── manual_md/                 # LAMMPS 官方手册转 Markdown（索引: manual_md/README.md）
└── tests/                     # 78 单元测试 (pytest)
```

## 环境与常用命令

- **Python**: uv 管理（`.venv` 在项目根），一律 `uv run ...`，不要用裸 `python`
- **容器**: Docker 容器 `lammpsd`（镜像 `lammps/lammps:latest`），`/data` = `lammps-data-docker/`
- **工作台**: `uv run workbench` → http://127.0.0.1:8000（FastAPI 后端 + React 前端）
- **终端**: 用户使用 PowerShell

```bash
# 测试
uv run pytest tests/ -q          # 78 用例基线, 改动前后都必须全绿

# 体系构建 (system.json → system.data + build_report.json)
uv run build-sr                  # strontium_adsorption
uv run build-mmt                 # Montmorillonite-test
# 等价: uv run python -m common.build <project_dir>

# 运行模拟 (暂存-运行-回收; 依赖闭包自动拷入任务工作区)
uv run run-sr-sim                # systems/strontium_adsorption/run.lmp (模板渲染产物)
uv run run-mmt-sim               # systems/Montmorillonite-test/01_run.lmp

# 分析
uv run analyze-sr                # Sr²⁺/Cl⁻ z 分布 (体系参数读自 system.json)
uv run postprocess-mmt           # MSD/RDF → xlsx/png

# 前端构建 (仅 frontend 源码变更后需要)
cd workbench/frontend && npm run build

# 手动等价 (与 runner 同一契约): 先拷脚本+依赖到 lammps-data-docker/jobs/<id>/, 然后
# docker exec -w /data/jobs/<id> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp 8 -in <script>.lmp
```

## 架构原则（修改代码前必读）

- **体系即数据**：体系参数唯一修改入口是 `system.json`（UI 表单或直接改文件）；
  改参数 → 重建（`uv run build-xx`）→ 重渲染脚本 → 运行。
  不要直接改渲染产物里的力场数值（会被下次渲染覆盖）
- **暂存-运行-回收**：LAMMPS 任务一律走 `common/runner.py` 契约或 workbench；
  直接 `docker exec -w /data/<项目>` 已失效（容器 `/data` 只挂数据目录）
- **双入口同源**：UI 每个动作都有文件/CLI 等价物；同一事实多处呈现必须一致
  （如挂载约定、项目清单、力场数值——发现漂移优先归一到真相源）
- **科学数值改动需用户拍板**：如力场参数切换预设（会改变科学结论），默认仅标注不修正
- **操作要可验证**：新增后台操作必须有对账/可见手段，不留静默失败路径

## 代码与文档规范

- `.lmp` 写作规范：9 板块结构 + 每行注释 + ASCII only + 力场行标注 source/confidence
  → 详见 [docs/workflows.md](docs/workflows.md)
- Python 脚本输出到**脚本自身目录**（`os.path.dirname(os.path.abspath(__file__))`）
- 新增研究项目 = 建目录 + `project.json`（id 与目录名一致；最小 3 字段 id/name/description）→零代码、零重启自动注册；`system.json` 体系层可选。规范详见 docs/workflows.md「手动创建项目」或工作台「手动创建指南」抽屉
- 文档即契约：改动后同步 `docs/work-log.md`（会话日志）与相关文档；数值真相源 = system.json，
  `docs/parameters.md` 仅为人工可读对照
- **LAMMPS 输入 lint**（`common/lammps_lint.py`）：发起任务前自动检查（必需板块/占位符/
  引用存在性/旧挂载路径），errors 拦截发车；手写/修改 .lmp 后先过 lint 再发车
- **失败案例库**：`workbench/backend/app/failure_rules.json`（错误签名→原因→severity/actions/can_resume），
  编辑即时生效；真实失败先沉淀为案例再写 fixture（tests/fixtures/logs/）

## 测试

```bash
uv run pytest tests/ -q
```

- 基线：78 用例全绿（体系配置/构建器等价/模板渲染/thermo/失败解析/任务状态迁移）
- **等价性验证方法**：重构构建器时保持 RNG 调用顺序，与旧产物同种子逐项对比
  （参考 tests/test_workbench.py 的 TestBuilders）
- 新增能力必须带单测（纯函数优先）

## 已知陷阱（IMPORTANT）

- LAMMPS **任务必须走暂存-运行-回收**；直接 `docker exec -w /data/<项目>` 已失效
- 渲染产物 run.lmp 手改后，重新渲染会检测并要求确认覆盖（rendered_sha 机制）
- strontium 的水参数是**历史混合体**（SPC 电荷 + SPC/E 型 LJ），如实记录于 system.json
  warning 字段；切换严格 SPC/E 需改参数并重跑
- 轨迹文件（`*.lammpstrj`）体积大，已被 `.gitignore` 排除
- `log.lammps` 是 LAMMPS 的**输出日志**，不是输入文件
- LAMMPS 可执行文件不在 Windows PATH 中，必须经容器运行
- projects/ 下**非空**目录缺 project.json 会被兜底注册（`unregistered: true`，id=目录名）；
  空目录不注册。为用户建项目时始终写全 manifest，避免界面出现「未注册」角标
- 手动 CLI 跑的任务（`uv run run-sr-sim` 等）**不进工作台任务记录**；代用户跑模拟请从工作台发起
  （或 API `POST /api/jobs`），否则界面无日志/曲线/记录可查
- 容器/环境状态与修复记录 → [docs/environment.md](docs/environment.md)

# LAMMPS 控制中心 — 架构总览 (v1.8, 2026-08-29)

> 本项目 = **分子动力学研究资产**（体系/脚本/产物）+ **控制中心工作台**（Web 操控层）。
> 设计目标：同时服务两个用户——人类（workbench UI）与 AI agent（结构化文件 + CLI + skill），
> 两者操作**同一份底层数据**，任何能力都有双入口。
> （历史改进记录见 docs/work-log.md；v1.5-v1.8 的外部评审借鉴来源见记忆文件 anl-lammps-agents-review /
>  md-dft-platform-review / vasp-deepseek-harness-review）

---

## 一、双空间设计

### 软性空间：人-agent 交互界面

| | 人 | Agent |
|---|---|---|
| 入口 | workbench UI | AGENTS.md + docs/ + 文件本身 + CLI + skills/lammps-diagnose |
| 读体系参数 | 体系配置页表格（置信度徽章/警告） | system.json（source/confidence/warning 字段） |
| 改体系参数 | 表单编辑 → 重建/渲染按钮 | 直接改 system.json → `uv run build-xx` |
| 发起任务 | 运行/扫描按钮 | CLI（uv run run-sr-sim 等，**入同一任务库**） |
| 诊断任务 | 详情页（失败解析/平衡胶囊/分析卡） | `python -m workbench.backend.app.diagnose --job <id> --json` |
| 跨界协作 | 失败卡「复制 AI 分析提示词」→ 粘贴给 agent | 拿结构化提示词即贴即开工 |

**同源原则**：UI 每个动作都有文件/CLI 等价物；数据文件是双方共享的"对话界面"；
CLI 任务与 UI 任务记同一本账（source 字段区分来源）。

### 硬性空间：前后端架构

```
┌──────────────── 浏览器 SPA (React 18 + TS + AntD 5, theme.css 设计系统) ────────────────┐
│  仪表盘(本地工具/受控退出)  项目(扫描/指南)  任务记录(对比)  详情(胶囊/续跑/AI提示词)  体系页  │
└──────────┬────────────┬──────────────┬──────────────┬──────────────┬────────────────────┘
           │ REST / WebSocket
┌──────────▼────────────▼──────────────▼──────────────▼──────────────┬────────────────────┐
│              FastAPI 后端 (uvicorn · 127.0.0.1:8000)               │  StaticFiles 托管   │
│  job_manager (暂存/队列调度/三段式取消/thermo 回放/指纹)  routers    │                    │
│  store(SQLite) failure(案例库) thermo equilibrium(平衡判据)          │                    │
│  lammps_lint(发车拦截) local_tools(探测/启动器) workspace(清理)      │                    │
└────────┬───────────────────────┬────────────────────────────────────┴────────────────────┘
         │ SQLite                │ 统一执行契约 common/runner.py (CLI 任务也入 store)
┌────────▼─────────┐   ┌────────▼─────────────────────────────────────┐
│ workbench/data/  │   │ 容器 lammpsd (/data = lammps-data-docker/)   │
│  workbench.db    │   │  jobs/<id>/ 任务工作区 (暂存→运行→产物留存)   │
│  jobs/<id>.log   │   └──────────────────────────────────────────────┘
│  local_tools.json│
└──────────────────┘
```

## 二、体系配置层（体系即数据）

体系参数单一真相源 = 每项目的 `system.json`（几何/组成/力场，力场带 source+confidence+warning）。

```
system.json ──► common/builders/{surface_adsorption, solution, clay_cif} ──► system.data + build_report.json
       └──────► templates/methods/{nvt_production, relax_production} (jinja2) ──► run.lmp
       └──────► 工作台「体系配置」页 (查看/编辑/重建/渲染/参数扫描/一致性徽章/3D 预览)
```

- 构建入口：`python -m common.build <project_dir>`（CLI: `uv run build-sr` / `build-mmt`）
- 渲染：pair_coeff/类型分组从 system.json 生成；`rendered_sha` 手改检测
- **一致性链**：system.json sha ↔ built_system_sha ↔ rendered_sha —— 体系页徽章呈现
  「参数已改未重建 / 脚本被手改」（ANL 就绪检查表的确定性落地）
- **参数扫描**：对一个方法参数取多值 → 每值渲染脚本副本（**只写任务工作区，项目文件不动**）
  → 批量发车进队列（batch id 关联，列表可勾选做 thermo 叠加对比）
- 项目注册：约定优于配置 — 含 `project.json` 的目录自动注册；缺 manifest 的非空目录兜底注册
  （unregistered 角标），工作台「手动创建指南」抽屉
- 构建器与旧脚本**种子级等价**（strontium 5137 原子 / mont 412 原子逐项一致）

## 三、任务生命周期

```
start (发车前 lint: errors 拦截) ──► queued? ──否──► running ──► completed/failed
        │                            │是(并发上限)        │           │
        │                            └─前序完成自动调度 ◄──┘           ├─► 检查点续跑
        └─ 环境指纹 (system sha/镜像 ID/LAMMPS 版本) 随任务入库            │  (read_restart 跨工作区
                                                                        │   + fix/kspace 重建)
CLI (runner.run_cli) ──► 同一 store (source=cli) ──► 详情页日志/thermo 回放可用
```

- **队列**：LAMMPS 并发上限 `MAX_CONCURRENT_LMP`（默认 1，单机容器串行）；store 计数为地面真相；
  后端重启后 queued 任务重新入队并自动调度
- **检查点续跑**：模板每阶段 `write_restart`；`POST /api/jobs/{id}/resume` 取最新 restart 生成
  自包含脚本（read_restart 用容器内绝对路径跨工作区引用 + fix/kspace_style/special_bonds 从原脚本重建）
- **CLI 任务入库**：runner.run_cli 落同一 store（source=cli，输出 tee 到 jobs/<id>.log）；
  运行中的 CLI 任务工作台不可取消（终端 Ctrl+C，后端互锁 409）

## 四、结果判读（确定性机制）

| 机制 | 位置 | 说明 |
|------|------|------|
| 发车前 lint | common/lammps_lint.py | errors 拦截：缺 units/pair_style/run、占位符、引用缺失、**toteng 关键字**（2021.07 不支持）、旧挂载路径警告 |
| 失败案例库 | workbench/backend/app/failure_rules.json | 错误签名 → 原因 → severity/actions/can_resume；编辑即时生效 |
| 平衡判据 | common/equilibrium.py | 末 20% 窗口 Density/TotEng 线性漂移 vs 阈值（RadonPy 参照）→ 详情页胶囊 已平衡/接近平衡/未收敛 |
| 轨迹统计 | common/traj_analysis.py | per-type z 分布 + MSD + 初末帧坐标；后台线程 + 工作区缓存；详情页 recharts 双图 + 3D 初末对比 |
| 环境指纹 | jobs.fingerprint | system sha/镜像 ID/LAMMPS 版本/扫描参数/续跑溯源 — 结果可比性 |
| 夹具回归 | tests/fixtures/logs | 真实任务日志 + 黄金断言 |
| AI 桥 | frontend utils/aiPrompt.ts | 失败/平衡 → 结构化提示词一键复制（零后端） |

## 五、关键设计决策

| 决策 | 理由 |
|------|------|
| 暂存-运行-回收（/data = 数据目录） | 容器不写项目根；Windows 挂小目录性能好；任务间隔离 |
| 精确取消（-in 绝对路径 + pkill 按工作区） | 并发任务互不波及；三段式验证不静默 |
| 队列用 store 记账而非进程句柄计数 | 进程注册有异步窗口，记账才是地面真相；重启后排队意图可恢复 |
| 扫描/续跑脚本文本只写工作区 | 项目目录的 run.lmp/system.json 永不被批量操作污染 |
| thermo 曲线三级传播 + 日志回放 | 权威副本(文件)/快读(tail)/实时(WS)；重启后终态任务自动重建 |
| CLI 与 workbench 同账本 (common/runner → store) | 双入口零行为差；诊断/对比对 CLI 任务同样可用 |
| 失败解析规则库外置 JSON | 策展即编辑文件；真实失败先沉淀案例再写 fixture |
| 确定性机制替代 LLM 自律 (lint/案例库/一致性链) | 外部评审 (ANL/VASP Harness) 反复验证提示词门禁不可靠 |
| SQLite + stdlib，无微服务 | 单用户本机场景，克制即正确 |
| 本地工具 = 启动器下载而非嵌入 | VMD/Vesta 是桌面 GUI；跨 OS 脚本零配置，网页内预览用 3Dmol 补位 |

## 六、模块地图

```
workbench/backend/app/   config(纯扫描注册) docker_env(挂载/指纹) job_manager(核心+队列)
                         failure(案例库) thermo(曲线) equilibrium(平衡) lammps_lint(拦截)
                         local_tools/detect(工具探测/启动器) diagnose(离线诊断 CLI)
                         store(SQLite) schemas template_render workspace(清理 sweeper)
                         routers/{jobs(analysis/restarts/resume/compare), projects(scan/render/system-data),
                                  system, local_tools}
workbench/backend/templates/methods/{nvt_production, relax_production}/   method.json + run.lmp.j2
workbench/backend/app/failure_rules.json   策展失败案例库
workbench/frontend/src/  pages/{Dashboard,Projects,Jobs,JobDetail,ProjectSystem}
                         components/{ui,ThermoChart,JobFiles,TrajectoryAnalysisCard}
                         utils/aiPrompt.ts api/client.ts theme.css
skills/lammps-diagnose/SKILL.md   可安装 agent skill (桥②)
common/                  system_config builders/{base,surface_adsorption,solution,clay_cif}
                         build runner entrypoints spce_params rdf traj_parser traj_analysis
                         equilibrium water_builder lammps_lint
```

## 七、验证基线与已知事项

- **78 个单元测试**（tests/，pytest）：体系配置/构建器等价/模板渲染/thermo/失败解析/取消迁移/
  lint/平衡判据/轨迹分析/指纹/本地工具/队列状态机
- **等价性基线**：strontium 5137 原子、mont 412 原子 — 新引擎与历史脚本同种子逐项一致
- **已知如实标注**：strontium 水参数为历史混合体（SPC 电荷 + SPC/E 型 O-LJ，system.json warning）
- **测试项目**：projects/my-first-solution 方法参数刻意调小（秒级完成），用于链路验证
- **遗留工作区**：`lammps-data-docker/jobs/` 14 天自动清理
- **部署**：非 git 仓库；docker+数据目录+后端须同机；跨机访问走拓扑 B（本机算力 + Tailscale 浏览器）
- 详细路线图：docs/roadmap.md；会话日志：docs/work-log.md

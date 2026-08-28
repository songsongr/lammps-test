# LAMMPS 控制中心 — 架构总览 (v1.4, 2026-08-28)

> 本项目 = **分子动力学研究资产**（体系/脚本/产物）+ **控制中心工作台**（Web 操控层）。
> 设计目标：同时服务两个用户——人类（workbench UI）与 AI agent（结构化文件 + CLI），
> 两者操作**同一份底层数据**，任何能力都有双入口。
> （本文档已由 2026-08-14 的分析报告重写为当前架构总览；历史改进记录见 docs/work-log.md）

---

## 一、双空间设计

### 软性空间：人-agent 交互界面

| | 人 | Agent |
|---|---|---|
| 入口 | workbench UI | AGENTS.md + docs/ + 文件本身 + CLI |
| 读体系参数 | 体系配置页表格（置信度徽章/警告） | system.json（source/confidence/warning 字段） |
| 改体系参数 | 表单编辑 → 重建/渲染按钮 | 直接改 system.json → `uv run build-xx` |
| 发起任务 | 运行按钮 | CLI（uv run run-sr-sim 等） |
| 学 | 界面注释/来源标注 | 9 板块教学注释脚本 + docs 契约 |

**同源原则**：UI 每个动作都有文件/CLI 等价物；数据文件是双方共享的"对话界面"。

### 硬性空间：前后端架构

```
┌──────────────── 浏览器 SPA (React 18 + TS + AntD 5, theme.css 设计系统) ────────────────┐
│   仪表盘        项目与脚本        任务记录        任务详情       体系配置                │
└──────────┬────────────┬──────────────┬──────────────┬──────────────┬────────────────────┘
           │ REST / WebSocket
┌──────────▼────────────▼──────────────▼──────────────▼──────────────┬────────────────────┐
│              FastAPI 后端 (uvicorn · 127.0.0.1:8000)               │  StaticFiles 托管   │
│  job_manager (暂存-运行-回收/三段式取消/thermo 回放)  routers  schemas │  前端 dist          │
│  store (SQLite)  failure (失败解析)  thermo (曲线解析)  workspace (清理) │                    │
└────────┬───────────────────────┬────────────────────────────────────┴────────────────────┘
         │ SQLite                │ 统一执行契约 common/runner.py
┌────────▼─────────┐   ┌────────▼─────────────────────────────────────┐
│ workbench/data/  │   │ 容器 lammpsd (/data = lammps-data-docker/)   │
│  workbench.db    │   │  jobs/<id>/ 任务工作区 (暂存→运行→产物留存)   │
│  jobs/<id>.log   │   └──────────────────────────────────────────────┘
└──────────────────┘
```

## 二、体系配置层（体系即数据）

体系参数单一真相源 = 每项目的 `system.json`（几何/组成/力场，力场带 source+confidence+warning）。

```
system.json ──► common/builders/{surface_adsorption, solution, clay_cif} ──► system.data + build_report.json
       └──────► workbench/backend/templates/methods/nvt_production (jinja2) ──► run.lmp
       └──────► workbench「体系配置」页 (查看/编辑/重建/渲染)
```

- 构建入口：`python -m common.build <project_dir>`（CLI: `uv run build-sr` / `build-mmt`）
- 渲染：pair_coeff/类型分组从 system.json 生成（消灭双源漂移）；`rendered_sha` 手改检测
- 项目注册：约定优于配置 — 任何含 `project.json` 的目录自动注册（内置 3 + projects/ 用户项目）；2026-08-28 起 projects/ 下缺 manifest 的非空目录兜底注册（unregistered 标记，补齐即转正），工作台提供「手动创建指南」抽屉
- 构建器与旧脚本**种子级等价**（strontium 5137 原子 / mont 412 原子逐项一致）

## 三、关键设计决策

| 决策 | 理由 |
|------|------|
| 暂存-运行-回收（/data = 数据目录） | 容器不写项目根；Windows 挂小目录性能好；任务间隔离 |
| 精确取消（-in 绝对路径 + pkill 按工作区） | 并发任务互不波及；三段式验证不静默 |
| thermo 曲线三级传播 + 日志回放 | 权威副本(文件)/快读(tail)/实时(WS)；重启后终态任务自动重建 |
| CLI 与 workbench 同源 (common/runner) | agent 与人两条路径零行为差 |
| 失败解析规则库 (failure.py) | 用户不翻原始日志 |
| SQLite + stdlib，无队列/微服务 | 单用户本机场景，克制即正确 |

## 四、模块地图

```
workbench/backend/app/   config(纯扫描注册) docker_env(挂载校验) job_manager(核心)
                         failure(失败解析) thermo(曲线) workspace(清理 sweeper)
                         store(SQLite) schemas template_render routers/{jobs,projects,system}
workbench/backend/templates/methods/nvt_production/   method.json + run.lmp.j2
workbench/frontend/src/  pages/{Dashboard,Projects,Jobs,JobDetail,ProjectSystem}
                         components/{ui,ThermoChart,JobFiles} api/client.ts theme.css
common/                  system_config builders/{base,surface_adsorption,solution,clay_cif}
                         build runner entrypoints spce_params rdf traj_parser water_builder
```

## 五、验证基线与已知事项

- **47 个单元测试**（tests/，pytest）：体系配置/构建器等价/模板渲染/thermo/失败解析/取消迁移
- **等价性基线**：strontium 5137 原子、mont 412 原子 — 新引擎与历史脚本同种子逐项一致
- **已知如实标注**：strontium 水参数为历史混合体（SPC 电荷 + SPC/E 型 O-LJ，system.json warning）
- **遗留工作区**：`lammps-data-docker/jobs/` 14 天自动清理；`projects/111` 为用户手建项目
- 详细路线图：桌面《LAMMPS控制中心-未来优化路线图.md》；会话日志：docs/work-log.md

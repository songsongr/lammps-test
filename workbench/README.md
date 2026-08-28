# LAMMPS 控制中心工作台

对项目内 LAMMPS 模拟管线的 Web 控制台：浏览项目脚本、发起模拟/分析任务、实时查看日志、管理任务历史。

**技术栈**：FastAPI (asyncio 子进程 + WebSocket + SQLite) · React 18 + TypeScript + Ant Design 5 · Vite

## 快速开始

```bash
# 前提: Docker 容器 lammpsd 已启动 (/data = lammps-data-docker/), uv 可用
cd workbench/frontend && npm install   # 仅首次
cd workbench/frontend && npm run build # 仅前端有改动时

# 项目根目录执行 (后端 + 静态托管前端):
uv run workbench
# → http://127.0.0.1:8000
```

开发模式（前端热更新）：

```bash
uv run uvicorn workbench.backend.app.main:app --reload --port 8000   # 终端 1: 后端
cd workbench/frontend && npm run dev                                  # 终端 2: Vite (5173, /api 与 /ws 反代 8000)
```

## 架构

```
workbench/
├── backend/app/
│   ├── config.py          # 路径/容器参数/已注册子项目 (加新子项目改这里)
│   ├── docker_env.py      # docker 可用性 + /data 挂载校验 (health 接口)
│   ├── job_manager.py     # 核心: 任务执行/取消/日志广播 (暂存-运行-回收)
│   ├── store.py           # SQLite 任务持久化 (stdlib sqlite3, 单表)
│   ├── schemas.py         # pydantic 模型
│   └── routers/           # system (health) / projects / jobs (+WS)
├── frontend/src/
│   ├── api/client.ts      # REST + WebSocket 客户端与类型
│   ├── App.tsx            # 侧栏布局 + 页面路由 (state 切换)
│   └── pages/             # Dashboard / Projects / Jobs / JobDetail
└── data/                  # 运行时: workbench.db + jobs/<id>.log (gitignore)
```

### 任务执行模型（暂存-运行-回收）

容器 `/data` 挂载独立数据目录（`lammps-data-docker/`），不挂项目根。LAMMPS 任务流程：

1. **暂存**：宿主机侧把所选 `.lmp` + 项目顶层 `*.data` 拷入工作区 `lammps-data-docker/jobs/<任务id>/`
2. **运行**：`docker exec -w /data/jobs/<任务id> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp 8 -in <script>.lmp`
3. **回收**：产物（轨迹/log 等）天然留在宿主机工作区，详情页展示路径

Python 类任务（`*.py`）本地运行：`uv run python <abs script>`，工作目录 = 项目目录（输出到脚本同目录，符合项目约定）。

### API 一览

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | docker/容器/挂载状态（3s 缓存） |
| POST | `/api/workbench/shutdown` | 受控退出后端进程；有运行中任务返回 409 互锁，退出前自动清理容器内孤儿 LAMMPS 进程 |
| GET | `/api/projects` | 子项目与脚本列表（实时扫描；`unregistered` = 缺 manifest 的兜底注册目录） |
| POST | `/api/jobs` | 发起任务 `{project_id, script, kind}` |
| GET | `/api/jobs` / `/api/jobs/{id}` | 任务列表 / 详情（含日志 tail + thermo 样本） |
| GET | `/api/jobs/stats` | 任务状态统计 |
| POST | `/api/jobs/{id}/cancel` | 取消（terminate + 按工作区路径精确 pkill，不波及其他任务） |
| GET | `/api/jobs/{id}/files` | 工作区产物列表（≤500 条） |
| GET | `/api/jobs/{id}/files/content` | 文本预览 / `&download=true` 下载（路径校验防逃逸） |
| DELETE | `/api/jobs/{id}` | 删除终态任务及其产物（工作区+日志+记录；运行中/进程残留返回 409） |
| WS | `/ws/jobs/{id}` | 实时日志 + thermo 帧：历史补发 → 增量流 → 15s 心跳 |

### 体系配置层与新建向导 (v1.3)

体系参数的单一真相源是各项目的 **system.json** (几何/组成/力场, 每个力场参数带来源+置信度):

- 构建引擎 `common/builders/` 从 system.json 确定性生成 system.data (任务 kind=build, 工作台"重建体系"按钮)
- 方法模板 `backend/templates/methods/` 从 system.json + 方法参数渲染 run 脚本 (pair_coeff 随体系生成, 消灭双源漂移)
- 项目详情「体系配置」页: 结构化查看/编辑 + 重建体系 + 重新渲染
- 项目页「+ 新建项目」三步向导 (体系 profile: surface_adsorption / solution; 方法模板: nvt_production), 用户项目存 `projects/` 自动注册, 可删除
- 新项目力场默认使用水模型权威值 (SPC/E); strontium 迁移数据保留历史 SPC 原始电荷并以 warning 标注 (用户决定仅标注不修正)
- thermo 曲线在服务重启后从日志文件自动回放 (终态任务首次访问时重建)

### 任务页能力 (v1.1)

- **热力学曲线**: 后端实时解析日志中的 thermo 表（`thermo.py`），WS 逐行推送，详情页 recharts 折线图（Temp/E_pair/TotEng/Press 等序列可勾选）
- **产物浏览**: 工作区文件列表 + 小文本在线预览 + 任意文件下载
- **再次运行**: 终态任务一键同参数重新提交

### 新增子项目 (v1.4.2: 向导或手动直建)

**方式一 · 三步向导**（项目页「新建项目」）：基本信息 → 体系 profile → 方法模板，自动生成
`projects/<id>/`（project.json + system.json + 渲染 run.lmp）。

**方式二 · 手动直建**：直接在 `projects/` 下建目录放文件，平台实时扫描自动发现（零重启）：

- 最小必需 `project.json`：`{"id": "与目录名一致", "name": "显示名", "description": "一句话"}`
- 顶层 `*.lmp` / `*.py` 按扩展名判型为 LAMMPS / Python 任务；`system.json` 体系层可选（纯脚本项目合法）
- 缺 manifest 的**非空目录兜底注册**（卡片带「未注册」角标，补 manifest 刷新即转正；空目录忽略）
- 界面内规范说明：项目页「手动创建指南」抽屉（与 `docs/workflows.md`「手动创建项目」节同源）
- 注意：手动 CLI（`uv run run-sr-sim` 等）与工作台同契约，但「任务记录」仅收录工作台发起的任务

## 已知限制 (v1.2)

- **无鉴权**——绑定 127.0.0.1，仅本机使用；上公网前必须加认证层
- 依赖暂存覆盖 `*.data` + 脚本 include/read_data/read_restart 引用闭包（按项目目录扁平解析，子目录相对引用需手动放入数据目录）
- WS 慢消费者会丢帧，日志文件（`workbench/data/jobs/<id>.log`）是权威副本
- 旧式绝对路径写法（`/data/<项目>/...`）的脚本与新挂载不兼容，请用相对路径（项目规范）
- 工作区保留 `WORKSPACE_RETENTION_DAYS`（默认 14 天，`config.py`），后台每小时自动清理；0 = 不清理

### 取消的可靠性 (v1.2)

取消是**三段式验证**，不静默：SIGTERM → 1s 后 `pgrep` 验证 → 残留则 SIGKILL → 仍残留把警告写入任务日志
（WS 实时可见，附手动 `kill -9` 命令）。仪表盘"容器内 LAMMPS 进程"行是 `pgrep` 实测的地面真相：
任务显示已取消但该行不为 0，即为孤儿进程；运行中任务日志停滞 2 分钟以上，详情页会提示可能不收敛。

## v1 候选方向

- 轨迹可视化（web 端 3D 渲染或 OVITO/VMD 联动）
- 参数预设表单 → 模板化生成 `.lmp`
- 分析图表页：RDF / MSD 在线出图（复用 `common/rdf.py`）
- 任务队列与并发控制、工作区清理策略
- 远程计算节点（SSH/Tailscale 备用路径接入）

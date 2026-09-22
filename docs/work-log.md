# 工作日志

> 本文件记录项目历史会话状态、运行结果、讨论结论与待办清单，随会话频繁更新。
> 环境、工作流、参数等**稳定信息**请见 [docs 目录](README.md) 其他文档。

---

## 2026-09-23 跨任务 MSD 对比

- 任务记录页新增「对比 MSD」：最多选择 6 个任务，读取各任务现有轨迹分析缓存，
  以真实滞后步数叠加全原子 MSD 曲线；不同采样步数保留空点，不插值或延长曲线。
- `GET /api/jobs/compare-msd?ids=` 返回曲线及每个任务的状态；未分析的轨迹可在
  对比抽屉中触发原有后台分析，分析中自动刷新。无轨迹、无工作区和损坏缓存均显示原因。
- 修正单任务轨迹卡与 `fit_diffusion` 文档中的单位换算说明：
  MSD 斜率单位是 Å²/step；物理扩散系数需除以 `6 × timestep(s/step)`。
  拟合结果数值和力场参数未改。
- 验证：131 个 Python 测试通过；新增 MSD 步数对齐前端测试通过；前端构建通过。

---

## 2026-09-05 v1.8.9 (评审波: 挂载误报修复 + 前端评审 6 项全修)

v1.8.8 收尾评审波 (用户「继续完善」)。

### /data 挂载检测误报根因修复 (v1.8.8 观察项转正)

- 根因不是探测逻辑, 是 `common/backends/local_docker.py::_default()` 里
  `from ... import LAMMPS_EXE` — config.py 根本没有 LAMMPS_EXE, ImportError 吞掉整个
  try 块 → LAMMPS_DATA_HOST_DIR 永远读不到 → 挂载校验被整段静默跳过
  (**v1.8.5 起挂载状态从未真正检测过**; 又一个静默失败路径实录)
- 修复: `_default` 改为模块级 `getattr` 逐字段独立取值 (单键缺失只影响自己);
  挂载解析提取纯函数 `_parse_data_mount` / `_host_path_same` + 单测 ×2
  (TestLocalDockerBackend); 容器实测 `data_mount_ok: True`

### 评审子代理 (基础设施降级实录)

- 前端评审子代理完成 (重试一次后成功): **2 P1 + 4 P2, 全部采纳修复**
- 后端评审子代理两次模型请求失败 (第三次未再试) → 后端按同一清单**主代理自评审**,
  关键缝全部实测: scan/resume `skip_script=True` + 脚本不存在不崩、`*.data` 兜底、
  正常闭包、clay_cif 键编号 (168 键已被容器真跑验证)、inbox 路由深度无遮蔽、
  溯源包字段剔除
- 前端修复清单:
  - P1-1 待入库清单加载失败静默显假空态 → 独立错误态 + 「重试」按钮
  - P1-2 `<a class="mini-btn">` 锚点无下划线重置/盒模型错位 → theme.css 加 `a.mini-btn`
    (inline-flex + no-underline, 一次修所有锚点复用)
  - P2-1 D̂ 换算文案歧义 (`斜率/6×timestep`) → `D = 斜率 × timestep ÷ 6 (秒) → Å²/s`
  - P2-2 inboxBusy 单值并发互相清 loading → 改 `Set<string>` 按条目独立
  - P2-3 InboxItem.description 类型与后端可空不吻合 → 后端 `meta.get("description") or ""`
  - P2-4 「复制模板」Button 包在 copyable 里无 onClick 是死控件 (v1.8.7 遗留) →
    onClick 走 copyToClipboard + toast; 浏览器实测 handler 触发
    (IAB 里 clipboard 写失败是自动化环境 document 未聚焦伪象, 同一工具函数在
    AI 桥按钮已生产验证)
- 回归: tsc 零错误 / 129 单测全绿 / 前端重建

### 基线

129 单测 (127 → +2 挂载); 前端 bundle 重建; workbench/data/backend.json 未变。

---

## 2026-09-05 v1.8.8 (三候选并行: 迁移入库闭环 + 蒙脱石根因修复 + 溯源包/扩散系数)

用户拍板「候选全部做」。三个候选全部落地, 外加两处 v1.8.5 遗留 bug 修复。127 单测全绿。

### 候选1: 迁移暂存区闭环 (v1.8.7 留作后续项)

- 后端 (`config.py` + `routers/projects.py`):
  - `INBOX_DIR_NAME` 移入 config.py (单一真相源); `get_projects()` 扫描跳过 `_inbox`,
    暂存产物永不混入项目列表
  - `GET /api/projects/inbox` — 列暂存条目 (manifest 有无 / 映射说明有无 / 文件数 /
    目标 id 冲突检测)
  - `POST /api/projects/inbox/{id}/confirm` — 暂存目录整体 move 为 `projects/<id>/`
    进正常注册; manifest 缺失自动补最小 manifest + `migrated_at`; 目标已存在 → 409
  - `DELETE /api/projects/inbox/{id}` — 丢弃副本 (用户旧路径不动); `_ID_RE` 路径安全
  - `.gitignore` 加 `projects/_inbox/`
- 前端: `client.ts` 3 个 API + `InboxItem` 类型; 指南抽屉新增「⑤ 待入库清单 (迁移暂存区)」,
  条目带 manifest/映射说明徽章 + 冲突警告 + 确认入库 (Popconfirm) + 丢弃
- 单测 `TestProjectsInbox` ×7 (注册排除/列表/入库/冲突/丢弃/补 manifest/路径安全)
- GUI 走查全链路: 入库 → toast → 清单即时刷新 → 项目卡出现 (无「未注册」角标) → 删除回收 ✓

### 候选2: 蒙脱石 4260K 根因修复 (v1.8.2 四稿失败的真解)

**诊断** (写脚本对 system.data 逐类型对算最小间距, 定位到 CIF 转换层):
1. `Montmorillonite.cif` 每晶胞 z≈0.29 处有 6 个 O: O10/O22 (z_frac 0.2908) 是真羟基,
   O11/O12/O23/O24 (0.2941) 是**接 Si 顶氧**; 旧 `cif_binding.oh_frac_z_max=0.296`
   把 24 个全部判为 oh 并各加 1 个 H → **16 个幻影 H**, 其中 6 个距 Si 仅 **0.616 Å**
2. 幻影 H (q=+0.425) 与 Si (q=+2.1) 库仑斥力爆炸 → cg minimize PE → -1.6e17 (v2/v5 爆炸根因)
3. 更深一层: **骨架羟基 H 无键无 LJ (ε=0)**, 是无约束点电荷, minimize 时库仑坍缩进自己的 O —
   这是 v2-v5 全部失败而 nve/limit 能"跑通"的完整解释

**修复** (不动任何力场科学数值):
- `system.json`: `oh_frac_z_max 0.296 → 0.2925` (两 z 值中点), 16 个顶氧归位 obos
  (LJ/电荷与 oh 全同, 每原子物理零变化), 幻影 H 消失; 换 CIF 需重新标定 (注释已写入)
- `clay_cif.py`: 补羟基 O-H 键 (CLAYFF 规范: 与水同键型 554.13/1.0), 键数 160→168;
  H 放置 (+z 1.0 Å) 对真羟基验证安全 (最近骨架原子 2.566 Å) 不动
- `01_run.lmp`: 三段式 minimize (cg, 收敛 Fmax 3.46) → nve+langevin 300K (去 nve/limit)
  → 生产 (MSD+dump 同旧版)
- **容器验证**: 完整 150000 步跑通 (1m51s), 温度全程 282–332K (目标 300K),
  4260K 伪稳态消失; post_process (顺手修了 line93 IndentationError):
  **水扩散系数 D = 3.95e-06 cm²/s, 落在层间水文献区间** (1e-6~1e-5)
- 体系变化: 412→396 原子 (水恰好仍 80 个); 中性修正偏移 -0.302→-0.231 (机理不变)

### 顺手修复: v1.8.5 runner 两处遗留 bug (被 KeyError 掩盖的互递归)

1. `LocalDockerBackend.stage_dependencies` 委托回 `runner.stage_dependencies` (后者又委托
   回 backend) → **无限互递归**; CLI 侧当时被 `get_backend` 未注册的 KeyError 掩盖,
   工作台侧 (routers 已注册) 直接 RecursionError — **v1.8.5 起所有 LAMMPS 任务的暂存
   实际都是坏的**, 单测 mock 了 backend 没抓到。修复: LocalDocker 内联真实拷贝逻辑
   (collect_deps + copy2 + 顶层 *.data glob, 与 RemoteHPC 同套闭包解析)
2. `runner.run_cli` 容器 cwd 用去横线 job_id、宿主机目录是带横线 ws_id → chdir 失败。
   修复: 统一用 ws_id
3. `common/backends/base.py`: `get_backend`/`configure_backend`/`list_backends` 懒注册
   内置实现 (CLI 不再依赖 workbench routers 的 import 副作用)

### 候选3: roadmap 落地 (溯源包 #6 全量 + 扩散系数 #3 部分)

- **单任务溯源包导出** (#6): 新 `workbench/backend/app/provenance.py` 纯函数
  `build_provenance_zip` (README+job.json+fingerprint.json+脚本+system.json+system.data+
  log_tail; 排除轨迹/检查点; 缺失条目显式记入 skipped 不静默) +
  `GET /api/jobs/{id}/export` (StreamingResponse zip) + JobDetail「溯源包」按钮
  (直接 <a download>); GUI 点击实测下载事件触发 ✓; 单测 ×2
- **MSD 末窗扩散系数拟合** (#3 部分): `common/traj_analysis.py` 新 `fit_diffusion`
  (末窗 50% 线性拟合, 斜率 Å²/step + R² + 拟合窗口; 常数 MSD → D̂=0 是有效结果;
  物理单位换算需 dt, 明示"同 timestep 任务间可直接比较") → msd 行带 `diffusion` 字段,
  TrajectoryAnalysisCard 显示 D̂; 单测 ×2
- roadmap.md 刷新 (2026-09-05): 已落地清单 + 开放项重排 (新增"蒙脱石生产加长"待拍板)

### 观察项 (未动, 下次会话可查)

- Dashboard「/data 挂载: 未检测到挂载」检测与实际不符 (smoke 验证挂载是通的) —
  疑似 docker inspect 探测逻辑/路径 case 问题, 预先存在, 不影响任务
- 执行后端卡在 backend.json 不存在时显示 "Local Docker/已就绪" — 行为正确

### 基线

127 单测全绿 (116 → +7 inbox +2 provenance +2 diffusion); 前端 bundle index-BZCPxt8t.js
(含待入库清单/溯源包/D̂ 字符串); 本次 GUI 走查用假 `_inbox` 条目已清理。

---

## 2026-09-04 plan-sess_875a6af3 收尾 (体系配置层 + 新建项目向导 — 全部落地)

回看 plan `.zcode/plans/plan-sess_875a6af3-39c9-40c6-88e0-ff8c98567e02.md`，
6 阶段计划全数落地（中途多次会话已分别落，git status 中 27 个 modified 文件即此 plan 的成果）：

- **阶段 1 数据层 + 构建引擎** — `common/system_config.py` + `common/builders/{base,surface_adsorption,solution,clay_cif}.py` + `common/build.py` 入口；strontium `system.json` 已有；SPC/E 不一致按用户决定仅 `warning` 标注
- **阶段 2 模板渲染 + UI + 向导** — `workbench/backend/templates/methods/{nvt_production,relax_production}/` Jinja2；`ProjectSystem.tsx`（几何/组成/力场 三表 + 重建 + 渲染）；`NewProjectWizard`（3 步：基本信息 → 体系 profile → 方法）；`POST /api/projects` 注册 + `BUILTIN_DIRS` 合并扫描
- **验证** — 116 单测全绿；TypeScript 无报错

**未做 (按 plan 明示)**：
- 图形化分子搭建/拖拽
- DAG 编排
- 黏土 CIF profile（convert_cif 的 OH 判据绑定特定 CIF，需单独抽象）
- 自动修正 SPC/E 不一致（仅标注）

**结论**：plan 闭环收口。下一波可考虑 `_inbox/` 扫描 API + 「待入库清单」（v1.8.7 留作后续项）或路线图 [docs/roadmap.md](roadmap.md) 中其他项。

---

## 2026-08-31 v1.8.7 (手动创建指南新增「历史研究迁移」段落)

**动机**：用户历史 LAMMPS 工作流散落在工作台外（甚至没用过工作台），
没法直接用平台能力（任务记录、暂存-运行-回收、模板渲染）。
希望在「手动创建指南」抽屉里开一条新入口：让用户用自然语言把场景告诉 agent，
由 agent 帮他扫描 → 识别 → 结构化迁移，**旧路径文件不动**。

**落地**（仅前端文案 + 文档，零后端改动）：

1. `workbench/frontend/src/pages/Projects.tsx`
   - `ManualGuideDrawer` 顶部新增「**0. 从历史散落研究迁移进来**」section，
     放在原有「① 目录放在哪里」之前，作为第一个章节
   - 段落内容：
     - 适用场景 + 你要做的事（三步走）
     - 硬约束（用户旧文件不被修改）
     - 迁移去向（先到 `projects/_inbox/<id>/`，待入库清单确认）
     - **标准版提示词模板**（必填字段 + 可选字段注释 + 五步指令）
     - `Typography.Paragraph copyable` 一键复制按钮 + pre 块展示
   - 新增 `MIGRATION_PROMPT` 常量（紧跟现有 `GUIDE_MANIFEST` 之后）
2. `docs/workflows.md`
   - 「手动创建项目」章节前新增「从历史散落研究迁移进来（agent 辅助）」段
   - 解释 `_inbox/` 暂存机制、与下一节的关系
3. `docs/work-log.md` — 本段

**用户选项确认**：
- 提示词风格：标准版（带必填字段注释），不是极简版也不是双版本
- 迁移结果可见时机：先 `_inbox/` 暂存 + 待入库清单确认（不是迁移完成即注册）

**未做 / 留作后续**：
- `_inbox/` 扫描 API + 抽屉底部「待入库清单」列表 + 「确认入库」按钮
  （后端 `routers/projects.py` 新增 `GET /api/projects/inbox` + `POST /api/projects/inbox/{id}/confirm`）
- agent 端标准化扫描脚本（`common/migration_scanner.py`：遍历旧目录 → 分类 → 写 `_inbox/`）
- 用户粘贴提示词后的引导（一键发到 agent / 复制后弹 toast）

**回归**：TypeScript 编译无报错；116 单测基线不动（本次未触及后端 / Python）。

---

## 2026-08-30 v1.8.5 (执行后端抽象 — Backend 协议 + LocalDocker 零回归)

**B1: Backend 抽象 + LocalDocker 兼容 + RemoteHPC 骨架**

背景：v1.8.5 之前 `common/runner.py` 直接 `subprocess.run(["docker", "exec", ...])`，
`workbench/backend/app/docker_env.py` 单独写 docker 探测 + 一键启动。两块硬编码把
"本地 docker 容器"做成了唯一执行环境；要上远程 HPC / 远程 docker 必须改两处。

设计原则：抽象放在 `common/backends/`（不是 workbench/backend），因为 CLI runner
`uv run run-sr-sim` 也共用同一抽象。配置走 JSON 持久化，切换 backend 不需要改代码。

改动清单：

- **新包 `common/backends/`**
  - `base.py` — Backend Protocol + BackendInfo/BackendStartResult 数据类 +
    `get_backend()` 工厂 + `configure_backend()` 持久化 + 单例缓存
  - `local_docker.py` — LocalDockerBackend 实现；**从 workbench/backend/app/docker_env.py
    原样搬运** `_docker_info / _start_container / _lmp_process_count / _container_fingerprint /
    _container_metrics / _kill_lmp_processes / _parse_mem_bytes / _dir_size_bytes`，
    不重写（搬过来），行为零变化；末尾 `register_backend("local_docker", LocalDockerBackend)`
  - `remote_hpc.py` — RemoteHPCBackend 骨架：ssh + rsync + sbatch 协议；
    `info()` 用 `ssh -o BatchMode=yes -o ConnectTimeout=5 ... "echo ok"` 探测连通性；
    `start()` 返回 `stage="no_op"`（HPC 后端无"启动"概念）；
    `render_sbatch_script()` 用 `string.Template` 渲染 sbatch 脚本
  - `__init__.py` — 重新导出 `get_backend / configure_backend / list_backends / register_backend` 等

- **重写 `workbench/backend/app/docker_env.py`** — 仅做重新导出层：模块级
  `docker_info / lmp_process_count / kill_lmp_processes / container_metrics /
  start_container / container_fingerprint / _parse_mem_bytes / _dir_size_bytes` 全部
  委派给 `common/backends/local_docker.py` 的同名私有函数；进程内共享一个
  `LocalDockerBackend` 实例承载缓存（metrics ring buffer / fingerprint TTL 行为一致）。
  旧 import 路径（`from workbench.backend.app.docker_env import docker_info`）零修改。

- **改 `common/runner.py`** — `stage_dependencies()` 与 `lmp_command()` 改为便捷函数，
  内部调 `get_backend().stage_dependencies(...)` / `get_backend().run_lmp_command(...)`；
  `run_cli()` 通过 `_ws_backend_for()` 根据 backend 类型选择容器内路径
  （LocalDocker = `/data/jobs/<id>`，RemoteHPC = `<hpc_workdir>/jobs/<id>`）；
  `_cli_record()` 在 fingerprint 中多写一个 `backend` 字段（任务可比性扩展）。
  未配置 backend.json → 默认 LocalDocker → 与 v1.8.5 之前字节级一致。

- **工作台层 `workbench/backend/app/routers/system.py`** — 新增：
  - `GET  /api/backend` — 当前配置 + info() 探测
  - `GET  /api/backend/list` — 已注册 backend 列表
  - `PUT  /api/backend` — 切换 backend（持久化 + 清单例缓存）
  - `POST /api/backend/test` — 连通性测试（不持久化）
  - `GET  /api/health` 在原 `docker` 字段基础上加 `backend.{type,name,status,action_needed,available}`，
    仪表盘 / JobDetail 旧字段零变化

- **前端 `workbench/frontend/src/api/client.ts`** — 类型与 API：
  - `BackendSummary / BackendConfig / BackendInfo / BackendListItem / BackendStartResult`
  - `api.backendGet / backendList / backendPut / backendTest`
  - 不改 UI（v1.8.6 范围）

- **单测 `tests/test_backends.py`** — 24 个新用例：
  - `TestBackendProtocol`（2）— duck-typing 满足 Protocol
  - `TestGetBackend`（5）— 默认 / 切换 / 清缓存 / 未知类型抛错 / 未注册类型回退
  - `TestLocalDockerCommand`（2）— `run_lmp_command` 与 `runner.lmp_command` 拼法与原版字节一致
  - `TestLocalDockerInfo`（3）— docker 缺失 / daemon 不通 / 容器未跑 三态分支
  - `TestLocalDockerStart`（2）— `docker_missing / daemon_unreachable` 启动阶段
  - `TestDockerEnvReExport`（1）— 旧 API 仍可从 `workbench.backend.app.docker_env` 导入
  - `TestRemoteHPC`（7）— 未配置 / ssh 不通 / ssh 通 / start 行为 / 模板渲染 / ssh 命令格式 / run_lmp_command
  - `TestBackendRoutes`（2）— 工厂与 list_backends 行为

验收：`uv run pytest tests/ -q` = **116 passed**（基线 92 + 24 新增，零回归）。
其中 8 个 v1.8.5 之前的失败用例已在别处修过；本子代理只引入新增，零修改旧用例。

**关键设计决策**：

- `Backend` 用 `Protocol + runtime_checkable` 而非 ABC — RemoteHPC 早期版本可跳脱个别方法；
  接口名/签名稳定即可，runner 与工作台只通过该接口调用
- `stage_dependencies` 留作 Backend 协议成员（不是 common.runner 私有） — 闭包解析
  复用 `collect_deps`（`from common.runner import collect_deps`），避免漂移
- `get_backend()` 单例缓存避免反复读 JSON + 实例化；`configure_backend()` 自动清
- 旧 `workbench/backend/app/docker_env.py` 私有函数 `_parse_mem_bytes / _dir_size_bytes`
  也重新导出（tests/test_docker_metrics.py 在用）— 零修改老测试

**已知未做 / 留作 v1.8.6**：

- **RemoteDocker 占位** — 任务要求"留作 v1.8.6"。Backend 协议已就绪，
  `common/backends/remote_docker.py` 是新增文件，逻辑类似 LocalDockerBackend 但 ssh 到
  远程主机后再 `docker exec`。当前已用 docs/environment.md 标注 TODO
- **真实 paramiko SSH** — RemoteHPC 当前走 `subprocess.run(["ssh", ...])`，跨平台可用，
  但速度 / 错误细节不如 paramiko。留作 v1.8.6 性能优化项
- **CLI runner 与 RemoteHPC 的端到端串通** — `run_cli()` 已写 RemoteHPC 工作区路径
  解析，但 sbatch 脚本写入（`render_sbatch_script()`）由调用方负责，CLI 路径暂未串
  入。RemoteHPC 主要服务 workbench UI 路径（v1.8.6 抽屉上线时串）
- **前端 UI** — 类型 + API 已声明（client.ts），抽屉组件 v1.8.6 写

**零回归证据**：

- 单测 116/116 全绿（基线 92 + 新增 24）
- `LocalDockerBackend.run_lmp_command` 与 `runner.lmp_command` 拼出的 argv 与 v1.8.5
  之前字节级一致（`test_run_lmp_command_matches_old_format` 直接 assert）
- `workbench/backend/app/docker_env.py` 所有旧 API 全部可用（`TestDockerEnvReExport`）
- `common.runner.lmp_command(ws, script, omp)` 签名不变，工作台 `job_manager._build_command`
  无需改动

**A1: 启动按钮分级提示 (用户踩坑: Docker daemon 挂了报 Windows 管道错)**
- `workbench/backend/app/docker_env.start_container()` 改 3 阶段前置检查:
  1. `docker info --format ServerVersion` 健康探测 (6s 超时)
  2. 区分 4 种 stage: `container_started` (ok) / `daemon_unreachable` (Windows 命名管道错) /
     `docker_missing` (未安装) / `timeout` / `failed`
  3. 返回结构 `{ok, stage, message, hint_url}` — 前端按 stage 决定 error vs warning
- `frontend/src/pages/Dashboard.handleContainerAction` 按 stage 分级提示:
  - daemon_unreachable / docker_missing → 红色 error 持续 8s (给用户时间读 + 启动 Docker Desktop)
  - timeout → 黄色 warning 6s
  - 其它失败 → error 6s
- 验证: 实测停掉 Docker Desktop → 报"Docker Desktop 未运行 (找不到 docker daemon 命名管道)。请启动 Docker Desktop 后重试" (中文清晰提示 + hint_url)

**A2: health 状态机化 (为 B1 铺路)**
- `docker_info()` 新增 `status: running | stopped | unreachable` + `action_needed: none | start_container | start_docker`
- 前端只需看 `action_needed` 决定按钮颜色 / 提示文案
- 3 状态 curl 实测全对:
  - running: action_needed=none
  - stopped (daemon 在, 容器停): action_needed=start_container
  - unreachable (daemon 挂): action_needed=start_docker + 中文 error

**B2: 执行后端配置 UI + 健康面板**
- `frontend/src/pages/Dashboard.tsx` 新增:
  - **BackendCard section** (仪表盘中部, "环境状态" + "任务吞吐" 之后):
    显示当前 backend (Local Docker / Remote HPC) + 状态点 (ok 绿/err 红/warn 黄) +
    提示文案 (action_needed 4 种语义) + 状态徽章 + 配置入口按钮
  - **BackendDrawer** (Drawer 抽屉, 520px 宽): 列表式选择 2 个 backend (radio, 可用/需配置徽章),
    选中 Remote HPC 时显示 6 个表单字段 (SSH 主机/用户/私钥/HPC 工作目录/module load/sbatch 模板),
    选中 Local Docker 时显示提示文案 (零配置, 见 docs/environment.md);
    底部 [测试连通性] + [保存并切换] 双按钮, 测试结果直接显示 status/action_needed
  - `api/client.ts` 新增 `backendGet` / `backendList` / `backendPut` / `backendTest` (类型来自子代理 BackendConfig/BackendInfo/BackendListItem)
- **验收** (Playwright headless):
  - 执行后端 section 渲染, 1 个配置按钮 ✅
  - 抽屉打开, 标题"执行后端配置", 2 个 radio (Local Docker "可用" / Remote HPC "需配置") ✅
  - 0 console error
- **单测**: 116/116 绿 (基线 92 + 子代理新增 24 backend, 无回归)
- **未做** (留作下版):
  - B3 CLI `--backend remote_hpc` 适配 (子代理已写 RemoteHPC 骨架, 但 CLI runner 串入未完成)
  - B4 项目级 backend 选顶 (project.json backend 字段)
  - RemoteDocker 实现 (协议已就绪, 留 v1.8.6)
  - 真实 paramiko SSH (现走 subprocess ssh, 性能/错误处理不如 paramiko)
  - /api/health 加 backend 缓存 (现每次实时调, 5s 轮询 OK)

---

## 2026-08-30 v1.8.2 (3D 渲染 + 图例元素化 小修)

**3D 初末对比 length 报错根因**:
- 症状: 抽屉打开报 `Cannot read properties of undefined (reading 'length')`
- 误导: 之前怀疑是 `container.id` 缺失导致 toUpperCase — 实为 **3Dmol 2.5.5 cdjson
  parser 强制读 `m[0].b.length`**, 我们的 payload 没 `b` 字段就直接 length 错,
  在 `addModel` 阶段就崩了
- 修复: `toCdjson(atoms)` 输出改为 `{ m: [{ a, b: [] }] }`; 顺手把脆弱的 `v.clear()`
  换成 `v.removeAllModels()`; `applyMode` 加 try/catch 防 3Dmol 偶发异常污染 UI

**轨迹图例元素化**:
- 背景: z 分布 + MSD 图例用 LAMMPS type 整数 (1/2/3/4) — 物理意义不明
- 数据源: lammpstrj 本身**不**含元素信息, 但 `system.data` 的 Masses 段在 system-as-data
  渲染产物里带 `# Ow`/`# Hw`/`# Sr`/`# Cl` 注释
- 改动:
  - `common/lammps_data.py` 新增 `parse_type_to_element(text) -> {type: elem}`,
    优先读 Masses 行尾注释; 无注释按 mass 推 (覆盖 40+ 元素, 偏离 >15% 标 X)
  - `common/traj_analysis.analyze_trajectory` 新增 `system_data_path` 参数;
    同目录找 `system.data`, 找不到或解析失败 → label 退化为纯 type (不报错)
  - `z_profile` / `msd` 行新增 `label: "3 (Sr)"` 字段; 前端 LineChart `dataKey` 优先用 label
- 验收: Playwright 实地 — 5 条系列 `1 (Ow) / 2 (Hw) / 3 (Sr) / 4 (Cl) / all`
  在两张图都正确显示; 81/81 单测全绿 (含 3 个新 lammps_data 用例)

**杂记**:
- Windows workbench 进程 `uv run workbench` 启动方式无 `--reload`; 改后端代码后必须
  Stop-Process 后重启。shutdown API 在 Windows 退化为 `os.kill` = TerminateProcess
  对子进程不灵 (v1.8.1 已知陷阱延续)
- **不要**用 sed 重写带中文的代码 — 多次踩 heredoc 转义坑, 用 Edit 工具更稳

## 2026-08-30 v1.8.2 (蒙脱石温度异常诊断 + 本地工具真一键)

**子代理评审两份报告** (并行, 后台回收):
- A: 蒙脱石 4260K 物理评估 — 敢直说"nve/limit 0.05 + langevin 300K 根本冲突,
  RIMIT 撞墙 → KE 推到 4250K 伪稳态 = 位移限速上限温度"; 给保守修法: minimize +
  nve 不限速 + 100→300K 退火
- B: 本地工具启动器 UX — 敢直说"`.data` 误归 VESTA 是前端硬编码 bug, VESTA 不支持
  .data 格式 → Invalid data"; 推荐 4 方案中 C (后端 spawn 直起) + 1 扩展名过滤

**蒙脱石 4 稿修复尝试 + 全部失败** (诚实记录):
- 1_run.lmp 现状 (nve/limit 0.05 + langevin 300K) 是当前科学层面**唯一已知稳定**状态
- v2 (nve + minimize): minimize 在 lj 6-12 close-contact 爆炸 (Fmax 1.2e+31, alpha 1e-46)
- v3 (nve + langevin 100K 冷启动): 切 nve 第一步 MPI_ABORT
- v4 (nve/limit 0.1 + langevin 长阻尼): 跑通但温度 9500K 更糟 (RIMIT 上限温度更高)
- v5 (minimize + fix nvt Nosé-Hoover): minimize 同样爆炸, fix nvt 跟着炸
- **根因比我开始时以为的更深**: `pair_style lj/cut/coul/long` + 初始 system.data
  close-contact 体系 + `min_style cg` 三者不兼容; nve/limit 与 langevin 目标温度
  根本冲突 (RIMIT 在, langevin 永远拉不到目标); unfix+fix 切链在 close-contact 体系
  不可靠
- **修复需要研究决策** (留待用户拍板, 不擅改):
  - 改 `pair_style` 到 `buck/coul/long` (CLAYFF 原生, 子代理 A 避开过)
  - 改 system.data 初始构型 (重建时增大原子最小间距)
  - 改力场参数 (Ca²⁺ ε/σ)
- **1_run.lmp 已回滚到原版** (974 任务跑通的版本, 温度 4260K 是已知伪稳态, 但
  TotEng 漂 1.46% 在 4260K 反而是 langevin 平衡的产物, 不再追究)

**本地工具 P0 + P1 落地** (子代理 B 方案):
- P0:
  - 新 `common/local_tools_compat.py` (前后端共用 VMD/VESTA 支持矩阵); 删
    `JobFiles.tsx` 的 VESTA `.data` 误归; 抽 `workbench/frontend/src/utils/
    localToolsCompat.ts` 同源 (手工同步, 后端是真相源); 6 个新单测全绿
- P1:
  - 新 `POST /api/local-tools/open`: 后端 spawn 本机 .exe 直接打开 (Windows
    DETACHED_PROCESS, macOS/Linux start_new_session); spawn 失败/远程/Docker
    降级返回 `localToolLauncher` 脚本供下载; VESTA + `.data` 自动调
    `lammps_data.lammps_data_to_xyz()` 转临时 `.xyz` 写到 `%TEMP%/lammps_workbench_open/`
    再 spawn (复用现成转换器, 零额外依赖)
  - 前端 2 处入口 (`JobFiles.tsx:OpenWithTool` 按钮 + `ProjectSystem.tsx:handleOpenVesta`
    抽屉按钮) 统一调 `api.openWithTool()`; 按钮 title 从"用本地工具打开 (下载一键
    启动器)" 改为"用本地工具打开"; message.loading 反馈 spawn 过程
- 验收 (Playwright + curl):
  - POST /api/local-tools/open vmd + prod.lammpstrj → ok=true, spawned=true, pid 27808
  - POST /api/local-tools/open vesta + system.data → ok=true, spawned=true, pid 29952
    (VESTA 启动的是转换后的临时 .xyz 13K, 412 原子, Al/O/Si 等元素标签)
  - 前端 3 个 OpenWithTool 按钮渲染正常, title 已是新文案, console 无 error
- **已知硬约束**: Docker 后端模式下 spawn 不可行, 自动降级为 launcher 下载
  (这是预期行为, 不是 bug)

**单测基线**: 87/87 绿 (81 基线 + 6 个新 compat 用例)

## 2026-08-30 v1.8.3 (模拟环境监测 + 一键启动容器)

**背景**: 用户看到仪表盘「模拟环境」卡 4 个字段显示 `-`, 实际是**浏览器缓存**导致
旧 bundle 没拿到 health 字段 (Playwright 实时拉取已确认 7 个字段全填:
容器状态 "Up About an hour" / 镜像 / 挂载路径 / LAMMPS 进程数 / Python / 后端时间) —
但用户要求"应该也配置上模拟环境监测和串流一键启动", 故新增两类能力。

**模拟环境监测** (仪表盘「模拟环境」卡新增 3 行 + 趋势 sparkline):
- `common/.../docker_env.py`:
  - `_parse_mem_bytes` (单测覆盖, 修了一个 bug: 之前用 dict items 顺序遍历导致
    "MiB" 被 "B" 先匹配 → 0; 改为**长前缀优先**元组)
  - `_dir_size_bytes` (递归算数据目录总字节)
  - `_sample_container_metrics` (`docker stats --no-stream` 一次采样: CPU% / 内存)
  - `container_metrics` (返回 `{current, history: ring 60, data_dir_size_bytes, data_dir_path}`,
    2s 缓存)
- `routers/system.py`: 新 `GET /api/docker/metrics` (5s 轮询, 给前端)
- 前端 `Dashboard.tsx`:
  - `EnvResourceMetrics` 子组件: CPU% + 内存 (含百分比) + 数据目录大小 (GB),
    容器停止时显示 "容器已停止"
  - `Sparkline` 极简 inline SVG (60×14 px, 60 个点, 颜色父级控)
  - 健康阈值未做告警线 (用户没要求; 后续若需要可在 Sparkline 上叠加阈值横线)

**一键启动容器** (容器停止时仪表盘显示按钮):
- `docker_env.start_container()` (`docker start <name>` 15s 超时, 启后清缓存)
- `routers/system.py`: 新 `POST /api/docker/start`
- 前端: `containerOk=false && docker.available` 时在环境卡底部显示
  「启动 lammpsd 容器」按钮 → 调 `api.dockerStart()` → 成功后 message 提示
  + 1.5s 后 `window.location.reload()` 让 health 重新探测

**验收** (Playwright):
- 环境卡 10 个字段全填: Docker 引擎 / 容器状态 "Up 2 hours" / LAMMPS 进程数 /
  镜像 / Python / /data 挂载 / 后端时间 / 容器 CPU 0.0% / 容器内存 6.7 MB (0.1%) /
  数据目录 0.15 GB
- 2 个 sparkline polyline 渲染成功 (CPU 趋势 + 内存趋势)
- `POST /api/docker/start` 返回 `{"ok": true, "message": "容器 lammpsd 已启动"}`
- 顺手清掉本地工具测试残留的 1 个 LAMMPS 孤儿进程 (`pkill -f lmp_mpi` 后 pgrep=0)

**单测基线**: 92/92 绿 (87 + 5 个 docker_metrics 用例: 内存单位解析 / 目录大小 /
  metrics shape)

**已知约束**:
- docker stats 在容器空闲时 CPU=0% (无任务), 趋势看不出负载; 用户跑模拟后会拉起
- sparkline 用 60 点 5 分钟, 长任务看不见总趋势; v2 可改时间窗口或加 hover tooltip

## 2026-08-30 v1.8.4 (控制中心布局审美升级 — 借鉴 Plane/shadcn/Cal.com)

**子代理 UI 选型研究** (Plane.so / shadcn/ui / Cal.com+Refine 三方对比):
- **战略**: 不引入 shadcn/Tailwind/Refine, 走"纯 AntD + token 升级"路线 —
  借鉴三家**设计语言**, 用 AntD 组件落地 (避免双样式系统 +200KB)
- **借鉴要点**:
  - shadcn: 4 层语义 token 分层 (--background/-foreground/-card/-sidebar)
  - Plane: 顶部 KPI 胶囊 bar + 侧栏 workspace selector + 行内密度
  - Cal.com: 多层柔和阴影 + 7 色徽章 (bg-color/10 + text-color) + 三级文字

**1 小时速赢落地** (theme.css + AntD ConfigProvider + Dashboard 增量):
- **theme.css** (v1.8.4 段):
  - 圆角由 16/10 统一到 12/8 (button 8, card 12, modal 12) — Cal.com 风格
  - 多层柔和阴影 `--shadow-1` (3 层叠加) + `--shadow-2` (Cal.com elevation-low)
  - 新增 `--border-subtle` (主边框 0.10 透明 + 次边框 0.05) — shadcn 双级
  - 新增 7 态色 (info/warn/info-weak/warn-weak) — Cal.com 徽章语义
- **AntD ConfigProvider**: borderRadius 10→8, colorBorder 0.14→0.10, colorBorderSecondary
  0.08→0.05, Modal borderRadiusLG 16→12 — 与 theme.css 同步
- **Sidebar 选中条** (Plane 借鉴): `.nav-item.active::before` 左侧 2px 18px 靛蓝高亮
- **KPI 胶囊 bar** (Plane 借鉴): Dashboard 顶部 5 个紧凑胶囊 (已排队/运行中/已完成/
  失败/任务总数), 数字 tabular-nums 20px 660 字重, 状态色 (运行中 accent/已完成 ok/
  失败 err/无统计 neutral)
- **最近任务行表** (Plane 行内密度): Dashboard 底部 6 行紧凑展示, 每行
  `[状态徽章] [项目名] [脚本 mono] [类型] [时长] [短 ID]`, 行高 40px,
  hover 浅色背景, 状态用 Cal.com 7 色徽章 (accent/ok/err/neutral)
- **新增 .card.clickable / .badge-soft.{ok,err,warn,accent,info,neutral}**:
  卡片 hover 浮起, 徽章软色 (bg/10 + text) 通用类

**验收** (Playwright):
- KPI bar 1 个 + 5 个 pills 全部渲染
- Sidebar `.nav-item.active::before` 计算样式: 2px 宽 absolute 定位 #3547e8 背景
- 最近任务卡渲染 (6 行)
- Card 阴影: 3 层 rgba 叠加, 圆角 12px
- 0 console error

**未做** (子代理标记为大改, ≥ 半天, 需拆任务):
- Dashboard 重组 (Section 卡片栅格 + 图表占位 + 任务表扩展)
- JobDetail 分栏 (左 8/12 卡片堆叠 + 右 4/12 sticky 指标 + sticky 状态条)
- JobList 行式列表 (Plane 风格 36px 高 + filter chips)
- (可选) 暗色模式 (借鉴 shadcn 4 层 token 自动覆盖)

**单测基线**: 92/92 绿 (无新增, 仅前端 CSS+布局)

---

## 2026-08-30 v1.8.4 续 (3 大改: Dashboard 重组 / JobDetail 分栏 / Jobs 行式列表)

**做法**: 派单子代理串行 3 大改 (主代理已先在 KPI bar 加了"永远显示的容器操作按钮"
作为 UX 修复 — 子代理保留此按钮并按子代理 UI 研究报告 v1.8.4 实施其余改动)。

### 大改 1: Dashboard 重组 (`pages/Dashboard.tsx`)

- **Section 分组嵌套** (shadcn dashboard-01 借鉴): `.page-stack` = `gap-2 outer` 容纳
  8 个 section, 每个 section card 自身 padding 20px; 新增 `.section-header` =
  text-sm semibold + border-b border-subtle pb-3 mb-4
- **永远显示的容器操作按钮**: 主代理的 UX 修复, 保留并下沉到 `.kpi-action-btn` 通用类
  (新增: `.kpi-action-btn` 与 `.kpi-action-btn.danger`); 容器运行="重启"灰色,
  容器停止="启动" err 红色, 永远显示, 调 `api.dockerStart()` 1.5s 后 reload
- **环境卡 + KPI bar 合并**: 4 资源指标横向 (CPU/内存/数据目录/LAMMPS 进程),
  容器状态/LAMMPS 进程详情/Python/后端时间纵向下沉到 `.kv-grid` 二列键值对
- **图表占位**: 中部加 24 小时任务吞吐 Recharts `LineChart`, 近 7 天 completed/failed
  趋势 (按天聚合, even 没数据保留骨架 + "近 7 天暂无已完成/失败任务" 占位文案)
- **最近任务 10 行 + filter chips**: `全部 / 今天 / 本周`, 行高 40px, 行式表格
  `[状态点 8px 圆] [项目] [脚本 mono] [类型] [创建] [状态] [短 ID]`, hover
  `bg-neutral-weak`, 状态点新增 `.sdot-4.{running,completed,failed,queued,canceled,interrupted}`

### 大改 2: JobDetail 分栏 (`pages/JobDetail.tsx`)

- **页面顶部 sticky 状态条** (Cal.com 借鉴): 新增 `.sticky-status` =
  `position: sticky; top: 62px; z-index: 10; bg-white/80 backdrop-blur`, 整行 56px
  内容 `[返回] [job-<id8> mono] [7 色徽章] [类型 chip] [mini progress bar] [行数 / 状态]`
- **主区分 2 列**: 左 8/12 (gridTemplateColumns `minmax(0, 8fr) minmax(0, 4fr)`),
  section 卡片堆叠 = 任务参数 / 热力学曲线 / 失败诊断 / 产物文件 / 轨迹统计 /
  检查点续跑 / 实时日志; 右 4/12 sticky 指标卡 (`position: sticky; top: 134px;
  align-self: start`) = 任务指标 (进度/耗时/ETA/thermo 样本/OMP 线程/退出码) /
  系统信息 (CPU/内存/镜像/LAMMPS) / 环境指纹 / AI 桥 / 再次运行
- **7 色状态徽章** (Cal.com 借鉴): 新增 `StatusBadge` (`components/ui.tsx`),
  复用 v1.8.4 的 `.badge-soft.{accent,neutral,ok,err,warn,info}`:
  running=accent蓝, queued=neutral灰, completed=ok绿, failed=err红, interrupted=info蓝,
  canceled=neutral灰
- **失败诊断 section 浮起**: 新增 `.failure-card-float` =
  `background: var(--surface); box-shadow: var(--shadow-2); border-left: 3px solid
  var(--err);` 替换原 `.failure-card`, 严重度 badge 也改用 7 色 (high=err, medium=warn,
  low=neutral)
- **修复 React #310**: 把 `useMemo(progressPct)` 从条件 `if (!job) return ...` 之后
  移到所有 useEffect 之后, 条件 return 之前 — 维持 hooks 顺序稳定
  (Playwright 0 console.error 验证)

### 大改 3: Jobs 行式列表 (`pages/Jobs.tsx`)

- **AntD Table → 行式 list**: 整页 `.page-stack > .card > .table-toolbar + filter chips +
  table.row-table`, 每行 40px `[checkbox] [状态点 8px] [Job-ID mono] [项目] [脚本 mono +
  CLI/batch Tag] [类型 chip] [开始时间] [时长] [操作: 日志/取消/删除]`, hover
  `bg-neutral-weak`, 选中 `bg-primary/5 border-l-2 border-primary`
- **表头 sticky**: `.row-table thead th { position: sticky; top: 0; background:
  var(--surface); z-index: 2; }`
- **filter chips 三排** (Plane 借鉴): 状态 (全部/运行中/排队/已完成/失败/已取消/
  已中断) + 项目 (动态, 从 jobs 聚合) + 时间 (全部/今天/本周), 每个 chip 右侧显示计数,
  active 态 = `.filter-chip.active` = `color: var(--accent); background: var(--accent-weak);
  border-color: rgba(53, 71, 232, 0.4)`
- **保留 AntD Table 多选/排序/分页行为**: Checkbox 列首列可控全选/反选, 多选态显示
  "已选 N 个 / 对比 thermo / 清除选择" 工具条; thermo 对比 Drawer 与删除 Modal 保留

### theme.css v1.8.4 续段新增

- `.page-stack` (gap-2 outer)
- `.section-header` (sm semibold + border-subtle 分隔线)
- `.filter-chip` / `.filter-chip.active` / `.filter-chip .count`
- `.row-table` (含 sticky 表头) + `.row-table tbody tr.selected`
- `.sdot-4` (8px 圆, 6 状态色)
- `.sticky-status` (Cal.com 顶部状态条)
- `.failure-card-float` (失败诊断浮起 + 左侧 3px 红条)
- `.kpi-action-btn` / `.kpi-action-btn.danger` (容器操作按钮)
- `.recharts-cartesian-*` 主题适配 (轴标签 text-3, 网格 border-subtle)

**验收** (Playwright headless 截图 + console.error 捕获):
- `verify-v185-dashboard.png`: 8 个 section 全部渲染, KPI bar 第 6 个按钮可见
  "容器 ↻ 启动" (err 红色, 容器停止状态), Recharts 折线图清晰 (近 7 天真实数据可见),
  最近任务 10 行 + 状态点 8px + filter chips 三选
- `verify-v185-jobs.png`: 50 行任务紧凑渲染, 3 排 filter chips (状态/项目/时间)
  + 计数正确 (50/0/27/18/5/0), 行高 40px
- `verify-v185-detail.png`: sticky 状态条 56px 含进度条 + "已取消" 徽章 + LAMMPS 类型
  chip + 50 行 / ENDED 计数;右 sticky 指标卡完整 (进度 100%/耗时 1 分 8 秒/
  ETA 已结束/thermo 样本 50 行/OMP 线程 4/退出码 -);AI 桥显示"复制平衡分析"按钮
- **0 console.error / 0 pageerror** (修 #310 后)

**单测基线**: 92/92 绿 (无新增, 仅前端 CSS+布局)
**Build**: `tsc --noEmit && vite build` 通过 (1.5MB JS / 23KB CSS, gzipped 466KB/5KB)

**改动文件** (5 个, 全部前端):
- `workbench/frontend/src/theme.css` (+ ~120 行 v1.8.4 续段)
- `workbench/frontend/src/pages/Dashboard.tsx` (重写 ~770 行)
- `workbench/frontend/src/pages/JobDetail.tsx` (重写 ~520 行)
- `workbench/frontend/src/pages/Jobs.tsx` (重写 ~470 行)
- `workbench/frontend/src/components/ui.tsx` (+ StatusBadge 13 行)

**未做** (留作下版):
- 暗色模式 (shadcn 4 层 token 已就位, 差 token 切换逻辑 + localStorage 偏好)
- Dashboard 资源指标卡片悬浮 (4 资源指标目前是 KPI bar 横排, 没单独卡 hover 浮起)
- JobList 虚拟滚动 (50 行未触发性能问题, 200+ 行时再考虑)

---

## 2026-08-29 工作台 v1.8.1 (双子代理代码评审: 17 项修复)

**做法**: 派两个子代理并行评审 v1.8 全部新增代码 (后端 1C/6M/12m + 前端 3C/6M/9m),
逐条核对修复; 浏览器交互走查由主代理执行 (Browser Use 技能限定主代理)。

**后端修复**:
- C1 (科学正确性): MSD 用周期包裹坐标计算 — 跨 PBC 边界原子产生箱长假位移。
  模板 dump 加 xu/yu/zu (非包裹坐标), traj_analysis 优先取用, z 分布仍用包裹 z (直方图语义正确)
- M1: CLI 任务完成不触发队列调度 → 队列永久停摆。加 `queue_sweeper` (10s 自愈调度,
  兜住一切外部事件); lifespan 启动
- M2: 日志 IO 异常击穿 `_run` 协程 → 任务永久 running 堵死队列。执行循环 try/except
  (terminate + failed), `_append_line` 日志写失败降级 warning, `_record_built_sha` 兜底
- M3: 后端重启后 queued 的扫描/续跑任务丢 script_text → 静默跑基准参数。script_text 落
  sidecar (`jobs/<id>.script`), 恢复读回; 丢失则取消 (宁可显式失败)
- M4: 删除 queued 任务与队列晋升竞态 → 删除前先 cancel 出队
- M5/M6: 后台轨迹分析无体积上限 (OOM 风险) → 64MB 上限 413; 同步路径改线程池不阻塞事件循环
- minors: analysis 缓存原子写 + 损坏容错 + 删除时回收内存态; run_cli try/finally (Ctrl+C
  回写终态); failure 正则坏签名守卫; diagnose 对 completed 跳过伪失败解析; scan 端点补 lint
  拦截门; _dispatch IndexError 修正; resume 响应 schema

**前端修复** (评审对照 3Dmol 2.5.5 bundle 反汇编逐条核实):
- C1: 「3D 初末对比」按钮从未加上 (补丁脚本半途失败) — 功能不可达。已补
- C2: 3Dmol API 三处误用 — setStyle 第三参被忽略 (样式互相覆盖)、hide() 无参
  (hide(false) 也是隐藏, 双 model 永久空白)、json 格式要求 cdjson 结构 (裸数组抛错)。
  改 per-model `getModel(i).setStyle` + hide/show 成对 + `{m:[{a:[...]}]}` cdjson
- C3: `addModel(text, "data")` — 3Dmol 无 "data" 格式, best-guess 按 PDB 解析出空模型仍报
  ready (静默错误)。新增 `common/lammps_data.py`: data→XYZ 转换 (Masses 质量最近元素匹配,
  覆盖主族/过渡金属, 偏差 15% 外记 X), 端点附带 xyz; 前端改 `addModel(xyz, "xyz")`。
  实测 my-first-solution 2091 原子渲染出完整水网格 + 溶质结构
- M1: 对比图数据锁死 series[0] 行数 (短曲线末值平台延长) → max 行数 + 越界 null 断线
- M2: 任务列表 CLI/batch 徽章从未渲染 → 已补 ( Tag)
- M3: 轨迹分析 run 无 catch + 卸载后轮询 → catch 提示 + mounted 标志
- M4: 受控退出成功后状态回退可二次点击 → shuttingDown 保持 + backendDown 自动关 Modal;
  孤儿清理数改用服务端返回值
- M5: 运行中任务到终态后检查点区不出现 → ws 终态分支补拉 restarts
- M6: 3Dmol viewer 泄漏 WebGL 上下文 (约 16 个上限) → useRef 复用实例 + clear
- m2 续跑步数钳制 ≥1 / m3 扫描非数字值显式报错 / m4 ProjectSystem 跨项目竞态 closed 标志 /
  m6 OpenWithTool 检查 resp.ok / m7 selected 清理 + 有效任务不足提示

**仍挂账** (低危, 见评审原文): WS 重连提示、WS 回放期间帧重复、collect_deps 深度语义、
resume 续跑段无轨迹输出、跨工作区依赖源任务清理时序、launcher .bat 转义、m1 工具探测错误态。

**方法**: 评审子代理 (后台并行) + 主代理 GUI 走查互补; 浏览器工具 (Browser Use) 按技能约束
仅主代理可用。修复后 78 测试全绿, 3D 预览真渲染验收 (2091 原子水网格+溶质清晰可见)。

---

## 2026-08-29 工作台 v1.8 (全量落地: CLI 入库/队列/扫描/续跑/双轴/3D 对比/桥②)

**背景**: 用户拍板"全部都做" — 落地平台调研与 VASP Harness 评审的全部剩余候选。
VASP 科研助理 (DeepSeek Harness) 评审的结论: 对方"薄 agent + 确定性看板"验证了本项目
确定性路线; agent 自由探索烧 token 的翻车实录反证提示词门禁不可靠。

**1. CLI 任务入库** (双入口同源收尾): store 加 source/batch 列; runner.run_cli 落同一任务库
(source=cli, stdout tee 到 jobs/<id>.log, 详情页日志/thermo 回放/产物/分析全可用);
运行中 CLI 任务工作台取消 409 (终端持有进程句柄)。E2E: CLI 跑 demos → 任务记录可见 completed。

**2. 任务队列** (RadonPy/pyiron 思想): MAX_CONCURRENT_LMP=1 (config 可调); 超限任务 queued,
前序完成自动调度; 后端重启 queued 重新入队并调度。状态机加 queued; store 计数为地面真相。
E2E: 双发 → 一跑一排队 → 自动接续; 重启恢复 → 调度完成。

**3. 检查点续跑** (can_resume 落地): 模板每阶段 write_restart (nvt_production 补生产后检查点;
MMT 手写脚本两段后补; 新模板 relax_production 三段弛豫=min→半温退火→平衡→生产);
GET restarts + POST resume 生成自包含 resume.in: read_restart 用**容器内绝对路径跨工作区**引用
源检查点 + fix/kspace_style/special_bonds 从原脚本重建 (restart 不保存这些) + run N。
指纹含 resumed_from/restart 溯源。E2E: 500 步续跑 completed。

**4. 参数扫描** (体系配置页按钮): 选方法参数+值列表 → 每值实时渲染脚本副本 (**只写任务工作区,
项目文件永不污染**) → 批量入队 (batch 关联); 任务列表 CLI/batch 徽章; 多选「对比」叠加 TotEng。
E2E: 温度 320/340 扫描 → 串行完成 → compare 端点双曲线 (TotEng/Density 列齐)。

**5. 弛豫收敛双轴图**: MMT 01_run thermo_style 加 fmax; ThermoChart 检测 Fmax 列自动挂右轴
(能量左轴 + 力右轴); 新模板 minimize 段同款。视觉验证: fmax 指数衰减叠加能量收敛, 一眼判弛豫。

**6. 3D 初末态对比**: traj_analysis 输出首末帧原子坐标 (入缓存); 轨迹统计卡「3D 初末对比」→
3Dmol 双 model (初帧灰线 + 末帧彩球, 叠加/切换)。

**7. 桥② skill 打包**: `skills/lammps-diagnose/SKILL.md` (可安装 agent skill) +
`python -m workbench.backend.app.diagnose --job <id> --json` (离线读任务库: 记录+lint+
案例库解析+检查点+日志尾, 不依赖工作台进程)。实测对历史失败任务输出完整结构化诊断。

**配套**: 测试项目 my-first-solution 方法参数调小 (5000+2000 步, 秒级完成, 职责=链路验证);
Docker Desktop 引擎停机一次已拉起。

### 经验与教训 (本轮实录)

1. **真实失败是最快的规则来源**: toteng 关键字 500 失败 → lint 规则 + 案例库签名当轮沉淀;
   剪贴板失焦静默失败 → 显式报错。每次真实失败都应问"能不能变成确定性检查"。
2. **夹具式思维用于前端**: 浏览器 E2E 多次被 heredoc 转义吃字符 (`
`/`` 变真实控制字符,
   写进源码成隐形 bug) — 用 Edit/chr() 构造替代 heredoc 转义; 构建通过 ≠ 逻辑正确
   (setCompareOpen 未定义但 esbuild 不查)。
3. **记账优于进程观测**: 队列并发判断从进程句柄计数改为 store 记账后, 竞态窗口消失;
   "地面真相"原则再次生效 (与容器 lmp 进程数 pgrep 一脉相承)。
4. **restart 不保存 fix/kspace**: LAMMPS 续跑脚本必须重建 fix/kspace_style/special_bonds;
   read_restart 可跨工作区用容器内绝对路径引用 — 这是续跑实现的关键知识点。
5. **文档驱动的自我修正**: 每块功能先想"CLI 等价物是什么" (双入口同源), 参数扫描/续跑/
   诊断全部同时具备 UI 与命令行形态, agent 与人共享同一能力集。

---

## 2026-08-28 工作台 v1.7.1 (AI 桥①: 复制 AI 分析提示词 — VASP Harness 借鉴)

**来源**: VASP DeepSeek Harness 评审 (会话 sess_3113e2dd 后半段) — 「薄 agent + 确定性看板」混合架构。
对方 demo 验证了本工作台确定性路线正确; 唯一缺口是工作台 ↔ AI agent 之间没有桥。落地评审候选①。

**实现** (`frontend/src/utils/aiPrompt.ts` 纯函数 + JobDetail 两处按钮, 零后端):
- 失败解析卡「复制 AI 分析提示词」: 任务上下文 (id/项目/退出码/工作区/环境指纹) + 案例库解析
  (错误行/严重度/续跑策略/建议动作) + 日志尾部 40 行 → 结构化 markdown, 粘贴给 ZCode 即贴即开工
- thermo 卡 (平衡非 unknown 时) 同款按钮: 判定 + 逐量漂移值 vs 阈值 + thermo 尾部 15 行样本
- 提示词不写死仓库路径 (agent 在仓库 cwd 内自知), 跨机部署安全

**修复**: copyToClipboard 静默失败 (IAB 失焦时 navigator.clipboard 被拒 → execCommand fallback
也失败仍提示「已复制」) — 两条路都失败显式抛错, 按钮 catch 后 message.error 不静默。

**验证**: 78 测试全绿; 浏览器 E2E 两种提示词剪贴板实测 — 失败提示词 (案例库 TypeError 命中 +
完整 traceback) 与平衡提示词 (接近平衡 + TotEng 漂移 0.0864% vs 0.05% + thermo 尾样) 内容完整。

**未拍板候选** (VASP Harness 评审): 桥② lint/诊断打包 ZCode skill (依赖 CLI 任务入库);
弛豫收敛双轴图 (MMT thermo 加 fmax); 浏览器内初末态结构对比 (低优先)。

---

## 2026-08-28 工作台 v1.7 (P0 结果判读: 平衡判据 + 轨迹在线分析 + 环境指纹)

**来源**: 平台调研候选 #1/#2 落地 (RadonPy 平衡判据 / pyiron 任务可比性思想); 补齐研究闭环「跑完之后」的判读能力。

**1. 平衡判据定量化** (`common/equilibrium.py`, 纯函数):
- 末 20% 窗口对 Density/TotEng 线性拟合, 相对漂移 vs 阈值 (密度 0.1% / 能量 0.05%, RadonPy 参照)
- 判级: 全 pass=good / 有 fair=fair / 有 poor=poor; 样本 <20 或无判据列 → unknown 不显示
- 详情页 thermo 卡标题旁胶囊: 已平衡(绿)/接近平衡(橙)/未收敛(红), tooltip 逐量漂移值

**2. 轨迹统计在线分析** (`common/traj_analysis.py` + 端点):
- per-type z 分布 (60 bins 归一频数) + per-type MSD (含 all; 最大滞后 50 帧, 轨迹截前 200 帧)
- 通用不假设体系化学 (前端只呈现不解读; 科学解读仍归项目分析脚本)
- POST /api/jobs/{id}/analysis 后台线程 (大轨迹) + GET 轮询; 结果缓存 workspace/analysis_cache.json;
  ≤8MB 同步算; 详情页「轨迹统计」卡 recharts 双图
- E2E: 12.7MB 真实轨迹 (MMT 2091 原子 4 类型 200 帧) idle→POST→10s done

**3. 任务环境指纹**: jobs 表加 fingerprint 列 (迁移); 发任务时采集 system.json sha(前16) +
镜像 ID + LAMMPS 版本 (docker_env.container_fingerprint, 10min TTL, 失败不阻塞);
详情页元信息「环境指纹」行。跨机/换力场后结果可比性有据可查。

**配套**: 教学模板 thermo_style 补 density 输出 (下次渲染生效; 存量渲染产物不动);
Docker Desktop 引擎停机被发现并拉起 (容器重启一次); insert 缺 fingerprint 列兼容旧调用。

**验证**: 78 测试全绿 (equilibrium 4 + traj_analysis 2 + fingerprint 1 + 既有回归);
浏览器验证: 胶囊「接近平衡」(60 行 TotEng fair) / 分析卡图表渲染 / 指纹行; demo 小任务正确
显示 unknown/无轨迹 的空态。

---

## 2026-08-28 工作台 v1.6 (本地工具集成: VMD / Vesta 自动检测 + 启动器 + 3D 预览)

**需求**: 仪表盘增加 VMD/Vesta 自动检测 + 手动配置浮窗; 任务详情与体系配置页「一键打开本地工具」;
为没有桌面工具的用户提供浏览器内 3D 结构预览。

**后端** (workbench/backend/app/local_tools/ + routers/local_tools.py):
- `local_tools/detect.py`: 跨平台常见安装路径探测 (Windows/macOS/Linux), 支持 VMD_EXE/VESTA_EXE
  环境变量覆盖; 返回结构化 {found, path, version_hint, source}
- `launcher()`: 纯函数, 按本机 OS 生成一键启动脚本 — Windows .bat (start "" + if exist 兜底 +
  pause 提示) / macOS .command / Linux .sh; 缺失 exe 时脚本自带「工具未找到」+ 指引
- `routers/local_tools.py`: GET /detect, POST /configure (路径持久化到 workbench/data/local_tools.json
  优先生效, 路径不存在返回 400), GET /launcher?tool=&path= 返回 {filename, content}, GET /install-hint
  返回按平台官网 URL
- `routers/projects.py` +1: GET /api/projects/{id}/system-data 供 3D 预览拉取 (32MB 上限)
- 依赖: pyproject 加 httpx (dev, 端到端测试用)

**前端**:
- **仪表盘**: 「工作台控制」卡上方新增「本地工具」卡 (10s 轮询 / 后端停止时清除);
  VMD/Vesta 状态点 (绿=已检测带版本/红=未检测); 点击展开右侧 Drawer — 自动状态 +
  手动输入框 (含 placeholder、清除按钮) + 两个工具的官网安装指引链接
- **任务详情 JobFiles**: 每个产物文件按扩展名映射推荐工具 (.lammpstrj/.dump → VMD, .data/.cif → Vesta),
  文件行新按钮触发「下载一键启动器」(.bat/.command/.sh) — 双击运行即打开; 未检测到时
  message.warning 提示先在仪表盘配置
- **体系配置页**: 「重建体系」按钮旁加「预览 3D 结构」按钮 → 拉取 system.data (32MB 上限) →
  动态加载 3Dmol.js CDN (不进主 bundle) → 480px 渲染区域; 顶部「用 Vesta 打开」同步走启动器

**验证**: 71 测试全绿 (新增 4: detect/launcher/configure 持久化+清除); 浏览器确认仪表盘「本地工具」
卡渲染、Drawer 浮窗打开 (含两工具输入框与官网链接); 端到端 `/api/local-tools/detect` 烟测,
VMD/Vesta 状态字段正确; system-data 端点返回 strontium 5137 原子 system.data (354808 字节)
文本 + 绝对路径。

---

## 2026-08-28 工作台 v1.5 (借鉴 LAMMPS-Agents 确定性机制落地)

**来源**: 本会话对 ANL-NST/LAMMPS-Agents 与 chatmaterials/lammps-workflows 的评审判定
「借鉴思想, 不照搬代码」— 他们用 LLM 提示词自律实现的门禁/评审/记忆, 我们以确定性机制落地。

**1. 发车前 lint** (`common/lammps_lint.py`, 纯函数零依赖):
- errors 拦截: 缺 units(pair_style/run)、占位符残留 (replace-with/TODO 等)、引用文件不存在
- warnings 放行: run 0、/data/ 旧挂载绝对路径 (已废弃约定)
- 接入: POST /api/jobs (lmp) 发车前 400 拦截; 渲染后兜底检查

**2. 失败案例库 + 结构化解析** (`failure_rules.json` + `failure.py` 重写):
- 规则外置 JSON (签名→原因→severity/actions/can_resume), 编辑即时生效无重启
- FailureInfo 增 severity (高/中/低风险) / actions (有序建议) / can_resume (续跑策略)
- 前端失败卡显示风险徽章 + 建议动作列表 + 续跑标签
- 修复: Python 错误行提取被 [workbench] 尾行污染 (真实夹具发现)

**3. 夹具回归**: tests/fixtures/logs/ 真实任务日志 (demo_completed / build_failed), 黄金断言加固失败解析

**4. 体系一致性链** (ANL「就绪检查表」思想的确定性落地):
- GET system 返回 consistency: built_state (built/stale/never) + script_state (sync/hand_edited/missing)
- build 任务成功后 job_manager 把 system.json 指纹写入 project.json (built_system_sha)
- 体系配置页顶部一致性徽章 (绿=一致 / 橙=已改未重建/已被手改 / 灰=从未)

**验证**: 67 测试全绿 (lint 8 + 失败案例库 6 + 一致性 3 = 新增 17); E2E: 坏脚本 400 拦截 /
never→build→built / 历史真实失败 (TypeError) 命中案例库出现动作建议; 浏览器验证失败卡与一致性徽章。

---

## 2026-08-28 仓库布局: 内置项目收进 systems/ (用户项目 projects/ 之外)

**需求**: strontium_adsorption / Montmorillonite-test 两个 agent 时代项目从仓库根收进子目录, 保持根目录整洁。

**决策**: 三个内置项目 (strontium_adsorption / Montmorillonite-test / demos) 统一迁入 `systems/`,
与用户自建 `projects/` 形成「内置 systems/ + 用户 projects/」的一致心智。项目 id 全部不变 (取自 manifest),
历史任务记录/工作区引用不受影响 (记录存 id + jobs/<id> 绝对路径, 与项目目录位置解耦)。

**代码适配** (引用面极小, 纯路径常量):
- `config.py`: BUILTIN_DIRS 改为 systems/ 相对路径; 内置兜底注册 id 取 basename (与子目录布局解耦)
- `common/entrypoints.py`: SR/MMT 常量与 analyze/postprocess 脚本路径
- `Dashboard.tsx`: 演示任务副标题文案
- 注意: montmorillonite 的 id 一直来自 manifest (非目录名 Montmorillonite-test), 历史记录不受影响

**验证**: 52 测试全绿; build-sr 新路径下种子级重建 (system.data 字节一致); demo LAMMPS 任务经
暂存-运行-回收 completed (exit 0); API 项目列表四个项目 dir 全部正确。

**文档对齐**: AGENTS.md (布局树重排 + 命令注释) / docs/parameters.md / docs/environment.md /
docs/README.md / strontium README (目录树 + VMD 绝对路径); work-log 历史条目按惯例不改写。

---

## 2026-08-28 工作台 v1.4.2 (手动创建项目: 规范指南 + 兜底注册)

**需求**: 工作台页面就地说明「手动建项目时文件放哪/怎么写/什么行为」; 手动操作要能同步展现在界面。

**后端** (`config.py` + `routers/projects.py`):
- projects/ 下非空但缺 project.json 的目录兜底注册 (id=目录名, `unregistered: True` 标记;
  空目录忽略防噪音) — 与内置目录兜底行为对齐, 文件夹即项目
- list_projects 透传 unregistered; 补 manifest 后刷新即转正 (零重启, 纯扫描架构天然支持)

**前端** (`Projects.tsx`):
- 「手动创建指南」抽屉 (项目页按钮 + 新建向导第一步入口): 目录树示意 / project.json 最小模板
  (一键复制) / 平台自动行为 (脚本判型·依赖闭包·体系层可选·产物去向·在线编辑边界) /
  CLI 与任务记录的边界 (手动 CLI 暂不入库, 已在指南明示)
- 未注册项目卡片: 橙色「未注册」角标 + 提示条 (含指南链接); 运行/删除照常

**验证**: 52 测试全绿 (新增兜底注册 2 例); E2E: 手动建目录→API 可见 unregistered=True→
补 manifest 转正→删除即消失, 全部零重启; 浏览器验证角标卡片与指南抽屉视觉。

---

## 2026-08-28 工作台 v1.4.1 (仪表盘: 结束工作台进程 — 受控退出)

**需求**: 仪表盘右侧补充「结束工作台进程」功能 (用户提出)。

**后端** (`routers/system.py` + `docker_env.py`):
- `POST /api/workbench/shutdown`: 三重防护 — ①有运行中任务 → 409 互锁 (返回任务清单, 不可越过);
  ②容器内孤儿 LAMMPS 进程 → 退出前自动 pkill + pgrep 复核; ③0.5s 延迟窗口内若新任务启动则放弃退出 (竞态互锁)
- 退出路径: 检测 uvicorn 装在主线程的 `Server.handle_exit` SIGTERM 处理器后 `signal.raise_signal(SIGTERM)`
  → 优雅停机, 跨平台 (Windows 上 os.kill(SIGTERM) 是 TerminateProcess 硬杀, 不可用; uvicorn 0.52 已删 `Server.instance` 类属性)
- 决策逻辑提为纯函数 `plan_shutdown()` 可单测; `docker_env.lmp_process_count()` 返回 `int | None` (探测失败=未知, 不猜 0)

**前端** (Dashboard/App/ui/client):
- 仪表盘右列新增「工作台控制」卡: 红色 danger 按钮 (电源图标 + 浅红底, 与蓝色运行类按钮明确区分)
- 确认 Modal 展示地面真相: 运行中任务 (有则阻止并列表) / 孤儿进程清理预告 / 文件保留说明 / 终端重启命令
- App 跟踪 `backendDown` (曾连通后 health 拉取失败即判定): 顶栏芯片→「后端已停止」红点, 仪表盘顶部停止横幅
  (含重启指引), 快速操作/控制按钮全部禁用 — 停止后状态不依赖内存态
- `api.shutdownWorkbench()` 返回结构化结果 (shutting_down / blocked / error), 不走通用抛错

**验证**: 50 测试全绿 (新增 plan_shutdown 3 例); API 级 E2E: 409 互锁 (假 running 记录) / 真实退出 (进程退出+容器 0 残留) /
孤儿清理 (容器内起真实 lmp → cleaned=1, residual=0); 浏览器视觉验证: 控制卡/Modal/取消/停止横幅/重启恢复全链。

---

## 2026-08-28 全仓重塑 v2 (双空间合规: 真相归一 + 注册统一 + 文档重塑)

用户授权大修: 全仓审计 (46 条违规) → 三阶段重塑。设计框架: 软性人-agent 交互空间 + 硬性前后端架构,
同源原则 (UI 每个动作有文件/CLI 等价物, 同一事实多处呈现必须一致)。

### P1 真相归一
- **strontium 力场如实化** (用户拍板): 审计发现 Ow LJ 四变体并存 (system.json 标"SPC/E 标准"
  却写 CLAYFF O 值, 实际运行脚本是第三组值)。system.json 改为如实记录历史混合体
  (SPC 电荷 -0.820/+0.410 + SPC/E 型 O-LJ 0.1553/3.1660), 渲染产物与历史轨迹一致, 无需重跑
- **spce_params.py 归一**: 常量改为从 system_config.WATER_PRESETS 派生 (消灭双常量源)
- **montmorillonite 数据层**: 新 profile `clay_cif` + `builders/clay_cif.py` (忠实移植
  convert_cif.py, 含 CIF 绑定阈值参数化); **等价性 ✓** (412 原子/160 键逐项一致);
  convert_cif.py 归档; 01_run.lmp 中文 print 改 ASCII + 头注"力场源 system.json";
  post_process.py 输入输出改脚本同目录
- **analyze_sr.py 参数化**: z 边界/真空层/离子类型读 system.json (步长仍为方法常量)
- 旧脚本归档: build_system.py / run_final.lmp(→run_final.handwritten.lmp) / convert_cif.py

### P2 注册与入口统一
- 三内置项目各配 **project.json** (builtin: true, strontium 含 rendered_sha);
  config.py 改纯扫描 (BUILTIN_DIRS + projects/, 零硬编码项目清单)
- 新 `common/runner.py`: 暂存-运行-回收统一契约 (collect_deps/stage_dependencies/lmp_command/run_cli);
  job_manager 与 CLI 同源消费; `python -m common.runner <dir> <script> [--omp N]`
- entrypoints.py 重写: build-sr/build-mmt/run-sr-sim/run-mmt-sim 全接新契约
  (旧 run-sr-sim 的 -w /data/<项目> 已失效), convert-mmt → build-mmt (pyproject 同步)
- projects/111 补构建 (system.data + build_report)

### P3 文档重塑 (软空间修复)
- CLAUDE.md / ARCHITECTURE.md 重写 (双空间设计 + 完整布局树 + 数据层说明);
  docs/environment.md 挂载段与命令重写 + workbench 章节;
  docs/workflows.md 增体系配置层章节 + 暂存路径契约;
  docs/parameters.md 声明数值真相源 = system.json; docs/README.md 索引补全;
  两子项目 README 命令修正; demos/adsorption.lmp 注释修正; common/__init__ 自描述更新
- **同源 grep 清零**: 活代码无旧挂载引用 (仅存 archive/ 历史与 entrypoints 弃用注记)
- .gitignore 补 cl_z_* 产物; 根目录遗留 _tmp_verify_rdf.py 删除
- 测试: 47 用例绿; build-sr/runner CLI 冒烟通过
- **CLAUDE.md → AGENTS.md** (AGENTS.md 开放约定, 规范化结构: 概述/布局/命令/架构原则/规范/测试/陷阱);
  CLAUDE.md 留 `@AGENTS.md` 导入指针 (Claude Code 兼容), 单一真相源零双维护

---

## 2026-08-28 工作台 v1.4 (快速修复包: 孤儿对账 + 入口降噪 + OMP 参数)

路线图快速修复项落地 (体系来源扩展 — 晶体/摩擦/导入路径 — 用户决定延后):

- **重启孤儿任务对账** (路线图 #1): 后端启动 lifespan 调 recover_orphans() —
  遗留 running 任务查容器内进程: 已消失 → interrupted("结果可能不完整");
  仍在 → interrupted + 告警 PID; interrupted 可从列表取消 (三段式清残留)。
  **回归 bug 修复**: _transition 原先依赖 start() 预建的锁, 恢复路径锁字典为空静默失败 —
  锁改为按需创建, 补回归测试。端到端: 造 running → 强杀后端 → 重启 →
  interrupted(如实标注 PID 39193) → 清理 → 进程归零 ✓
- **运行参数面板** (路线图 #8): JobCreate 增 omp_threads (1-64, 默认 8),
  LAMMPS 命令按其生成 -pk omp N; 运行确认弹窗可调; store 轻量迁移 (ALTER TABLE)
- **入口降噪** (路线图 #2): /api/projects 返回 has_system, 无体系配置的项目卡隐藏入口
- **测试**: +3 用例 (omp 命令生成 / interrupted 迁移表 / 无锁迁移回归), 全套 47 用例绿

---

## 2026-08-28 体系配置层 v1.3 (system as data + 新建向导)

用户提出"体系搭建流程未融入平台, AI 一键生成导致参数掌控性低" — 设计原则: 体系即数据。
system.json 成为体系参数单一真相源 (几何/组成/力场, 含来源+置信度), 构建引擎与脚本渲染都从它读取。

- **数据层**: 新 `common/system_config.py` (加载/校验/水模型预设/PROFILE_SCHEMAS 表单 schema/
  default_system 构造器); `strontium_adsorption/system.json` 迁移 (保持原值, Ow/Hw 的
  SPC 原始电荷 vs 权威 SPC/E 不一致以 warning 字段标注 — 用户确认仅标注不修正)
- **构建引擎**: 新 `common/builders/` (base 写入器+报告 / surface_adsorption 忠实移植 /
  solution 均相溶液); `python -m common.build <dir>` 入口; 任务 kind=build。
  **等价性验证**: 种子 42 下新引擎与旧 build_system.py 产物原子/盒子/键/角完全一致 (5137 原子)
- **方法模板**: `workbench/backend/templates/methods/nvt_production/` (method.json 参数 +
  run.lmp.j2 按 9 板块规范生成, 每行注释, pair_coeff 从 system.json 渲染带来源/置信度 —
  消灭 build 与 run.lmp 双源漂移); jinja2 依赖; 手改检测 (rendered_sha, 覆盖需 force);
  内置项目渲染到 run_rendered.lmp (绝不覆盖手写 run_final.lmp)
- **新建向导**: 项目页 "+ 新建项目" 三步向导 (基本信息→体系参数→模拟方法), schema 驱动表单;
  用户项目存 projects/<id>/ (project.json 自动注册, 零重启), 可删除
- **工作台 UI**: 项目详情「体系配置」页 — 体系参数卡 (schema 分组表单) + 力场参数表
  (来源/置信度徽章 + 不一致红字) + 编辑/重建体系/重新渲染按钮
- **thermo 回放修复** (用户反馈重启后曲线消失): 终态任务首次访问时从日志文件回放重建
  thermo 缓冲 (日志为权威副本)
- **测试**: +16 用例 (config 校验/builder 计数与复现/模板渲染/thermo 回放), 全套 44 用例绿;
  端到端: 向导建 solution 项目 → 构建 (681 水/电荷 0) → 渲染 → 运行新脚本 → 取消 ✓;
  已知不一致按用户决定仅标注
- 待办 (v1.4 候选): 黏土 CIF profile 抽象、脚本在线编辑器 (CodeMirror)、参数扫描批量生成

---

## 2026-08-28 工作台 v1.2 (取消可靠性 + 容器真相 + 再次运行防误触)

- **再次运行防误触** (用户误触反馈): Redo 图标(似刷新)→播放图标, 中性灰→靛蓝着色 (mini-btn accent),
  点击后 Popconfirm 确认; 误触启动的任务已代为取消
- **取消三段式验证** (用户提出"无法真实取消不可知"): SIGTERM → 1s 后 pgrep 验证 →
  残留升级 SIGKILL → 仍残留警告写入任务日志 (WS 可见, 附手动 kill 命令)。
  端到端: 取消 1.3s 完成, 进程归零, SIGTERM 一次到位
- **容器真相指标**: /api/health 增加 lmp_processes (docker exec pgrep -c 实测);
  仪表盘"容器内 LAMMPS 进程"行 — 任务记账说已取消但此处 >0 即孤儿进程,
  无运行中任务却 >0 时红点标"疑似孤儿"
- **日志停滞告警**: 运行中任务 2 分钟无日志输出 (LAMMPS 正常持续打 thermo),
  详情页红字提示"可能不收敛或被阻塞"
- **失败解析卡** (用户反馈): 新 `failure.py` — 失败任务提取 LAMMPS ERROR 行 + Last command /
  Python Traceback 尾行, 按规则库给中文解析建议 (package 位置 / 文件缺失 / 原子丢失 /
  数值发散 / 命令无效 / OOM / SIGKILL / 常见 Python 异常等);
  详情页日志上方红色卡片展示; 7 个单测覆盖, 全套 33 用例绿
- **任务删除** (用户反馈): 表格行内删除按钮 (仅终态任务), 双重确认 =
  Popconfirm + 勾选"不可恢复"门控 Modal; DELETE /api/jobs/{id} 删工作区+日志+记录,
  返回释放字节数; 安全拦截: 运行中 409, 容器内进程残留 409; 端到端验证文件/记录全清

---

## 2026-08-28 工作台 v1.1 (评审改进: 可靠性 + 体验)

按外部 AI 架构评审落实两波改进 (评审"不建议动"清单全部采纳; 其 P0 建议的 PID 方案会破坏
日志流, 改用其 fallback: 绝对路径 -in + 按工作区路径 pkill):

- **P0 精确取消**: LAMMPS 命令 `-in` 改为容器内绝对路径 `/data/jobs/<id>/<script>`,
  命令行含任务唯一标识; cancel 只 `pkill -f /data/jobs/<id>/`。
  端到端验证: 双任务并发取消 A, B 进程 (pgrep 按路径区分) 存活且日志持续增长 ✓
- **P1 依赖暂存**: `collect_deps` 解析 include/read_data/read_restart 引用闭包
  (剥注释/传递/只扫 <2MB 文本/跳二进制扩展名), 随脚本一并拷入工作区, 缺失写告警行
- **P2 工作区清理**: `workspace.py` 后台 sweeper (每 6h), 终态任务 finished_at 超过
  `WORKSPACE_RETENTION_DAYS`(14 天) 删工作区; 孤儿目录 (>1 天) 也清
- **P3 状态防重入**: VALID_TRANSITIONS 表 + per-job asyncio.Lock,
  cancel 与自然退出竞态先到先得, 重复操作幂等
- **Thermo 实时曲线**: 新 `thermo.py` (识别 "Step" 表头 + 数值行, 列变化重置缓冲, 上限 5000 行);
  日志行实时喂入, WS 增量帧 + 握手全量补发, REST 详情附最近 500 行;
  详情页 recharts 折线图 (Temp/E_pair/TotEng/Press 可勾选, 渲染最近 1000 点)
- **产物浏览**: GET /api/jobs/{id}/files + /files/content (文本预览 ≤256KB / 下载,
  realpath 防路径逃逸, 二进制 415); 详情页文件卡
- **再次运行**: 终态任务同参数一键重新提交
- **测试**: 新增 tests/test_workbench.py 12 用例 (依赖闭包 6 + thermo 6), 全套 26 用例绿;
  端到端: 精确取消 / thermo 帧序列 / 文件预览下载 / 路径逃逸 400 全部通过
- 待办 (v1.2 候选): 任务提交参数面板 (omp 线程数等)、脚本预览+基础校验、多容器 config 扩展位

---

## 2026-08-28 LAMMPS 控制中心工作台 v0 (workbench/)

新增全栈工作台 (FastAPI + React/AntD + Vite), `uv run workbench` 一条命令启动 (http://127.0.0.1:8000, 后端静态托管前端构建产物):

- **功能**: 仪表盘 (容器/挂载状态 + 任务统计) / 项目与脚本浏览 (3 个子项目, .lmp+.py) /
  任务发起与历史 (SQLite, workbench/data/) / 实时日志 (WebSocket /ws/jobs/<id>) / 任务取消
- **挂载方案变更 (用户决定)**: 容器 lammpsd 的 /data 改挂独立数据目录 `lammps-data-docker/`,
  不再挂项目根 (Windows 下挂小目录性能好, 容器不写项目根)。工作台任务采用「暂存-运行-回收」:
  每个任务建工作区 `lammps-data-docker/jobs/<id>/`, 宿主机侧拷入 .lmp + 顶层 *.data,
  容器内 `-w /data/jobs/<id>` 运行, 产物天然留在工作区。
  手动命令模板: `docker exec -w /data/jobs/<id> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp 8 -in <script>.lmp`
  ⚠️ 文档中旧的 `-w /data/<项目>` 命令已失效 (docs/environment.md / workflows.md 待后续整理)
- **修复 run_final.lmp**: 脚本内 `package omp 8` 位于 read_data 之后, 触发 LAMMPS
  "Package command after simulation box is defined" (修复前用标准命令运行也会报错);
  已改为注释并注明由命令行 `-pk omp 8` 统一设置
- **已知限制 (v0)**: 仅自动暂存 *.data 依赖 (脚本 include 其他文件需先手动放入数据目录);
  取消时容器内 pkill 会终止所有 lmp_mpi (单用户单任务可接受); WS 慢消费者丢帧 (日志文件为权威)
- **端到端验证**: demos/test.lmp 完成 / analyze_sr.py (Python) 完成 / run_final.lmp 取消成功
  (容器无残留进程) / WS 历史补发+状态帧 / 前端四页浏览器验收通过
- 待办 (v1 候选): 轨迹可视化 (web 3D / OVITO 集成)、参数预设生成 .lmp、分析图表页 (RDF/MSD 在线出图)、
  任务队列与并发控制、远程计算节点

---

## 2026-08-17 分析工具链性能与可靠性优化

按架构报告剩余空间自主优化 (工程侧, 不改变科学结论):

- **RDF 向量化**: 新建 `common/rdf.py`, 用 numpy 广播替代 post_process.py 内 O(N²) 纯 Python 双层循环;
  修复归一化死代码 (未使用的 norm) 与同种原子 (Ow-Ow) 自身对伪峰污染 bin0;
  验证: 向量化与朴素参考实现 diff=0, post_process.py 回归通过 (501 帧)
- **单元测试**: 新增 `tests/` (test_traj_parser / test_water_builder / test_rdf / test_spce_params),
  共 14 用例全绿; `pyproject.toml` 加 `[dependency-groups] dev = ["pytest"]` 与 pytest 配置
- **一键入口补 OMP**: `entrypoints.py` 的 `_run_docker` 加 `-sf omp -pk omp 8` (OMP_FLAGS 常量), 与文档命令一致
- **Cl⁻ 分析**: `analyze_sr.py` 泛化为 Sr²⁺/Cl⁻ 双离子分析, 直方图改 `numpy.histogram`;
  新增 cl_z_*.txt/png, Sr 输出与历史完全一致 (浓度比 7.69);
  Cl⁻ 富集比 2.79 (作 Sr²⁺ 反离子进入吸附层, 双电层结构, 合理)

---

## 2026-08-14 架构改进（路径/参数/公共库/入口/OMP）

按架构分析报告 (ARCHITECTURE.md) 建议落实:

- **P0-1 路径硬编码重构**: `build_system.py`/`run_final.lmp`/`analyze_sr.py`/`demos/adsorption.lmp`
  改为相对路径, 运行用 `docker exec -w <脚本目录>`; `analyze_sr.py` 的 xy_area 改从轨迹盒子动态读取
- **P0-2 力场参数**: 核对 JC 2008 Cl⁻(SPC/E) = ε0.1000/σ4.045 (推荐替换), Sr²⁺ 无统一文献值;
  参数来源/置信度已标注于 `build_system.py` (`type_lj` 结构化 + `LJ_ION_REF`) 与 `run_final.lmp` pair_coeff 注释
- **P1-3 公共库 `common/`**: `spce_params.py` (SPC/E 常量), `traj_parser.py` (统一轨迹解析, 供 analyze_sr/post_process),
  `water_builder.py` (水分子随机取向, 供 convert_cif); 消除 A/B 项目重复实现
- **P1-4 一键入口**: 新增 `pyproject.toml` + `common/entrypoints.py`, 注册 6 个命令
  (`build-sr`/`analyze-sr`/`run-sr-sim`/`convert-mmt`/`postprocess-mmt`/`run-mmt-sim`)
- **P2-5 OMP + gitignore**: `run_final.lmp` 加 `package omp 8`, 命令含 `-sf omp -pk omp 8`;
  `.gitignore` 排除 system.data/msd.dat/*.xlsx/*.png 等可再生成物
- **环境修复**: 项目移动导致 `.venv` 失效 (uv trampoline os error 448), 已删除并用
  Python 3.14.3 重建 venv, `uv run` 恢复; 详见 docs/environment.md
- **行为影响说明**: ① 重新生成 system.data 后与旧文件哈希不同 (历史版本差异, 结构/规模一致);
  ② `convert_cif.py` 水取向改用 np.random (物理等价, 重新生成 system.data 会变化)

---

## 2026-08-14 文档与目录重构

- 按 Anthropic CLAUDE.md 官方规范重构文档：`CLAUDE.md` 精简为快速指引（<200 行），
  详细内容拆分至 `docs/`（environment / workflows / parameters / work-log）
- 文件整理：根目录测试/教学脚本移入 `demos/`（adsorption.lmp、test.lmp、trajectory.lammpstrj、log.lammps）；
  删除 `benchmark.ps1`、`strontium_adsorption/benchmark.lmp`（基准结果见下）、`package-lock.json`（npm 空壳）、
  `Montmorillonite-test/rdf_owow.dat`（0B 孤儿文件，无脚本写入）
- **修复 Docker volume**：容器 `lammpsd` 挂载的宿主机路径 `Desktop\lammps-test` 已不存在
  （项目实际在 `cc-proj\lammps-test`），已创建目录联接 `Desktop\lammps-test → cc-proj\lammps-test` 修复，无需重建容器
- 脚本改动（仅 2 处，不影响运行逻辑）：`demos/adsorption.lmp` dump 输出路径 → `/data/demos/trajectory.lammpstrj`；
  `strontium_adsorption/run_final.lmp:64` 注释更新为当前宿主机路径
- `manual_md/CLAUDE.md` 改名 `manual_md/README.md`（手册索引非指令文件）
- 待办清单未变，见文末

---

## 项目当前状态

```
Docker 容器: lammpsd (lammps/lammps:latest)，2026-08-14 修复 volume 映射后可用
Windows Python: uv 管理, venv 在项目根目录, 有 matplotlib
CLI: uv run python <script>.py   # 不要用裸 python
建模: build_system.py (Python, Docker 内无 Python, 输出路径 /data/strontium_adsorption/system.data)
```

## 运行结果

### 分析脚本: analyze_sr.py

功能: 解析 prod.lammpstrj, 输出 sr_z_histogram.txt/csv/png

- sr_z_histogram.txt: z_center(Å), count, density(per_Å_per_frame), conc(mol/L)
- sr_z_distribution.txt: frame_idx, sr_idx, z（每帧每颗 Sr 的 z）
- sr_z_histogram.png: 柱状图, 纵轴 mol/L, 全盒显示含真空区

### Sr²⁺ 分布数据 (100 ps 生产, 500 帧, 15 Sr/帧)

```
z(Å)    count  conc(mol/L)  含义
1.5     500    1.845         1 颗 Sr 卡在两层表面之间
7.5     1497   5.524         表面正上方 ~3 颗 Sr 堆积
10.5    314    1.159         次表层
30+     <100   <0.1          本体水
```

### 分区浓度

| 区域 | z 范围(Å) | 平均计数 | 体积(Å³) | 浓度(mol/L) |
|------|----------|---------|---------|------------|
| 近表面 | -1~16 | 8.09 | 15300 | **0.878** |
| 过渡区 | 16~30 | 4.06 | 12600 | **0.535** |
| 本体水 | 30~76 | 2.85 | 41400 | **0.114** |
| 真空 | 76~116 | 0 | - | 0 |

**表面/本体浓度比: 7.69**

### 关键发现: 一颗 Sr 卡在表面层间

sr_idx=0 在所有 500 帧中 z≈1.1-1.6 Å（在两层表面原子 z=0 和 z=3 之间）

- 距离最近表面原子 ~2.6 Å
- LJ 排斥 +2.4 kcal/mol, 静电吸引 -30.7 kcal/mol
- 净 -28.3 kcal/mol -> 深阱, 不可能热逃逸
- 初始在 z≈7.6（水分子替换位置）, 300 ps 内自行迁移进去
- **但是 Sr sigma=3.0 偏小, 这个阱可能是力场假象**

## 加速基准测试 (5137 atoms, 1000 steps)

```
1 MPI (serial):        65 steps/s -> 150K 步 = 38 min
4 MPI:                108 steps/s -> 150K 步 = 23 min
8 MPI:                159 steps/s -> 150K 步 = 16 min
1 MPI + OMP 8t:       198 steps/s -> 150K 步 = 13 min  <- 最快
4 MPI + OMP 2t:       168 steps/s -> 150K 步 = 15 min
```

OMP 用法: `mpirun -np 1 /usr/bin/lmp_mpi -sf omp -pk omp 8`

## 关键讨论结论

### 1. 真空区 40 Å

周期边界要求, 镜像屏蔽用。20 Å 也够, 但 40 Å 不额外消耗。不改。

### 2. 水不进入真空区

300 K 蒸汽压 ~0.03 atm, 蒸发概率 ~3e-7/分子, 1700 分子期望 < 1。
密闭周期盒子, 非开口蒸发实验。

### 3. 本体浓度 0.114 M vs 预期 0.25 M

**原因: 15 颗 Sr 中 8 颗被近表面吸附, 本体只剩 7 颗分布在 70% 水体积中**

- 15 总 Sr = 9（SrCl₂ 贡献）+ 6（额外平衡 -12 表面电荷）
- 1 卡在层间, 7 在近表面/过渡区, 7 在本体

**解决方案（讨论后未决）:**

- A. 拉长水层到 200-300 Å -> 本体 Sr 增多, 浓度趋近 0.25 M（推荐）
- B. `fix gcmc` 恒化学势 -> 最准确, 但需额外配置
- C. 只报浓度比 7.69, 不纠结绝对值

### 4. 10 分钟目标

- 198 steps/s -> 150K 步 = 13 min
- 进 10 min 需砍步数到 ~110K
- 建议: NVT 50000 + 生产 25000 = 75K 步 -> ~6 min
- 物理: 水 ~10 ps 弛豫, 100 ps NVT 足够; 生产 50 ps 有 250 帧够统计
- 代价: Sr 扩散仍不充分 (RMS_z ≈ 7-10 Å)

### 5. 真实蒙脱石 TOT 层

- 空间群 C2/m, ~24 原子/晶胞, 多种原子类型
- 层间距 ~6.6 Å（当前 3.0 Å）
- 同晶取代产生不均匀层电荷
- CLAYFF 力场 ~30 组参数
- 估计 1 天工作量（Montmorillonite-test 已有雏形, 用 VESTA/CIF 结构）

### 6. 离子平衡所需时间

- Sr D ≈ 1 Å²/ps
- 70 Å 水层来回 ~5 ns, 充分平衡 10-50 ns
- 当前 300 ps 只能看趋势

## 用户环境偏好

- 终端: **PowerShell**, 不是 Git Bash
- Python: **uv run python** script.py, 不是裸 python
- Docker 容器内无 Python（apt-get 需要 root 权限, 不要装）
- GPU: RTX 3050, 但当前 Docker 内无 CUDA, 5K 原子太小不值得

## 临时文件记录

- `demos/test.lmp` - 最简验证用 (5×5×5 FCC, 10 步 NVE)
- `demos/adsorption.lmp` - 教学 demo（Ar 吸附 Cu(100) 表面）
- `benchmark.ps1` / `benchmark.lmp` - 加速测试脚本，**已于 2026-08-14 删除**（结果见上文）
- `package-lock.json` - npm 空壳残留，**已于 2026-08-14 删除**

## 未完成 / 下次可继续的工作清单

按推荐顺序排列:

- [x] **P0: 路径硬编码重构 (2026-08-14)** - build_system.py / run_final.lmp / analyze_sr.py 已改相对路径, 用 `docker exec -w` 解析
- [x] **P0: OMP 加速改造 (2026-08-14)** - run_final.lmp 加 package omp 8, 命令含 -sf omp -pk omp 8; 步数削减(75K)属研究决策未动
- [~] **P0: 校正 Sr/Cl LJ 参数 (部分完成 2026-08-14)** - 已核对 JC 2008: Cl⁻(SPC/E)=ε0.1000/σ4.045 待替换; Sr²⁺ 无统一文献值(Aqvist/Mamatkulov/Merz 候选, 待定案)
- [ ] **P1: 重跑并验证** - 新参数 + OMP + 砍步数, 看趋势是否一致
- [x] **P1: 分析脚本加 Cl⁻ 分析 (2026-08-17)** - analyze_sr.py 已泛化支持 type 5, 输出 cl_z_*.txt/png
- [x] **P1: 抽取公共库 common/ (2026-08-14)** - 轨迹解析/spce参数/水取向已复用; 体系构建与 LMP 参数模板尚未完全统一
- [x] **P1: 一键化入口 (2026-08-14)** - pyproject.toml + common/entrypoints.py, 6 个命令可用
- [ ] **P2: 拉长水层到 200-300 Å** - 解决本体浓度偏差, build_system.py 改 water_thickness
- [ ] **P2: 跑 1-5 ns 过夜模拟** - 获取更接近平衡的吸附分布
- [ ] **P3: 真实蒙脱石结构** - TOT 层 + CLAYFF, 约 1 天工作量
- [ ] **P3: NPT 平衡** - 调整水层密度到正确值

## 2026-08-31 — 任务状态色觉友好改造 (WCAG 1.4.1 不仅靠颜色传信息)

**问题**：Dashboard / Jobs 两张任务表格的「状态」列原先只用一个 8px 纯色点
(sdot-4) 表示，靠 background color 区分 6 种状态。三处违规：
1. 红绿色盲下 completed(绿) / failed(红) 几乎不可分;
2. queued / canceled 都是 --text-3 灰，仅靠 opacity 0.5 区分——对色觉正常用户也难辨;
3. 表格行首再无第二信号。

**方案** (单一真相源驱动)：
- `utils.ts` `statusMeta` 扩展为 `{ label, dot, glyph, tone }`：
  queued=○ 排 / running=● 运(脉冲) / completed=✓ 完 / failed=✕ 失 /
  canceled=⊘ 消 / interrupted=◆ 断；
- `StatusChip` / `StatusBadge` 统一升级为「形状符号 + 文字 + 语义色」三通道胶囊
  (`.status-chip.tone-{accent,ok,err,info,neutral}` 着色)；
- Dashboard / Jobs 表格移除 `.sdot-4` 纯色点（与列头空格位），状态列改用
  `<StatusChip status={j.status} />`；
- 116 单测全绿；浏览器走查 Dashboard 表格与 Jobs 列表，✕失败/⊘取消/✓完成
  三个状态在灰度下也清晰可辨。

**未改**（颜色合规无需文字陪衬）：
- ThermoChart 序列自带勾选式文字图例；
- 顶栏 EnvChip、Docker 引擎/数据目录 kv 行——点旁已有"运行中"/"可用"/"未检测到挂载"等
  文字标签，颜色仅作辅助强调。

**遗留/可继续**：
- 排序/筛选胶囊（如失败 19 / 已取消 5）当前用色块+数字，已合规
- JobDetail 的 LIVE/CLOSED 状态徽章已是 点+文字，无需动

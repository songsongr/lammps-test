# 工作日志

> 本文件记录项目历史会话状态、运行结果、讨论结论与待办清单，随会话频繁更新。
> 环境、工作流、参数等**稳定信息**请见 [docs 目录](README.md) 其他文档。

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

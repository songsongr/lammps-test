# LAMMPS 模拟工作流与输入文件规范

## 体系配置层（system as data — 2026-08-28 起）

每个研究项目的**体系参数单一真相源**是项目目录下的 `system.json`（几何/组成/力场，
力场参数带 `source` + `confidence` 标注）。三个消费端都从它读取：

```
system.json ──► 构建引擎 (common/builders) ──► system.data + build_report.json
       └──────► 方法模板渲染 (jinja2, 9 板块) ──► run.lmp (pair_coeff 单一真相)
       └──────► workbench「体系配置」页 (结构化查看/编辑/重建/渲染)
```

- 构建：`uv run python -m common.build <project_dir>` 或 CLI `uv run build-sr` / `uv run build-mmt`
- 渲染：workbench「重新渲染脚本」按钮；生成物首行带 `# [generated]` 标记，
  手改后再次渲染会检测并要求确认（`rendered_sha` 记录于 project.json）
- 修改体系参数 → 改 system.json（UI 表单或直接改文件）→ 重建 → 重渲染 → 运行

## 标准模拟流程

每个模拟项目遵循以下 7 步工作流：

1. **生成体系** — 体系配置 (system.json) 经构建引擎产出 `system.data`（原子坐标、键、角、电荷）
2. **读入 & 分组** — `read_data` + `group` 分组
3. **力场设置** — `pair_style`、`kspace_style`、`bond_style`、`angle_style`
4. **能量最小化** — `min_style cg`、`minimize`
5. **NVT 平衡** — `velocity create`、`fix nvt`、`run`
6. **生产模拟** — `dump`、`run`
7. **分析** — `compute`、`dump` 输出离子分布（如 Sr²⁺ z 分布、MSD、RDF）

## 输入文件写作规范

所有 `.lmp` 文件遵循统一格式（生成类脚本由方法模板按此规范渲染，如
`workbench/backend/templates/methods/nvt_production/run.lmp.j2`）：

1. **顶部注释块** — 模拟目标、体系、力场概览；渲染产物首行带 `# [generated]` 标记
2. **分板块** — 用 `# ====...====` 分隔线 + `# 第 N 部分: ...` 标题
3. **每行注释** — 命令后跟注释，解释参数含义、单位、选择原因；
   力场行标注参数 `source` / `confidence`
4. **ASCII only** — `print` 语句只用英文/数字
5. **对齐** — 命令和参数用空格对齐

### 板块划分标准

```
第 1 部分: 全局设置      (units, atom_style, boundary)
第 2 部分: 读入数据      (read_data)
第 3 部分: 分组          (group, fix setforce)
第 4 部分: 非键力场      (pair_style, kspace_style, pair_coeff)
第 5 部分: 分子内力场    (bond_style, angle_style, special_bonds)
第 6 部分: 控制参数      (neighbor, thermo_modify, thermo)
第 7 部分: 能量最小化    (min_style, minimize)
第 8 部分: NVT 平衡      (velocity, fix nvt, timestep, run)
第 9 部分: 生产模拟      (dump, run)
```

## 输入检查（lint，2026-08-28 起）

发起 LAMMPS 任务前自动静态检查（`common/lammps_lint.py`，CLI 与工作台同源）：

- **errors（阻止发车）**：缺 units / pair_style / run-minimize；占位符残留（replace-with/TODO 等）；
  read_data/include/read_restart 引用文件在项目目录中不存在
- **warnings（放行提示）**：`run 0`（仅评估 thermo）；`/data/` 旧挂载绝对路径（2026-08-28 起已废弃，改用相对路径）
- 渲染 run.lmp 后同样跑 lint 兜底（模板异常防御）

## 各项目脚本索引

| 项目 | 体系配置 | 体系构建 | 模拟脚本 | 分析脚本 |
|------|----------|----------|----------|----------|
| Sr 吸附（strontium_adsorption） | `system.json` | `uv run build-sr`（builders/surface_adsorption） | `run.lmp`（模板渲染产物；历史手写版归档于 archive/） | `analyze_sr.py` |
| 蒙脱石（Montmorillonite-test） | `system.json` | `uv run build-mmt`（builders/clay_cif） | `01_run.lmp`（手写两段弛豫，力场数值已与 system.json 核对） | `post_process.py` |
| 教学 demo（demos） | —（自包含脚本） | — | `adsorption.lmp`、`test.lmp` | — |
| 用户项目（projects/） | 向导生成 `system.json` | `python -m common.build projects/<id>` | `run.lmp`（渲染产物） | — |

## 手动创建项目（文件系统直建）

向导之外，任意体系都可以直接在 `projects/` 下建目录、写文件 — 平台按约定自动发现（实时扫描，零重启）：

```
projects/my-tensile/
├─ project.json     必需·项目身份（最小 3 字段；缺失时非空目录按目录名兜底注册，卡片带「未注册」角标）
├─ run.lmp          顶层 *.lmp → LAMMPS 任务；*.py → Python 分析任务（扩展名判型）
├─ system.json      可选·体系配置真相源（启用体系配置页/重建/渲染；纯脚本项目可省）
├─ system.data      可选·构建产物（uv run python -m common.build projects/my-tensile）
└─ ff.field         脚本 include/read_data 引用的同目录依赖（任务发起时自动闭包暂存）
```

- `project.json` 最小模板：`{"id": "my-tensile", "name": "显示名", "description": "一句话"}`（id 必须与目录名一致）
- 任务产物在 `lammps-data-docker/jobs/<任务id>/`；Python 分析输出到脚本同目录
- 工作台「项目与脚本」页右上「手动创建指南」抽屉与本节同源，界面内可查
- CLI 与工作台同契约（common.runner），但「任务记录」仅收录工作台发起的任务

## 路径约定（IMPORTANT）

- **LAMMPS 任务一律走暂存-运行-回收**（2026-08-28 起）：任务工作区 =
  `lammps-data-docker/jobs/<任务id>/`（= 容器 `/data/jobs/<任务id>/`），
  脚本与依赖（`include`/`read_data` 引用闭包 + 顶层 `*.data`）自动拷入，
  容器内 `-w /data/jobs/<任务id>` 运行。执行契约统一在 `common/runner.py`
  （CLI 与 workbench 同源），**不要**手写 `docker exec -w /data/<项目>`（旧约定已失效）
- Python 脚本输出到**脚本自身目录**（`os.path.dirname(os.path.abspath(__file__))`），容器内/Windows 本地行为一致
- 旧版运行命令（若有留存于历史文档/注释）一律以本文件为准

---
name: lammps-diagnose
description: 诊断 LAMMPS 控制中心工作台的任务 — 读取任务记录、发车 lint、失败案例库解析、检查点与日志尾部, 输出结构化 JSON 供 agent 直接消费。当用户问"任务为什么失败/任务状态/帮我修 run.lmp/分析这个任务"时使用。
---

# LAMMPS 任务诊断

对 lammps-test 工作台的任务做离线诊断 (不依赖工作台进程, 直接读 SQLite 任务库与日志文件)。

## 使用

```bash
# 结构化诊断 (agent 消费): 任务记录 + lint + 失败解析 + 检查点 + 日志尾
uv run python -m workbench.backend.app.diagnose --job <任务id> --json

# 最近一个任务
uv run python -m workbench.backend.app.diagnose --last --json

# 人类可读
uv run python -m workbench.backend.app.diagnose --job <任务id>
```

## 输出字段

- `status/exit_code/source`: 状态与来源 (workbench | cli)
- `lint`: {errors (阻止发车), warnings} — errors 需要在项目目录修复
- `failure`: {summary, error_line, severity, actions, can_resume} — 案例库命中
- `checkpoints`: 工作区 .restart 列表 (存在则可续跑: POST /api/jobs/<id>/resume 或 read_restart)
- `fingerprint`: {system_sha, image, lmp_version} — 结果可比性
- `log_tail`: 日志最后 40 行

## 修复流程

1. 读 lint.errors 与 failure.actions 定位问题
2. 修改项目目录下的脚本/参数 (力场真相源 = system.json, 勿改渲染产物数值)
3. 重新发起任务 (工作台 UI / POST /api/jobs), 或有 checkpoints 时走续跑

## 注意

- "Never silently invent": 不猜力场参数; system.json 是唯一真相源
- CLI 来源 (source=cli) 的运行中任务不可从工作台取消 (终端 Ctrl+C)

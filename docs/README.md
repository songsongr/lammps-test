# 项目文档索引

本目录存放项目的详细文档。根目录 `AGENTS.md` 是 AI 代理规范指引（人类入口亦从这里开始），本文档是完整信息的入口。

## 文档列表

| 文档 | 内容 |
|------|------|
| [environment.md](environment.md) | 环境与工具链：Docker 容器（挂载/暂存约定）、uv/Python、workbench、VMD、远程 SSH |
| [workflows.md](workflows.md) | 体系配置层 (system.json)、标准工作流、`.lmp` 写作规范、手动创建项目、路径约定 |
| [parameters.md](parameters.md) | 力场与参数体系（数值真相源 = 各项目 system.json，本文为人工可读对照） |
| [roadmap.md](roadmap.md) | 未来优化路线图 (已落地/开放/不再追) |
| [work-log.md](work-log.md) | 工作日志（会话记录、运行结果、讨论结论、待办清单） |

## 平台与架构

- [workbench/README.md](../workbench/README.md) — 控制中心工作台（FastAPI + React：任务编排/实时日志/thermo 曲线/体系配置/新建向导）
- [ARCHITECTURE.md](../ARCHITECTURE.md) — 当前架构总览（双空间设计：人-agent 交互 + 前后端）

## 各子项目 README

- [systems/strontium_adsorption/README.md](../systems/strontium_adsorption/README.md) — 带电表面 + 水 + SrCl₂ 吸附
- [systems/Montmorillonite-test/README.md](../systems/Montmorillonite-test/README.md) — 蒙脱石层间水 / Ca²⁺ 动力学（CLAYFF）
- [manual_md/README.md](../manual_md/README.md) — LAMMPS 官方手册转 Markdown 图谱索引

## 阅读顺序建议

1. **新会话**：先读 `work-log.md` → 了解项目当前状态与待办
2. **环境配置**：`environment.md` → 工作台启动见 `workbench/README.md`
3. **建体系/写脚本**：`workflows.md`（体系配置层 + 写作规范）+ `parameters.md`（力场参数）
4. **具体体系**：对应子项目 README

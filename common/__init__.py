"""
公共库 (common/): 体系构建引擎 + 共享模拟工具 — CLI 与 workbench 同源使用。

体系配置层:
- system_config: system.json 模型/校验/水模型预设/向导 schema (体系参数单一真相源)
- builders/: 体系构建器 (surface_adsorption / solution / clay_cif) → system.data
- build: python -m common.build <dir> 构建入口
- runner: 暂存-运行-回收统一执行契约 (staging/命令/CLI), workbench job_manager 同源

共享模拟工具:
- spce_params: SPC/E 水模型常量 (数值源: system_config 预设)
- traj_parser: LAMMPS 轨迹 (.lammpstrj) 通用解析器
- water_builder: SPC/E 水分子构建与随机取向
- rdf: 向量化径向分布函数
- entrypoints: 一键 CLI (build-sr/run-sr-sim/...)
"""

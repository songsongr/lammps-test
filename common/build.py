"""体系构建入口: python -m common.build <project_dir>

读取 <project_dir>/system.json → 构建 → 写 system.data + build_report.json。
工作台以 kind=build 任务运行本入口 (uv run python -m common.build <dir>)。
"""
import json
import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("用法: python -m common.build <project_dir>", file=sys.stderr)
        return 2
    project_dir = args[0]

    from .builders import base

    try:
        report = base.run_build(project_dir)
    except ValueError as e:
        print(f"[build] 校验失败:\n{e}", file=sys.stderr)
        return 1
    except FileNotFoundError as e:
        print(f"[build] 找不到体系配置: {e}", file=sys.stderr)
        return 1

    print(f"[build] profile: {report['profile']}")
    print(f"[build] 总原子: {report['n_atoms']} (类型分布 {report['type_counts']})")
    print(f"[build] 水分子: {report['n_angles']}, 键: {report['n_bonds']}, 角: {report['n_angles']}")
    print(f"[build] 总电荷: {report['total_charge']} (应为 0)")
    for w in report["warnings"]:
        print(f"[build] 警告: {w}")
    print(f"[build] 完成: {project_dir}/system.data (报告 build_report.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

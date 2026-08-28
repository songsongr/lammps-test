"""一键化 CLI 入口 — 与 workbench 共用同一执行契约 (common.build / common.runner)。

可用命令:
  build-sr        构建 SrCl₂ 表面吸附体系 (system.json → system.data + build_report.json)
  run-sr-sim      暂存-运行-回收 运行 run.lmp (容器 lammpsd, 渲染产物)
  analyze-sr      Sr²⁺/Cl⁻ z 分布分析 (读 system.json 体系参数)
  build-mmt       构建蒙脱石层间水体系 (CIF → CLAYFF → system.data)
  run-mmt-sim     运行 01_run.lmp (手写两段弛豫脚本)
  postprocess-mmt MSD/RDF 后处理 (输出到脚本同目录)
  workbench       控制中心服务 (独立入口: uv run workbench)

注意: 旧挂载约定 (/data = 项目根) 已于 2026-08-28 废弃; 本模块所有容器命令
均走 common.runner 的 jobs/<id> 工作区契约。
"""
import argparse
import os
import subprocess
import sys

from . import build as _build_mod
from . import runner

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = "systems/strontium_adsorption"
MMT = "systems/Montmorillonite-test"


def _run_py(rel_path: str) -> None:
    """以脚本所在目录为工作目录运行项目内 Python 脚本。"""
    script = os.path.join(ROOT, rel_path)
    subprocess.run([sys.executable, script], check=True, cwd=os.path.dirname(script))


def build_sr() -> None:
    sys.exit(_build_mod.main([SR]))


def build_mmt() -> None:
    sys.exit(_build_mod.main([MMT]))


def run_sr_sim() -> None:
    sys.exit(runner.run_cli(SR, "run.lmp"))


def run_mmt_sim() -> None:
    sys.exit(runner.run_cli(MMT, "01_run.lmp"))


def analyze_sr() -> None:
    _run_py("systems/strontium_adsorption/analyze_sr.py")


def postprocess_mmt() -> None:
    _run_py("systems/Montmorillonite-test/post_process.py")


_COMMANDS = {
    "build-sr": build_sr,
    "run-sr-sim": run_sr_sim,
    "analyze-sr": analyze_sr,
    "build-mmt": build_mmt,
    "run-mmt-sim": run_mmt_sim,
    "postprocess-mmt": postprocess_mmt,
}


def main(argv=None):
    parser = argparse.ArgumentParser(prog="lammps-test", description=__doc__)
    parser.add_argument("command", choices=list(_COMMANDS), help="要执行的命令")
    args = parser.parse_args(argv)
    _COMMANDS[args.command]()


if __name__ == "__main__":
    main()

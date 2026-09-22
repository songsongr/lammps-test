"""任务诊断 CLI (桥②: ZCode skill 数据源) — 离线读任务库, 不依赖工作台进程。

用法:
    python -m workbench.backend.app.diagnose --job <id>          # 人类可读
    python -m workbench.backend.app.diagnose --job <id> --json   # 结构化 (agent 消费)
    python -m workbench.backend.app.diagnose --last [--json]     # 最近一个任务

输出: 任务记录 + 发车 lint + 失败解析 (案例库) + 检查点列表 + 环境指纹。
"""
from __future__ import annotations

import argparse
import json
import os
import sys


def _diagnose(job_id: str) -> dict:
    from . import store
    from .config import ROOT
    from .failure import analyze_failure

    store.init()
    job = store.get(job_id)
    if job is None:
        raise SystemExit(f"任务不存在: {job_id}")

    out: dict = {k: job.get(k) for k in
                 ("id", "project_id", "project_name", "script", "kind", "status",
                  "exit_code", "workspace", "source", "batch", "fingerprint")}
    if job.get("fingerprint"):
        try:
            out["fingerprint"] = json.loads(job["fingerprint"])
        except Exception:
            pass

    log_text = ""
    if job.get("log_path") and os.path.isfile(job["log_path"]):
        with open(job["log_path"], encoding="utf-8", errors="replace") as f:
            log_text = f.read()
        out["log_tail"] = log_text.splitlines()[-40:]

    if job["kind"] == "lmp":
        # 项目目录: 通过 project.json 注册表解析 (纯扫描)
        try:
            from .config import get_projects
            proj = next((p for p in get_projects() if p["id"] == job["project_id"]), None)
            if proj:
                pdir = os.path.join(ROOT, proj["dir"])
                out["project_dir"] = pdir
                script_path = os.path.join(pdir, job["script"])
                if os.path.isfile(script_path):
                    from common.lammps_lint import lint_lammps_input
                    with open(script_path, encoding="utf-8", errors="replace") as f:
                        out["lint"] = lint_lammps_input(f.read(), pdir)
        except Exception as e:  # 注册表不可读等 — 诊断不应因此中断
            out["lint_error"] = str(e)

    if job["status"] == "failed" and log_text:
        out["failure"] = analyze_failure(job["kind"], job.get("exit_code"), log_text)

    if job.get("workspace") and os.path.isdir(job["workspace"]):
        out["checkpoints"] = [n for n in sorted(os.listdir(job["workspace"]))
                              if n.endswith(".restart")]

    out["resume_hint"] = (
        "POST /api/jobs/<id>/resume (需工作台运行) 或参照 checkpoints 用 read_restart 续跑"
        if out.get("checkpoints") else None)
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="diagnose", description=__doc__)
    parser.add_argument("--job", help="任务 id")
    parser.add_argument("--last", action="store_true", help="取最近一个任务")
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON")
    args = parser.parse_args(argv)

    if not args.job and not args.last:
        parser.error("需要 --job <id> 或 --last")
    if args.last:
        from . import store
        store.init()
        jobs = store.list_jobs(limit=1)
        if not jobs:
            raise SystemExit("任务库为空")
        job_id = jobs[0]["id"]
    else:
        job_id = args.job

    result = _diagnose(job_id)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
        return 0

    # 人类可读
    print(f"任务 {result['id']} · {result['project_name']} · {result['kind']} · {result['status']}"
          + (f" (退出码 {result['exit_code']})" if result.get("exit_code") is not None else ""))
    print(f"来源: {result.get('source')} | 脚本: {result['script']}")
    if result.get("fingerprint"):
        print(f"指纹: {json.dumps(result['fingerprint'], ensure_ascii=False)}")
    lint = result.get("lint")
    if lint:
        for e in lint["errors"]:
            print(f"  [lint·error] {e}")
        for w in lint["warnings"]:
            print(f"  [lint·warn] {w}")
    f = result.get("failure")
    if f:
        print(f"失败解析: {f['summary']} | 风险 {f.get('severity')} | 续跑 {'有' if f.get('can_resume') else '无'}")
        if f.get("error_line"):
            print(f"  错误行: {f['error_line']}")
        for i, a in enumerate(f.get("actions") or [], 1):
            print(f"  动作 {i}: {a}")
    if result.get("checkpoints"):
        print(f"检查点: {', '.join(result['checkpoints'])}")
    for e in result.get("log_tail", [])[-10:]:
        print(f"  | {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

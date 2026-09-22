"""失败任务的简要解析: 从日志提取错误行并给出结构化中文解析建议。

纯函数, 输入 (kind, exit_code, 日志文本), 输出结构化解析或 None。
规则库外置于 failure_rules.json (策展案例库: 错误签名 → 原因 → severity/actions/can_resume),
每次分析时加载 — 编辑规则文件即时生效, 无需重启。
借鉴 ANL LAMMPS-Agents 的案例库思想与 chatmaterials/lammps-workflows 的结构化恢复记录,
用确定性数据替代 LLM 模糊召回。
"""
import json
import os
import re

_RULES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "failure_rules.json")


def _load_rules() -> dict:
    with open(_RULES_PATH, encoding="utf-8") as f:
        return json.load(f)


def analyze_failure(kind: str, exit_code: int | None, log_text: str) -> dict | None:
    rules = _load_rules()
    lines = log_text.splitlines()

    def _out(summary: str, error_line: str | None, detail_line: str | None,
             hint: str, severity: str = "medium", can_resume: bool = False,
             actions: list[str] | None = None) -> dict:
        return {"summary": summary, "error_line": error_line, "detail_line": detail_line,
                "hint": hint, "severity": severity,
                "actions": actions or ["查看完整日志定位问题"],
                "can_resume": can_resume}

    def _match(rule_list: list[dict], text: str) -> dict | None:
        for rule in rule_list:
            try:
                m = re.search(rule["signature"], text)
            except re.error:  # 策展正则写坏 → 跳过该条而不是 500
                continue
            if m:
                return {"rule": rule, "groups": m.groups()}
        return None

    # 工作台自身的启动失败 (docker/uv 缺失等)
    for line in reversed(lines):
        if "[workbench] 进程启动失败" in line:
            return _out("进程未能启动", line.strip(), None,
                        "通常是 Docker 容器未运行、uv 不可用或暂存阶段失败; 见错误详情与仪表盘环境状态。",
                        severity="low",
                        actions=["检查仪表盘 Docker/容器状态", "确认 lammpsd 容器已启动"])

    if kind == "lmp":
        err_idx = next(
            (i for i in range(len(lines) - 1, -1, -1) if lines[i].startswith("ERROR:")), None)
        if err_idx is not None:
            error_line = lines[err_idx].strip()
            detail_line = next(
                (l.strip() for l in lines[err_idx + 1:] if l.startswith("Last command:")), None)
            hit = _match(rules["lmp_rules"], error_line)
            if hit:
                rule = hit["rule"]
                return _out("LAMMPS 输入脚本运行报错", error_line, detail_line,
                            rule["hint"].format(*hit["groups"]),
                            severity=rule["severity"], can_resume=rule["can_resume"],
                            actions=[a.format(*hit["groups"]) for a in rule["actions"]])
            return _out("LAMMPS 输入脚本运行报错", error_line, detail_line,
                        "LAMMPS 运行报错; 可用下方错误行在 manual_md/ 手册库中检索对应章节。",
                        actions=["在 manual_md/ 手册库检索错误关键词"])
        if exit_code == 137:
            return _out("进程被 SIGKILL 强制终止 (exit 137)", None, None,
                        "常见于内存不足触发 OOM、手动 kill 或取消流程; 结合运行时长与体系规模判断。",
                        severity="medium",
                        actions=["减小体系规模或 OMP 线程数", "若为手动取消可忽略"])
        if exit_code == 139:
            return _out("段错误 (SIGSEGV, exit 139)", None, None,
                        "LAMMPS 或势文件的非预期崩溃; 尝试复现并检查最近的脚本/参数改动。",
                        severity="high",
                        actions=["回查最近的脚本/参数改动", "用最小体系复现定位"])
        last = lines[-1].strip() if lines else ""
        return _out(f"进程以退出码 {exit_code} 结束", last or None, None,
                    "日志中未见 LAMMPS ERROR 行; 检查脚本是否提前退出或存在空 run。")

    # python
    tb_idx = next((i for i in range(len(lines) - 1, -1, -1)
                   if "Traceback (most recent call last)" in lines[i]), None)
    if tb_idx is not None:
        # 过滤工作台尾行 ([workbench] ...), 否则真实异常行被吞掉、规则匹配落空
        block = [l for l in lines[tb_idx:]
                 if l.strip() and not l.startswith("[workbench]")]
        error_line = block[-1].strip() if block else ""
        hit = _match(rules["python_rules"], error_line)
        if hit:
            rule = hit["rule"]
            return _out("Python 脚本异常退出", error_line, None,
                        rule["hint"].format(*hit["groups"]),
                        severity=rule["severity"], can_resume=rule["can_resume"],
                        actions=[a.format(*hit["groups"]) for a in rule["actions"]])
        return _out("Python 异常退出", error_line, None,
                    "Python 异常退出; 按下方错误行定位脚本位置。")

    return _out(f"进程以退出码 {exit_code} 结束",
                lines[-1].strip() if lines else None, None,
                "未见常见错误特征; 可查看完整日志定位。")

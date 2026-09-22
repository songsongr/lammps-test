"""单任务溯源包 (AiiDA 轻量思想, roadmap #6): 任务记录 + 指纹 + 脚本 + 体系快照 → zip。

设计原则:
- 追求「可邮寄的最小可复现快照」: 排除轨迹/检查点等大体积可再生文件;
- 纯函数 (输入 job 记录 + 项目目录路径 + 日志文本, 输出 zip bytes), 可直接单测;
- 内容缺失 (无 system.json / 无日志) 时静默跳过对应条目, 不让导出失败。
"""
from __future__ import annotations

import io
import json
import os
import zipfile
from datetime import datetime

# 单文件入包上限 (bytes); 超过则跳过并在 README 记录
_MAX_FILE_BYTES = 32 * 1024 * 1024
# 永不入包的产物 (体积大且可由脚本再生)
_SKIP_EXTS = (".lammpstrj", ".dump", ".restart", ".xlsx", ".png", ".jpg", ".zip", ".gz")

_INTERNAL_KEYS = ("_log_path",)


def _read_if_small(path: str) -> str | None:
    try:
        if os.path.getsize(path) > _MAX_FILE_BYTES:
            return None
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def build_provenance_zip(job: dict, project_dir: str | None,
                         log_text: str | None) -> tuple[bytes, list[str]]:
    """构建溯源包。返回 (zip bytes, skipped 条目说明列表)。

    包内条目:
      README.txt        — 包清单 + 复现指引
      job.json          — 任务记录 (去除内部字段)
      fingerprint.json  — 环境/体系指纹 (system sha + 镜像 + LAMMPS 版本)
      script            — 运行脚本 (工作区快照优先, 项目目录兜底)
      system.json       — 体系参数真相源 (项目目录有才入包)
      system.data       — 构建产物 (项目目录有才入包)
      log_tail.txt      — 运行日志尾部 (最多 ~400 行, 调用方截好)
    """
    skipped: list[str] = []
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        job_public = {k: v for k, v in job.items() if k not in _INTERNAL_KEYS}
        fingerprint = None
        if job_public.get("fingerprint"):
            try:
                fingerprint = json.loads(job_public["fingerprint"])
            except (TypeError, ValueError):
                fingerprint = {"raw": str(job_public["fingerprint"])}

        # ---- 先收集脚本, 供 README 复现指引引用 (工作区快照优先, 项目目录兜底) ----
        script = job.get("script") or ""
        script_text = None
        if script:
            for base in (job.get("workspace"), project_dir):
                if not base:
                    continue
                text = _read_if_small(os.path.join(base, script))
                if text is not None:
                    script_text = text
                    break
            if script_text is None:
                skipped.append(f"script {script} (工作区/项目目录均不可读)")

        # ---- README (清单 + 复现指引) ----
        lines = [
            "LAMMPS 工作台 — 单任务溯源包",
            f"导出时间: {datetime.now().isoformat(timespec='seconds')}",
            "",
            f"任务 id   : {job.get('id')}",
            f"项目      : {job.get('project_id')} ({job.get('project_name', '')})",
            f"脚本      : {script or '-'}",
            f"类型      : {job.get('kind')}  状态: {job.get('status')}  退出码: {job.get('exit_code')}",
            f"创建时间  : {job.get('created_at')}  结束: {job.get('finished_at')}",
            f"OMP 线程  : {job.get('omp_threads')}",
            "",
            "包内容: job.json (任务记录) / fingerprint.json (环境指纹) /",
            "        脚本副本 / system.json (体系参数真相源) / system.data / log_tail.txt",
            "",
            "复现指引 (本地 Docker 后端):",
            f"  docker exec -w <工作区> lammpsd /usr/bin/lmp_mpi -sf omp -pk omp "
            f"{job.get('omp_threads', 8)} -in {script or '<script>'}",
            "  体系参数修改请改 system.json 后经工作台「重建体系」+「重新渲染」再生脚本。",
            "  轨迹/检查点等大体积可再生文件未入包。",
        ]
        if skipped:
            lines += ["", "未入包条目: " + "; ".join(skipped)]
        zf.writestr("README.txt", "\n".join(lines) + "\n")
        zf.writestr("job.json", json.dumps(job_public, ensure_ascii=False, indent=2) + "\n")
        if fingerprint is not None:
            zf.writestr("fingerprint.json",
                        json.dumps(fingerprint, ensure_ascii=False, indent=2) + "\n")
        if script_text is not None:
            zf.writestr(script, script_text)

        # ---- 体系快照 (项目目录) ----
        if project_dir:
            for name in ("system.json", "system.data"):
                text = _read_if_small(os.path.join(project_dir, name))
                if text is not None:
                    zf.writestr(name, text)
                else:
                    skipped.append(f"{name} (缺失或超限)")
        else:
            skipped.append("system.json/system.data (项目目录不可用)")
        if log_text:
            zf.writestr("log_tail.txt", log_text)
    return buf.getvalue(), skipped

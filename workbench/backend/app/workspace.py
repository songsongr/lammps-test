"""任务工作区生命周期: 过期清理 (后台 sweeper)。

清理规则:
- DB 中终态任务且 finished_at 超过保留期 → 删除其工作区
- 目录存在但 DB 无记录 (孤儿, 如手动删除过 DB) 且 mtime 超过 1 天 → 删除
- running 任务永不清理
"""
import asyncio
import logging
import os
import shutil
import time
from datetime import datetime

from . import store
from .config import LAMMPS_DATA_HOST_DIR, WORKSPACE_RETENTION_DAYS

log = logging.getLogger("workbench.workspace")

_INTERVAL_SECONDS = 6 * 3600
_ORPHAN_GRACE_SECONDS = 86400


def _parse_ts(iso: str | None) -> float | None:
    if not iso:
        return None
    try:
        return datetime.fromisoformat(iso).timestamp()
    except ValueError:
        return None


async def cleanup_once() -> int:
    """执行一轮清理, 返回删除的目录数。"""
    if WORKSPACE_RETENTION_DAYS <= 0:
        return 0
    jobs_root = os.path.join(LAMMPS_DATA_HOST_DIR, "jobs")
    if not os.path.isdir(jobs_root):
        return 0

    known: dict[str, dict] = {}
    for job in store.list_jobs(limit=5000):
        if job.get("workspace"):
            known[os.path.normcase(job["workspace"])] = job

    now = time.time()
    deadline = now - WORKSPACE_RETENTION_DAYS * 86400
    removed = 0
    for name in os.listdir(jobs_root):
        path = os.path.join(jobs_root, name)
        if not os.path.isdir(path):
            continue
        job = known.get(os.path.normcase(path))
        if job is not None:
            finished_ts = _parse_ts(job.get("finished_at"))
            if job["status"] != "running" and finished_ts is not None and finished_ts < deadline:
                shutil.rmtree(path, ignore_errors=True)
                removed += 1
        elif os.path.getmtime(path) < now - _ORPHAN_GRACE_SECONDS:
            shutil.rmtree(path, ignore_errors=True)
            removed += 1
    if removed:
        log.info("工作区清理: 删除 %d 个目录 (保留期 %d 天)", removed, WORKSPACE_RETENTION_DAYS)
    return removed


async def start_sweeper() -> None:
    async def _loop() -> None:
        while True:
            try:
                await cleanup_once()
            except Exception:
                log.exception("工作区清理失败")
            await asyncio.sleep(_INTERVAL_SECONDS)

    asyncio.create_task(_loop())

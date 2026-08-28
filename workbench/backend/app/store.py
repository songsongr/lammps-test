"""任务持久化: SQLite (stdlib sqlite3), 单表 jobs。

工作台 v0 不引入 ORM; 任务记录字段少、写入频率低, 直接 SQL 足够。
"""
import os
import sqlite3
import threading
from typing import Any, Optional

from .config import DB_PATH, JOBS_LOG_DIR

_lock = threading.Lock()

_SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id          TEXT PRIMARY KEY,
    project_id  TEXT NOT NULL,
    project_name TEXT NOT NULL,
    script      TEXT NOT NULL,
    kind        TEXT NOT NULL,
    command     TEXT NOT NULL,
    status      TEXT NOT NULL,
    exit_code   INTEGER,
    created_at  TEXT,
    started_at  TEXT,
    finished_at TEXT,
    log_path    TEXT,
    workspace   TEXT
)
"""

_JOB_COLS = ("id, project_id, project_name, script, kind, command, status, exit_code,"
             " created_at, started_at, finished_at, log_path, workspace, omp_threads, fingerprint,"
             " source")


def init() -> None:
    os.makedirs(JOBS_LOG_DIR, exist_ok=True)
    with _conn() as conn:
        conn.execute(_SCHEMA)
        # 轻量迁移: 旧库补列
        cols = [r[1] for r in conn.execute("PRAGMA table_info(jobs)")]
        if "omp_threads" not in cols:
            conn.execute("ALTER TABLE jobs ADD COLUMN omp_threads INTEGER DEFAULT 8")
        if "fingerprint" not in cols:
            conn.execute("ALTER TABLE jobs ADD COLUMN fingerprint TEXT")
        if "source" not in cols:
            conn.execute("ALTER TABLE jobs ADD COLUMN source TEXT DEFAULT 'workbench'")


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def insert(job: dict[str, Any]) -> None:
    job = {**job, "fingerprint": job.get("fingerprint"),
           "source": job.get("source", "workbench")}  # 旧调用缺列时补默认
    with _lock, _conn() as conn:
        conn.execute(
            f"INSERT INTO jobs ({_JOB_COLS}) VALUES (:id, :project_id, :project_name,"
            " :script, :kind, :command, :status, :exit_code, :created_at, :started_at,"
            " :finished_at, :log_path, :workspace, :omp_threads, :fingerprint, :source)",
            job,
        )


def update(job_id: str, **fields: Any) -> None:
    if not fields:
        return
    cols = ", ".join(f"{k} = :{k}" for k in fields)
    with _lock, _conn() as conn:
        conn.execute(f"UPDATE jobs SET {cols} WHERE id = :id", {**fields, "id": job_id})


def get(job_id: str) -> Optional[dict[str, Any]]:
    with _conn() as conn:
        row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
    return dict(row) if row else None


def list_jobs(limit: int = 200) -> list[dict[str, Any]]:
    with _conn() as conn:
        rows = conn.execute(
            "SELECT * FROM jobs ORDER BY created_at DESC, id DESC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(r) for r in rows]


def counts() -> dict[str, int]:
    with _conn() as conn:
        rows = conn.execute("SELECT status, COUNT(*) AS n FROM jobs GROUP BY status").fetchall()
    out = {r["status"]: r["n"] for r in rows}
    out["total"] = sum(out.values())
    return out


def delete(job_id: str) -> bool:
    with _lock, _conn() as conn:
        cur = conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    return cur.rowcount > 0

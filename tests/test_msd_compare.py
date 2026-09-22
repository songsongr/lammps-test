"""多任务 MSD 对比只读取分析缓存，并保留各任务不可用原因。"""
import asyncio
import json

import pytest
from fastapi import HTTPException

from workbench.backend.app.routers import jobs


def test_compare_msd_cached_and_missing(monkeypatch, tmp_path):
    ready = tmp_path / "ready"
    ready.mkdir()
    (ready / "analysis_cache.json").write_text(json.dumps({
        "msd": [{"type": "all", "points": [{"step": 100, "value": 2.5}],
                 "diffusion": {"slope_a2_per_step": 0.025, "r2": 1.0}}],
        "frames_3d": {"first": ["large payload"]},
    }), encoding="utf-8")
    idle = tmp_path / "idle"
    idle.mkdir()
    (idle / "dump.lammpstrj").write_text("ITEM: TIMESTEP\n", encoding="utf-8")
    empty = tmp_path / "empty"
    empty.mkdir()
    data = {
        "a": {"id": "a", "kind": "lmp", "script": "run.lmp", "project_name": "A", "workspace": str(ready)},
        "b": {"id": "b", "kind": "lmp", "script": "run.lmp", "project_name": "B", "workspace": str(idle)},
        "c": {"id": "c", "kind": "lmp", "script": "run.lmp", "project_name": "C", "workspace": str(empty)},
    }
    monkeypatch.setattr(jobs, "get", data.get)
    jobs._analysis_state.clear()
    result = asyncio.run(jobs.compare_msd("a,b,c,gone,a"))["series"]
    assert [entry["id"] for entry in result] == ["a", "b", "c", "gone"]
    assert result[0]["status"] == "done"
    assert result[0]["msd"]["points"] == [{"step": 100, "value": 2.5}]
    assert "frames_3d" not in result[0]
    assert [entry["status"] for entry in result[1:]] == ["idle", "none", "missing"]
    assert result[2]["note"] == "工作区无轨迹文件"


def test_compare_msd_rejects_single_job():
    with pytest.raises(HTTPException) as exc:
        asyncio.run(jobs.compare_msd("only"))
    assert exc.value.status_code == 400

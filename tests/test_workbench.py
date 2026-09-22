"""collect_deps / thermo / 失败解析 / 体系配置 / 构建器 / 模板渲染 单元测试。"""
import os
import random
import textwrap

import pytest

from common import system_config
from common.builders import base as builder_base
from common.builders import solution
from workbench.backend.app.failure import analyze_failure
from workbench.backend.app.job_manager import collect_deps
from workbench.backend.app.thermo import ThermoBuffer
from workbench.backend.app.template_render import render_run_lmp


@pytest.fixture
def project_dir(tmp_path):
    d = tmp_path / "proj"
    d.mkdir()
    return d


def _write(d, name, content):
    p = d / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(textwrap.dedent(content), encoding="utf-8")
    return name


class TestCollectDeps:
    def test_read_data_direct(self, project_dir):
        _write(project_dir, "in.run", "read_data system.data\nrun 100\n")
        _write(project_dir, "system.data", "_atoms\n")
        present, missing = collect_deps("in.run", str(project_dir))
        assert present == ["system.data"]
        assert missing == []

    def test_include_chain_transitive(self, project_dir):
        _write(project_dir, "in.main", "include in.mod\n")
        _write(project_dir, "in.mod", "# 注释里的 include fake.data 不应生效\n"
                                      "read_data a.data\ninclude ff.field\n")
        _write(project_dir, "a.data", "atoms\n")
        _write(project_dir, "ff.field", "pair_style lj/cut 2.5\n")
        present, missing = collect_deps("in.main", str(project_dir))
        assert sorted(present) == ["a.data", "ff.field", "in.mod"]
        assert missing == []

    def test_missing_reported(self, project_dir):
        _write(project_dir, "in.run", "read_data nope.data\n")
        present, missing = collect_deps("in.run", str(project_dir))
        assert present == []
        assert missing == ["nope.data"]

    def test_comment_lines_ignored(self, project_dir):
        _write(project_dir, "in.run", "# read_data ghost.data\nread_data real.data\n")
        _write(project_dir, "real.data", "x\n")
        present, missing = collect_deps("in.run", str(project_dir))
        assert present == ["real.data"]
        assert missing == []

    def test_read_restart(self, project_dir):
        _write(project_dir, "in.run", "read_restart saved.restart\n")
        _write(project_dir, "saved.restart", "binary\n")
        present, _ = collect_deps("in.run", str(project_dir))
        assert present == ["saved.restart"]

    def test_skips_large_files(self, project_dir):
        big = _write(project_dir, "in.big", "read_data x.data\n" + "print hi\n" * 500_000)
        assert os.path.getsize(project_dir / big) > 2_000_000
        present, _ = collect_deps(big, str(project_dir))
        assert present == []  # 超大文件不扫描也不拷贝引用


class TestThermoBuffer:
    def test_basic_block(self):
        buf = ThermoBuffer()
        lines = [
            "LAMMPS (30 Jul 2021)",
            "Step Temp E_pair TotEng Press",
            "0 300.0 -12345.6 -12000.1 101.3",
            "100 298.7 -12344.9 -11999.8 99.1",
            "Loop time of 0.1 on 1 procs",
        ]
        fed = [buf.feed(l) for l in lines]
        assert fed == [False, False, True, True, False]
        snap = buf.snapshot()
        assert snap["columns"] == ["Step", "Temp", "E_pair", "TotEng", "Press"]
        assert snap["rows"] == [
            [0.0, 300.0, -12345.6, -12000.1, 101.3],
            [100.0, 298.7, -12344.9, -11999.8, 99.1],
        ]

    def test_column_change_resets(self):
        buf = ThermoBuffer()
        buf.feed("Step Temp")
        buf.feed("0 300")
        buf.feed("Step PotEng")  # minimize 块, 列不同 → 重置
        buf.feed("0 -100.5")
        assert buf.columns == ["Step", "PotEng"]
        assert buf.snapshot()["rows"] == [[0.0, -100.5]]

    def test_scientific_and_negative(self):
        buf = ThermoBuffer()
        buf.feed("Step Press")
        assert buf.feed("5 -1.23e+08") is True
        assert buf.snapshot()["rows"] == [[5.0, -1.23e8]]

    def test_non_numeric_row_ignored(self):
        buf = ThermoBuffer()
        buf.feed("Step Temp")
        assert buf.feed("abc def") is False
        assert buf.snapshot()["rows"] == []

    def test_ring_buffer_cap(self):
        buf = ThermoBuffer()
        buf.feed("Step Temp")
        for i in range(6000):
            assert buf.feed(f"{i} 300") is True
        assert len(buf.rows) == ThermoBuffer.MAX_ROWS
        assert buf.snapshot()["rows"][-1] == [5999.0, 300.0]

    def test_snapshot_limit(self):
        buf = ThermoBuffer()
        buf.feed("Step Temp")
        for i in range(10):
            buf.feed(f"{i} 300")
        assert len(buf.snapshot(limit=3)["rows"]) == 3


class TestAnalyzeFailure:
    def test_lammps_package_error_with_hint(self):
        log = "reading atoms ...\nERROR: Package command after simulation box is defined (src/input.cpp:1663)\nLast command: package omp 8\n"
        r = analyze_failure("lmp", 1, log)
        assert r["summary"] == "LAMMPS 输入脚本运行报错"
        assert r["error_line"].startswith("ERROR: Package command")
        assert r["detail_line"] == "Last command: package omp 8"
        assert "package" in r["hint"] and "-pk omp" in r["hint"]

    def test_lammps_cannot_open(self):
        r = analyze_failure("lmp", 1, "ERROR: Cannot open file system.data")
        assert "文件" in r["hint"]

    def test_lammps_generic_error_no_hint_match(self):
        r = analyze_failure("lmp", 1, "ERROR: something unexpected")
        assert r["error_line"].startswith("ERROR:")
        assert "manual_md" in r["hint"]

    def test_exit_137_sigkill(self):
        r = analyze_failure("lmp", 137, "run finished partially")
        assert "SIGKILL" in r["summary"]

    def test_python_module_missing(self):
        log = "Traceback (most recent call last):\n  File 'x.py'\nModuleNotFoundError: No module named 'scipy'\n"
        r = analyze_failure("python", 1, log)
        assert r["summary"] == "Python 脚本异常退出"
        assert "`scipy`" in r["hint"] and "uv add" in r["hint"]

    def test_workbench_start_failure(self):
        r = analyze_failure("lmp", None, "[workbench] 进程启动失败: docker 不存在")
        assert r["summary"] == "进程未能启动"

    def test_completed_status_returns_none_is_caller_duty(self):
        # analyze_failure 本身不判断状态 (由路由层只在 failed 时调用)
        r = analyze_failure("lmp", 0, "all good")
        assert r["summary"].startswith("进程以退出码 0")


class TestSystemConfig:
    def test_default_profiles_validate(self):
        for profile in ("surface_adsorption", "solution"):
            cfg = system_config.default_system(profile)
            assert system_config.validate(cfg) == []

    def test_unknown_profile_rejected(self):
        with pytest.raises(ValueError):
            system_config.default_system("magic")

    def test_validate_catches_broken(self):
        cfg = system_config.default_system("solution")
        cfg["geometry"]["box"]["x"] = -5
        cfg["atom_types"][0].pop("charge")
        errors = system_config.validate(cfg)
        assert any("必须为正" in e for e in errors)
        assert any("charge" in e for e in errors)

    def test_overrides_applied(self):
        cfg = system_config.default_system("solution", overrides={"ions.conc_mol": 1.5})
        assert cfg["ions"]["conc_mol"] == 1.5


class TestBuilders:
    def test_solution_reproducible(self):
        cfg = system_config.default_system("solution")
        out1 = solution.build(cfg, random.Random(42))
        out2 = solution.build(cfg, random.Random(42))
        assert out1.atoms == out2.atoms
        assert out1.total_charge() == pytest.approx(0.0, abs=1e-9)

    def test_solution_concentration_counts(self):
        cfg = system_config.default_system("solution", overrides={"geometry.box.z": 40.0})
        out = solution.build(cfg, random.Random(1))
        counts = out.type_counts()
        vol_l = 30 * 30 * 40 * 1e-27
        n_sr_expected = max(1, int(0.5 * vol_l * 6.022e23))
        id_sr = next(t["id"] for t in cfg["atom_types"] if t["name"] == "Sr")
        id_cl = next(t["id"] for t in cfg["atom_types"] if t["name"] == "Cl")
        assert counts[id_sr] == n_sr_expected
        assert counts[id_cl] == 2 * n_sr_expected

    def test_surface_profile_matches_reference_counts(self):
        # 与 strontium 参考体系一致: 100 表面 / 1668 水 / 15 Sr / 18 Cl
        from common.builders import surface_adsorption

        cfg = system_config.default_system("surface_adsorption")
        out = surface_adsorption.build(cfg, random.Random(42))
        counts = out.type_counts()
        assert counts == {1: 100, 2: 1668, 3: 3336, 4: 15, 5: 18}


class TestTemplateRender:
    def test_renders_pair_coeff_from_system(self):
        cfg = system_config.default_system("surface_adsorption")
        text = render_run_lmp(cfg, "nvt_production", {})
        pc = [l for l in text.splitlines() if l.startswith("pair_coeff")]
        assert len(pc) == len(cfg["atom_types"])
        # pair_coeff 数值与 system.json 一致
        for t in cfg["atom_types"]:
            assert any(l.split()[3:5] == [str(t["eps"]), str(t["sigma"])] for l in pc)

    def test_thermo_replay_after_restart(self):
        """后端重启后, 终态任务从日志文件回放重建 thermo 曲线。"""
        import tempfile

        from common import system_config as sc
        from common.builders import surface_adsorption

        cfg = sc.default_system("surface_adsorption")
        d = tempfile.mkdtemp()
        sc.save(os.path.join(d, "system.json"), cfg)
        surface_adsorption.build(cfg, random.Random(42))
        # 构造带 thermo 输出的日志文件
        log_path = os.path.join(d, "job.log")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("Step Temp TotEng\n0 300.0 -100.0\n100 301.0 -99.0\n")

        # 模拟重启后的状态: 缓冲不存在 → 重建 manager 内存态
        from workbench.backend.app import job_manager as jm
        from workbench.backend.app import store

        store.init()  # 建表/迁移 (测试进程内不会经过应用入口)
        store.insert({
            "id": "replay01", "project_id": "demos", "project_name": "t",
            "script": "run.lmp", "kind": "lmp", "command": "x", "status": "completed",
            "exit_code": 0, "created_at": "2026-01-01", "started_at": "2026-01-01",
            "finished_at": "2026-01-01", "log_path": log_path, "workspace": None,
            "omp_threads": 8,
        })
        jm.manager._thermo["replay01"] = ThermoBuffer()  # 空 (重启后)
        snap = jm.manager.thermo_snapshot("replay01")
        assert snap["columns"] == ["Step", "Temp", "TotEng"]
        assert snap["rows"] == [[0.0, 300.0, -100.0], [100.0, 301.0, -99.0]]
        store.delete("replay01")

    def test_generated_marker_present(self):
        cfg = system_config.default_system("solution")
        text = render_run_lmp(cfg, "nvt_production", {"temperature": 350})
        assert text.startswith("# [generated]")
        assert "350" in text

    def test_solution_template_has_no_surf_group(self):
        cfg = system_config.default_system("solution")
        text = render_run_lmp(cfg, "nvt_production", {})
        assert "setforce" not in text  # 无表面 → 无冻结


class TestOmpAndInterrupted:
    def test_omp_threads_in_lmp_command(self):
        from workbench.backend.app.config import get_projects
        from workbench.backend.app.job_manager import JobManager

        m = JobManager()
        p = next(p for p in get_projects() if p["id"] == "demos")
        cmd = m._build_command(p, "test.lmp", "lmp", "abc123", 4)
        i = cmd.index("-pk")
        assert cmd[i + 1] == "omp" and cmd[i + 2] == "4"  # 线程数按参数生成

    def test_interrupted_transitions_legal(self):
        from workbench.backend.app.job_manager import VALID_TRANSITIONS

        assert "interrupted" in VALID_TRANSITIONS["running"]  # 启动对账: running → interrupted
        assert "canceled" in VALID_TRANSITIONS["interrupted"]  # 中断后仍可清理
        assert VALID_TRANSITIONS["completed"] == set()

    def test_transition_works_without_preexisting_lock(self):
        """重启后恢复路径: 全新 manager 没有锁, 迁移也必须成功 (回归: 锁字典早退 bug)。"""
        import asyncio
        import tempfile

        from workbench.backend.app import job_manager as jm
        from workbench.backend.app import store

        store.init()
        d = tempfile.mkdtemp()
        job = {
            "id": "transi01", "project_id": "demos", "project_name": "t",
            "script": "run.lmp", "kind": "lmp", "command": "x", "status": "running",
            "exit_code": None, "created_at": "2026-01-01", "started_at": "2026-01-01",
            "finished_at": None, "log_path": os.path.join(d, "x.log"),
            "workspace": None, "omp_threads": 8,
        }
        store.insert(job)
        m = jm.JobManager()

        async def scenario():
            ok1 = await m._transition("transi01", "interrupted", None)
            ok2 = await m._transition("transi01", "canceled", None)
            ok3 = await m._transition("transi01", "canceled", None)  # 幂等
            return ok1, ok2, ok3

        ok1, ok2, ok3 = asyncio.run(scenario())
        assert ok1 and ok2 and not ok3
        assert store.get("transi01")["status"] == "canceled"
        store.delete("transi01")


class TestShutdownPlan:
    """结束工作台进程的互锁决策 (纯函数; 端点层仅做取数与透传)。"""

    def test_blocked_when_any_job_running(self):
        from workbench.backend.app.routers.system import plan_shutdown

        plan = plan_shutdown(
            [{"id": "j1", "project_name": "p", "script": "run.lmp"}], lmp_processes=0
        )
        assert plan["action"] == "blocked"
        assert plan["jobs"][0]["id"] == "j1"

    def test_shutdown_cleans_orphan_processes(self):
        from workbench.backend.app.routers.system import plan_shutdown

        plan = plan_shutdown([], lmp_processes=2)
        assert plan == {"action": "shutdown", "clean_processes": 2}

    def test_shutdown_without_processes(self):
        from workbench.backend.app.routers.system import plan_shutdown

        # None (探测失败/无 docker) 与 0 同样视为无需清理
        assert plan_shutdown([], lmp_processes=None) == {
            "action": "shutdown", "clean_processes": 0,
        }
        assert plan_shutdown([], lmp_processes=0)["clean_processes"] == 0


class TestProjectRegistration:
    """手动直建目录的兜底注册 (文件夹即项目; 空/已注册目录不受影响)。"""

    def _scan(self, monkeypatch, tmp_path):
        from workbench.backend.app import config

        monkeypatch.setattr(config, "USER_PROJECTS_DIR", str(tmp_path))
        return {p["id"]: p for p in config.get_projects()}

    def test_unregistered_dir_fallback(self, monkeypatch, tmp_path):
        raw = tmp_path / "my-raw"
        raw.mkdir()
        (raw / "run.lmp").write_text("# manual\n", encoding="utf-8")
        (tmp_path / "zz-empty-dir").mkdir()  # 空目录 → 忽略
        ps = self._scan(monkeypatch, tmp_path)

        assert ps["my-raw"]["unregistered"] is True
        assert ps["my-raw"]["dir"] == "projects/my-raw"
        assert ps["my-raw"]["builtin"] is False
        assert "zz-empty-dir" not in ps

    def test_registered_dir_has_no_flag(self, monkeypatch, tmp_path):
        d = tmp_path / "with-manifest"
        d.mkdir()
        (d / "project.json").write_text(
            '{"id": "with-manifest", "name": "正常项目", "description": ""}',
            encoding="utf-8",
        )
        (d / "run.lmp").write_text("# x\n", encoding="utf-8")
        ps = self._scan(monkeypatch, tmp_path)

        assert ps["with-manifest"]["name"] == "正常项目"
        assert not ps["with-manifest"].get("unregistered")


class TestProjectsInbox:
    """历史研究迁移暂存区 (projects/_inbox/) API: 列表 / 确认入库 / 丢弃。"""

    @pytest.fixture
    def inbox_env(self, tmp_path, monkeypatch):
        from fastapi.testclient import TestClient

        from workbench.backend.app import config as cfg_mod
        from workbench.backend.app.main import app
        from workbench.backend.app.routers import projects as projects_router

        monkeypatch.setattr(cfg_mod, "USER_PROJECTS_DIR", str(tmp_path))
        monkeypatch.setattr(projects_router, "USER_PROJECTS_DIR", str(tmp_path))
        return TestClient(app), tmp_path

    def _stage(self, tmp_path, inbox_id, files=None, manifest=None):
        d = tmp_path / "_inbox" / inbox_id
        d.mkdir(parents=True)
        for name, content in (files or {}).items():
            (d / name).write_text(content, encoding="utf-8")
        if manifest is not None:
            import json as _json
            (d / "project.json").write_text(
                _json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        return d

    def test_inbox_dir_never_registered_as_project(self, inbox_env):
        from workbench.backend.app import config as cfg_mod

        client, tmp_path = inbox_env
        self._stage(tmp_path, "clay-2024", files={"run.lmp": "# x\n"})
        ps = {p["id"] for p in cfg_mod.get_projects()}
        assert "_inbox" not in ps and "clay-2024" not in ps

    def test_list_reports_staged_entries(self, inbox_env):
        client, tmp_path = inbox_env
        self._stage(tmp_path, "clay-2024", files={"run.lmp": "# x\n", "analyze.py": "1\n"},
                    manifest={"id": "clay-2024", "name": "黏土 2024", "description": "旧研究"})
        (tmp_path / "_inbox" / "clay-2024" / "migration_manifest.md").write_text(
            "| 原路径 | 新路径 |\n", encoding="utf-8")
        self._stage(tmp_path, "bare-copy", files={"run.lmp": "# y\n"})

        r = client.get("/api/projects/inbox")
        assert r.status_code == 200
        items = {i["id"]: i for i in r.json()["items"]}
        full = items["clay-2024"]
        assert full["name"] == "黏土 2024" and full["target_id"] == "clay-2024"
        assert full["has_manifest"] is True and full["has_migration_manifest"] is True
        assert full["file_count"] == 4 and full["target_conflict"] is False
        assert items["bare-copy"]["has_manifest"] is False
        assert items["bare-copy"]["target_id"] == "bare-copy"

    def test_confirm_moves_and_registers(self, inbox_env):
        client, tmp_path = inbox_env
        self._stage(tmp_path, "clay-2024", files={"run.lmp": "# x\n"},
                    manifest={"id": "clay-2024", "name": "黏土 2024", "description": "旧研究"})
        r = client.post("/api/projects/inbox/clay-2024/confirm")
        assert r.status_code == 201
        assert r.json()["dir"] == "projects/clay-2024"
        assert not (tmp_path / "_inbox" / "clay-2024").exists()
        import json as _json
        meta = _json.loads((tmp_path / "clay-2024" / "project.json").read_text(encoding="utf-8"))
        assert meta["id"] == "clay-2024" and meta.get("migrated_at")

        from workbench.backend.app import config as cfg_mod
        ps = {p["id"] for p in cfg_mod.get_projects()}
        assert "clay-2024" in ps

    def test_confirm_backfills_minimal_manifest(self, inbox_env):
        client, tmp_path = inbox_env
        self._stage(tmp_path, "bare-copy", files={"run.lmp": "# y\n"})
        r = client.post("/api/projects/inbox/bare-copy/confirm")
        assert r.status_code == 201 and r.json()["manifest_backfilled"] is True
        import json as _json
        meta = _json.loads((tmp_path / "bare-copy" / "project.json").read_text(encoding="utf-8"))
        assert meta["id"] == "bare-copy" and meta["name"] == "bare-copy"

    def test_confirm_rejects_target_conflict(self, inbox_env):
        client, tmp_path = inbox_env
        existing = tmp_path / "foo"
        existing.mkdir()
        (existing / "project.json").write_text(
            '{"id": "foo", "name": "已有项目", "description": ""}', encoding="utf-8")
        self._stage(tmp_path, "foo", files={"run.lmp": "# x\n"})
        r = client.get("/api/projects/inbox")
        assert r.json()["items"][0]["target_conflict"] is True
        r = client.post("/api/projects/inbox/foo/confirm")
        assert r.status_code == 409
        assert (tmp_path / "_inbox" / "foo" / "run.lmp").exists()  # 暂存副本原封不动

    def test_discard_removes_staged_copy_only(self, inbox_env):
        client, tmp_path = inbox_env
        self._stage(tmp_path, "junk", files={"run.lmp": "# x\n"})
        r = client.delete("/api/projects/inbox/junk")
        assert r.status_code == 200 and r.json()["discarded"] is True
        assert not (tmp_path / "_inbox" / "junk").exists()

    def test_inbox_id_path_safety(self, inbox_env):
        client, tmp_path = inbox_env
        # URL 层 .. 会被归一化到不了 handler; 遍历防护在 handler 内直接验证
        from workbench.backend.app.routers import projects as projects_router

        for bad in ("..", "../escape", "a/b", ".hidden"):
            with pytest.raises(Exception) as ei:
                projects_router._inbox_dir_or_404(bad)
            assert getattr(ei.value, "status_code", None) == 400
        # HTTP 层: 段内非法字符 (首位 .) 与不存在 id
        assert client.post("/api/projects/inbox/.hidden/confirm").status_code == 400
        assert client.post("/api/projects/inbox/missing/confirm").status_code == 404
        assert not (tmp_path.parent / "escape").exists()


class TestProvenance:
    """单任务溯源包 (roadmap #6): zip 内容完整性 + 内部字段剔除 + 缺失容错。"""

    def _make_job(self, tmp_path):
        ws = tmp_path / "ws"
        ws.mkdir()
        (ws / "run.lmp").write_text("units real\nrun 0\n", encoding="utf-8")
        (ws / "prod.lammpstrj").write_text("big trajectory\n", encoding="utf-8")
        proj = tmp_path / "proj"
        proj.mkdir()
        (proj / "system.json").write_text('{"profile": "clay_cif"}', encoding="utf-8")
        (proj / "system.data").write_text("atoms\n", encoding="utf-8")
        job = {
            "id": "job123", "project_id": "proj", "project_name": "Proj",
            "script": "run.lmp", "kind": "lmp", "status": "completed", "exit_code": 0,
            "created_at": "2026-09-05T12:00:00", "finished_at": "2026-09-05T12:01:00",
            "omp_threads": 8, "workspace": str(ws),
            "fingerprint": '{"system_sha": "abc"}',
            "_log_path": str(tmp_path / "internal.log"),
        }
        return job, ws, proj

    def test_zip_contains_core_entries(self, tmp_path):
        import io
        import json as _json
        import zipfile

        from workbench.backend.app.provenance import build_provenance_zip

        job, _ws, proj = self._make_job(tmp_path)
        data, skipped = build_provenance_zip(job, str(proj), "LAMMPS log tail")
        assert skipped == []
        zf = zipfile.ZipFile(io.BytesIO(data))
        names = set(zf.namelist())
        assert {"README.txt", "job.json", "fingerprint.json", "run.lmp",
                "system.json", "system.data", "log_tail.txt"} <= names
        assert "prod.lammpstrj" not in names  # 大体积可再生文件不入包
        job_back = _json.loads(zf.read("job.json").decode("utf-8"))
        assert "_log_path" not in job_back and job_back["id"] == "job123"
        assert _json.loads(zf.read("fingerprint.json").decode("utf-8"))["system_sha"] == "abc"

    def test_missing_pieces_do_not_break_export(self, tmp_path):
        import io
        import zipfile

        from workbench.backend.app.provenance import build_provenance_zip

        job = {"id": "x", "project_id": "ghost", "script": "run.lmp",
               "kind": "lmp", "status": "failed", "workspace": None, "fingerprint": None}
        data, skipped = build_provenance_zip(job, None, None)
        zf = zipfile.ZipFile(io.BytesIO(data))
        assert "README.txt" in zf.namelist()
        assert any("run.lmp" in s for s in skipped)
        assert any("system.json" in s for s in skipped)


class TestLocalDockerBackend:
    """/data 挂载检测 (v1.8.8 实录: _default 单键 ImportError 曾静默跳过整个校验)"""

    def test_default_missing_key_does_not_poison_others(self):
        from common.backends.local_docker import _default

        # config.py 不存在的 key → fallback, 且不影响存在的 key
        assert _default("NOT_A_CONFIG_KEY", "fb") == "fb"
        assert _default("CONTAINER_NAME", "x") == "lammpsd"
        assert _default("LAMMPS_DATA_HOST_DIR", None) is not None

    def test_parse_data_mount(self):
        from common.backends.local_docker import _host_path_same, _parse_data_mount

        out = "C:\\Users\\x\\data|/data;\n"
        assert _parse_data_mount(out, "/data") == "C:\\Users\\x\\data"
        assert _parse_data_mount(out, "/other") is None
        assert _parse_data_mount("", "/data") is None
        # Windows 大小写/分隔符不敏感
        assert _host_path_same("C:/Users/X/Data", "c:\\users\\x\\data") is True
        assert _host_path_same("C:/a", "C:/b") is False


class TestLammpsLint:
    """发车前确定性 lint (占位符/必需板块/引用存在性/旧挂载残留)。"""

    def test_clean_script_passes(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        _write(project_dir, "system.data", "atoms\n")
        text = "units real\natom_style atomic\npair_style lj/cut 2.5\nread_data system.data\nrun 100\n"
        r = lint_lammps_input(text, str(project_dir))
        assert r["errors"] == []

    def test_placeholder_is_error(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        text = 'units real\npair_style "replace-with-force-field"\nrun 10\n'
        r = lint_lammps_input(text, str(project_dir))
        assert any("占位符" in e for e in r["errors"])

    def test_missing_required_sections(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        r = lint_lammps_input("atom_style atomic\n", str(project_dir))
        joined = "\n".join(r["errors"])
        assert "units" in joined and "pair_style" in joined and "run / minimize" in joined

    def test_run_zero_is_warning(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        r = lint_lammps_input("units real\npair_style lj/cut 2.5\nrun 0\n", str(project_dir))
        assert r["errors"] == []
        assert any("run 0" in w for w in r["warnings"])

    def test_missing_reference(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        text = "units real\npair_style lj/cut 2.5\nread_data ghost.data\nrun 10\n"
        r = lint_lammps_input(text, str(project_dir))
        assert any("ghost.data" in e for e in r["errors"])

    def test_legacy_mount_path_is_warning(self, project_dir):
        from common.lammps_lint import lint_lammps_input

        r = lint_lammps_input(
            "units real\npair_style lj/cut 2.5\nread_data /data/proj/system.data\nrun 10\n",
            str(project_dir))
        assert r["errors"] == []  # 绝对路径无法在项目目录校验 → 警告而非误报
        assert any("旧挂载" in w for w in r["warnings"])

    def test_real_rendered_script_passes(self):
        # 真实渲染产物冒烟: strontium run.lmp + system.data 均在项目目录
        from common.lammps_lint import lint_lammps_input

        root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "systems", "strontium_adsorption")
        with open(os.path.join(root, "run.lmp"), encoding="utf-8") as f:
            r = lint_lammps_input(f.read(), root)
        assert r["errors"] == []


class TestFailureCaseLibrary:
    """策展案例库驱动: severity / actions / can_resume 结构化字段。"""

    def test_lmp_rule_hit_full_structure(self):
        from workbench.backend.app.failure import analyze_failure

        r = analyze_failure("lmp", 1, "step 0\nERROR: Lost atoms (../ngc.cpp)")
        assert r["severity"] == "high"
        assert r["can_resume"] is False
        assert len(r["actions"]) >= 2
        assert "原子丢失" in r["hint"]

    def test_nan_rule_can_resume(self):
        from workbench.backend.app.failure import analyze_failure

        r = analyze_failure("lmp", 1, "ERROR: Non-numeric pressure - nan")
        assert r["severity"] == "high" and r["can_resume"] is True

    def test_python_rule_formatting(self):
        from workbench.backend.app.failure import analyze_failure

        r = analyze_failure("python", 1, "Traceback (most recent call last):\n"
                                         "ModuleNotFoundError: No module named 'scipy'")
        assert r["severity"] == "low"
        assert "uv add scipy" in r["hint"]
        assert any("uv add scipy" in a for a in r["actions"])

    def test_fixture_real_build_failure(self):
        # 夹具回归: 真实任务日志 (TypeError 案例, 已沉淀入案例库)
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "fixtures", "logs", "build_failed.log")
        with open(log_path, encoding="utf-8") as f:
            r = analyze_failure("python", 1, f.read())
        assert r["summary"] == "Python 脚本异常退出"
        assert "TypeError" in r["error_line"]
        assert r["severity"] == "high"
        assert any("builder" in a for a in r["actions"])

    def test_fixture_completed_log_no_lmp_error(self):
        # 正常完成日志: 不应误报 LAMMPS ERROR
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "fixtures", "logs", "demo_completed.log")
        with open(log_path, encoding="utf-8") as f:
            text = f.read()
        assert "ERROR:" not in text  # 夹具前提
        r = analyze_failure("lmp", 0, text)
        assert "报错" not in r["summary"]


class TestConsistencyChain:
    """体系一致性链: built_state (built/stale/never) + script_state (sync/hand_edited/missing)。"""

    def _mk(self, tmp_path, system_text, lmp_text, meta):
        import json as _json
        (tmp_path / "system.json").write_text(system_text, encoding="utf-8")
        (tmp_path / "run.lmp").write_text(lmp_text, encoding="utf-8")
        (tmp_path / "project.json").write_text(_json.dumps(meta), encoding="utf-8")

    def test_built_and_sync(self, tmp_path):
        import hashlib
        import json as _json
        from workbench.backend.app.routers.projects import compute_consistency

        self._mk(tmp_path, '{"a":1}', "run 1\n", {})
        sys_sha = hashlib.sha256((tmp_path / "system.json").read_bytes()).hexdigest()
        lmp_sha = hashlib.sha256((tmp_path / "run.lmp").read_bytes()).hexdigest()
        c = compute_consistency(str(tmp_path), {"built_system_sha": sys_sha,
                                                "rendered_sha": lmp_sha})
        assert c["built_state"] == "built" and c["script_state"] == "sync"

    def test_stale_and_hand_edited(self, tmp_path):
        import hashlib
        from workbench.backend.app.routers.projects import compute_consistency

        self._mk(tmp_path, '{"a":2}', "run 2\n", {})
        old_sha = hashlib.sha256(b"old").hexdigest()
        c = compute_consistency(str(tmp_path), {"built_system_sha": old_sha,
                                                "rendered_sha": old_sha})
        assert c["built_state"] == "stale" and c["script_state"] == "hand_edited"

    def test_never_built(self, tmp_path):
        from workbench.backend.app.routers.projects import compute_consistency

        self._mk(tmp_path, "{}", "run 1\n", {})
        c = compute_consistency(str(tmp_path), {})
        assert c["built_state"] == "never" and c["script_state"] == "hand_edited"
        # 从未渲染 (无 run.lmp) → missing
        (tmp_path / "run.lmp").unlink()
        c = compute_consistency(str(tmp_path), {})
        assert c["script_state"] == "missing"


class TestLocalTools:
    """本地工具自动探测 (VMD / Vesta) 与启动器生成 — 跨平台纯函数。"""

    def test_detect_returns_structure(self):
        from workbench.backend.app.local_tools.detect import detect

        d = detect()
        assert "platform" in d and d["platform"] in ("Windows", "Darwin", "Linux")
        for tool in ("vmd", "vesta"):
            assert tool in d
            assert "found" in d[tool] and "path" in d[tool] and "version_hint" in d[tool]
            assert d[tool]["found"] in (True, False)
            # 未检测到时 path 为 None, source 为 None
            if not d[tool]["found"]:
                assert d[tool]["path"] is None

    def test_launcher_windows_bat(self):
        from workbench.backend.app.local_tools.detect import launcher

        r = launcher("vesta", "C:/data/test.cif", exe_override="C:/Program Files/Vesta/VESTA.exe")
        assert r["filename"].endswith(".bat")
        assert r["exe"] == "C:/Program Files/Vesta/VESTA.exe"
        assert "@echo off" in r["content"]
        assert "start \"\" \"C:/Program Files/Vesta/VESTA.exe\" \"C:/data/test.cif\"" in r["content"]
        # 启动器会自带 if exist 兜底
        assert "if exist" in r["content"]
        assert "pause" in r["content"]

    def test_launcher_bad_exe_self_guard(self):
        # 指向不存在的 exe 时仍生成可读脚本, 启动器自身 if exist + 提示兜底
        from workbench.backend.app.local_tools.detect import launcher

        r = launcher("vmd", "/tmp/x.lammpstrj", exe_override="C:/nonexistent/vmd.exe")
        assert r["filename"]
        assert "if exist" in r["content"]
        assert "工具未找到" in r["content"] and "C:/nonexistent/vmd.exe" in r["content"]

    def test_configure_persists_and_clears(self, tmp_path, monkeypatch):
        import json as _json
        from workbench.backend.app import config as cfg_mod
        from workbench.backend.app.routers import local_tools as lt_router
        from fastapi.testclient import TestClient
        from workbench.backend.app.main import app

        fake_cfg = tmp_path / "local_tools.json"
        # router 里的 LOCAL_TOOLS_CONFIG 是 import-time 绑定, 也要 patch
        monkeypatch.setattr(cfg_mod, "LOCAL_TOOLS_CONFIG", str(fake_cfg))
        monkeypatch.setattr(lt_router, "LOCAL_TOOLS_CONFIG", str(fake_cfg))
        client = TestClient(app)
        # 保存到不存在的文件应 400
        r = client.post("/api/local-tools/configure", json={"tool": "vmd", "path": "C:/nonexistent.exe"})
        assert r.status_code == 400
        # 真实存在的文件 (pytest 自身) 应 200 并持久化
        import sys
        real = sys.executable
        r = client.post("/api/local-tools/configure", json={"tool": "vmd", "path": real})
        assert r.status_code == 200
        assert fake_cfg.exists()
        persisted = _json.loads(fake_cfg.read_text(encoding="utf-8"))
        assert persisted["vmd"]["path"] == real
        # 清除
        r = client.post("/api/local-tools/configure", json={"tool": "vmd", "path": ""})
        assert r.status_code == 200
        assert "vmd" not in _json.loads(fake_cfg.read_text(encoding="utf-8"))


class TestEquilibrium:
    """平衡判据 (RadonPy 思想): 后窗口线性漂移检验。"""

    def _thermo(self, density_drift: float, steps_end: float = 100000, n: int = 100):
        columns = ["Step", "Temp", "TotEng", "Density"]
        rows = []
        for i in range(n):
            step = steps_end * i / (n - 1)
            # 密度线性漂移; 能量平稳 (小幅噪声); 温度涨落
            dens = 1.0 + density_drift * (i / (n - 1))
            eng = -5000.0 + 0.5 * ((i % 7) - 3) * 0.01
            rows.append([step, 300.0 + (i % 5), eng, dens])
        return {"columns": columns, "rows": rows}

    def test_stable_is_good(self):
        from common.equilibrium import analyze_equilibrium

        r = analyze_equilibrium(self._thermo(density_drift=0.0001))
        assert r["status"] == "good"
        assert all(c["verdict"] == "pass" for c in r["checks"])
        quantities = {c["quantity"].lower() for c in r["checks"]}
        assert "density" in quantities and "toteng" in quantities

    def test_large_drift_is_poor(self):
        from common.equilibrium import analyze_equilibrium

        r = analyze_equilibrium(self._thermo(density_drift=0.2))  # 20% 漂移
        assert r["status"] == "poor"
        dens = next(c for c in r["checks"] if c["quantity"].lower() == "density")
        assert dens["verdict"] == "poor"

    def test_insufficient_samples_unknown(self):
        from common.equilibrium import analyze_equilibrium

        t = {"columns": ["Step", "Density"], "rows": [[i * 10.0, 1.0] for i in range(10)]}
        assert analyze_equilibrium(t)["status"] == "unknown"

    def test_missing_columns_unknown(self):
        from common.equilibrium import analyze_equilibrium

        t = {"columns": ["Step", "Temp"], "rows": [[i * 10.0, 300.0] for i in range(100)]}
        assert analyze_equilibrium(t)["status"] == "unknown"


class TestTrajectoryAnalysis:
    """轨迹统计纯函数: 合成小轨迹的黄金断言。"""

    def _write_traj(self, path):
        """2 帧 × 2 原子 (type 1, 2), 第二帧 atom1 沿 x 移动 1.0。"""
        lines = []
        for ts, (x1,) in enumerate([(0.0,), (1.0,)]):
            lines.append("ITEM: TIMESTEP"); lines.append(str(ts * 1000))
            lines.append("ITEM: NUMBER OF ATOMS"); lines.append("2")
            lines.append("ITEM: BOX BOUNDS xy xz yz pp pp pp")
            lines.append("0 10 0 0"); lines.append("0 10 0 0"); lines.append("0 10 0 0")
            lines.append("ITEM: ATOMS id type x y z")
            lines.append(f"1 1 {x1} 0.0 0.0")
            lines.append("2 2 5.0 5.0 5.0")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_summary_and_z(self, tmp_path):
        from common.traj_analysis import analyze_trajectory

        f = tmp_path / "t.lammpstrj"
        self._write_traj(f)
        r = analyze_trajectory(str(f), msd_max_lag=1)
        assert r["summary"]["frames"] == 2
        assert r["summary"]["atoms"] == 2
        assert r["summary"]["types"] == {"1": 1, "2": 1}
        # z 分布: type1 全部 z=0, type2 全部 z=5
        zp = {p["type"]: p["bins"] for p in r["z_profile"]}
        assert all(b["z"] == 0.0 for b in zp["1"])
        assert sum(b["freq"] for b in zp["1"]) == 1.0

    def test_msd_displacement(self, tmp_path):
        from common.traj_analysis import analyze_trajectory

        f = tmp_path / "t.lammpstrj"
        self._write_traj(f)
        r = analyze_trajectory(str(f), msd_max_lag=1)
        msd = {m["type"]: m["points"] for m in r["msd"]}
        assert msd["1"], "type1 应有 MSD 点"
        assert abs(msd["1"][0]["value"] - 1.0) < 1e-9  # 位移 1.0 → MSD 1.0
        assert abs(msd["2"][0]["value"]) < 1e-9  # 静止 → MSD 0
        assert "all" in msd

    def test_fit_diffusion_linear(self):
        from common.traj_analysis import fit_diffusion

        # 完美线性 MSD = 0.002 × step → 斜率 0.002, R²=1
        pts = [{"step": s, "value": 0.002 * s} for s in range(0, 1000, 50)]
        d = fit_diffusion(pts)
        assert d is not None
        assert abs(d["slope_a2_per_step"] - 0.002) < 1e-9
        assert d["r2"] == 1.0
        assert d["window"][1] == 950.0

    def test_fit_diffusion_insufficient_points(self):
        from common.traj_analysis import fit_diffusion

        assert fit_diffusion([{"step": 0, "value": 0.0}]) is None
        # 平坦 MSD (完全不动): D̂=0 是有效物理结果, R²=1 (完美预测常数)
        pts = [{"step": s, "value": 1.0} for s in range(10)]
        d = fit_diffusion(pts)
        assert d is not None and d["slope_a2_per_step"] == 0.0 and d["r2"] == 1.0


class TestFingerprint:
    """任务环境指纹: store 列迁移 + 详情响应。"""

    def test_store_column_migration(self):
        import json as _json
        import tempfile
        from workbench.backend.app import store

        store.init()
        job = {
            "id": "fp01", "project_id": "demos", "project_name": "t",
            "script": "x.lmp", "kind": "lmp", "command": "x", "status": "completed",
            "exit_code": 0, "created_at": "2026-01-01", "started_at": "2026-01-01",
            "finished_at": "2026-01-01", "log_path": None, "workspace": None,
            "omp_threads": 8,
            "fingerprint": _json.dumps({"system_sha": "abc123", "image": "lammps/lammps:latest"}),
        }
        store.insert(job)
        got = store.get("fp01")
        assert got["fingerprint"] is not None
        assert _json.loads(got["fingerprint"])["system_sha"] == "abc123"
        store.delete("fp01")

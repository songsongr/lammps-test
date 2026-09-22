"""docker_env 资源监测 / 一键启动 单测 (纯函数 + 不依赖 docker daemon)。"""
from common.local_tools_compat import supports  # noqa: F401  仅为占位避免 test_*.py 命名冲突

from workbench.backend.app.docker_env import (
    _parse_mem_bytes, _dir_size_bytes, container_metrics,
)


def test_parse_mem_bytes_units():
    assert _parse_mem_bytes("100B") == 100
    assert _parse_mem_bytes("12.5MiB") == 12 * 1024 * 1024 + 512 * 1024
    assert _parse_mem_bytes("1GiB") == 1024 ** 3
    assert _parse_mem_bytes("2.5K") == 2560


def test_parse_mem_bytes_garbage():
    assert _parse_mem_bytes("") == 0
    assert _parse_mem_bytes("xyz") == 0
    assert _parse_mem_bytes("12.5Z") == 0  # 未知单位走 fallback 整数


def test_dir_size_bytes_nonexistent():
    assert _dir_size_bytes("C:/this/path/does/not/exist/__nope__") is None


def test_dir_size_bytes_real(tmp_path):
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "b.txt").write_text("world!" * 10)
    sz = _dir_size_bytes(str(tmp_path))
    assert sz == 5 + 60  # "hello" + "world!" * 10 = 5 + 60


def test_container_metrics_shape():
    """容器未运行或 docker 不可用时返回结构, current 可能 None。"""
    m = container_metrics()
    assert "current" in m
    assert "history" in m
    assert isinstance(m["history"], list)
    assert "data_dir_size_bytes" in m
    assert "data_dir_path" in m

"""LAMMPS 轨迹解析器单元测试。"""
from common.traj_parser import parse_lammpstrj, atoms_of_type


SAMPLE = """ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
3
ITEM: BOX BOUNDS pp pp pp
0.0 10.0
0.0 10.0
0.0 10.0
ITEM: ATOMS id type x y z
1 1 0.0 0.0 0.0
2 2 1.0 1.0 1.0
3 1 2.0 2.0 2.0
ITEM: TIMESTEP
100
ITEM: NUMBER OF ATOMS
3
ITEM: BOX BOUNDS pp pp pp
0.0 10.0
0.0 10.0
0.0 10.0
ITEM: ATOMS id type x y z
1 1 0.5 0.5 0.5
2 2 1.5 1.5 1.5
3 1 2.5 2.5 2.5
"""


def test_parse_basic(tmp_path):
    p = tmp_path / "sample.lammpstrj"
    p.write_text(SAMPLE)
    frames = parse_lammpstrj(str(p))

    assert len(frames) == 2
    assert frames[0]["timestep"] == 0
    assert frames[1]["timestep"] == 100
    assert frames[0]["box"] == (0.0, 10.0, 0.0, 10.0, 0.0, 10.0)
    assert len(frames[0]["atoms"]) == 3

    a0 = frames[0]["atoms"][0]
    assert a0["id"] == 1 and a0["type"] == 1
    assert a0["x"] == 0.0 and a0["y"] == 0.0 and a0["z"] == 0.0

    a1 = frames[1]["atoms"][1]
    assert a1["id"] == 2 and a1["type"] == 2
    assert a1["x"] == 1.5 and a1["z"] == 1.5


def test_atoms_of_type(tmp_path):
    p = tmp_path / "sample.lammpstrj"
    p.write_text(SAMPLE)
    frames = parse_lammpstrj(str(p))

    # type 1 每帧应有 2 个原子
    for coords in atoms_of_type(frames, 1):
        assert len(coords) == 2
    # type 2 每帧应有 1 个原子
    for coords in atoms_of_type(frames, 2):
        assert len(coords) == 1


def test_parse_empty(tmp_path):
    p = tmp_path / "empty.lammpstrj"
    p.write_text("")
    assert parse_lammpstrj(str(p)) == []

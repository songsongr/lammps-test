"""common/lammps_data.py 解析测试: type→element 映射两条路径。"""
from common.lammps_data import parse_type_to_element, lammps_data_to_xyz


SAMPLE_WITH_LABEL = """\
random title

4 atom types

0.0 30.0 xlo xhi
0.0 30.0 ylo xhi
0.0 30.0 zlo xhi

Masses

1 15.9994  # Ow
2 1.0079  # Hw
3 87.62  # Sr
4 35.453  # Cl

Atoms

1 1 1 -0.84 0 0 0
2 1 2 0.42 0 0 0
"""


SAMPLE_NO_LABEL = """\
random title

2 atom types

0.0 10.0 xlo xhi
0.0 10.0 ylo xhi
0.0 10.0 zlo zhi

Masses

1 12.011
2 1.008

Atoms

1 1 1 0 0 0
"""


def test_parse_label_priority():
    """system.data 注释里的元素名优先于 mass 推。"""
    out = parse_type_to_element(SAMPLE_WITH_LABEL)
    assert out == {1: "Ow", 2: "Hw", 3: "Sr", 4: "Cl"}, out


def test_parse_mass_fallback():
    """无注释时按质量推元素 (12.011 → C, 1.008 → H)。"""
    out = parse_type_to_element(SAMPLE_NO_LABEL)
    assert out == {1: "C", 2: "H"}, out


def test_lammps_data_to_xyz_uses_xyz_format():
    """xyz 输出是元素+坐标形式, 首行原子数。"""
    out = lammps_data_to_xyz(SAMPLE_WITH_LABEL)
    lines = out.splitlines()
    assert lines[0] == "2"  # 2 原子
    # 第一行注释 + 2 原子行
    assert lines[1].startswith("LAMMPS system")
    # 至少一行 Ow (质量匹配) — 注释不被 xyz 解析, 用 mass
    assert "Ow" in lines[2] or "O" in lines[2], lines[2]

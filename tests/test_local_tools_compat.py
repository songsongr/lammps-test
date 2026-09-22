"""本地工具文件类型支持矩阵单测。"""
from common.local_tools_compat import supports, VMD_EXTS, VESTA_EXTS


def test_vmd_supports_lammpstrj():
    assert supports("vmd", ".lammpstrj")


def test_vmd_supports_dump():
    assert supports("vmd", ".dump")


def test_vesta_does_not_support_lammps_data():
    """VESTA 不支持 .data — bug 复现: 用户点 VESTA 打开 .data → Invalid data!"""
    assert not supports("vesta", ".data")


def test_vesta_supports_cif_and_xyz():
    assert supports("vesta", ".cif")
    assert supports("vesta", ".xyz")
    assert supports("vesta", ".pdb")


def test_case_insensitive():
    assert supports("vmd", ".LAMMPSTRJ")
    assert supports("vesta", ".CIF")


def test_unknown_tool_returns_false():
    assert not supports("unknown_tool", ".xyz")
    assert not supports("vmd", ".unknown_ext")

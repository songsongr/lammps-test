"""VMD / VESTA 文件类型支持矩阵 (前后端共用单例)。

事实来源:
  - VMD 文档支持: lammpstrj, dcd, xtc, trr, xyz, pdb, gro 等分子/晶体轨迹
  - VESTA 文档支持: vesta, cif, xsf, xyz, pdb, cssr, struct, xod, xtl, fdf
  - VESTA **不支持** LAMMPS .data 格式 (会弹 "Invalid data! This file type is not supported.")

判断函数供前端按扩展名筛按钮、后端 spawn 前再次校验 (.data 自动转 .xyz 临时文件)。
"""
from __future__ import annotations

VMD_EXTS: frozenset[str] = frozenset({
    ".lammpstrj", ".dump", ".dcd", ".xtc", ".trr", ".xyz", ".pdb", ".gro",
})

VESTA_EXTS: frozenset[str] = frozenset({
    ".vesta", ".cif", ".xsf", ".xyz", ".pdb", ".cssr", ".struct", ".xod", ".xtl", ".fdf",
})


def supports(tool: str, ext: str) -> bool:
    """扩展名是否被指定工具原生支持 (不经过转换)。"""
    ext = ext.lower()
    if not ext.startswith("."):
        ext = "." + ext
    if tool == "vmd":
        return ext in VMD_EXTS
    if tool == "vesta":
        return ext in VESTA_EXTS
    return False

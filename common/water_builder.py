"""
SPC/E 水分子构建工具。

提供标准 SPC/E 水几何与均匀随机取向生成, 供体系生成脚本复用。
取向生成与 convert_cif.py 原实现一致 (均匀随机四元数)。
"""
import math
import numpy as np

from .spce_params import OH_DIST, HOH_ANGLE


def random_water_orientation():
    """
    生成 SPC/E 水分子的随机取向 (均匀随机四元数旋转)。

    返回: (h1_rel, h2_rel) 两个 H 相对 O 的笛卡尔坐标向量 (长度 = OH_DIST)。
    """
    theta = math.radians(HOH_ANGLE)
    r_oh = OH_DIST
    # 参考: O 在原点, H 在 xy 平面两侧
    h_ref = np.array([
        [r_oh * math.cos(theta / 2), r_oh * math.sin(theta / 2), 0.0],   # H1
        [r_oh * math.cos(theta / 2), -r_oh * math.sin(theta / 2), 0.0],  # H2
    ])

    # 均匀随机四元数
    u1, u2, u3 = np.random.random(), np.random.random(), np.random.random()
    q = np.array([
        math.sqrt(1 - u1) * math.sin(2 * math.pi * u2),
        math.sqrt(1 - u1) * math.cos(2 * math.pi * u2),
        math.sqrt(u1) * math.sin(2 * math.pi * u3),
        math.sqrt(u1) * math.cos(2 * math.pi * u3),
    ])

    # 四元数 → 旋转矩阵
    R = np.array([
        [1 - 2 * (q[2] ** 2 + q[3] ** 2), 2 * (q[1] * q[2] - q[0] * q[3]), 2 * (q[1] * q[3] + q[0] * q[2])],
        [2 * (q[1] * q[2] + q[0] * q[3]), 1 - 2 * (q[1] ** 2 + q[3] ** 2), 2 * (q[2] * q[3] - q[0] * q[1])],
        [2 * (q[1] * q[3] - q[0] * q[2]), 2 * (q[2] * q[3] + q[0] * q[1]), 1 - 2 * (q[1] ** 2 + q[2] ** 2)],
    ])

    h_rot = h_ref @ R.T
    return h_rot


def make_spce_molecule(center, rng=None):
    """
    以 center = (ox, oy, oz) 为 O 位置, 生成一个随机取向的 SPC/E 水分子。

    返回: ((ox,oy,oz), (h1x,h1y,h1z), (h2x,h2y,h2z)) 三个笛卡尔坐标。
    可用 rng (np.random.Generator) 注入随机源以复现; 默认用全局 np.random。
    """
    h1, h2 = random_water_orientation()
    o = np.asarray(center, dtype=float)
    return (tuple(o), tuple(o + h1), tuple(o + h2))

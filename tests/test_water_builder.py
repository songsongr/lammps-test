"""SPC/E 水分子构建工具几何测试。"""
import math

import numpy as np

from common.water_builder import make_spce_molecule, random_water_orientation
from common.spce_params import OH_DIST, HOH_ANGLE


def test_orientation_oh_distance():
    h1, h2 = random_water_orientation()
    assert abs(np.linalg.norm(h1) - OH_DIST) < 1e-9
    assert abs(np.linalg.norm(h2) - OH_DIST) < 1e-9


def test_orientation_hoh_angle():
    h1, h2 = random_water_orientation()
    cos = np.dot(h1, h2) / (np.linalg.norm(h1) * np.linalg.norm(h2))
    ang = math.degrees(math.acos(np.clip(cos, -1.0, 1.0)))
    assert abs(ang - HOH_ANGLE) < 1e-6


def test_molecule_centered_and_geometry():
    o, h1, h2 = make_spce_molecule((1.0, 2.0, 3.0))
    assert o == (1.0, 2.0, 3.0)
    for h in (h1, h2):
        d = math.sqrt(sum((h[i] - o[i]) ** 2 for i in range(3)))
        assert abs(d - OH_DIST) < 1e-6

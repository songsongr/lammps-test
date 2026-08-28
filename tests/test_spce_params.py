"""SPC/E 水模型公共参数常量测试。"""
from common import spce_params as sp


def test_geometry_constants():
    assert sp.OH_DIST == 1.0
    assert sp.HOH_ANGLE == 109.47


def test_charges_neutral():
    assert abs(sp.Q_OW - (-0.8476)) < 1e-9
    assert abs(sp.Q_HW - 0.4238) < 1e-9
    # 水分子电中性: Q_OW + 2*Q_HW = 0
    assert abs(sp.Q_OW + 2 * sp.Q_HW) < 1e-9


def test_lj_parameters():
    assert abs(sp.EPS_OW - 0.1553) < 1e-9
    assert abs(sp.SIG_OW - 3.1660) < 1e-9


def test_intramolecular():
    assert sp.K_BOND == 554.13
    assert sp.K_ANGLE == 45.77
    assert sp.SPECIAL_BONDS.startswith("lj 0.0 0.0 0.5")

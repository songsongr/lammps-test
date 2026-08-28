"""SPC/E 水模型公共参数 (real 单位: kcal/mol, Angstrom, e)。

数值单一来源为 system_config.WATER_PRESETS; 本模块保留既有导入接口
(water_builder / tests / 脚本引用), 不再独立硬编码。

差异说明: 早期 build_system.py 曾用 SPC 原始电荷 (-0.820/+0.410), 项目权威为
SPC/E (-0.8476/+0.4238)。该历史混合体已如实记录于 strontium_adsorption/system.json。
"""
from .system_config import WATER_PRESETS

_p = WATER_PRESETS["SPCE"]

# ---- 几何 ----
OH_DIST = _p["oh_dist"]        # O-H 键长 (Angstrom)
HOH_ANGLE = _p["hoh_angle"]    # H-O-H 键角 (度)

# ---- 部分电荷 (e) ----
Q_OW = _p["q_ow"]              # 水氧 (SPC/E 修正值)
Q_HW = _p["q_hw"]              # 水氢

# ---- LJ 12-6 参数 ----
EPS_OW = _p["eps_ow"]          # 水氧 epsilon
SIG_OW = _p["sigma_ow"]        # 水氧 sigma
# 水氢无 LJ (epsilon = 0)

# ---- 分子内 harmonic 力常数 ----
K_BOND = 554.13                # kcal/(mol·Angstrom^2), O-H 键
K_ANGLE = 45.77                # kcal/(mol·rad^2), H-O-H 角

# ---- special_bonds 排除权重 (lj w12 w13 w14 coul w12 w13 w14) ----
SPECIAL_BONDS = "lj 0.0 0.0 0.5 coul 0.0 0.0 0.5"

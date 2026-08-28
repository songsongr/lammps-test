"""体系配置 (system.json): 体系参数的单一真相源。

体系参数 (几何/组成/力场) 以结构化 JSON 存储于各项目目录, 构建引擎
(common/builders) 与方法模板渲染 (workbench) 都从它读取,
替代散落在 build 脚本与 .lmp 之间的双源硬编码。

水模型预设引用 common/spce_params.py 的权威值;
已知不一致 (如 build 侧 SPC 原始电荷) 以 atom_types 的 warning 字段标注, 不自动修正。
"""
import json
import os

# 水模型预设 (权威值; 来源 common/spce_params.py / 文献)
WATER_PRESETS: dict[str, dict] = {
    "SPCE": {
        "q_ow": -0.8476, "q_hw": 0.4238,
        "eps_ow": 0.1553, "sigma_ow": 3.1660,
        "oh_dist": 1.0, "hoh_angle": 109.47,
        "source": "Berendsen et al. 1987",
    },
    "SPC": {
        "q_ow": -0.820, "q_hw": 0.410,
        "eps_ow": 0.1553, "sigma_ow": 3.1660,
        "oh_dist": 1.0, "hoh_angle": 109.47,
        "source": "Berendsen et al. 1981",
    },
}

CONFIDENCE_LEVELS = ("高", "中", "低")
PROFILES = ("surface_adsorption", "solution", "clay_cif")

# 向导表单 schema: 每个体系 profile 暴露的参数字段 (前端表单由它驱动)
PROFILE_SCHEMAS: dict[str, dict] = {
    "surface_adsorption": {
        "name": "带电表面 + 水层 + 盐离子",
        "description": "底部带电固定表面 + 水层 + 盐离子 (复刻 SrCl₂ 吸附体系结构)",
        "fields": [
            {"key": "geometry.surface.a", "label": "表面晶格常数 a (Å)", "type": "number", "default": 3.0},
            {"key": "geometry.surface.nx", "label": "表面 x 方向超胞数", "type": "int", "default": 10},
            {"key": "geometry.surface.ny", "label": "表面 y 方向超胞数", "type": "int", "default": 10},
            {"key": "geometry.surface.layers", "label": "表面层数", "type": "int", "default": 2},
            {"key": "geometry.surface.occupancy", "label": "表面占位率", "type": "number", "default": 0.5,
             "note": "0.5 = 菱形图案"},
            {"key": "geometry.surface.charge_per_atom", "label": "表面单原子电荷 (e)", "type": "number", "default": -0.12},
            {"key": "geometry.water.z_start", "label": "水面起始高度 (Å)", "type": "number", "default": 6.0},
            {"key": "geometry.water.thickness", "label": "水层厚度 (Å)", "type": "number", "default": 70.0},
            {"key": "geometry.water.grid", "label": "水分子网格间距 (Å)", "type": "number", "default": 3.2,
             "note": "≈1 g/cm³ 密度"},
            {"key": "geometry.water.min_dist_surface", "label": "水-表面最小距离 (Å)", "type": "number", "default": 3.2},
            {"key": "geometry.vacuum", "label": "真空层厚度 (Å)", "type": "number", "default": 40.0,
             "note": "减弱周期镜像干扰"},
            {"key": "ions.conc_mol", "label": "盐浓度 (mol/L)", "type": "number", "default": 0.25},
            {"key": "ions.extra_sr", "label": "额外阳离子数 (平衡表面电荷)", "type": "int", "default": 6},
            {"key": "seed", "label": "随机种子", "type": "int", "default": 42, "note": "固定可复现"},
        ],
    },
    "solution": {
        "name": "均相溶液",
        "description": "纯水盒子 + 盐离子 (无表面), 适合本体性质/收敛性测试",
        "fields": [
            {"key": "geometry.box.x", "label": "盒子 x (Å)", "type": "number", "default": 30.0},
            {"key": "geometry.box.y", "label": "盒子 y (Å)", "type": "number", "default": 30.0},
            {"key": "geometry.box.z", "label": "盒子 z (Å)", "type": "number", "default": 30.0},
            {"key": "geometry.water.grid", "label": "水分子网格间距 (Å)", "type": "number", "default": 3.2,
             "note": "≈1 g/cm³ 密度"},
            {"key": "ions.conc_mol", "label": "盐浓度 (mol/L)", "type": "number", "default": 0.5},
            {"key": "seed", "label": "随机种子", "type": "int", "default": 42, "note": "固定可复现"},
        ],
    },
    "clay_cif": {
        "name": "黏土 CIF + 层间水",
        "description": "从 CIF 结构构建黏土超胞 + CLAYFF 分型 + OH 加氢 + 层间水 (CIF 绑定阈值随配置提供)",
        "fields": [
            {"key": "cif_file", "label": "CIF 文件名 (项目目录内)", "type": "string", "default": "Montmorillonite.cif"},
            {"key": "supercell.nx", "label": "超胞 x 倍数", "type": "int", "default": 2},
            {"key": "supercell.ny", "label": "超胞 y 倍数", "type": "int", "default": 2},
            {"key": "supercell.nz", "label": "超胞 z 倍数", "type": "int", "default": 1},
            {"key": "interlayer_water.target", "label": "层间水目标分子数", "type": "int", "default": 80},
            {"key": "interlayer_water.grid_xy", "label": "水 O-O 最小间距 (Å)", "type": "number", "default": 4.0},
            {"key": "interlayer_water.grid_z", "label": "层间格点 z 间距 (Å)", "type": "number", "default": 3.0},
            {"key": "interlayer_water.min_dist_o_fw", "label": "水 O-骨架最小距离 (Å)", "type": "number", "default": 4.0},
            {"key": "interlayer_water.min_dist_h_fw", "label": "水 H-骨架最小距离 (Å)", "type": "number", "default": 2.5},
            {"key": "seed", "label": "随机种子", "type": "int", "default": 42, "note": "固定可复现"},
        ],
    },
}


def _set_path(cfg: dict, dotted_key: str, value) -> None:
    node = cfg
    parts = dotted_key.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = value


def _get_path(cfg: dict, dotted_key: str):
    node = cfg
    for p in dotted_key.split("."):
        node = node.get(p) if isinstance(node, dict) else None
        if node is None:
            return None
    return node


def default_system(profile: str, water_model: str = "SPCE",
                   overrides: dict[str, object] | None = None) -> dict:
    """按 profile 构造一份带默认值的完整 system 配置 (新建向导用)。

    atom_types 使用水模型预设的权威值 — 新项目从源头保持参数一致。
    """
    if profile not in PROFILES:
        raise ValueError(f"未知 profile: {profile}")
    preset = WATER_PRESETS[water_model]
    cfg: dict = {
        "version": 1,
        "profile": profile,
        "seed": 42,
        "water_model": water_model,
    }
    schema = PROFILE_SCHEMAS[profile]
    for field in schema["fields"]:
        _set_path(cfg, field["key"], field["default"])
    if overrides:
        for key, value in overrides.items():
            _set_path(cfg, key, value)

    ow = {"name": "Ow", "charge": preset["q_ow"], "mass": 15.9994,
          "eps": preset["eps_ow"], "sigma": preset["sigma_ow"],
          "source": f"{water_model} ({preset['source']})", "confidence": "高"}
    hw = {"name": "Hw", "charge": preset["q_hw"], "mass": 1.0079,
          "eps": 0.0, "sigma": 1.0,
          "source": f"{water_model} 标准 (H 无 LJ)", "confidence": "高"}
    sr = {"name": "Sr", "charge": 2.0, "mass": 87.62,
          "eps": 0.1, "sigma": 3.0, "source": "随手设定, 无文献", "confidence": "低",
          "ref": "候选: Aqvist 1990 / Mamatkulov 2013 / Li-Song-Merz 2015"}
    cl = {"name": "Cl", "charge": -1.0, "mass": 35.453,
          "eps": 0.1, "sigma": 4.0, "source": "随手设定, 无文献", "confidence": "低",
          "ref": "推荐替换 JC 2008 (SPC/E): eps=0.1000, sigma=4.045"}
    if profile == "surface_adsorption":
        surf = {"name": "Surf", "charge": -0.12, "mass": 28.0855,
                "eps": 0.1554, "sigma": 3.1655,
                "source": "近似 CLAYFF O 参数", "confidence": "中"}
        cfg["atom_types"] = [surf, ow, hw, sr, cl]
    else:
        cfg["atom_types"] = [ow, hw, sr, cl]
    for i, t in enumerate(cfg["atom_types"]):
        t["id"] = i + 1
    return cfg


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path: str, cfg: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validate(cfg: dict) -> list[str]:
    """校验体系配置, 返回错误列表 (空 = 通过)。按 profile 分派几何规则。"""
    errors: list[str] = []
    profile = cfg.get("profile")
    if profile not in PROFILES:
        return [f"未知 profile: {profile!r} (可选: {', '.join(PROFILES)})"]
    if not isinstance(cfg.get("seed"), int) or cfg["seed"] < 0:
        errors.append("seed 必须为非负整数")
    if cfg.get("water_model") not in WATER_PRESETS:
        errors.append(f"water_model 必须为 {' / '.join(WATER_PRESETS)}")

    types = cfg.get("atom_types") or []
    if not types:
        errors.append("atom_types 不能为空")
    for i, t in enumerate(types):
        tid = i + 1
        if t.get("id") != tid:
            errors.append(f"atom_types[{i}].id 应为 {tid} (连续编号)")
        for key in ("name", "charge", "mass", "eps", "sigma"):
            if key not in t:
                errors.append(f"atom_types[{i}] 缺少 {key}")
        for key in ("charge", "mass", "eps", "sigma"):
            v = t.get(key)
            if v is not None and not isinstance(v, (int, float)):
                errors.append(f"atom_types[{i}].{key} 必须为数值")
        conf = t.get("confidence")
        if conf and conf not in CONFIDENCE_LEVELS:
            errors.append(f"atom_types[{i}].confidence 应为 {' / '.join(CONFIDENCE_LEVELS)}")

    geo = cfg.get("geometry") or {}
    if profile == "surface_adsorption":
        surf = geo.get("surface") or {}
        for key in ("a", "nx", "ny", "layers", "occupancy", "charge_per_atom"):
            if key not in surf:
                errors.append(f"geometry.surface 缺少 {key}")
        if surf.get("a", 0) <= 0:
            errors.append("geometry.surface.a 必须为正")
        if not (0 < surf.get("occupancy", 0) <= 1):
            errors.append("geometry.surface.occupancy 必须在 (0, 1]")
        water = geo.get("water") or {}
        for key in ("z_start", "thickness", "grid", "min_dist_surface"):
            if key not in water:
                errors.append(f"geometry.water 缺少 {key}")
        if (water.get("thickness") or 0) <= 0:
            errors.append("geometry.water.thickness 必须为正")
        if "vacuum" not in geo:
            errors.append("geometry 缺少 vacuum")
    elif profile == "solution":
        box = geo.get("box") or {}
        for key in ("x", "y", "z"):
            if (box.get(key) or 0) <= 0:
                errors.append(f"geometry.box.{key} 必须为正")
        if "grid" not in (geo.get("water") or {}):
            errors.append("geometry.water 缺少 grid")
    else:  # clay_cif
        if not cfg.get("cif_file"):
            errors.append("缺少 cif_file")
        sup = cfg.get("supercell") or {}
        for key in ("nx", "ny", "nz"):
            if (sup.get(key) or 0) <= 0:
                errors.append(f"supercell.{key} 必须为正")
        iw = cfg.get("interlayer_water") or {}
        for key in ("target", "grid_xy", "grid_z", "min_dist_o_fw", "min_dist_h_fw"):
            if key not in iw:
                errors.append(f"interlayer_water 缺少 {key}")
        bind = cfg.get("cif_binding") or {}
        for key in ("oh_frac_z_min", "oh_frac_z_max", "z_ob_max", "z_obos_max", "z_oh_min", "z_oh_max"):
            if key not in bind:
                errors.append(f"cif_binding 缺少 {key} (CIF 绑定阈值)")

    ions = cfg.get("ions") or {}
    if (ions.get("conc_mol") or 0) < 0:
        errors.append("ions.conc_mol 不能为负")
    return errors


def ion_type_ids(cfg: dict, cation: str = "Sr", anion: str = "Cl") -> tuple[int, int]:
    """按名称查阳/阴离子类型 id。"""
    ids = {t["name"]: t["id"] for t in cfg["atom_types"]}
    return ids[cation], ids[anion]

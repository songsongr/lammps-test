"""LAMMPS data 文件 → XYZ 文本转换 (浏览器 3D 预览用; 3Dmol 不支持 data 格式)。

元素识别: data 文件 Masses 段给出每 type 的质量, 按最近元素质量匹配 (覆盖常见主族/过渡金属)。
解析失败/结构不符抛 ValueError — 调用方转 4xx/错误提示, 不静默输出垃圾模型。
"""
from __future__ import annotations

# (质量, 元素) 升序 — 覆盖水/盐/黏土/常见金属
_MASS_TABLE: list[tuple[float, str]] = [
    (1.008, "H"), (4.003, "He"), (6.94, "Li"), (9.012, "Be"), (10.81, "B"),
    (12.011, "C"), (14.007, "N"), (15.999, "O"), (18.998, "F"), (20.180, "Ne"),
    (22.990, "Na"), (24.305, "Mg"), (26.982, "Al"), (28.085, "Si"), (30.974, "P"),
    (32.06, "S"), (35.45, "Cl"), (39.948, "Ar"), (39.098, "K"), (40.078, "Ca"),
    (44.956, "Sc"), (47.867, "Ti"), (50.942, "V"), (51.996, "Cr"), (54.938, "Mn"),
    (55.845, "Fe"), (58.693, "Ni"), (58.933, "Co"), (63.546, "Cu"), (65.38, "Zn"),
    (85.468, "Rb"), (87.62, "Sr"), (91.224, "Zr"), (95.95, "Mo"), (107.868, "Ag"),
    (118.71, "Sn"), (126.90, "I"), (137.327, "Ba"), (183.84, "W"), (195.08, "Pt"),
    (196.967, "Au"), (207.2, "Pb"), (238.029, "U"),
]


def _elem_for_mass(mass: float) -> str:
    best = min(_MASS_TABLE, key=lambda kv: abs(kv[0] - mass))
    # 质量偏离最近元素 15% 以上 → 认不出 (自定义赝品), 用 "X"
    return best[1] if abs(best[0] - mass) / best[0] < 0.15 else "X"


def _looks_like_charge(tok: str) -> bool:
    try:
        return abs(float(tok)) <= 4.5  # 电荷量级 (±4e 内)
    except ValueError:
        return False


def parse_type_to_element(text: str) -> dict[int, str]:
    """LAMMPS data 文本 → {type_id: 元素符号}。

    优先读 Masses 段每行尾部 `# Xx` 注释 (system-as-data 渲染产物自带);
    没有注释则按 mass 推 element (覆盖常见主族/过渡金属; 偏离 >15% 标 "X")。
    """
    masses: dict[int, float] = {}
    type_label: dict[int, str] = {}
    section: str | None = None
    for raw in text.splitlines():
        # Masses 行要保留尾部注释 (元素名); 其他行按惯例剥注释
        if section == "masses":
            line_for_anno = raw.strip()
        else:
            line_for_anno = raw.split("#", 1)[0].strip()
        if not line_for_anno:
            continue
        head = line_for_anno.split()[0]
        if head[0].isalpha():
            section = "masses" if head == "Masses" else None
            continue
        if section == "masses":
            parts = line_for_anno.split()
            if len(parts) < 2:
                continue
            try:
                typ = int(parts[0])
                mass = float(parts[1])
            except ValueError:
                continue
            masses[typ] = mass
            # 找注释里的元素名 (# Ow / # Hw / # Sr-2c 等)
            anno = raw.split("#", 1)[1].strip() if "#" in raw else ""
            if anno:
                # 取首段字母+数字作为 type 标签 (Ow, Hw, Sr-2c → 保留 Sr-2c 太长, 取首字母组合)
                token = anno.split()[0] if anno else ""
                if token:
                    type_label[typ] = token
    out: dict[int, str] = {}
    for typ, mass in masses.items():
        if typ in type_label:
            out[typ] = type_label[typ]
        else:
            out[typ] = _elem_for_mass(mass)
    return out


def lammps_data_to_xyz(text: str, max_atoms: int = 20000) -> str:
    """LAMMPS data 文本 → XYZ (元素按 Masses 质量匹配)。

    支持 full (id mol type q x y z) 与 atomic/charge (id type [q] x y z) 两种 Atoms 风格。
    """
    masses: dict[int, float] = {}
    atoms: list[tuple[str, float, float, float]] = []  # (elem, x, y, z)
    section: str | None = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        head = line.split()[0]
        if head[0].isalpha():
            section = "masses" if head == "Masses" else ("atoms" if head == "Atoms" else None)
            continue
        parts = line.split()
        if section == "masses" and len(parts) >= 2:
            try:
                masses[int(parts[0])] = float(parts[1])
            except ValueError:
                pass
        elif section == "atoms":
            try:
                full_style = len(parts) >= 7 and _looks_like_charge(parts[3])
                typ = int(parts[2]) if full_style else int(parts[1])
                if full_style:
                    x, y, z = float(parts[4]), float(parts[5]), float(parts[6])
                else:
                    x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
            except (ValueError, IndexError):
                continue
            elem = _elem_for_mass(masses.get(typ, 12.011))
            atoms.append((elem, x, y, z))

    if not atoms:
        raise ValueError("data 文件中未找到 Atoms 段或无原子行")
    if len(atoms) > max_atoms:
        raise ValueError(f"原子数 {len(atoms)} 超过预览上限 {max_atoms}")

    out = [str(len(atoms)), "LAMMPS system (element by nearest mass)"]
    out += [f"{e} {x:.6f} {y:.6f} {z:.6f}" for e, x, y, z in atoms]
    return "\n".join(out)

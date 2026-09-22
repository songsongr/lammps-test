"""轨迹统计在线分析: per-type z 分布 + MSD (通用, 不假设体系化学)。

复用 common/traj_parser 的帧解析; 纯函数, 服务于工作台详情页「分析」卡
(服务端后台线程计算, 结果缓存到任务工作区 analysis_cache.json)。

输出约定:
  summary: {frames, atoms, types: {type_id: count}}
  z_profile: [{type, label, bins: [{z, freq}]}]  # label = "type_id (elem)" 或纯 type_id
  msd: [{type, label, points: [{step, value}]}]  # per-type + "all"
z 分布的物理含义依赖体系 (吸附/层间等), 前端只呈现, 不解读 — 解读交给项目分析脚本。
"""
from __future__ import annotations

import math
import os

from .traj_parser import parse_lammpstrj

_Z_BINS = 60  # z 直方图 bins
_MSD_MAX_LAG = 50  # MSD 最大时间延迟 (帧数), 控制计算量


def _resolve_type_to_element(traj_path: str, system_data_path: str | None) -> dict[int, str] | None:
    """从 system.data 推 type→elem 映射; 找不到/解析失败 → None (走纯数字 label)。

    默认在工作区根目录找 system.data; 调用方可显式指定。
    """
    from .lammps_data import parse_type_to_element
    path = system_data_path
    if not path:
        guess = os.path.join(os.path.dirname(os.path.abspath(traj_path)), "system.data")
        path = guess if os.path.isfile(guess) else None
    if not path:
        return None
    try:
        return parse_type_to_element(open(path, encoding="utf-8").read())
    except Exception:
        return None


def _label(t: int | str, type2elem: dict[int, str] | None) -> str:
    """生成 z_profile/msd 行的 label: '3 (Sr)' 或 '3' (无 elem 映射时)。"""
    if isinstance(t, str) or type2elem is None or t not in type2elem:
        return str(t)
    return f"{t} ({type2elem[t]})"


def _bin_z(values: list[float], bins: int) -> tuple[list[float], list[int]]:
    lo, hi = min(values), max(values)
    if hi <= lo:
        return [lo], [len(values)]
    width = (hi - lo) / bins
    edges = [lo + i * width for i in range(bins + 1)]
    centers = [(edges[i] + edges[i + 1]) / 2 for i in range(bins)]
    counts = [0] * bins
    for v in values:
        idx = min(int((v - lo) / width), bins - 1)
        counts[idx] += 1
    return centers, counts


def _msd_for(track: dict[int, list[tuple[float, float, float]]], steps: list[float],
             max_lag: int) -> list[dict]:
    """track: atom_id -> [(frame_idx, x, y, z)]; 帧级 MSD (时间平均)。"""
    out = []
    max_len = max((len(tr) for tr in track.values()), default=0)
    for lag in range(1, min(max_lag, max_len - 1) + 1):
        total, n = 0.0, 0
        for traj in track.values():
            for i in range(len(traj) - lag):
                dx = traj[i + lag][1] - traj[i][1]
                dy = traj[i + lag][2] - traj[i][2]
                dz = traj[i + lag][3] - traj[i][3]
                total += dx * dx + dy * dy + dz * dz
                n += 1
        if n == 0:
            continue
        step_idx = min(lag, len(steps) - 1)
        out.append({"step": steps[step_idx] - steps[0] if steps[step_idx] != steps[0] else lag,
                    "lag": lag, "value": total / n})
    return out


def fit_diffusion(points: list[dict], *, late_fraction: float = 0.5) -> dict | None:
    """MSD 末窗线性拟合 → 扩散系数估计 (roadmap #3)。

    返回 {"slope_a2_per_step", "r2", "window"}; 物理单位换算
    (D = slope/(6×dt) → Å²/s, 其中 dt 单位为 s/step) 需要 timestep,
    本层不知道 dt — 只给斜率原值 + R² + 拟合窗口,
    同 dt 的任务间可直接横向比较。点数 < 4 / 窗口太短 / ss_tot 退化 → None。
    """
    if len(points) < 4:
        return None
    xs = [float(p["step"]) for p in points]
    ys = [float(p["value"]) for p in points]
    start = int(len(xs) * (1.0 - late_fraction))
    xs_w, ys_w = xs[start:], ys[start:]
    if len(xs_w) < 3 or xs_w[-1] == xs_w[0]:
        return None
    n = len(xs_w)
    mean_x = sum(xs_w) / n
    mean_y = sum(ys_w) / n
    s_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs_w, ys_w))
    s_xx = sum((x - mean_x) ** 2 for x in xs_w)
    s_yy = sum((y - mean_y) ** 2 for y in ys_w)
    if s_xx <= 0:
        return None
    slope = s_xy / s_xx
    # 常数 MSD (完全不动): OLS 完美预测常数, R² 记 1.0 — D̂=0 是有效物理结果
    r2 = (s_xy * s_xy) / (s_xx * s_yy) if s_yy > 0 else 1.0
    return {"slope_a2_per_step": round(slope, 10), "r2": round(r2, 4),
            "window": [xs_w[0], xs_w[-1]]}


def analyze_trajectory(path: str, *, z_bins: int = _Z_BINS,
                       msd_max_lag: int = _MSD_MAX_LAG,
                       system_data_path: str | None = None) -> dict:
    """计算轨迹统计。大轨迹耗时分钟级 — 调用方应放线程池并提供缓存。

    system_data_path: 解析 type→element 映射的文件路径; 不传则在轨迹同目录找
    system.data; 找不到/解析失败时 z_profile/msd 的 label 退化为纯 type_id。
    """
    frames = parse_lammpstrj(path)
    if not frames:
        raise ValueError("轨迹为空或无法解析")

    type2elem = _resolve_type_to_element(path, system_data_path)

    type_of: dict[int, int] = {}
    track: dict[int, dict[str, list[float]]] = {}
    z_by_type: dict[int, list[float]] = {}

    for fi, frame in enumerate(frames):
        for ai, atom in enumerate(frame["atoms"]):
            aid = int(atom.get("id", ai))
            t = int(atom.get("type", 1))
            type_of[aid] = t
            z_by_type.setdefault(t, []).append(atom["z"])
            # MSD 用非包裹坐标 xu/yu/zu (dump 未输出时回退包裹坐标 — 跨界会有假位移)
            x = atom.get("xu", atom["x"])
            y = atom.get("yu", atom["y"])
            z3 = atom.get("zu", atom["z"])
            track.setdefault(aid, {"f": [], "x": [], "y": [], "z": []})
            track[aid]["f"].append(fi)
            track[aid]["x"].append(x)
            track[aid]["y"].append(y)
            track[aid]["z"].append(z3)

    types = sorted(z_by_type)
    summary = {"frames": len(frames), "atoms": len(type_of),
               "types": {str(t): sum(1 for v in type_of.values() if v == t) for t in types}}

    # z 直方图 (每 type 归一化频数)
    z_profile = []
    for t in types:
        centers, counts = _bin_z(z_by_type[t], z_bins)
        total = sum(counts) or 1
        z_profile.append({
            "type": str(t),
            "label": _label(t, type2elem),
            "bins": [{"z": round(c, 3), "freq": n / total} for c, n in zip(centers, counts)],
        })

    # MSD: 全体 + 每 type (轨迹长度截断到前 200 帧控制计算量, 帧均匀)
    MAX_TRACK_FRAMES = 200
    steps = [float(f.get("timestep", fi)) for fi, f in enumerate(frames)]
    per_type_atoms: dict[int | str, list[int]] = {"all": []}
    for aid, t in type_of.items():
        per_type_atoms.setdefault(t, []).append(aid)
        per_type_atoms["all"].append(aid)

    def _tracks_for(atom_ids: list[int]) -> dict[int, list[tuple[float, float, float]]]:
        out = {}
        for aid in atom_ids:
            tr = track[aid]
            keep = min(len(tr["f"]), MAX_TRACK_FRAMES)
            out[aid] = [(tr["f"][i], tr["x"][i], tr["y"][i], tr["z"][i]) for i in range(keep)]
        return out

    msd = []
    for key in ["all", *types]:
        atoms = per_type_atoms[key]
        tr0 = _tracks_for(atoms[:1])[atoms[0]]  # 帧数上限与全体一致
        frame_steps = [float(frames[min(i, len(frames) - 1)].get("timestep", i)) for i in range(len(tr0))]
        series = _msd_for(_tracks_for(atoms), frame_steps, msd_max_lag)
        msd.append({"type": str(key), "label": _label(key, type2elem), "points": series,
                    "diffusion": fit_diffusion(series)})

    # 首末帧原子坐标 (浏览器 3D 初末对比; 缓存体积 ~原子数 × 2 × 40B)
    def _frame_payload(fi: int) -> list[dict]:
        out = []
        for atom in frames[fi]["atoms"]:
            out.append({"id": int(atom.get("id", 0)), "type": int(atom.get("type", 1)),
                        "x": atom["x"], "y": atom["y"], "z": atom["z"]})
        return out

    frames_3d = {"first": _frame_payload(0), "last": _frame_payload(len(frames) - 1),
                 "timestep_first": frames[0].get("timestep", 0),
                 "timestep_last": frames[-1].get("timestep", 0)}

    return {"summary": summary, "z_profile": z_profile, "msd": msd, "frames_3d": frames_3d,
            "type_labels": {str(t): _label(t, type2elem) for t in types}}

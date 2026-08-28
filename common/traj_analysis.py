"""轨迹统计在线分析: per-type z 分布 + MSD (通用, 不假设体系化学)。

复用 common/traj_parser 的帧解析; 纯函数, 服务于工作台详情页「分析」卡
(服务端后台线程计算, 结果缓存到任务工作区 analysis_cache.json)。

输出约定:
  summary: {frames, atoms, types: {type_id: count}}
  z_profile: [{type, bin, z, count}]   # 每 type 的 z 直方图 (归一化频数)
  msd: [{type, points: [{step, value}]}]  # per-type + "all"; step 为帧序 × dump 间隔近似
z 分布的物理含义依赖体系 (吸附/层间等), 前端只呈现, 不解读 — 解读交给项目分析脚本。
"""
from __future__ import annotations

import math

from .traj_parser import parse_lammpstrj

_Z_BINS = 60  # z 直方图 bins
_MSD_MAX_LAG = 50  # MSD 最大时间延迟 (帧数), 控制计算量


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


def analyze_trajectory(path: str, *, z_bins: int = _Z_BINS,
                       msd_max_lag: int = _MSD_MAX_LAG) -> dict:
    """计算轨迹统计。大轨迹耗时分钟级 — 调用方应放线程池并提供缓存。"""
    frames = parse_lammpstrj(path)
    if not frames:
        raise ValueError("轨迹为空或无法解析")

    type_of: dict[int, int] = {}
    track: dict[int, dict[str, list[float]]] = {}
    z_by_type: dict[int, list[float]] = {}

    for fi, frame in enumerate(frames):
        for ai, atom in enumerate(frame["atoms"]):
            aid = int(atom.get("id", ai))
            t = int(atom.get("type", 1))
            type_of[aid] = t
            z_by_type.setdefault(t, []).append(atom["z"])
            track.setdefault(aid, {"f": [], "x": [], "y": [], "z": []})
            track[aid]["f"].append(fi)
            track[aid]["x"].append(atom["x"])
            track[aid]["y"].append(atom["y"])
            track[aid]["z"].append(atom["z"])

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
        msd.append({"type": str(key), "points": series})

    return {"summary": summary, "z_profile": z_profile, "msd": msd}

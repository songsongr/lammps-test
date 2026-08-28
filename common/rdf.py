"""
径向分布函数 (RDF) 计算 —— numpy 向量化实现。

用法:
    from common.rdf import compute_rdf
    r_vals, g = compute_rdf(positions_a, positions_b, box, dr=0.1, rmax=10.0)

说明:
    - 采用最小镜像约定 (minimum image convention) 处理周期边界
    - 同种原子对 (positions_a is positions_b) 自动排除自身 (i==j),
      避免 r≈0 处的自身伪峰污染首个 bin
    - 归一化: g(r) = count(r, r+dr) / (n_a · ρ_b · 4πr²dr), 其中 ρ_b = n_b / V
    - 相比原 post_process.py 内的 O(N²) 纯 Python 双层循环,
      本实现对每个中心原子做 numpy 广播, 显著加速

算法来源: 标准 RDF 定义 (Allen & Tildesley, Computer Simulation of Liquids)
"""
import numpy as np


def compute_rdf(positions_a, positions_b, box, dr=0.1, rmax=10.0,
                exclude_self=None):
    """
    计算 A-B 原子对间的径向分布函数 g(r)。

    参数:
        positions_a: (n_a, 3) 形状的中心原子坐标序列
        positions_b: (n_b, 3) 形状的伙伴原子坐标序列
        box: (xlo, xhi, ylo, yhi, zlo, zhi) 正交盒边界
        dr: 直方图 bin 宽度 (Angstrom)
        rmax: 最大距离 (Angstrom)
        exclude_self: 是否排除自身对。None 时自动判断:
            当 positions_a 与 positions_b 为同一对象时视为同种, 排除自身。

    返回:
        (r_vals, g) 其中 r_vals 为各 bin 中心距离, g 为对应 g(r) 值
    """
    a = np.asarray(positions_a, dtype=float)
    b = np.asarray(positions_b, dtype=float)

    xlo, xhi, ylo, yhi, zlo, zhi = box
    Lx, Ly, Lz = xhi - xlo, yhi - ylo, zhi - zlo
    vol = Lx * Ly * Lz

    nbins = int(rmax / dr)
    r_vals = np.arange(nbins) * dr + dr / 2
    hist = np.zeros(nbins)

    n_a = a.shape[0]
    n_b = b.shape[0]
    if n_a == 0 or n_b == 0 or vol <= 0:
        return r_vals, hist

    # 同种原子自动排除自身 (调用方传入同一 list/array 引用时)
    if exclude_self is None:
        exclude_self = positions_a is positions_b

    cell = np.array([Lx, Ly, Lz])

    for i in range(n_a):
        d = b - a[i]                          # (n_b, 3) 距离向量
        d -= np.round(d / cell) * cell        # 最小镜像 PBC
        r = np.sqrt(np.einsum("ij,ij->i", d, d))

        if exclude_self:
            # 将自身对 (i==j) 的距离置为 rmax 之外, 使其不计入直方图
            r[i] = rmax + 1.0

        mask = r < rmax
        if np.any(mask):
            hist += np.histogram(r[mask], bins=nbins, range=(0.0, rmax))[0]

    # 归一化: g(r) = count / (n_a · ρ_b · 球壳体积)
    rho_b = n_b / vol
    for i in range(nbins):
        r = r_vals[i]
        shell_vol = 4.0 / 3.0 * np.pi * ((r + dr / 2) ** 3 - (r - dr / 2) ** 3)
        hist[i] /= (n_a * rho_b * shell_vol)

    return r_vals, hist

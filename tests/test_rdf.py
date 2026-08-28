"""RDF 向量化实现的正确性与归一化测试。"""
import numpy as np

from common.rdf import compute_rdf


def naive(pa, pb, box, dr, rmax, exclude_self=False):
    """参考实现: O(N²) 朴素双层循环 (与原 post_process.py 一致)。"""
    xlo, xhi, ylo, yhi, zlo, zhi = box
    Lx, Ly, Lz = xhi - xlo, yhi - ylo, zhi - zlo
    vol = Lx * Ly * Lz
    nb = int(rmax / dr)
    h = np.zeros(nb)
    for ia, A in enumerate(pa):
        for ib, B in enumerate(pb):
            if exclude_self and ia == ib:
                continue
            dx = A[0] - B[0]
            dy = A[1] - B[1]
            dz = A[2] - B[2]
            dx -= round(dx / Lx) * Lx
            dy -= round(dy / Ly) * Ly
            dz -= round(dz / Lz) * Lz
            rr = np.sqrt(dx * dx + dy * dy + dz * dz)
            if rr < rmax:
                h[min(nb - 1, int(rr / dr))] += 1
    rv = np.arange(nb) * dr + dr / 2
    for i in range(nb):
        r = rv[i]
        sh = 4 / 3 * np.pi * ((r + dr / 2) ** 3 - (r - dr / 2) ** 3)
        h[i] /= (len(pa) * len(pb) / vol) * sh
    return rv, h


def _grid(n_side, offset=0.0):
    pts = []
    for i in range(n_side):
        for j in range(n_side):
            for k in range(n_side):
                pts.append([i * 2.0 + offset, j * 2.0 + offset, k * 2.0 + offset])
    return np.array(pts)


def test_matches_naive_cross():
    a = _grid(4)
    b = _grid(4, offset=1.0)
    box = (0.0, 20.0, 0.0, 20.0, 0.0, 20.0)
    rv, gv = compute_rdf(a, b, box, dr=0.2, rmax=8.0)
    rn, hn = naive(a, b, box, dr=0.2, rmax=8.0)
    assert np.max(np.abs(gv - hn)) < 1e-12


def test_matches_naive_same_excl_self():
    a = _grid(4)
    box = (0.0, 20.0, 0.0, 20.0, 0.0, 20.0)
    rv, gv = compute_rdf(a, a, box, dr=0.2, rmax=8.0)
    rn, hn = naive(a, a, box, dr=0.2, rmax=8.0, exclude_self=True)
    assert np.max(np.abs(gv - hn)) < 1e-12


def test_self_pair_excluded():
    # 单原子体系: 排除自身后 g(r) 应全为 0
    a = np.array([[0.0, 0.0, 0.0]])
    box = (0.0, 10.0, 0.0, 10.0, 0.0, 10.0)
    r, g = compute_rdf(a, a, box, dr=0.1, rmax=5.0)
    assert np.all(g == 0.0)


def test_ideal_gas_uniform():
    # 均匀随机分布下 g(r) 应 ≈ 1
    rng = np.random.default_rng(42)
    box = (0.0, 30.0, 0.0, 30.0, 0.0, 30.0)
    a = rng.uniform(0, 30, (2000, 3))
    b = rng.uniform(0, 30, (2000, 3))
    r, g = compute_rdf(a, b, box, dr=0.1, rmax=8.0)
    mid = (r >= 2.0) & (r <= 6.0)
    assert abs(g[mid].mean() - 1.0) < 0.05

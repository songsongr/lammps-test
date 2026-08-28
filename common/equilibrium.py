"""平衡判据定量化 (RadonPy 思想的简化落地): 对 thermo 末段窗口做线性漂移检验。

原理: 平衡态的守衡量 (密度 / 总能量) 在采样窗口内不应有系统性漂移。
对每个可用量取后 window_frac 的样本做线性拟合, 相对漂移 =
|slope × window_step_span| / |mean|, 与阈值比较:
  drift ≤ threshold          → pass
  drift ≤ 5 × threshold      → fair
  否则                        → poor
判级: 全部 pass → good; 有 fair 无 poor → fair; 有 poor → poor; 数据不足/无可用列 → unknown。

温度/压力涨落大, 不作判据 (RadonPy 同样只用量子化阈值可控的分量)。
纯函数, CLI 与工作台同源可用。
"""
from __future__ import annotations

# 量名 (thermo 列匹配不分大小写) → 相对漂移阈值
_TARGETS: dict[str, float] = {"density": 0.001, "toteng": 0.0005}
_WINDOW_FRAC = 0.2
_MIN_SAMPLES = 20  # 窗口内最少样本数, 不足则 unknown
_FAIR_FACTOR = 5.0


def _find_column(columns: list[str], target: str) -> str | None:
    for c in columns:
        if c.lower() == target:
            return c
    return None


def _drift(steps: list[float], values: list[float]) -> float:
    """窗口内线性拟合的相对漂移 (0..inf)。"""
    n = len(values)
    mean = sum(values) / n
    if abs(mean) < 1e-12:
        return float("inf")
    step_span = steps[-1] - steps[0]
    if step_span <= 0:
        return float("inf")
    # 最小二乘斜率
    sx = sum(steps)
    sy = sum(values)
    sxx = sum(x * x for x in steps)
    sxy = sum(x * y for x, y in zip(steps, values))
    denom = n * sxx - sx * sx
    if denom == 0:
        return float("inf")
    slope = (n * sxy - sx * sy) / denom
    return abs(slope) * step_span / abs(mean)


def analyze_equilibrium(thermo: dict, window_frac: float = _WINDOW_FRAC) -> dict:
    """输入 thermo snapshot {columns, rows}, 返回平衡质量判定。"""
    columns: list[str] = thermo.get("columns") or []
    rows: list[list[float]] = thermo.get("rows") or []
    checks: list[dict] = []

    if rows and columns:
        n_total = len(rows)
        win = max(_MIN_SAMPLES, int(n_total * window_frac))
        win = min(win, n_total)
        window = rows[-win:]
        steps = [r[0] for r in window]  # thermo 首列恒为 Step
        for key, threshold in _TARGETS.items():
            col = _find_column(columns, key)
            if col is None:
                continue
            idx = columns.index(col)
            values = [r[idx] for r in window]
            if len([v for v in values if v == v]) < _MIN_SAMPLES:  # NaN 过滤
                continue
            d = _drift(steps, values)
            if d <= threshold:
                verdict = "pass"
            elif d <= threshold * _FAIR_FACTOR:
                verdict = "fair"
            else:
                verdict = "poor"
            checks.append({
                "quantity": col,
                "drift": d,
                "threshold": threshold,
                "verdict": verdict,
                "samples": len(values),
            })

    if not checks:
        return {"status": "unknown", "checks": [], "note": "样本不足或无可判据量 (需要 Density / TotEng)"}
    verdicts = {c["verdict"] for c in checks}
    if "poor" in verdicts:
        status = "poor"
    elif "fair" in verdicts:
        status = "fair"
    else:
        status = "good"
    return {"status": status, "checks": checks, "window_frac": window_frac, "samples": len(rows)}

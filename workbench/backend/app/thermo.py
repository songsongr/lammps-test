"""LAMMPS thermo 输出解析: 识别表头行, 逐行收集数值样本。

规则 (针对日志行设计, 非完整 LAMMPS 解析):
- 表头行: 首列为 "Step" 且所有列都是标识符 ([A-Za-z_][A-Za-z0-9_]*)
- 数据行: 列数与表头一致且全部为数值 → 收录
- 其他行 (空行/Loop time/阶段标记) 结束当前数据块
- 列结构变化 (如 minimize → run) 时重置缓冲, 避免不同量纲混在一起
"""
import re
from collections import deque

_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_NUM = re.compile(r"^-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$")


def _is_header(tokens: list[str]) -> bool:
    return (
        len(tokens) >= 2
        and tokens[0] == "Step"
        and all(_IDENT.fullmatch(t) is not None for t in tokens)
    )


def _is_row(tokens: list[str], n_cols: int) -> bool:
    return len(tokens) == n_cols and all(_NUM.fullmatch(t) is not None for t in tokens)


class ThermoBuffer:
    """单个任务的热力学样本缓冲 (FIFO, 超限丢最旧)。

    replayed: 是否已从日志文件回放过 (后端重启后内存缓冲丢失, 首次访问时回放重建)。
    """

    MAX_ROWS = 5000

    def __init__(self) -> None:
        self.columns: list[str] = []
        self.rows: deque[list[float]] = deque(maxlen=self.MAX_ROWS)
        self.replayed = False

    def feed(self, line: str) -> bool:
        """喂入一行日志; 产生新样本返回 True。"""
        tokens = line.split()
        if not tokens:
            return False
        if _is_header(tokens):
            if tokens != self.columns:  # 列结构变化 → 新数据块, 重置
                self.columns = list(tokens)
                self.rows.clear()
            return False
        if self.columns and _is_row(tokens, len(self.columns)):
            self.rows.append([float(t) for t in tokens])
            return True
        return False

    def snapshot(self, limit: int | None = None) -> dict:
        rows = list(self.rows)
        if limit is not None:
            rows = rows[-limit:]
        return {"columns": list(self.columns), "rows": rows}

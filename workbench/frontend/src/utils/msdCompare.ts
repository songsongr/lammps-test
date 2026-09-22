import type { MsdCompareEntry } from "../api/client";

/** 按实际滞后步数合并曲线；缺失采样点保留为 null，不补值。 */
export function mergeMsdSeries(series: MsdCompareEntry[]): Record<string, number | null>[] {
  const rows = new Map<number, Record<string, number | null>>();
  const ready = series.filter((s) => s.status === "done" && s.msd?.points?.length);
  for (const s of ready) {
    for (const point of s.msd!.points) {
      if (!Number.isFinite(point.step) || !Number.isFinite(point.value)) continue;
      if (!rows.has(point.step)) rows.set(point.step, { step: point.step });
      rows.get(point.step)![s.id] = point.value;
    }
  }
  return Array.from(rows.values())
    .sort((a, b) => a.step! - b.step!)
    .map((row) => {
      for (const s of ready) if (!(s.id in row)) row[s.id] = null;
      return row;
    });
}

/** 展示辅助: 状态映射 / 尺寸 / 耗时格式化 */
import type { JobStatus } from "./api/client";

/** glyph = 形状符号 (色盲可辨第二通道, WCAG 1.4.1 不仅靠颜色传信息);
 *  tone = 语义色 (status-chip.tone-* / badge-soft 同名类) */
export const statusMeta: Record<
  JobStatus,
  { label: string; dot: string; glyph: string; tone: "accent" | "ok" | "err" | "info" | "neutral" }
> = {
  queued: { label: "排队中", dot: "", glyph: "○", tone: "neutral" },
  running: { label: "运行中", dot: "running", glyph: "●", tone: "accent" },
  completed: { label: "已完成", dot: "completed", glyph: "✓", tone: "ok" },
  failed: { label: "失败", dot: "failed", glyph: "✕", tone: "err" },
  canceled: { label: "已取消", dot: "", glyph: "⊘", tone: "neutral" },
  interrupted: { label: "已中断", dot: "", glyph: "◆", tone: "info" },
};

export function fmtSize(n: number): string {
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / 1024 / 1024).toFixed(1)} MB`;
}

/** 任务耗时; 运行中的任务用当前时间估算 */
export function fmtDuration(startedAt: string | null, finishedAt: string | null): string {
  if (!startedAt) return "-";
  const start = new Date(startedAt).getTime();
  const end = finishedAt ? new Date(finishedAt).getTime() : Date.now();
  const s = Math.max(0, Math.round((end - start) / 1000));
  if (s < 60) return `${s} 秒`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m} 分 ${s % 60} 秒`;
  return `${Math.floor(m / 60)} 时 ${m % 60} 分`;
}

/** 精简时间显示: 2026-08-28T03:22:43 → 08-28 03:22:43 */
export function fmtTime(iso: string | null): string {
  if (!iso) return "-";
  const m = iso.match(/^\d{4}-(\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})/);
  return m ? `${m[1]} ${m[2]}` : iso;
}

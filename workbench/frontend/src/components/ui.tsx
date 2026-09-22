/** 共享 UI 小组件: 状态点/状态胶囊/类型胶囊/环境芯片/统计卡 */
import type { ReactNode } from "react";
import type { Health, JobKind, JobStatus } from "../api/client";
import { statusMeta } from "../utils";

export function StatusDot({ status }: { status: JobStatus | "ok" | "bad" }) {
  const cls = status === "ok" || status === "bad" ? status : statusMeta[status as JobStatus].dot;
  return <span className={`sdot ${cls}`} />;
}

export function StatusChip({ status }: { status: JobStatus }) {
  const meta = statusMeta[status];
  return (
    <span className={`status-chip tone-${meta.tone}`}>
      <span className={status === "running" ? "status-glyph live" : "status-glyph"}>
        {meta.glyph}
      </span>
      {meta.label}
    </span>
  );
}

/** 语义色徽章 (Cal.com 借鉴): 形状符号 + 文字 + 颜色三通道 (色觉友好);
 *  running=accent蓝, queued/canceled=neutral灰, completed=ok绿, failed=err红,
 *  interrupted=info蓝 */
export function StatusBadge({ status }: { status: JobStatus }) {
  const meta = statusMeta[status];
  return (
    <span className={`badge-soft ${meta.tone}`}>
      <span className="status-glyph">{meta.glyph}</span>
      {meta.label}
    </span>
  );
}

export function KindChip({ kind }: { kind: JobKind }) {
  if (kind === "build") {
    return <span className="kind-chip kind-build">构建</span>;
  }
  return (
    <span className={`kind-chip ${kind === "lmp" ? "kind-lmp" : "kind-python"}`}>
      {kind === "lmp" ? "LAMMPS" : "Python"}
    </span>
  );
}

/** 顶栏右侧: 容器环境状态 */
export function EnvChip({ health, backendDown }: { health: Health | null; backendDown?: boolean }) {
  if (backendDown) {
    return (
      <span className="env-chip" title="后端进程已退出, 等待重启">
        <StatusDot status="bad" />
        后端已停止
      </span>
    );
  }
  const ok = health?.docker.container_running ?? false;
  return (
    <span className="env-chip" title={health?.docker.container_status ?? "检测中"}>
      <StatusDot status={ok ? "ok" : "bad"} />
      {health === null ? "环境检测中…" : ok ? "lammpsd 运行中" : "容器不可用"}
    </span>
  );
}

/** 统计卡 */
export function StatCard({
  icon,
  tint,
  label,
  children,
}: {
  icon: ReactNode;
  tint: "accent" | "ok" | "err" | "neutral";
  label: string;
  children: ReactNode;
}) {
  return (
    <div className="card stat-card">
      <div className="stat-head">
        <span className="stat-label">{label}</span>
        <span className={`stat-icon tint-${tint}`}>{icon}</span>
      </div>
      <div className="stat-value">{children}</div>
    </div>
  );
}

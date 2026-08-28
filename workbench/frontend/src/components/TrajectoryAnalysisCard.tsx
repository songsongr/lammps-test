/** 轨迹统计在线分析卡: z 分布 + MSD (recharts); 小轨迹同步算, 大轨迹后台触发+轮询 */
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { useCallback, useEffect, useState } from "react";
import { Button } from "antd";
import { ThunderboltOutlined } from "@ant-design/icons";
import { api, type JobDetail, type TrajectoryAnalysis } from "../api/client";

const TYPE_COLORS = ["#3547e8", "#e5484d", "#12994e", "#d97706", "#7c5cbf", "#0e8a8a"];

export default function TrajectoryAnalysisCard({ job }: { job: JobDetail }) {
  const [status, setStatus] = useState<string>("loading");
  const [note, setNote] = useState<string>("");
  const [result, setResult] = useState<TrajectoryAnalysis | null>(null);
  const [working, setWorking] = useState(false);

  const refresh = useCallback(async () => {
    try {
      const r = await api.getAnalysis(job.id);
      setStatus(r.status);
      setNote(r.note || r.error || "");
      if (r.result) setResult(r.result);
      return r;
    } catch (e) {
      setStatus("error");
      setNote(e instanceof Error ? e.message : String(e));
      return null;
    }
  }, [job.id]);

  useEffect(() => {
    if (job.kind !== "lmp" || job.status === "running") return;
    refresh();
  }, [job.id, job.kind, job.status, refresh]);

  const run = async () => {
    setWorking(true);
    try {
      await api.runAnalysis(job.id);
      // 轮询至完成 (最多 ~4 分钟)
      for (let i = 0; i < 60; i++) {
        await new Promise((r) => setTimeout(r, 4000));
        const r = await refresh();
        if (r && (r.status === "done" || r.status === "error")) break;
      }
    } finally {
      setWorking(false);
    }
  };

  if (job.kind !== "lmp") return null;

  return (
    <section className="card card-pad" style={{ marginTop: 16 }}>
      <div className="card-title" style={{ marginBottom: 12, display: "flex", alignItems: "center", gap: 10 }}>
        轨迹统计
        <span className="topbar-sub">z 分布 · MSD (通用统计, 不作科学解读)</span>
        <span style={{ marginLeft: "auto" }}>
          {(status === "done" || status === "idle") && (
            <Button size="small" icon={<ThunderboltOutlined />} loading={working} onClick={run}>
              {status === "done" ? "重新计算" : "计算统计"}
            </Button>
          )}
        </span>
      </div>

      {status === "loading" && <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>检查轨迹…</div>}
      {status === "none" && <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>{note || "工作区无轨迹文件"}</div>}
      {status === "error" && (
        <div style={{ padding: 12, background: "var(--err-weak)", borderRadius: 10, fontSize: 12.5 }}>{note}</div>
      )}
      {status === "running" && <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>后台计算中… (大轨迹约需 1-3 分钟)</div>}
      {status === "idle" && <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>{note}</div>}

      {status === "done" && result && (
        <>
          <div style={{ fontSize: 12, color: "var(--text-2)", marginBottom: 10 }}>
            {result.summary.frames} 帧 · {result.summary.atoms} 原子 · 类型{" "}
            {Object.entries(result.summary.types).map(([t, n]) => `${t}×${n}`).join(" / ")}
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
            <div>
              <div style={{ fontSize: 12.5, fontWeight: 650, marginBottom: 6 }}>z 分布 (频数归一)</div>
              <ResponsiveContainer width="100%" height={220}>
                <LineChart
                  data={result.z_profile[0]?.bins.map((b, i) => {
                    const row: Record<string, number> = { z: b.z };
                    for (const p of result.z_profile) row[p.type] = p.bins[i]?.freq ?? 0;
                    return row;
                  })}
                >
                  <XAxis dataKey="z" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 12 }} />
                  <Legend wrapperStyle={{ fontSize: 11 }} />
                  {result.z_profile.map((p, i) => (
                    <Line key={p.type} type="monotone" dataKey={p.type} dot={false} stroke={TYPE_COLORS[i % TYPE_COLORS.length]} />
                  ))}
                </LineChart>
              </ResponsiveContainer>
            </div>
            <div>
              <div style={{ fontSize: 12.5, fontWeight: 650, marginBottom: 6 }}>MSD (Å²)</div>
              <ResponsiveContainer width="100%" height={220}>
                <LineChart
                  data={result.msd[0]?.points.map((pt, i) => {
                    const row: Record<string, number> = { step: pt.step };
                    for (const m of result.msd) row[m.type] = m.points[i]?.value ?? NaN;
                    return row;
                  })}
                >
                  <XAxis dataKey="step" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 12 }} />
                  <Legend wrapperStyle={{ fontSize: 11 }} />
                  {result.msd.map((m, i) => (
                    <Line key={m.type} type="monotone" dataKey={m.type} dot={false} stroke={TYPE_COLORS[i % TYPE_COLORS.length]} />
                  ))}
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        </>
      )}
    </section>
  );
}

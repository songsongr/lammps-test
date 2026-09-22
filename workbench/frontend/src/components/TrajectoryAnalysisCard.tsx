/** 轨迹统计在线分析卡: z 分布 + MSD (recharts); 小轨迹同步算, 大轨迹后台触发+轮询 */
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { useCallback, useEffect, useRef, useState } from "react";
import { Button, Drawer, message } from "antd";
import { EyeOutlined, ThunderboltOutlined } from "@ant-design/icons";
import { api, type FrameAtom, type JobDetail, type TrajectoryAnalysis } from "../api/client";

const TYPE_COLORS = ["#3547e8", "#e5484d", "#12994e", "#d97706", "#7c5cbf", "#0e8a8a"];

export default function TrajectoryAnalysisCard({ job }: { job: JobDetail }) {
  const [status, setStatus] = useState<string>("loading");
  const [note, setNote] = useState<string>("");
  const [result, setResult] = useState<TrajectoryAnalysis | null>(null);
  const [working, setWorking] = useState(false);
  const [compareOpen, setCompareOpen] = useState(false);
  const mountedRef = useRef(true);

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
    mountedRef.current = true;
    return () => { mountedRef.current = false; };
  }, []);

  useEffect(() => {
    if (job.kind !== "lmp" || job.status === "running") return;
    refresh();
  }, [job.id, job.kind, job.status, refresh]);

  const run = async () => {
    setWorking(true);
    try {
      await api.runAnalysis(job.id);
      // 轮询至完成 (最多 ~4 分钟); 卸载即停
      for (let i = 0; i < 60; i++) {
        await new Promise((r) => setTimeout(r, 4000));
        if (!mountedRef.current) return;
        const r = await refresh();
        if (r && (r.status === "done" || r.status === "error")) break;
      }
    } catch (e) {
      if (mountedRef.current) {
        setStatus("error");
        setNote(e instanceof Error ? e.message : String(e));
        message.error(`分析失败: ${e instanceof Error ? e.message : String(e)}`);
      }
    } finally {
      if (mountedRef.current) setWorking(false);
    }
  };

  if (job.kind !== "lmp") return null;

  return (
    <section className="card card-pad" style={{ marginTop: 16 }}>
      <div className="card-title" style={{ marginBottom: 12, display: "flex", alignItems: "center", gap: 10 }}>
        轨迹统计
        <span className="topbar-sub">z 分布 · MSD (通用统计, 不作科学解读)</span>
        <span style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
          {status === "done" && result?.frames_3d && (
            <Button size="small" icon={<EyeOutlined />} onClick={() => setCompareOpen(true)}>
              3D 初末对比
            </Button>
          )}
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
                    for (const p of result.z_profile) row[p.label || p.type] = p.bins[i]?.freq ?? 0;
                    return row;
                  })}
                >
                  <XAxis dataKey="z" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 12 }} />
                  <Legend wrapperStyle={{ fontSize: 11 }} />
                  {result.z_profile.map((p, i) => (
                    <Line key={p.type} type="monotone" dataKey={p.label || p.type} dot={false} stroke={TYPE_COLORS[i % TYPE_COLORS.length]} />
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
                    for (const m of result.msd) row[m.label || m.type] = m.points[i]?.value ?? NaN;
                    return row;
                  })}
                >
                  <XAxis dataKey="step" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip contentStyle={{ fontSize: 12 }} />
                  <Legend wrapperStyle={{ fontSize: 11 }} />
                  {result.msd.map((m, i) => (
                    <Line key={m.type} type="monotone" dataKey={m.label || m.type} dot={false} stroke={TYPE_COLORS[i % TYPE_COLORS.length]} />
                  ))}
                </LineChart>
              </ResponsiveContainer>
              {result.msd.some((m) => m.diffusion) && (
                <div style={{ fontSize: 11.4, color: "var(--text-2)", marginTop: 4, lineHeight: 1.7 }}>
                  {result.msd.filter((m) => m.diffusion).map((m) => (
                    <span key={m.type} style={{ marginRight: 12 }}>
                      <span style={{ color: "var(--text-1)", fontWeight: 600 }}>{m.label || m.type}</span>
                      : 末窗斜率 = {m.diffusion!.slope_a2_per_step.toExponential(2)} Å²/step
                      (R²={m.diffusion!.r2.toFixed(2)}, 末窗拟合)
                    </span>
                  ))}
                  <div style={{ color: "var(--text-3)" }}>
                    D = 斜率 ÷ (6 × timestep) (先将积分步长换算为秒/step; 结果单位 Å²/s);
                    相同 timestep 的任务可直接比较斜率
                  </div>
                </div>
              )}
            </div>
          </div>
        </>
      )}
      <FrameCompareDrawer
        open={compareOpen}
        onClose={() => setCompareOpen(false)}
        frames={result?.frames_3d}
        jobId={job.id}
      />
    </section>
  );
}

/** 初末态 3D 对比 (3Dmol): 初帧灰线 + 末帧彩色球, 可切换显示。
 *  3Dmol 2.5.5 API 要点: setStyle 只有 (selector, style) 两参 — per-model 样式须
 *  getModel(i).setStyle; hide()/show() 均无参; json (cdjson) 格式要求 {m:[{a:[原子]}]}。 */
function FrameCompareDrawer({ open, onClose, frames, jobId }: {
  open: boolean; onClose: () => void;
  frames?: TrajectoryAnalysis["frames_3d"]; jobId: string;
}) {
  const viewerRef = useRef<HTMLDivElement>(null);
  const viewerInst = useRef<any>(null);
  const [mode, setMode] = useState<"both" | "first" | "last">("both");
  const [err, setErr] = useState<string>("");

  useEffect(() => {
    if (!open || !frames || !viewerRef.current) return;
    setErr("");
    const w = window as any;
    const loadViewer = () => {
      try {
        if (!viewerInst.current) {
          viewerInst.current = w.$3Dmol.createViewer(viewerRef.current, { backgroundColor: "#fcfcfa" });
        }
        const v = viewerInst.current;
        // 移除旧 models 但保留 viewer 本体 (3Dmol 2.5.5 的 clear() 偶尔会留下
        // 内部计数不一致, 改为逐个 removeAllModels 是最稳的)
        v.removeAllModels();
        // 元素标签: 3Dmol 2.5.5 的 cdjson 只支持用 mass 数推元素, 我们的原子没有
        // 元素字段, 统一画成 C 灰骨架即可 (对比侧重位移/重排, 不需要化学着色)
        // 注意: 3Dmol 2.5.5 的解析器会读 m[0].b.length (即使没键合), 所以 b: [] 必填
        const toCdjson = (atoms: FrameAtom[]) =>
          JSON.stringify({ m: [{ a: atoms.map(a => ({ x: a.x, y: a.y, z: a.z, l: "C" })), b: [] }] });
        v.addModel(toCdjson(frames.first), "json");
        v.addModel(toCdjson(frames.last), "json");
        const m0 = v.getModel(0);
        const m1 = v.getModel(1);
        if (m0) m0.setStyle({}, { line: { linewidth: 1 } });
        if (m1) m1.setStyle({}, { sphere: { scale: 0.28 }, stick: { radius: 0.12 } });
        applyMode(v, mode);
        v.zoomTo();
        v.render();
      } catch (e) {
        setErr("渲染失败: " + (e instanceof Error ? e.message : String(e)));
      }
    };
    if (!w.$3Dmol) {
      const s = document.createElement("script");
      s.src = "https://cdn.jsdelivr.net/npm/3dmol@2.5.5/build/3Dmol-min.js";
      s.onload = loadViewer;
      s.onerror = () => setErr("3Dmol CDN 加载失败 (网络问题)");
      document.head.appendChild(s);
    } else loadViewer();
  }, [open, frames]);

  const applyMode = (v: any, m: "both" | "first" | "last") => {
    try {
      const m0 = v.getModel(0);
      const m1 = v.getModel(1);
      if (m0) (m === "last" ? m0.hide() : m0.show());
      if (m1) (m === "first" ? m1.hide() : m1.show());
    } catch {
      // model 索引异常时静默吞掉 (3Dmol 2.5.5 偶发), 下一次 setMode 会重试
    }
  };

  useEffect(() => {
    const v = viewerInst.current;
    if (!v) return;
    applyMode(v, mode);
    try { v.render(); } catch { /* 静默: 渲染失败不影响 UI */ }
  }, [mode]);

  return (
    <Drawer title={`3D 初末态对比 · ${jobId}`} open={open} onClose={onClose} width={680}>
      <div style={{ marginBottom: 10, display: "flex", alignItems: "center", gap: 9 }}>
        <span style={{ fontSize: 12.5, color: "var(--text-2)" }}>
          初帧 (灰线) vs 末帧 (彩色球) — 位移/重排一目了然
        </span>
        <span style={{ flex: 1 }} />
        {(["both", "first", "last"] as const).map(m => (
          <Button key={m} size="small" type={mode === m ? "primary" : "default"}
            onClick={() => setMode(m)}>
            {m === "both" ? "叠加" : m === "first" ? "初帧" : "末帧"}
          </Button>
        ))}
      </div>
      {err && <div style={{ padding: 12, background: "var(--err-weak)", borderRadius: 10, fontSize: 12.5 }}>{err}</div>}
      <div ref={viewerRef} id={`frame3d-viewer-${jobId}`}
        style={{ height: 480, border: "1px solid var(--border)", borderRadius: 12 }} />
      {frames && (
        <div style={{ marginTop: 8, fontSize: 11.5, color: "var(--text-3)", fontFamily: "var(--font-mono)" }}>
          timestep {frames.timestep_first} → {frames.timestep_last} · {frames.first.length} 原子
        </div>
      )}
    </Drawer>
  );
}

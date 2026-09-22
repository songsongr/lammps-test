import { ArrowLeftOutlined, CaretRightOutlined, CopyOutlined, ExportOutlined, ReloadOutlined } from "@ant-design/icons";
import { Checkbox, Popconfirm, Typography, message } from "antd";
import { useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import { api, openJobSocket, type JobDetail as JobDetailData, type ThermoData } from "../api/client";
import JobFiles from "../components/JobFiles";
import TrajectoryAnalysisCard from "../components/TrajectoryAnalysisCard";
import ThermoChart from "../components/ThermoChart";
import { KindChip, StatusBadge } from "../components/ui";
import { buildEquilibriumPrompt, buildFailurePrompt, copyToClipboard } from "../utils/aiPrompt";
import { fmtDuration, fmtTime } from "../utils";

const MAX_LINES = 5000;

interface JobDetailProps {
  jobId: string;
  onBack: () => void;
  onOpenJob: (id: string) => void;
}

/** 任务详情页 v1.8.4: 顶部 sticky 状态条 + 左 8/12 (section 卡堆叠) + 右 4/12 (sticky 指标卡)
 *  (Cal.com 7 色徽章 + shadcn Card 布局, 0 新依赖) */
export default function JobDetail({ jobId, onBack, onOpenJob }: JobDetailProps) {
  const [job, setJob] = useState<JobDetailData | null>(null);
  const [restarts, setRestarts] = useState<{ name: string }[]>([]);
  const [resumeSteps, setResumeSteps] = useState(50000);
  const [resuming, setResuming] = useState(false);
  const [lines, setLines] = useState<string[]>([]);
  const [thermo, setThermo] = useState<ThermoData>({ columns: [], rows: [] });
  const [autoScroll, setAutoScroll] = useState(true);
  const [notFound, setNotFound] = useState(false);
  const [rerunning, setRerunning] = useState(false);
  const [stalledMin, setStalledMin] = useState<number | null>(null);
  const [dockerMetrics, setDockerMetrics] = useState<{
    current: { cpu_pct: number; mem_used_bytes: number; mem_pct: number } | null;
  } | null>(null);
  const lastLogRef = useRef(Date.now());
  const boxRef = useRef<HTMLPreElement | null>(null);

  useEffect(() => {
    let closed = false;
    setJob(null);
    setLines([]);
    setThermo({ columns: [], rows: [] });
    setNotFound(false);

    api
      .job(jobId)
      .then((d) => {
        if (closed) return;
        setJob(d);
        setLines(d.log_tail);
        if (d.thermo?.columns?.length) setThermo(d.thermo);
        if (d.kind === "lmp" && d.workspace && d.status !== "running") {
          api.getRestarts(jobId).then((r) => setRestarts(r.restarts)).catch(() => setRestarts([]));
        } else {
          setRestarts([]);
        }
      })
      .catch(() => setNotFound(true));

    const ws = openJobSocket(jobId, (msg) => {
      if (closed) return;
      if (msg.type === "log") {
        lastLogRef.current = Date.now();
        setStalledMin(null);
        setLines((prev) =>
          prev.length >= MAX_LINES ? [...prev.slice(-MAX_LINES + 1), msg.line] : [...prev, msg.line],
        );
      } else if (msg.type === "status") {
        setJob((j) => (j ? { ...j, status: msg.status, exit_code: msg.exit_code ?? j.exit_code } : j));
        if (msg.status !== "running") {
          api.job(jobId).then((d) => {
            setJob(d);
            // 任务刚到终态: 此时才有检查点 — 补拉 (否则续跑区永不出现, 须重进页面)
            if (d.kind === "lmp" && d.workspace) {
              api.getRestarts(jobId).then((r) => setRestarts(r.restarts)).catch(() => {});
            }
          }).catch(() => {});
        }
      } else if (msg.type === "thermo") {
        if (msg.columns && msg.rows) {
          setThermo({ columns: msg.columns, rows: msg.rows });
        } else if (msg.row) {
          setThermo((prev) =>
            prev.columns.length
              ? {
                  columns: prev.columns,
                  rows: prev.rows.length >= MAX_LINES ? [...prev.rows.slice(1), msg.row!] : [...prev.rows, msg.row!],
                }
              : prev,
          );
        }
      }
    });

    return () => {
      closed = true;
      ws.close();
    };
  }, [jobId]);

  // 容器资源指标 — sticky 右侧卡用
  useEffect(() => {
    let c2 = false;
    const load = () => api.dockerMetrics().then(d => { if (!c2) setDockerMetrics(d); }).catch(() => {});
    load();
    const t = setInterval(load, 5000);
    return () => { c2 = true; clearInterval(t); };
  }, []);

  useEffect(() => {
    if (autoScroll && boxRef.current) {
      boxRef.current.scrollTop = boxRef.current.scrollHeight;
    }
  }, [lines, autoScroll]);

  // 运行中任务 2 分钟无任何日志输出 → 提示可能不收敛/被阻塞
  const status = job?.status;
  useEffect(() => {
    const t = setInterval(() => {
      if (status !== "running") {
        setStalledMin(null);
        return;
      }
      const idleMs = Date.now() - lastLogRef.current;
      setStalledMin(idleMs > 120_000 ? Math.max(1, Math.round(idleMs / 60_000)) : null);
    }, 15_000);
    return () => clearInterval(t);
  }, [status]);

  // 进度估算: thermo 行数 / 期望总行数 (无期望时按 max 500 行粗估)
  // 必须在条件 return 之前 (hooks 规则: 顺序稳定)
  const totalRows = thermo.rows.length;
  const progressPct = useMemo(() => {
    if (!job || job.status !== "running") return totalRows > 0 ? 100 : 0;
    return Math.min(99, Math.round((totalRows / 500) * 100));
  }, [job?.status, totalRows]);

  if (notFound) {
    return (
      <div className="card card-pad" style={{ textAlign: "center", padding: 48 }}>
        <div style={{ fontSize: 15, fontWeight: 620, marginBottom: 6 }}>任务不存在或已被清理</div>
        <div style={{ fontSize: 13, color: "var(--text-2)", marginBottom: 18 }}>{jobId}</div>
        <button className="mini-btn" onClick={onBack}>
          返回任务列表
        </button>
      </div>
    );
  }
  if (!job) {
    return <div className="card" style={{ height: 300 }} />;
  }

  const doResume = async () => {
    const steps = Math.max(1, Math.round(resumeSteps || 0));
    if (steps !== resumeSteps) setResumeSteps(steps);
    setResuming(true);
    try {
      const nj = await api.resumeJob(job.id, steps, job.omp_threads);
      message.success(`续跑任务 ${nj.id} 已发起 (源检查点: ${(nj as { source_restart?: string }).source_restart ?? "latest"})`);
      onOpenJob(nj.id);
    } catch (e) {
      message.error(`续跑失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setResuming(false);
    }
  };

  const doCancel = async () => {
    try {
      const updated = await api.cancelJob(job.id);
      setJob((j) => (j ? { ...j, status: updated.status, exit_code: updated.exit_code } : j));
      message.success("已发送取消请求");
    } catch (e) {
      message.error(`取消失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  };

  const doRerun = async () => {
    setRerunning(true);
    try {
      const created = await api.createJob(job.project_id, job.script, job.kind, job.omp_threads);
      message.success(`新任务 ${created.id} 已启动`);
      onOpenJob(created.id);
    } catch (e) {
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setRerunning(false);
    }
  };

  // 进度估算: thermo 行数 / 期望总行数 (无期望时按 max 500 行粗估)
  // ↑ 移到条件 return 之前 (hooks 规则)

  const fmtMB = (b: number) =>
    b < 1024 ** 2 ? `${(b / 1024).toFixed(0)} KB`
      : b < 1024 ** 3 ? `${(b / 1024 ** 2).toFixed(1)} MB`
        : `${(b / 1024 ** 3).toFixed(2)} GB`;

  return (
    <div>
      {/* --- 顶部 sticky 状态条 (Cal.com 借鉴) ---------------------- */}
      <div className="sticky-status">
        <button className="back-btn" onClick={onBack} title="返回任务列表" style={{ height: 32, width: 32 }}>
          <ArrowLeftOutlined style={{ fontSize: 13 }} />
        </button>
        <span className="id-mono" title={job.id}>job-{job.id.slice(0, 8)}</span>
        <StatusBadge status={job.status} />
        <KindChip kind={job.kind} />
        <div className="progress-track" title={job.status === "running" ? `thermo 样本 ${totalRows} 行` : "已结束"}>
          <div className="progress-fill" style={{ width: `${progressPct}%` }} />
        </div>
        <span style={{ fontSize: 11.5, color: "var(--text-3)", fontFeatureSettings: '"tnum"' }}>
          {job.status === "running" ? `${totalRows} 行 / LIVE` : `${totalRows} 行 / ENDED`}
        </span>
      </div>

      {/* --- 主区 2 列: 左 8/12 (section 卡堆叠) + 右 4/12 (sticky 指标) --- */}
      <div style={{ display: "grid", gridTemplateColumns: "minmax(0, 8fr) minmax(0, 4fr)", gap: 16 }}>
        {/* ============ 左主区 ============ */}
        <div style={{ display: "flex", flexDirection: "column", gap: 16, minWidth: 0 }}>

          {/* ---- 参数卡 ---- */}
          <section className="card card-pad">
            <div className="section-header">
              <span>任务参数</span>
              <span className="sub" style={{ display: "inline-flex", gap: 6, marginLeft: "auto" }}>
                <a
                  className="mini-btn"
                  href={`/api/jobs/${job.id}/export`}
                  download
                  title="下载溯源 zip: 任务记录+环境指纹+脚本+体系快照+日志尾部"
                >
                  <ExportOutlined /> 溯源包
                </a>
                <button className="mini-btn" onClick={() => onOpenJob(job.id)} title="在任务列表中查看">
                  <ReloadOutlined /> 刷新
                </button>
              </span>
            </div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0 28px" }}>
              <MetaRow label="项目" value={<span>{job.project_name}</span>} />
              <MetaRow label="脚本" value={<span className="mono" title={job.script}>{job.script}</span>} />
              <MetaRow label="类型" value={job.kind === "lmp" ? "LAMMPS (容器)" : "Python (本地)"} />
              <MetaRow label="退出码" value={job.exit_code ?? "-"} />
              <MetaRow label="开始" value={<span className="muted">{fmtTime(job.started_at)}</span>} />
              <MetaRow label="结束" value={<span className="muted">{fmtTime(job.finished_at)}</span>} />
              <MetaRow label="耗时" value={<span className="muted">{fmtDuration(job.started_at, job.finished_at)}</span>} />
              <MetaRow label="OMP 线程" value={job.omp_threads} />
              <MetaRow label="命令" value={<span className="mono" title={job.command} style={{ fontSize: 11.5, wordBreak: "break-all" }}>{job.command}</span>} fullRow />
              <MetaRow label="日志文件" value={
                <>
                  <span className="mono" title={job.log_path ?? ""} style={{ fontSize: 11.5 }}>
                    {job.log_path ?? "-"}
                  </span>
                  {job.log_path && (
                    <Typography.Text copyable={{ text: job.log_path }} style={{ color: "var(--text-3)", fontSize: 12 }} />
                  )}
                </>
              } fullRow />
              <MetaRow label="工作区" value={
                job.workspace ? (
                  <>
                    <span className="mono" title={job.workspace} style={{ fontSize: 11.5 }}>
                      {job.workspace}
                    </span>
                    <Typography.Text copyable={{ text: job.workspace }} style={{ color: "var(--text-3)", fontSize: 12 }} />
                  </>
                ) : <span className="muted">-</span>
              } fullRow />
              {job.fingerprint && (
                <MetaRow label="环境指纹" value={
                  <span className="mono" style={{ fontSize: 11.5, color: "var(--text-3)", wordBreak: "break-all" }}
                    title={JSON.stringify(job.fingerprint, null, 2)}>
                    {[
                      job.fingerprint.system_sha ? `system:${job.fingerprint.system_sha}` : null,
                      job.fingerprint.image ? `image:${job.fingerprint.image}` : null,
                      job.fingerprint.image_id ? `id:${job.fingerprint.image_id}` : null,
                      job.fingerprint.lmp_version ? `lmp:${job.fingerprint.lmp_version.slice(0, 60)}` : null,
                    ].filter(Boolean).join(" · ")}
                  </span>
                } fullRow />
              )}
            </div>
          </section>

          {/* ---- 热力学曲线 ---- */}
          {thermo.columns.length > 0 && thermo.rows.length > 0 && (
            <section className="card card-pad">
              <div className="section-header">
                <span>热力学曲线</span>
                <span className="sub" style={{ display: "inline-flex", gap: 9, alignItems: "center" }}>
                  {job.equilibrium && job.equilibrium.status !== "unknown" && (
                    <>
                      <span
                        title={(job.equilibrium.checks || [])
                          .map(c => `${c.quantity}: 漂移 ${(c.drift * 100).toFixed(3)}% (阈值 ${(c.threshold * 100).toFixed(3)}%)`)
                          .join("\n")}
                        className={"badge-soft " + (
                          job.equilibrium.status === "good" ? "ok"
                            : job.equilibrium.status === "fair" ? "warn"
                              : "err"
                        )}
                      >
                        {job.equilibrium.status === "good" ? "已平衡" : job.equilibrium.status === "fair" ? "接近平衡" : "未收敛"}
                      </span>
                      <button
                        className="mini-btn"
                        title="打包平衡判据+thermo 尾部样本为结构化提示词, 粘贴给 AI 编码代理解读"
                        onClick={async () => {
                          try {
                            await copyToClipboard(buildEquilibriumPrompt(job, job.equilibrium!, thermo));
                            message.success("平衡分析提示词已复制 — 粘贴给 ZCode 即可解读");
                          } catch (e) {
                            message.error(e instanceof Error ? e.message : String(e));
                          }
                        }}
                      >
                        <CopyOutlined style={{ marginRight: 5 }} />
                        复制 AI 分析提示词
                      </button>
                    </>
                  )}
                  <span>共 {thermo.rows.length} 行 · {job.status === "running" ? "实时更新" : "已结束"}</span>
                </span>
              </div>
              <ThermoChart data={thermo} />
            </section>
          )}

          {/* ---- 失败诊断 (单独浮起 + 左侧 3px 红条) ---- */}
          {job.status === "failed" && job.failure && (
            <section className="failure-card-float">
              <div className="section-header">
                <span style={{ color: "var(--err)" }}>失败解析 · {job.failure.summary}</span>
                <span className="sub" style={{ display: "inline-flex", gap: 8, alignItems: "center" }}>
                  <span className={"badge-soft " + (
                    job.failure.severity === "high" ? "err"
                      : job.failure.severity === "medium" ? "warn"
                        : "neutral"
                  )}>
                    {job.failure.severity === "high" ? "高" : job.failure.severity === "medium" ? "中" : "低"}风险
                  </span>
                  {job.failure.can_resume && (
                    <span className="badge-soft ok">存在续跑策略</span>
                  )}
                  <button
                    className="mini-btn"
                    title="打包失败解析+日志尾部+环境指纹为结构化提示词, 粘贴给 AI 编码代理即可开工修复"
                    onClick={async () => {
                      try {
                        await copyToClipboard(buildFailurePrompt(job, job.failure!));
                        message.success("AI 分析提示词已复制 — 粘贴给 ZCode 即可开工");
                      } catch (e) {
                        message.error(e instanceof Error ? e.message : String(e));
                      }
                    }}
                  >
                    <CopyOutlined style={{ marginRight: 5 }} />
                    复制 AI 分析提示词
                  </button>
                </span>
              </div>
              {(job.failure.error_line || job.failure.detail_line) && (
                <pre className="failure-err">
                  {[job.failure.error_line, job.failure.detail_line].filter(Boolean).join("\n")}
                </pre>
              )}
              <div className="failure-hint">{job.failure.hint}</div>
              {job.failure.actions?.length > 0 && (
                <div style={{ marginTop: 10 }}>
                  <div style={{ fontSize: 12, fontWeight: 650, color: "var(--text-2)", marginBottom: 6 }}>
                    建议动作
                  </div>
                  <ol style={{ margin: 0, paddingLeft: 20, fontSize: 12.6, lineHeight: 1.9 }}>
                    {job.failure.actions.map((a, i) => (
                      <li key={i}>{a}</li>
                    ))}
                  </ol>
                </div>
              )}
            </section>
          )}

          {/* ---- 产物文件 ---- */}
          {job.workspace && (
            <section className="card card-pad">
              <div className="section-header">
                <span>产物文件</span>
                <span className="sub mono" style={{ fontSize: 11.5 }}>{job.workspace}</span>
              </div>
              <JobFiles jobId={job.id} />
            </section>
          )}

          {/* ---- 轨迹统计 ---- */}
          {job.status !== "running" && <TrajectoryAnalysisCard job={job} />}

          {/* ---- 检查点续跑 ---- */}
          {restarts.length > 0 && (
            <section className="card card-pad">
              <div className="section-header">
                <span>检查点续跑</span>
                <span className="sub">{restarts.length} 个检查点 · {restarts[0]?.name} (最新)</span>
              </div>
              <div style={{ display: "flex", gap: 9, alignItems: "center" }}>
                <span style={{ fontSize: 12.5, color: "var(--text-2)" }}>继续</span>
                <input
                  className="sys-input"
                  type="number"
                  style={{ width: 110 }}
                  value={resumeSteps}
                  min={1}
                  onChange={(e) => setResumeSteps(parseInt(e.target.value || "0", 10) || 0)}
                />
                <span style={{ fontSize: 12.5, color: "var(--text-2)" }}>步 (read_restart 后接跑)</span>
                <button className="mini-btn accent" disabled={resuming} onClick={doResume}>
                  {resuming ? "发起中…" : "发起续跑任务"}
                </button>
              </div>
              <div style={{ fontSize: 11.5, color: "var(--text-3)", marginTop: 7 }}>
                read_restart 恢复体系与力场; fix 定义从原脚本提取重建。续跑产物在新任务工作区, 与源任务 {job.id} 关联。
              </div>
            </section>
          )}

          {/* ---- 实时日志 (留在主区底部, 不下沉) ---- */}
          <div>
            <div className="log-toolbar" style={{ margin: "4px 0 10px" }}>
              <span className="label">
                实时日志
                {job.status === "running" ? (
                  <span className="log-live on" style={{ margin: 0 }}>
                    <span className="sdot running" />
                    LIVE
                  </span>
                ) : (
                  <span className="log-live" style={{ margin: 0 }}>
                    ENDED
                  </span>
                )}
                {stalledMin !== null && (
                  <span style={{ color: "var(--err)", fontWeight: 600 }}>
                    ⚠ 输出已停滞约 {stalledMin} 分钟 — 任务可能不收敛或被阻塞
                  </span>
                )}
              </span>
              <Checkbox checked={autoScroll} onChange={(e) => setAutoScroll(e.target.checked)}>
                自动滚动
              </Checkbox>
            </div>
            <div className="log-shell">
              <div className="log-titlebar">
                <span className="traffic">
                  <span />
                  <span />
                  <span />
                </span>
                <span className="log-title">log · job-{job.id}</span>
                <span className={`log-live ${job.status === "running" ? "on" : ""}`}>
                  <span className={`sdot ${job.status === "running" ? "running" : ""}`} />
                  {job.status === "running" ? "STREAMING" : "CLOSED"}
                </span>
              </div>
              <pre ref={boxRef} className="log-viewer">
                {lines.length ? lines.join("\n") : "（暂无输出）"}
              </pre>
            </div>
          </div>
        </div>

        {/* ============ 右 sticky 指标区 ============ */}
        <aside style={{ display: "flex", flexDirection: "column", gap: 16, position: "sticky", top: 134, alignSelf: "start", minWidth: 0 }}>
          <section className="card card-pad">
            <div className="section-header">
              <span>任务指标</span>
              <span className="sub">实时</span>
            </div>
            <MetricRow label="进度" value={
              <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                <div className="progress-track" style={{ flex: 1, height: 4 }}>
                  <div className="progress-fill" style={{ width: `${progressPct}%` }} />
                </div>
                <span style={{ fontSize: 12, fontFeatureSettings: '"tnum"', color: "var(--text-2)", minWidth: 30, textAlign: "right" }}>
                  {progressPct}%
                </span>
              </div>
            } />
            <MetricRow label="耗时" value={
              <span className="mono" style={{ fontSize: 12.5 }}>
                {fmtDuration(job.started_at, job.finished_at)}
              </span>
            } />
            <MetricRow label="ETA" value={
              <span style={{ fontSize: 12, color: "var(--text-2)" }}>
                {job.status === "running" ? "运行中, 无终点" : job.status === "queued" ? "排队中" : "已结束"}
              </span>
            } />
            <MetricRow label="thermo 样本" value={
              <span className="mono" style={{ fontSize: 12.5 }}>{thermo.rows.length}<span style={{ color: "var(--text-3)" }}> 行</span></span>
            } />
            <MetricRow label="OMP 线程" value={
              <span className="mono" style={{ fontSize: 12.5 }}>{job.omp_threads}</span>
            } />
            <MetricRow label="退出码" value={
              <span className="mono" style={{ fontSize: 12.5, color: job.exit_code && job.exit_code !== 0 ? "var(--err)" : "var(--text-2)" }}>
                {job.exit_code ?? "-"}
              </span>
            } />
          </section>

          <section className="card card-pad">
            <div className="section-header">
              <span>系统信息</span>
              <span className="sub">容器资源</span>
            </div>
            <MetricRow label="容器 CPU" value={
              dockerMetrics?.current ? (
                <span className="mono" style={{ fontSize: 12.5 }}>
                  {dockerMetrics.current.cpu_pct.toFixed(1)}<span style={{ color: "var(--text-3)" }}>%</span>
                </span>
              ) : <span style={{ fontSize: 11.5, color: "var(--text-3)" }}>采样中…</span>
            } />
            <MetricRow label="容器内存" value={
              dockerMetrics?.current ? (
                <span className="mono" style={{ fontSize: 12.5 }}>
                  {fmtMB(dockerMetrics.current.mem_used_bytes)}<span style={{ color: "var(--text-3)" }}> ({dockerMetrics.current.mem_pct.toFixed(1)}%)</span>
                </span>
              ) : <span style={{ fontSize: 11.5, color: "var(--text-3)" }}>采样中…</span>
            } />
            {job.fingerprint && (
              <>
                <MetricRow label="镜像" value={
                  <span className="mono" style={{ fontSize: 11.5, color: "var(--text-2)" }}>
                    {job.fingerprint.image ?? "-"}
                  </span>
                } />
                <MetricRow label="LAMMPS" value={
                  <span className="mono" style={{ fontSize: 11, color: "var(--text-2)", wordBreak: "break-all" }}>
                    {job.fingerprint.lmp_version?.slice(0, 40) ?? "-"}
                  </span>
                } />
              </>
            )}
          </section>

          <section className="card card-pad">
            <div className="section-header">
              <span>环境指纹</span>
              <span className="sub">可复现性</span>
            </div>
            {job.fingerprint ? (
              <div className="mono" style={{ fontSize: 11.5, color: "var(--text-2)", lineHeight: 1.7, wordBreak: "break-all" }}>
                {job.fingerprint.system_sha && <div>system: {job.fingerprint.system_sha}</div>}
                {job.fingerprint.image_id && <div>id: {job.fingerprint.image_id}</div>}
              </div>
            ) : (
              <div style={{ fontSize: 11.5, color: "var(--text-3)" }}>未记录</div>
            )}
          </section>

          <section className="card card-pad">
            <div className="section-header">
              <span>AI 桥</span>
              <span className="sub">一键复制提示词</span>
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              {job.equilibrium && job.equilibrium.status !== "unknown" && (
                <button className="action-btn" onClick={async () => {
                  try {
                    await copyToClipboard(buildEquilibriumPrompt(job, job.equilibrium!, thermo));
                    message.success("平衡分析提示词已复制");
                  } catch (e) { message.error(e instanceof Error ? e.message : String(e)); }
                }}>
                  <CopyOutlined />
                  复制平衡分析
                </button>
              )}
              {job.failure && (
                <button className="action-btn" onClick={async () => {
                  try {
                    await copyToClipboard(buildFailurePrompt(job, job.failure!));
                    message.success("失败分析提示词已复制");
                  } catch (e) { message.error(e instanceof Error ? e.message : String(e)); }
                }}>
                  <CopyOutlined />
                  复制失败分析
                </button>
              )}
              {!job.equilibrium && !job.failure && (
                <div style={{ fontSize: 11.5, color: "var(--text-3)", lineHeight: 1.7 }}>
                  任务运行结束后, 这里会出现「平衡分析」或「失败分析」提示词, 一键粘贴给 ZCode 即可解读或修复。
                </div>
              )}
            </div>
          </section>

          {/* 操作行 (放最底部便于发现) */}
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {job.status !== "running" && job.status !== "interrupted" && (
              <Popconfirm
                title="再次运行该任务？"
                description={`将以相同参数 (${job.script}) 发起一个新任务, 不影响本次结果`}
                onConfirm={doRerun}
                okText="发起任务"
                cancelText="算了"
              >
                <button className="action-btn primary" disabled={rerunning} style={{ width: "100%" }}>
                  <CaretRightOutlined />
                  {rerunning ? "启动中…" : "再次运行"}
                </button>
              </Popconfirm>
            )}
            {(job.status === "running" || job.status === "interrupted") && (
              <Popconfirm title="确认取消该任务？" onConfirm={doCancel} okText="取消任务" cancelText="返回">
                <button className="action-btn danger" style={{ width: "100%" }}>
                  {job.status === "interrupted" ? "清理残留" : "取消任务"}
                </button>
              </Popconfirm>
            )}
          </div>
        </aside>
      </div>
    </div>
  );
}

/* ============================================================
   小工具
   ============================================================ */

/** 左主区 MetaRow: label + value, fullRow 时跨整行 */
function MetaRow({ label, value, fullRow }: { label: string; value: ReactNode; fullRow?: boolean }) {
  return (
    <div className="kv-row" style={{ gridColumn: fullRow ? "1 / -1" : undefined }}>
      <span className="kv-label">{label}</span>
      <span className="kv-value">{value}</span>
    </div>
  );
}

/** 右 sticky 指标行: label 左, value 右 */
function MetricRow({ label, value }: { label: string; value: ReactNode }) {
  return (
    <div style={{
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      gap: 12,
      padding: "10px 0",
      borderBottom: "1px dashed var(--border)",
    }}>
      <span style={{ fontSize: 11.5, color: "var(--text-3)", flex: "none" }}>{label}</span>
      <span style={{ fontSize: 12.5, minWidth: 0, textAlign: "right", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
        {value}
      </span>
    </div>
  );
}
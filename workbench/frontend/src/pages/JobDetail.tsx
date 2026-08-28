import { ArrowLeftOutlined, CaretRightOutlined, CopyOutlined } from "@ant-design/icons";
import { Checkbox, Popconfirm, Typography, message } from "antd";
import { useEffect, useRef, useState, type ReactNode } from "react";
import { api, openJobSocket, type JobDetail as JobDetailData, type ThermoData } from "../api/client";
import JobFiles from "../components/JobFiles";
import TrajectoryAnalysisCard from "../components/TrajectoryAnalysisCard";
import ThermoChart from "../components/ThermoChart";
import { KindChip, StatusChip } from "../components/ui";
import { buildEquilibriumPrompt, buildFailurePrompt, copyToClipboard } from "../utils/aiPrompt";
import { fmtDuration, fmtTime } from "../utils";

const MAX_LINES = 5000;

interface JobDetailProps {
  jobId: string;
  onBack: () => void;
  onOpenJob: (id: string) => void;
}

/** 任务详情页: 元信息 + thermo 曲线 + 产物浏览 + WebSocket 实时日志 */
export default function JobDetail({ jobId, onBack, onOpenJob }: JobDetailProps) {
  const [job, setJob] = useState<JobDetailData | null>(null);
  const [lines, setLines] = useState<string[]>([]);
  const [thermo, setThermo] = useState<ThermoData>({ columns: [], rows: [] });
  const [autoScroll, setAutoScroll] = useState(true);
  const [notFound, setNotFound] = useState(false);
  const [rerunning, setRerunning] = useState(false);
  const [stalledMin, setStalledMin] = useState<number | null>(null);
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
          api.job(jobId).then(setJob).catch(() => {});
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

  const metaCell = (label: string, value: ReactNode, span?: number) => (
    <div className="meta-cell" style={span ? { gridColumn: `span ${span}` } : undefined}>
      <div className="meta-label">{label}</div>
      <div className="meta-value">{value}</div>
    </div>
  );

  return (
    <div>
      <div className="detail-head">
        <button className="back-btn" onClick={onBack} title="返回任务列表">
          <ArrowLeftOutlined />
        </button>
        <div className="detail-title">
          任务 <span className="mono">{job.id}</span>
          <StatusChip status={job.status} />
          <KindChip kind={job.kind} />
        </div>
        <div style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
          {job.status !== "running" && job.status !== "interrupted" && (
            <Popconfirm
              title="再次运行该任务？"
              description={`将以相同参数 (${job.script}) 发起一个新任务, 不影响本次结果`}
              onConfirm={doRerun}
              okText="发起任务"
              cancelText="算了"
            >
              <button className="mini-btn accent" disabled={rerunning}>
                <CaretRightOutlined style={{ marginRight: 5 }} />
                {rerunning ? "启动中…" : "再次运行"}
              </button>
            </Popconfirm>
          )}
          {(job.status === "running" || job.status === "interrupted") && (
            <Popconfirm title="确认取消该任务？" onConfirm={doCancel} okText="取消任务" cancelText="返回">
              <button className="mini-btn danger">
                {job.status === "interrupted" ? "清理残留" : "取消任务"}
              </button>
            </Popconfirm>
          )}
        </div>
      </div>

      <section className="card">
        <div className="detail-meta">
          {metaCell("项目", job.project_name)}
          {metaCell(
            "脚本",
            <span className="mono" title={job.script}>
              {job.script}
            </span>,
          )}
          {metaCell("类型", job.kind === "lmp" ? "LAMMPS (容器)" : "Python (本地)")}
          {metaCell("退出码", job.exit_code ?? "-")}
          {metaCell("开始", <span className="muted">{fmtTime(job.started_at)}</span>)}
          {metaCell("结束", <span className="muted">{fmtTime(job.finished_at)}</span>)}
          {metaCell("耗时", <span className="muted">{fmtDuration(job.started_at, job.finished_at)}</span>)}
          {metaCell("命令", <span className="mono" title={job.command}>{job.command}</span>)}
          <div className="meta-cell" style={{ gridColumn: "span 2" }}>
            <div className="meta-label">日志文件</div>
            <div className="meta-value">
              <span className="mono" title={job.log_path ?? ""}>
                {job.log_path ?? "-"}
              </span>
              <Typography.Text
                copyable={{ text: job.log_path ?? "" }}
                style={{ color: "var(--text-3)", fontSize: 12 }}
              />
            </div>
          </div>
          <div className="meta-cell" style={{ gridColumn: "span 2" }}>
            <div className="meta-label">工作区</div>
            <div className="meta-value">
              {job.workspace ? (
                <>
                  <span className="mono" title={job.workspace}>
                    {job.workspace}
                  </span>
                  <Typography.Text
                    copyable={{ text: job.workspace }}
                    style={{ color: "var(--text-3)", fontSize: 12 }}
                  />
                </>
              ) : (
                <span className="muted">-</span>
              )}
            </div>
          </div>
          {job.fingerprint && (
            <div className="meta-cell" style={{ gridColumn: "span 4" }}>
              <div className="meta-label">环境指纹</div>
              <div className="meta-value">
                <span
                  className="mono"
                  style={{ fontSize: 11.5, color: "var(--text-3)", wordBreak: "break-all" }}
                  title={JSON.stringify(job.fingerprint, null, 2)}
                >
                  {[
                    job.fingerprint.system_sha ? `system:${job.fingerprint.system_sha}` : null,
                    job.fingerprint.image ? `image:${job.fingerprint.image}` : null,
                    job.fingerprint.image_id ? `id:${job.fingerprint.image_id}` : null,
                    job.fingerprint.lmp_version ? `lmp:${job.fingerprint.lmp_version.slice(0, 60)}` : null,
                  ].filter(Boolean).join(" · ")}
                </span>
              </div>
            </div>
          )}
        </div>
      </section>

      {thermo.columns.length > 0 && thermo.rows.length > 0 && (
        <section className="card card-pad" style={{ marginTop: 16 }}>
          <div className="card-title" style={{ marginBottom: 12, display: "flex", alignItems: "center", gap: 9 }}>
            热力学曲线
            {job.equilibrium && job.equilibrium.status !== "unknown" && (
              <>
                <span
                  title={(job.equilibrium.checks || [])
                    .map(c => `${c.quantity}: 漂移 ${(c.drift * 100).toFixed(3)}% (阈值 ${(c.threshold * 100).toFixed(3)}%)`)
                    .join("\n")}
                  style={{
                    fontSize: 11, fontWeight: 650, padding: "2px 9px", borderRadius: 999,
                    color: "#fff",
                    background:
                      job.equilibrium.status === "good" ? "var(--ok)"
                        : job.equilibrium.status === "fair" ? "#d97706" : "var(--err)",
                  }}
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
            <span className="topbar-sub" style={{ marginLeft: "auto" }}>
              共 {thermo.rows.length} 行 · {job.status === "running" ? "实时更新" : "已结束"}
            </span>
          </div>
          <ThermoChart data={thermo} />
        </section>
      )}

      {job.status === "failed" && job.failure && (
        <section className="card card-pad failure-card" style={{ marginTop: 16 }}>
          <div className="card-title" style={{ display: "flex", alignItems: "center", gap: 9 }}>
            失败解析 · {job.failure.summary}
            <span
              style={{
                fontSize: 11,
                fontWeight: 650,
                padding: "2px 9px",
                borderRadius: 999,
                color: "#fff",
                background:
                  job.failure.severity === "high"
                    ? "var(--err)"
                    : job.failure.severity === "medium"
                      ? "#d97706"
                      : "var(--text-3)",
              }}
            >
              {job.failure.severity === "high" ? "高" : job.failure.severity === "medium" ? "中" : "低"}风险
            </span>
            {job.failure.can_resume && (
              <span
                style={{
                  fontSize: 11,
                  fontWeight: 600,
                  padding: "2px 9px",
                  borderRadius: 999,
                  color: "var(--ok)",
                  background: "var(--ok-weak)",
                }}
              >
                存在续跑策略
              </span>
            )}
            <button
              className="mini-btn"
              style={{ marginLeft: "auto" }}
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

      {job.workspace && (
        <section className="card card-pad" style={{ marginTop: 16 }}>
          <div className="card-title" style={{ marginBottom: 12 }}>
            产物文件
            <span className="topbar-sub" style={{ marginLeft: 10 }}>
              {job.workspace}
            </span>
          </div>
          <JobFiles jobId={job.id} />
        </section>
      )}

      {job.status !== "running" && <TrajectoryAnalysisCard job={job} />}

      <div className="log-toolbar" style={{ margin: "20px 0 10px" }}>
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
  );
}

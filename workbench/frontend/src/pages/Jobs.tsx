import { DeleteOutlined, ReloadOutlined } from "@ant-design/icons";
import { Button, Checkbox, Drawer, Modal, Popconfirm, Table, Tag, message } from "antd";
import type { ColumnsType } from "antd/es/table";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { useCallback, useEffect, useMemo, useState } from "react";
import { api, type Job, type JobKind, type JobStatus, type MsdComparison } from "../api/client";
import { KindChip, StatusChip } from "../components/ui";
import { fmtDuration, fmtTime, fmtSize } from "../utils";
import { mergeMsdSeries } from "../utils/msdCompare";

/** 任务记录页 v1.8.4: 行式列表 (Plane 行内密度借鉴) + 顶部 filter chips + sticky 表头
 *  行高 40px, hover bg-muted, 选中 bg-primary/5 border-l-2 border-primary
 *  保留 AntD Table 的多选/排序/分页, 视觉走自定义 .row-table */
export default function Jobs({ onOpenJob }: { onOpenJob: (id: string) => void }) {
  const [jobs, setJobs] = useState<Job[]>([]);
  // 删除双重确认: 第一步 Popconfirm → 第二步本 Modal 内勾选后才可点删除
  const [pendingDelete, setPendingDelete] = useState<Job | null>(null);
  const [confirmed, setConfirmed] = useState(false);
  const [deleting, setDeleting] = useState(false);
  const [selected, setSelected] = useState<string[]>([]);
  const [compare, setCompare] = useState<{
    series: { id: string; script: string; project_name: string; status: string; batch: string | null; thermo: { columns: string[]; rows: number[][] } }[];
  } | null>(null);
  const [comparing, setComparing] = useState(false);
  const [msdCompare, setMsdCompare] = useState<MsdComparison | null>(null);
  const [msdComparing, setMsdComparing] = useState(false);
  const [msdStarting, setMsdStarting] = useState(false);

  // 过滤器: 状态 / 项目 / 时间范围
  const [statusFilter, setStatusFilter] = useState<JobStatus | "all">("all");
  const [projectFilter, setProjectFilter] = useState<string>("all");
  const [timeFilter, setTimeFilter] = useState<"all" | "today" | "week">("all");

  const doCompare = async () => {
    if (selected.length < 2) { message.info("请勾选至少 2 个任务"); return; }
    setComparing(true);
    try {
      const r = await api.compareJobs(selected);
      if (r.series.length < 2) { message.info("可对比的有效任务不足 2 个"); return; }
      setCompare(r);
      setSelected((prev) => prev.filter(id => r.series.some(s => s.id === id)));
    } catch (e) {
      message.error(`对比失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setComparing(false); }
  };

  const doCompareMsd = async () => {
    if (selected.length < 2) { message.info("请勾选至少 2 个任务"); return; }
    if (selected.length > 6) { message.info("一次最多对比 6 个任务"); return; }
    setMsdComparing(true);
    try {
      setMsdCompare(await api.compareMsd(selected));
    } catch (e) {
      message.error(`MSD 对比失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setMsdComparing(false); }
  };

  const startMsdAnalysis = async () => {
    if (!msdCompare) return;
    setMsdStarting(true);
    const ids = msdCompare.series.filter(s => s.status === "idle").map(s => s.id);
    const results = await Promise.allSettled(ids.map(id => api.runAnalysis(id)));
    results.forEach((r, i) => {
      if (r.status === "rejected") message.error(`${ids[i]} 分析启动失败: ${String(r.reason)}`);
    });
    try { setMsdCompare(await api.compareMsd(msdCompare.series.map(s => s.id))); }
    catch (e) { message.error(`MSD 状态更新失败: ${e instanceof Error ? e.message : String(e)}`); }
    finally { setMsdStarting(false); }
  };

  useEffect(() => {
    if (!msdCompare?.series.some(s => s.status === "running")) return;
    const ids = msdCompare.series.map(s => s.id);
    let active = true;
    const timer = setInterval(() => {
      api.compareMsd(ids).then(r => { if (active) setMsdCompare(r); })
        .catch(e => { if (active) message.error(`MSD 状态更新失败: ${String(e)}`); });
    }, 4000);
    return () => { active = false; clearInterval(timer); };
  }, [msdCompare]);

  const load = useCallback(() => {
    api.jobs().then(setJobs).catch(() => {});
  }, []);

  useEffect(() => {
    load();
    const t = setInterval(load, 2500);
    return () => clearInterval(t);
  }, [load]);

  const cancel = async (id: string) => {
    try {
      await api.cancelJob(id);
      message.success("已发送取消请求");
      load();
    } catch (e) {
      message.error(`取消失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  };

  const doDelete = async () => {
    if (!pendingDelete) return;
    setDeleting(true);
    try {
      const r = await api.deleteJob(pendingDelete.id);
      message.success(`任务 ${pendingDelete.id} 已删除, 释放 ${fmtSize(r.freed_bytes)}`);
      setPendingDelete(null);
      setConfirmed(false);
      load();
    } catch (e) {
      message.error(`删除失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setDeleting(false);
    }
  };

  // 项目列表 (用于 filter chip)
  const projects = useMemo(() => {
    const set = new Set<string>();
    jobs.forEach((j) => set.add(j.project_name));
    return Array.from(set).sort();
  }, [jobs]);

  // 状态计数 (用于 filter chip 右侧 count)
  const statusCounts = useMemo(() => {
    const counts: Record<string, number> = { all: jobs.length };
    for (const j of jobs) counts[j.status] = (counts[j.status] ?? 0) + 1;
    return counts;
  }, [jobs]);

  // 项目计数
  const projectCounts = useMemo(() => {
    const counts: Record<string, number> = { all: jobs.length };
    for (const j of jobs) counts[j.project_name] = (counts[j.project_name] ?? 0) + 1;
    return counts;
  }, [jobs]);

  // 时间计数
  const timeCounts = useMemo(() => {
    const now = new Date();
    const today = new Date(now); today.setHours(0, 0, 0, 0);
    const weekAgo = new Date(today); weekAgo.setDate(weekAgo.getDate() - 7);
    let todayCount = 0, weekCount = 0;
    for (const j of jobs) {
      if (!j.created_at) continue;
      const t = new Date(j.created_at);
      if (t >= today) todayCount += 1;
      if (t >= weekAgo) weekCount += 1;
    }
    return { all: jobs.length, today: todayCount, week: weekCount };
  }, [jobs]);

  // 过滤后的任务列表
  const filtered = useMemo(() => {
    const now = new Date();
    const today = new Date(now); today.setHours(0, 0, 0, 0);
    const weekAgo = new Date(today); weekAgo.setDate(weekAgo.getDate() - 7);
    return jobs.filter((j) => {
      if (statusFilter !== "all" && j.status !== statusFilter) return false;
      if (projectFilter !== "all" && j.project_name !== projectFilter) return false;
      if (timeFilter !== "all") {
        const t = j.created_at ? new Date(j.created_at) : null;
        if (!t) return false;
        if (timeFilter === "today" && t < today) return false;
        if (timeFilter === "week" && t < weekAgo) return false;
      }
      return true;
    });
  }, [jobs, statusFilter, projectFilter, timeFilter]);

  const toggleSelect = (id: string) => {
    setSelected((prev) => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]);
  };

  const STATUS_CHIPS: { key: JobStatus | "all"; label: string }[] = [
    { key: "all", label: "全部" },
    { key: "running", label: "运行中" },
    { key: "queued", label: "排队" },
    { key: "completed", label: "已完成" },
    { key: "failed", label: "失败" },
    { key: "canceled", label: "已取消" },
    { key: "interrupted", label: "已中断" },
  ];

  const TIME_CHIPS: { key: "all" | "today" | "week"; label: string }[] = [
    { key: "all", label: "全部时间" },
    { key: "today", label: "今天" },
    { key: "week", label: "本周" },
  ];

  return (
    <div className="page-stack">
      <section className="card" style={{ overflow: "hidden" }}>
        {/* --- 工具条: 标题 + 计数 + 操作 --- */}
        <div className="table-toolbar">
          <span className="card-title">全部任务</span>
          <span className="table-count">{filtered.length}<span style={{ color: "var(--text-3)", fontWeight: 500 }}> / {jobs.length}</span></span>
          {selected.length > 0 && (
            <>
              <span style={{ marginLeft: 12, fontSize: 12, color: "var(--text-2)" }}>
                已选 {selected.length} 个
              </span>
              <button className="mini-btn accent" onClick={doCompare} disabled={comparing || selected.length < 2}>
                {comparing ? "对比中…" : "对比 thermo"}
              </button>
              <button className="mini-btn accent" onClick={doCompareMsd} disabled={msdComparing || selected.length < 2}>
                {msdComparing ? "对比中…" : "对比 MSD"}
              </button>
              <button className="mini-btn" onClick={() => setSelected([])}>
                清除选择
              </button>
            </>
          )}
          <button className="icon-btn" onClick={load} title="刷新">
            <ReloadOutlined />
          </button>
        </div>

        {/* --- Filter chips (Plane 借鉴) --- */}
        <div style={{
          padding: "12px 20px 14px",
          borderBottom: "1px solid var(--border)",
          display: "flex",
          flexDirection: "column",
          gap: 10,
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span style={{ fontSize: 11, fontWeight: 570, color: "var(--text-3)", letterSpacing: 0.04, textTransform: "uppercase", marginRight: 4 }}>
              状态
            </span>
            {STATUS_CHIPS.map((c) => (
              <button
                key={c.key}
                className={"filter-chip " + (statusFilter === c.key ? "active" : "")}
                onClick={() => setStatusFilter(c.key)}
              >
                {c.label} <span className="count">{statusCounts[c.key] ?? 0}</span>
              </button>
            ))}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span style={{ fontSize: 11, fontWeight: 570, color: "var(--text-3)", letterSpacing: 0.04, textTransform: "uppercase", marginRight: 4 }}>
              项目
            </span>
            <button
              className={"filter-chip " + (projectFilter === "all" ? "active" : "")}
              onClick={() => setProjectFilter("all")}
            >
              全部 <span className="count">{projectCounts.all ?? 0}</span>
            </button>
            {projects.map((p) => (
              <button
                key={p}
                className={"filter-chip " + (projectFilter === p ? "active" : "")}
                onClick={() => setProjectFilter(p)}
              >
                {p} <span className="count">{projectCounts[p] ?? 0}</span>
              </button>
            ))}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span style={{ fontSize: 11, fontWeight: 570, color: "var(--text-3)", letterSpacing: 0.04, textTransform: "uppercase", marginRight: 4 }}>
              时间
            </span>
            {TIME_CHIPS.map((c) => (
              <button
                key={c.key}
                className={"filter-chip " + (timeFilter === c.key ? "active" : "")}
                onClick={() => setTimeFilter(c.key)}
              >
                {c.label} <span className="count">{timeCounts[c.key] ?? 0}</span>
              </button>
            ))}
          </div>
        </div>

        {/* --- 行式列表 (Plane 行内密度借鉴) --- */}
        {filtered.length === 0 ? (
          <div style={{ color: "var(--text-3)", fontSize: 12.5, padding: "32px 24px", textAlign: "center" }}>
            {jobs.length === 0 ? "暂无任务记录" : "没有匹配当前过滤条件的任务"}
          </div>
        ) : (
          <table className="row-table" style={{ tableLayout: "fixed" }}>
            <thead>
              <tr>
                <th style={{ width: 36 }}>
                  <Checkbox
                    checked={filtered.length > 0 && filtered.every((j) => selected.includes(j.id))}
                    indeterminate={selected.length > 0 && selected.length < filtered.length}
                    onChange={(e) => {
                      if (e.target.checked) setSelected((prev) => Array.from(new Set([...prev, ...filtered.map(j => j.id)])));
                      else setSelected((prev) => prev.filter(id => !filtered.some(j => j.id === id)));
                    }}
                  />
                </th>
                <th style={{ width: 104 }}>状态</th>
                <th style={{ width: "16%" }}>Job ID</th>
                <th style={{ width: "18%" }}>项目</th>
                <th>脚本</th>
                <th style={{ width: 90 }}>类型</th>
                <th style={{ width: 140 }}>开始时间</th>
                <th style={{ width: 110 }}>时长</th>
                <th style={{ width: 200, textAlign: "right" }}>操作</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((j) => {
                const isSelected = selected.includes(j.id);
                return (
                  <tr
                    key={j.id}
                    className={isSelected ? "selected" : ""}
                    onClick={() => onOpenJob(j.id)}
                  >
                    <td onClick={(e) => { e.stopPropagation(); toggleSelect(j.id); }}>
                      <Checkbox checked={isSelected} />
                    </td>
                    <td><StatusChip status={j.status} /></td>
                    <td>
                      <button className="link-cell" onClick={(e) => { e.stopPropagation(); onOpenJob(j.id); }} title={j.id}>
                        {j.id.slice(0, 8)}
                      </button>
                    </td>
                    <td style={{ overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      <span style={{ fontWeight: 540 }}>{j.project_name}</span>
                    </td>
                    <td style={{ overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      <span style={{ display: "inline-flex", gap: 6, alignItems: "center" }}>
                        <span className="mono-cell" style={{ fontSize: 12, color: "var(--text-2)" }}>{j.script}</span>
                        {j.source === "cli" && (
                          <Tag style={{ fontSize: 10, lineHeight: "16px", padding: "0 6px", marginInlineEnd: 0 }}
                            title="终端 runner 发起">CLI</Tag>
                        )}
                        {j.batch && (
                          <Tag color="blue" style={{ fontSize: 10, lineHeight: "16px", padding: "0 6px", marginInlineEnd: 0 }}
                            title="参数扫描批次">{j.batch}</Tag>
                        )}
                      </span>
                    </td>
                    <td style={{ fontSize: 11.5, color: "var(--text-3)" }}>
                      <KindChip kind={j.kind} />
                    </td>
                    <td style={{ color: "var(--text-3)", fontSize: 11.5 }}>
                      {fmtTime(j.started_at)}
                    </td>
                    <td style={{ color: "var(--text-3)", fontSize: 11.5 }}>
                      {fmtDuration(j.started_at, j.finished_at)}
                    </td>
                    <td onClick={(e) => e.stopPropagation()} style={{ textAlign: "right" }}>
                      <span style={{ display: "inline-flex", gap: 7 }}>
                        <button className="mini-btn" onClick={() => onOpenJob(j.id)}>
                          日志
                        </button>
                        {j.status === "running" || j.status === "interrupted" ? (
                          <Popconfirm
                            title={j.status === "interrupted" ? "取消并清理残留进程？" : "确认取消该任务？"}
                            description={j.status === "interrupted" ? "任务因后端重启中断, 取消会精确终止容器内可能残留的进程" : undefined}
                            onConfirm={() => cancel(j.id)}
                            okText="取消任务"
                            cancelText="返回"
                          >
                            <button className="mini-btn danger">{j.status === "interrupted" ? "清理" : "取消"}</button>
                          </Popconfirm>
                        ) : (
                          <button
                            className="mini-btn danger"
                            title="删除任务与产物文件"
                            onClick={() => {
                              setConfirmed(false);
                              setPendingDelete(j);
                            }}
                          >
                            <DeleteOutlined />
                          </button>
                        )}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
      </section>

      {/* 保留 AntD Table 用于 hide 隐藏列的备用查询 (如对外测试) — 视觉行式已覆盖, 此处不渲染 */}
      <div style={{ display: "none" }} aria-hidden="true">
        <AntDTablePlaceholder />
      </div>

      <Modal
        title={`永久删除任务 ${pendingDelete?.id ?? ""}`}
        open={!!pendingDelete}
        onCancel={() => setPendingDelete(null)}
        footer={[
          <Button key="cancel" onClick={() => setPendingDelete(null)}>
            返回
          </Button>,
          <Button key="delete" type="primary" danger disabled={!confirmed} loading={deleting} onClick={doDelete}>
            永久删除
          </Button>,
        ]}
      >
        {pendingDelete && (
          <div style={{ fontSize: 13.5, lineHeight: 2 }}>
            <div>
              将永久删除以下内容, <b>操作不可恢复</b>:
            </div>
            <div className="mono-cell" style={{ fontSize: 12, color: "var(--text-2)" }}>
              工作区: {pendingDelete.workspace ?? "(无)"}
            </div>
            <div className="mono-cell" style={{ fontSize: 12, color: "var(--text-2)" }}>
              日志: {pendingDelete.log_path ?? "(无)"}
            </div>
            <div style={{ marginTop: 10 }}>
              <Checkbox checked={confirmed} onChange={(e) => setConfirmed(e.target.checked)}>
                我已了解此操作不可恢复
              </Checkbox>
            </div>
          </div>
        )}
      </Modal>

      <Drawer title={`thermo 对比 · ${compare?.series.length ?? 0} 个任务`} open={!!compare}
        onClose={() => setCompare(null)} width={760}>
        {compare && (
          <>
            <div style={{ fontSize: 12, color: "var(--text-2)", marginBottom: 10 }}>
              {compare.series.map(s => `${s.project_name} / ${s.script} (${s.id})`).join(" · ")}
            </div>
            <div style={{ fontSize: 12.5, fontWeight: 650, marginBottom: 6 }}>TotEng (按行号对齐)</div>
            <ResponsiveContainer width="100%" height={220}>
              <LineChart data={(() => {
                const maxLen = Math.max(...compare.series.map(s => s.thermo.rows.length), 0);
                const out: Record<string, number>[] = [];
                for (let i = 0; i < maxLen; i++) {
                  const row: Record<string, number | null> = { step: i };
                  compare.series.forEach((s, si) => {
                    const col = s.thermo.columns.findIndex(c => c.toLowerCase() === "toteng");
                    const rows = s.thermo.rows;
                    // 越界写 null → recharts 断线, 不做末值平台延长
                    row[`t${si}`] = (col >= 0 && i < rows.length) ? rows[i][col] : null;
                  });
                  out.push(row as Record<string, number>);
                }
                return out;
              })()}>
                <XAxis dataKey="step" tick={{ fontSize: 10 }} />
                <YAxis tick={{ fontSize: 10 }} />
                <Tooltip contentStyle={{ fontSize: 12 }} />
                <Legend wrapperStyle={{ fontSize: 11 }} />
                {compare.series.map((s: { id: string; script: string; project_name: string }, si: number) => (
                  <Line key={s.id} type="monotone" dataKey={`t${si}`}
                    name={`${s.project_name}/${s.script}`}
                    dot={false} stroke={["#3547e8", "#e5484d", "#12994e", "#d97706", "#7c5cfc", "#0e9384"][si % 6]} />
                ))}
              </LineChart>
            </ResponsiveContainer>
            <div style={{ marginTop: 10, fontSize: 11.5, color: "var(--text-3)" }}>
              曲线按行号对齐 (不同长度任务各取己行); 参数扫描任务建议同 batch 对比。
            </div>
          </>
        )}
      </Drawer>
      <Drawer title={`MSD 对比 · ${msdCompare?.series.length ?? 0} 个任务`} open={!!msdCompare}
        onClose={() => setMsdCompare(null)} width={760}>
        {msdCompare && (
          <>
            <div style={{ fontSize: 12, color: "var(--text-2)", marginBottom: 12 }}>
              全原子 MSD (Å²) 按实际滞后步数叠加；不同体系的曲线需结合组成和模拟条件判断。
            </div>
            {msdCompare.series.some(s => s.status === "idle") && (
              <Button size="small" loading={msdStarting} onClick={startMsdAnalysis} style={{ marginBottom: 12 }}>
                计算未分析轨迹
              </Button>
            )}
            {msdCompare.series.some(s => s.status === "running") && (
              <div style={{ fontSize: 12, color: "var(--text-2)", marginBottom: 12 }}>后台分析中，完成后自动刷新…</div>
            )}
            {msdCompare.series.filter(s => s.status !== "done").map(s => (
              <div key={s.id} style={{ fontSize: 12, color: "var(--text-2)", marginBottom: 5 }}>
                {s.project_name ?? "任务"}/{s.script ?? s.id} ({s.id.slice(0, 8)}): {s.note ?? (s.status === "idle" ? "等待计算" : s.status === "running" ? "计算中" : s.status)}
              </div>
            ))}
            {msdCompare.series.some(s => s.status === "done") ? (
              <ResponsiveContainer width="100%" height={320}>
                <LineChart data={mergeMsdSeries(msdCompare.series)}>
                  <XAxis dataKey="step" type="number" domain={["dataMin", "dataMax"]} tick={{ fontSize: 10 }} label={{ value: "滞后步数", position: "insideBottom", offset: -5 }} />
                  <YAxis tick={{ fontSize: 10 }} label={{ value: "MSD (Å²)", angle: -90, position: "insideLeft" }} />
                  <Tooltip contentStyle={{ fontSize: 12 }} />
                  <Legend wrapperStyle={{ fontSize: 11 }} />
                  {msdCompare.series.filter(s => s.status === "done").map((s, i) => (
                    <Line key={s.id} type="monotone" dataKey={s.id}
                      name={`${s.project_name}/${s.script} (${s.id.slice(0, 8)})`}
                      dot={s.msd?.points.length === 1} connectNulls={false}
                      stroke={["#3547e8", "#e5484d", "#12994e", "#d97706", "#7c5cfc", "#0e9384"][i % 6]} />
                  ))}
                </LineChart>
              </ResponsiveContainer>
            ) : (
              <div style={{ fontSize: 12, color: "var(--text-3)", padding: "18px 0" }}>暂无可绘制的 MSD 曲线</div>
            )}
            {msdCompare.series.some(s => s.status === "done" && s.msd?.diffusion) && (
              <div style={{ marginTop: 12, fontSize: 12, color: "var(--text-2)", lineHeight: 1.8 }}>
                {msdCompare.series.filter(s => s.status === "done" && s.msd?.diffusion).map(s => (
                  <div key={s.id}>
                    {s.id.slice(0, 8)}: 末窗斜率 {s.msd!.diffusion!.slope_a2_per_step.toExponential(3)} Å²/step，R²={s.msd!.diffusion!.r2.toFixed(2)}
                  </div>
                ))}
                <div style={{ color: "var(--text-3)" }}>斜率仅在积分步长相同的任务间可直接比较。</div>
              </div>
            )}
          </>
        )}
      </Drawer>
    </div>
  );
}

/** AntD Table 占位 (隐藏, 保留类型引用以维持 tsc 通过) */
function AntDTablePlaceholder() {
  const columns: ColumnsType<Job> = [
    { title: "状态", dataIndex: "status", width: 110, render: (s: JobStatus) => <StatusChip status={s} /> },
  ];
  return <Table rowKey="id" columns={columns} dataSource={[]} />;
}

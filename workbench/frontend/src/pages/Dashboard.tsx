import {
  CloseCircleOutlined,
  CloudServerOutlined,
  FolderOpenOutlined,
  InfoCircleOutlined,
  PlayCircleOutlined,
  PoweroffOutlined,
  ReloadOutlined,
  ThunderboltOutlined,
} from "@ant-design/icons";
import { useCallback, useEffect, useMemo, useState } from "react";
import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { Drawer, Modal, Typography, Button, message } from "antd";
import type { PageKey } from "../App";
import { api, type Health, type Job, type LocalToolsDetect, type BackendSummary, type BackendInfo, type BackendConfig, type BackendListItem } from "../api/client";
import { StatusChip, StatusDot } from "../components/ui";

/** 仪表盘 v1.8.4 布局: section 分组嵌套 + 永远可见的容器操作 + 7 天吞吐图 + 10 行最近任务
 *  (shadcn dashboard-01 / Plane / Cal.com 借鉴, 0 新依赖, 全部走 theme.css 变量) */
export default function Dashboard({
  health,
  jobs,
  backendDown,
  onNav,
}: {
  health: Health | null;
  jobs: Job[];
  backendDown: boolean;
  onNav: (p: PageKey) => void;
}) {
  const [starting, setStarting] = useState(false);
  const [confirmOpen, setConfirmOpen] = useState(false);
  const [shuttingDown, setShuttingDown] = useState(false);
  const [tools, setTools] = useState<LocalToolsDetect | null>(null);
  const [toolsDrawerOpen, setToolsDrawerOpen] = useState(false);
  const [backendDrawerOpen, setBackendDrawerOpen] = useState(false);

  // 统计卡数字需要实时性, 单独快轮询任务列表
  const [liveJobs, setLiveJobs] = useState<Job[]>(jobs);
  useEffect(() => setLiveJobs(jobs), [jobs]);
  useEffect(() => {
    const t = setInterval(() => api.jobs().then(setLiveJobs).catch(() => {}), 3000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    api.localToolsDetect().then(setTools).catch(() => setTools(null));
    const iv = setInterval(() => api.localToolsDetect().then(setTools).catch(() => setTools(null)), 10000);
    return () => clearInterval(iv);
  }, []);
  useEffect(() => { if (backendDown) setTools(null); }, [backendDown]);
  useEffect(() => {
    if (backendDown) setConfirmOpen(false);  // 后端已停 → 关闭退出确认框 (指令已生效)
  }, [backendDown]);

  const docker = health?.docker;
  const containerOk = docker?.container_running ?? false;
  const runningJobs = liveJobs.filter((j) => j.status === "running");
  const running = runningJobs.length;
  const completed = liveJobs.filter((j) => j.status === "completed").length;
  const failed = liveJobs.filter((j) => j.status === "failed").length;
  const queued = liveJobs.filter((j) => j.status === "queued").length;
  const lmpProc = docker?.lmp_processes ?? null;
  const orphanProcs = lmpProc !== null && lmpProc > 0 && running === 0;

  const handleContainerAction = useCallback(async () => {
    const hide = message.loading("正在启动容器…", 0);
    try {
      const r = await api.dockerStart();
      hide();
      // 按后端 stage 分级提示 (P0 A1: 不再让用户看 Windows 管道错)
      if (r.ok) {
        message.success(r.message);
        setTimeout(() => window.location.reload(), 1500);
        return;
      }
      const tip = r.hint_url ? ` — ${r.hint_url}` : "";
      const txt = (r.message || "启动失败") + tip;
      if (r.stage === "daemon_unreachable" || r.stage === "docker_missing") {
        // 红色错误, 持续 8s 让用户有时间读
        message.error({ content: txt, duration: 8 });
      } else if (r.stage === "timeout") {
        message.warning({ content: txt, duration: 6 });
      } else {
        message.error({ content: txt, duration: 6 });
      }
    } catch (e) {
      hide();
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  }, []);

  const startDemo = async () => {
    setStarting(true);
    try {
      const job = await api.createJob("demos", "test.lmp", "lmp");
      message.success(`演示任务 ${job.id} 已启动`);
      onNav("jobs");
    } catch (e) {
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setStarting(false);
    }
  };

  const doShutdown = useCallback(async () => {
    setShuttingDown(true);
    const r = await api.shutdownWorkbench();
    if (r.outcome === "shutting_down") {
      // 保持 shuttingDown: 等 App 轮询感知后端下线自动关 Modal, 中途回退会误导二次点击
      if (r.orphan_processes_cleaned > 0) {
        message.info(`已清理 ${r.orphan_processes_cleaned} 个容器内孤儿 LAMMPS 进程`);
      } else {
        message.success("结束指令已发出, 工作台进程即将退出");
      }
    } else if (r.outcome === "blocked") {
      message.error(r.message);
      setConfirmOpen(false);
      setShuttingDown(false);
      api.jobs().then(setLiveJobs).catch(() => {});
    } else {
      message.error(`结束失败: ${r.message}`);
      setShuttingDown(false);
    }
  }, []);

  const blocked = running > 0;

  return (
    <div className="page-stack">
      {backendDown && (
        <section className="stop-banner">
          <PoweroffOutlined style={{ color: "var(--err)", fontSize: 20, marginTop: 2 }} />
          <div>
            <div style={{ fontWeight: 650, marginBottom: 3 }}>工作台进程已结束</div>
            <div style={{ lineHeight: 1.7 }}>
              后端无响应, 页面数据不再更新。请在终端运行{" "}
              <span className="mono">uv run workbench</span> 重启, 然后刷新本页恢复。
            </div>
          </div>
        </section>
      )}

      {/* --- 顶部 KPI bar (Plane 借鉴) --------------------------------- */}
      <section className="kpi-bar" role="status" aria-label="任务实时状态">
        <div className="kpi-pill">
          <span className="kpi-pill-label">已排队</span>
          <span className="kpi-pill-value">
            {queued}
            <span className="unit">个</span>
          </span>
        </div>
        <div className={"kpi-pill " + (running > 0 ? "accent" : "")}>
          <span className="kpi-pill-label">运行中</span>
          <span className="kpi-pill-value">
            {running}
            <span className="unit">个</span>
          </span>
        </div>
        <div className="kpi-pill ok">
          <span className="kpi-pill-label">已完成</span>
          <span className="kpi-pill-value">
            {completed}
            <span className="unit">个</span>
          </span>
        </div>
        <div className={"kpi-pill " + (failed > 0 ? "err" : "")}>
          <span className="kpi-pill-label">失败</span>
          <span className="kpi-pill-value">
            {failed}
            <span className="unit">个</span>
          </span>
        </div>
        <div className="kpi-pill">
          <span className="kpi-pill-label">任务总数</span>
          <span className="kpi-pill-value">
            {liveJobs.length}
            <span className="unit">个</span>
          </span>
        </div>
        {/* 容器操作按钮: 永远显示 (UX 修复, 主代理已先做的小改) — 默认浅红(警告/启动态), 容器可用时变浅绿(已就绪/重启态) */}
        <button
          className={"kpi-action-btn " + (containerOk ? "ok" : "")}
          onClick={handleContainerAction}
          disabled={backendDown}
          title={containerOk ? "重启 lammpsd 容器" : "启动 lammpsd 容器"}
        >
          <span className="kpi-pill-label">容器</span>
          <span className="kpi-pill-value" style={{ display: "flex", alignItems: "center", gap: 4 }}>
            <ReloadOutlined style={{ fontSize: 14 }} />
            {containerOk ? "重启" : "启动"}
          </span>
        </button>
      </section>

      {/* --- 资源卡 + 环境卡 (合并版) ------------------------------- */}
      <section className="card card-pad">
        <div className="section-header">
          <span>环境状态</span>
          <span className="sub">
            {containerOk ? "lammpsd 运行中" : docker === null ? "检测中" : "容器不可用"}
          </span>
        </div>
        {/* 4 资源指标横向 (CPU/内存/数据目录/LAMMPS 进程) */}
        <div className="kpi-bar" style={{ marginBottom: 16 }}>
          <ResourcePill icon={<CloudServerOutlined />} label="容器 CPU" liveKey="cpu" />
          <ResourcePill icon={<ThunderboltOutlined />} label="容器内存" liveKey="mem" />
          <ResourcePill icon={<FolderOpenOutlined />} label="数据目录" liveKey="data" />
          <div className={"kpi-pill " + (orphanProcs ? "err" : lmpProc === 0 ? "ok" : "")}>
            <span className="kpi-pill-label">LAMMPS 进程</span>
            <span className="kpi-pill-value">
              {lmpProc === null ? "未知" : lmpProc}
              <span className="unit">个{orphanProcs ? " · 孤儿" : ""}</span>
            </span>
          </div>
        </div>
        {/* 容器状态 / LAMMPS 进程详情 / Python / 后端时间 纵向下沉 */}
        <div className="kv-grid">
          <div className="kv-row">
            <span className="kv-label">Docker 引擎</span>
            <span className="kv-value">
              <StatusDot status={docker?.available ? "ok" : "bad"} />
              {docker == null ? "检测中" : docker.available ? "可用" : "不可用"}
            </span>
          </div>
          <div className="kv-row">
            <span className="kv-label">容器状态</span>
            <span className="kv-value">{docker?.container_status ?? "-"}</span>
          </div>
          <div className="kv-row">
            <span className="kv-label">镜像</span>
            <span className="kv-value">
              <span className="mono">{docker?.image ?? "-"}</span>
            </span>
          </div>
          <div className="kv-row">
            <span className="kv-label">Python</span>
            <span className="kv-value">
              <span className="mono">v{health?.python ?? "-"}</span>
            </span>
          </div>
          <div className="kv-row" style={{ gridColumn: "1 / -1" }}>
            <span className="kv-label">/data 挂载</span>
            <span className="kv-value">
              {docker?.data_mount_ok ? (
                <StatusDot status="ok" />
              ) : (
                <CloseCircleOutlined style={{ color: "var(--err)", fontSize: 12 }} />
              )}
              <span className="mono" title={docker?.data_mount_host ?? ""}>
                {docker?.data_mount_host ?? "未检测到挂载"}
              </span>
              <Typography.Text
                copyable={{ text: docker?.data_mount_host ?? "" }}
                style={{ color: "var(--text-3)", fontSize: 12 }}
              />
            </span>
          </div>
          <div className="kv-row" style={{ gridColumn: "1 / -1" }}>
            <span className="kv-label">后端时间</span>
            <span className="kv-value">
              <span className="mono">{health?.time ?? "-"}</span>
            </span>
          </div>
        </div>
      </section>

      {/* --- 24h 任务吞吐图 (Recharts LineChart, 即使无数据保留骨架) --- */}
      <section className="card card-pad">
        <div className="section-header">
          <span>任务吞吐</span>
          <span className="sub">近 7 天 · 按天聚合 completed / failed</span>
        </div>
        <JobThroughputChart jobs={liveJobs} />
      </section>

      {/* --- 执行后端 (B2: 选 LocalDocker / RemoteHPC) ----------------- */}
      <BackendCard
        backend={health?.backend}
        onConfigure={() => setBackendDrawerOpen(true)}
      />

      {/* --- 操作 + 工具 + 控制 (左 1.35fr 右 1fr) ------------------- */}
      <section style={{ display: "grid", gridTemplateColumns: "1.35fr 1fr", gap: 8 }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          <section className="card card-pad">
            <div className="section-header">
              <span>快速操作</span>
              <span className="sub">从演示到正式任务</span>
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              <button
                className="action-btn primary"
                onClick={startDemo}
                disabled={starting || !containerOk || backendDown}
              >
                <PlayCircleOutlined />
                {starting ? "正在启动…" : "运行演示模拟"}
                <span className="sub">systems/demos/test.lmp</span>
              </button>
              <button
                className="action-btn"
                onClick={() => onNav("projects")}
                disabled={backendDown}
              >
                <FolderOpenOutlined />
                浏览项目与脚本
                <span className="sub">发起正式任务</span>
              </button>
            </div>
            <div
              style={{
                marginTop: 16,
                display: "flex",
                gap: 9,
                alignItems: "flex-start",
                background: "var(--neutral-weak)",
                borderRadius: 12,
                padding: 13,
                fontSize: 12.3,
                lineHeight: 1.75,
                color: "var(--text-2)",
              }}
            >
              <InfoCircleOutlined style={{ color: "var(--text-3)", marginTop: 3, flex: "none" }} />
              <span>
                LAMMPS 任务经容器运行, 每个任务使用独立工作区 (脚本与 *.data 自动暂存至
                lammps-data-docker/jobs/&lt;id&gt;/), 产物保留在工作区内; Python
                分析脚本本地执行。
              </span>
            </div>
          </section>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          <section
            className="card card-pad clickable"
            onClick={() => setToolsDrawerOpen(true)}
            title="点击配置本地可视化工具 (VMD / Vesta)"
          >
            <div className="section-header">
              <span>本地工具</span>
              <span className="sub">VMD / Vesta</span>
            </div>
            <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
              {tools ? (
                <>
                  <ToolChip name="VMD" info={tools.vmd} />
                  <ToolChip name="Vesta" info={tools.vesta} />
                </>
              ) : (
                <span style={{ fontSize: 12, color: "var(--text-3)" }}>检测中…</span>
              )}
            </div>
            <p style={{ margin: "12px 0 0", fontSize: 11.8, lineHeight: 1.65, color: "var(--text-3)" }}>
              点击此处配置路径、查看安装指引; 配置后任务详情页与体系配置页可直接「用 VMD/Vesta 打开」。
            </p>
          </section>

          <section className="card card-pad">
            <div className="section-header">
              <span>工作台控制</span>
              <span className="sub">受控退出</span>
            </div>
            <p style={{ margin: "0 0 12px", fontSize: 12.3, lineHeight: 1.75, color: "var(--text-2)" }}>
              结束后端工作台进程。有运行中任务时会被拒绝; 容器内残留的 LAMMPS
              孤儿进程会在退出前自动清理; 已完成任务与工作区文件不受影响。
            </p>
            <button
              className="action-btn danger"
              onClick={() => setConfirmOpen(true)}
              disabled={backendDown}
            >
              <PoweroffOutlined />
              {backendDown ? "工作台已停止" : "结束工作台进程"}
              <span className="sub">{backendDown ? "等待重启" : "受控退出"}</span>
            </button>
          </section>
        </div>
      </section>

      {/* --- 最近任务 (10 行 + filter chips) ----------------------- */}
      <RecentJobs jobs={liveJobs} onOpenJobs={() => onNav("jobs")} />

      <Modal
        open={confirmOpen}
        title={null}
        onCancel={() => setConfirmOpen(false)}
        footer={
          shuttingDown
            ? [
                <button key="ok" className="mini-btn" onClick={() => setConfirmOpen(false)}>
                  知道了
                </button>,
              ]
            : undefined
        }
        okText={shuttingDown ? undefined : "结束工作台进程"}
        cancelText={shuttingDown ? undefined : "取消"}
        onOk={shuttingDown ? undefined : doShutdown}
        okButtonProps={blocked && !shuttingDown ? { style: { display: "none" } } : { danger: true }}
      >
        <div style={{ display: "flex", gap: 13, alignItems: "flex-start" }}>
          <span
            className="stat-icon tint-err"
            style={{ fontSize: 20, width: 42, height: 42, flex: "none" }}
          >
            <PoweroffOutlined />
          </span>
          <div style={{ minWidth: 0, flex: 1 }}>
            {shuttingDown ? (
              <>
                <div style={{ fontWeight: 650, fontSize: 15, marginBottom: 8 }}>
                  结束指令已发出
                </div>
                <div style={{ fontSize: 12.8, lineHeight: 1.8, color: "var(--text-2)" }}>
                  工作台进程正在退出。本页将显示「后端已停止」;
                  在终端运行 <span className="mono">uv run workbench</span> 重启后刷新页面即可恢复。
                  {orphanProcs && <> 容器内 {lmpProc} 个孤儿 LAMMPS 进程已一并清理。</>}
                </div>
              </>
            ) : (
              <>
                <div style={{ fontWeight: 650, fontSize: 15, marginBottom: 8 }}>
                  确认结束工作台进程?
                </div>
                <div style={{ fontSize: 12.8, lineHeight: 1.9, color: "var(--text-2)" }}>
                  <div>
                    <span className="kv-label" style={{ marginRight: 8 }}>运行中任务</span>
                    {blocked ? (
                      <span style={{ color: "var(--err)", fontWeight: 600 }}>
                        {running} 个 — 已阻止结束, 请先取消:
                      </span>
                    ) : (
                      <span>无</span>
                    )}
                  </div>
                  {blocked && (
                    <div
                      style={{
                        margin: "8px 0",
                        padding: "9px 12px",
                        borderRadius: 10,
                        background: "var(--err-weak)",
                        border: "1px solid rgba(229, 72, 77, 0.3)",
                        fontFamily: "var(--font-mono)",
                        fontSize: 11.8,
                        maxHeight: 130,
                        overflowY: "auto",
                      }}
                    >
                      {runningJobs.map((j) => (
                        <div key={j.id}>
                          {j.id} · {j.project_name} · {j.script}
                        </div>
                      ))}
                    </div>
                  )}
                  <div>
                    <span className="kv-label" style={{ marginRight: 8 }}>容器内 LAMMPS 进程</span>
                    {lmpProc === null
                      ? "未知"
                      : lmpProc === 0
                        ? "无"
                        : `${lmpProc} 个${orphanProcs ? " (孤儿, 退出前自动清理)" : ""}`}
                  </div>
                  <div>
                    <span className="kv-label" style={{ marginRight: 8 }}>任务记录与文件</span>
                    保留在磁盘, 不受影响
                  </div>
                  <div style={{ marginTop: 8, color: "var(--text-3)" }}>
                    结束后需在终端 <span className="mono">uv run workbench</span> 重新启动。
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      </Modal>
      <LocalToolsDrawer
        open={toolsDrawerOpen}
        onClose={() => setToolsDrawerOpen(false)}
        tools={tools}
        onConfigured={setTools}
      />
      <BackendDrawer
        open={backendDrawerOpen}
        onClose={() => setBackendDrawerOpen(false)}
        onSaved={() => window.location.reload()}
      />
    </div>
  );
}

/* ============================================================
   小组件
   ============================================================ */

/** 资源 pill (3 项横向 KPI: CPU/内存/数据目录) — 拉 dockerMetrics 数据 */
function ResourcePill({
  icon,
  label,
  liveKey,
}: {
  icon: React.ReactNode;
  label: string;
  liveKey: "cpu" | "mem" | "data";
}) {
  const [data, setData] = useState<{
    current: { cpu_pct: number; mem_used_bytes: number; mem_pct: number } | null;
    history: { t: number; cpu_pct: number; mem_used_bytes: number; mem_pct: number }[];
    data_dir_size_bytes: number | null;
  } | null>(null);

  useEffect(() => {
    let closed = false;
    const load = () => api.dockerMetrics().then(d => { if (!closed) setData(d); }).catch(() => {});
    load();
    const t = setInterval(load, 5000);
    return () => { closed = true; clearInterval(t); };
  }, []);

  const fmtMB = (b: number) =>
    b < 1024 ** 2 ? `${(b / 1024).toFixed(1)} KB`
      : b < 1024 ** 3 ? `${(b / 1024 ** 2).toFixed(1)} MB`
        : `${(b / 1024 ** 3).toFixed(2)} GB`;
  const fmtGB = (b: number) => `${(b / 1024 ** 3).toFixed(2)} GB`;

  return (
    <div className="kpi-pill">
      <span className="kpi-pill-label" style={{ display: "inline-flex", gap: 5, alignItems: "center" }}>
        {icon}
        {label}
      </span>
      <span className="kpi-pill-value">
        {!data || !data.current ? (
          <span style={{ fontSize: 12, color: "var(--text-3)" }}>采样中…</span>
        ) : liveKey === "cpu" ? (
          <>
            {data.current.cpu_pct.toFixed(1)}
            <span className="unit">%</span>
          </>
        ) : liveKey === "mem" ? (
          <>
            {fmtMB(data.current.mem_used_bytes)}
            <span className="unit">({data.current.mem_pct.toFixed(1)}%)</span>
          </>
        ) : (
          <>
            {data.data_dir_size_bytes == null ? "-" : fmtGB(data.data_dir_size_bytes)}
          </>
        )}
      </span>
    </div>
  );
}

/** 7 天任务吞吐 Recharts LineChart: 按天聚合计数 completed/failed; 即使无数据保留骨架 */
function JobThroughputChart({ jobs }: { jobs: Job[] }) {
  const data = useMemo(() => {
    const days: { date: string; label: string; completed: number; failed: number }[] = [];
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    for (let i = 6; i >= 0; i--) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      const key = d.toISOString().slice(5, 10);  // MM-DD
      const label = i === 0 ? "今" : i === 1 ? "昨" : key;
      days.push({ date: key, label, completed: 0, failed: 0 });
    }
    const map = new Map(days.map((d) => [d.date, d]));
    for (const j of jobs) {
      if (!j.finished_at) continue;
      if (j.status !== "completed" && j.status !== "failed") continue;
      const t = new Date(j.finished_at);
      const key = t.toISOString().slice(5, 10);
      const slot = map.get(key);
      if (!slot) continue;
      if (j.status === "completed") slot.completed += 1;
      else slot.failed += 1;
    }
    return days;
  }, [jobs]);

  const hasData = data.some((d) => d.completed > 0 || d.failed > 0);

  return (
    <div style={{ width: "100%", height: 200, position: "relative" }}>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data} margin={{ top: 8, right: 24, left: 0, bottom: 4 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border-subtle)" />
          <XAxis dataKey="label" tick={{ fontSize: 10.5, fill: "var(--text-3)" }} axisLine={{ stroke: "var(--border)" }} tickLine={false} />
          <YAxis tick={{ fontSize: 10.5, fill: "var(--text-3)" }} axisLine={false} tickLine={false} width={32} allowDecimals={false} />
          <Tooltip
            contentStyle={{
              background: "var(--surface)",
              border: "1px solid var(--border)",
              borderRadius: 8,
              fontSize: 12,
              boxShadow: "var(--shadow-1)",
            }}
            labelStyle={{ color: "var(--text-2)", fontWeight: 600 }}
          />
          <Legend wrapperStyle={{ fontSize: 11.5, paddingTop: 4 }} iconType="circle" iconSize={7} />
          <Line
            type="monotone"
            dataKey="completed"
            name="已完成"
            stroke="#12994e"
            strokeWidth={2}
            dot={{ r: 3, fill: "#12994e" }}
            activeDot={{ r: 5 }}
            isAnimationActive={hasData}
          />
          <Line
            type="monotone"
            dataKey="failed"
            name="失败"
            stroke="#e5484d"
            strokeWidth={2}
            dot={{ r: 3, fill: "#e5484d" }}
            activeDot={{ r: 5 }}
            isAnimationActive={hasData}
          />
        </LineChart>
      </ResponsiveContainer>
      {!hasData && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "var(--text-3)",
            fontSize: 12.5,
            pointerEvents: "none",
          }}
        >
          近 7 天暂无已完成/失败任务, 曲线将自动填充
        </div>
      )}
    </div>
  );
}

function ToolChip({ name, info }: { name: string; info: { found: boolean; version_hint: string | null; source: string | null } }) {
  const ok = info.found;
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 6,
      fontSize: 12, fontWeight: 600, padding: "5px 11px", borderRadius: 999,
      color: ok ? "var(--ok)" : "var(--err)",
      background: ok ? "var(--ok-weak)" : "var(--err-weak)",
    }}>
      <span style={{ width: 6, height: 6, borderRadius: 999, background: ok ? "var(--ok)" : "var(--err)" }} />
      {name}{ok ? (info.version_hint ? ` ${info.version_hint}` : " · 已检测") : " · 未检测到"}
    </span>
  );
}

/** B2: 执行后端卡 — 显示当前 backend (Local Docker / Remote HPC) + 状态点 + 配置入口 */
function BackendCard({ backend, onConfigure }: {
  backend: BackendSummary | null | undefined;
  onConfigure: () => void;
}) {
  const status = backend?.status || "unknown";
  const action = backend?.action_needed || "configure";
  const ok = status === "running";
  const unreachable = status === "unreachable" || status === "unconfigured";
  const dot = ok ? "var(--ok)" : unreachable ? "var(--err)" : "var(--warn)";
  return (
    <section className="card card-pad" style={{ marginTop: 8 }}>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 6 }}>
        <div className="section-header" style={{ marginBottom: 0 }}>
          <span>执行后端</span>
          <span className="sub">LAMMPS 在哪儿跑</span>
        </div>
        <button className="mini-btn" onClick={onConfigure}>配置</button>
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: 12, padding: "6px 0" }}>
        <span style={{ width: 10, height: 10, borderRadius: 999, background: dot, display: "inline-block", flex: "none" }} />
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontSize: 14, fontWeight: 650, color: "var(--text)" }}>
            {backend?.name || "未配置"}
          </div>
          <div style={{ fontSize: 12, color: "var(--text-3)", marginTop: 2 }}>
            {ok && "已就绪 · 任务可发车"}
            {!ok && action === "configure" && "未配置 · 点击右上「配置」填入 SSH/工作目录"}
            {!ok && action === "start_docker" && "本地 Docker daemon 不可达 · 检查 Docker Desktop"}
            {!ok && action === "start_container" && "Docker 在跑但 lammpsd 容器没起 · 点击「容器启动」"}
            {!ok && action === "unavailable" && "Remote HPC 需要 SSH 凭据 (见配置抽屉)"}
            {!ok && !["configure", "start_docker", "start_container", "unavailable"].includes(action) && `状态: ${status}`}
          </div>
        </div>
        <span className="badge-soft" style={{
          background: ok ? "var(--ok-weak)" : unreachable ? "var(--err-weak)" : "var(--warn-weak)",
          color: ok ? "var(--ok)" : unreachable ? "var(--err)" : "var(--warn)",
        }}>
          {status}
        </span>
      </div>
    </section>
  );
}

/** B2: 执行后端配置抽屉 (Local Docker 提示免配置 / Remote HPC 表单) */
function BackendDrawer({ open, onClose, onSaved }: {
  open: boolean; onClose: () => void; onSaved: () => void;
}) {
  const [list, setList] = useState<BackendListItem[]>([]);
  const [current, setCurrent] = useState<BackendConfig | null>(null);
  const [type, setType] = useState<string>("local_docker");
  const [draft, setDraft] = useState<Record<string, string>>({});
  const [testResult, setTestResult] = useState<{ status: string; action_needed: string; message: string } | null>(null);
  const [testing, setTesting] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    if (!open) return;
    setError(""); setTestResult(null);
    Promise.all([api.backendList(), api.backendGet()]).then(([l, g]) => {
      setList(l.backends || []);
      setCurrent(g.config || null);
      const t = g.config?.type || "local_docker";
      setType(t);
      // 预填表单
      setDraft({
        ssh_host: g.config?.ssh_host || "",
        ssh_user: g.config?.ssh_user || "",
        ssh_key_path: g.config?.ssh_key_path || "",
        hpc_workdir: g.config?.hpc_workdir || "",
        hpc_sbatch_template: g.config?.hpc_sbatch_template || "",
        hpc_modules: (g.config?.hpc_modules || []).join(" "),
      });
    }).catch((e) => setError(`加载失败: ${e instanceof Error ? e.message : String(e)}`));
  }, [open]);

  const isLocal = type === "local_docker";
  const isHpc = type === "remote_hpc";

  const doTest = async () => {
    setTesting(true); setError(""); setTestResult(null);
    try {
      const cfg: Partial<BackendConfig> = { type };
      if (isHpc) {
        cfg.ssh_host = draft.ssh_host || undefined;
        cfg.ssh_user = draft.ssh_user || undefined;
        cfg.ssh_key_path = draft.ssh_key_path || undefined;
        cfg.hpc_workdir = draft.hpc_workdir || undefined;
        cfg.hpc_sbatch_template = draft.hpc_sbatch_template || undefined;
        cfg.hpc_modules = draft.hpc_modules ? draft.hpc_modules.split(/\s+/).filter(Boolean) : undefined;
      }
      const r = await api.backendTest(cfg);
      setTestResult(r.info as any);
    } catch (e) {
      setError(`测试失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setTesting(false); }
  };

  const doSave = async () => {
    setSaving(true); setError("");
    try {
      const cfg: BackendConfig = { type } as BackendConfig;
      if (isHpc) {
        cfg.ssh_host = draft.ssh_host || "";
        cfg.ssh_user = draft.ssh_user || "";
        cfg.ssh_key_path = draft.ssh_key_path || "";
        cfg.hpc_workdir = draft.hpc_workdir || "";
        cfg.hpc_sbatch_template = draft.hpc_sbatch_template || "";
        cfg.hpc_modules = draft.hpc_modules ? draft.hpc_modules.split(/\s+/).filter(Boolean) : [];
      }
      await api.backendPut(cfg);
      message.success("后端配置已保存");
      onSaved();
      onClose();
    } catch (e) {
      setError(`保存失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setSaving(false); }
  };

  return (
    <Drawer title="执行后端配置" open={open} onClose={onClose} width={520}>
      <Typography.Paragraph type="secondary" style={{ fontSize: 12.5, marginTop: 0 }}>
        选择 LAMMPS 任务在哪儿跑: 本地 Docker 容器 (默认, 零配置) 或 远程 HPC
        (SSH 提交 sbatch 作业)。切换后, 后续任务走新后端; 旧任务不受影响。
      </Typography.Paragraph>
      <div style={{ display: "flex", flexDirection: "column", gap: 10, marginBottom: 16 }}>
        {list.map((b) => (
          <label key={b.type} style={{
            display: "flex", alignItems: "center", gap: 10, padding: "10px 12px",
            borderRadius: 10, border: "1px solid " + (type === b.type ? "var(--accent)" : "var(--border)"),
            background: type === b.type ? "var(--accent-weak)" : "var(--surface)",
            cursor: "pointer", fontSize: 13,
          }}>
            <input type="radio" checked={type === b.type} onChange={() => setType(b.type)} />
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 620 }}>{b.name}</div>
              <div style={{ fontSize: 11.5, color: "var(--text-3)" }}>
                {b.type === "local_docker" && "本机 Docker Desktop 跑 lammpsd 容器, 暂存-运行-回收"}
                {b.type === "remote_hpc" && "SSH 到远程集群, sbatch 提交 LAMMPS 任务"}
                {!["local_docker", "remote_hpc"].includes(b.type) && "(未实现)"}
              </div>
            </div>
            <span className="badge-soft" style={{
              background: b.available ? "var(--ok-weak)" : "var(--warn-weak)",
              color: b.available ? "var(--ok)" : "var(--warn)",
            }}>
              {b.available ? "可用" : "需配置"}
            </span>
          </label>
        ))}
      </div>
      {isHpc && (
        <div style={{ display: "flex", flexDirection: "column", gap: 8, marginBottom: 12 }}>
          <Field label="SSH 主机" value={draft.ssh_host || ""} onChange={(v) => setDraft({ ...draft, ssh_host: v })} placeholder="hpc.univ.edu" />
          <Field label="SSH 用户" value={draft.ssh_user || ""} onChange={(v) => setDraft({ ...draft, ssh_user: v })} placeholder="alice" />
          <Field label="SSH 私钥路径 (本机)" value={draft.ssh_key_path || ""} onChange={(v) => setDraft({ ...draft, ssh_key_path: v })} placeholder="C:/Users/.../id_rsa (留空用默认)" />
          <Field label="HPC 工作目录" value={draft.hpc_workdir || ""} onChange={(v) => setDraft({ ...draft, hpc_workdir: v })} placeholder="/home/alice/lammps" />
          <Field label="module load 列表" value={draft.hpc_modules || ""} onChange={(v) => setDraft({ ...draft, hpc_modules: v })} placeholder="openmpi/4.1 lammps/20240328" />
          <Field label="sbatch 模板 (可选)" value={draft.hpc_sbatch_template || ""} onChange={(v) => setDraft({ ...draft, hpc_sbatch_template: v })} placeholder="留空用默认 (1 节点 4 核)" multiline />
        </div>
      )}
      {isLocal && (
        <div style={{ fontSize: 12.5, color: "var(--text-2)", padding: 12, background: "var(--accent-weak)", borderRadius: 10, marginBottom: 12 }}>
          本地 Docker 后端零配置, 系统会拉起 lammpsd 容器并自动暂存依赖。如需修改容器名/挂载路径, 见 docs/environment.md。
        </div>
      )}
      {error && <div style={{ padding: 10, background: "var(--err-weak)", color: "var(--err)", borderRadius: 8, fontSize: 12, marginBottom: 8 }}>{error}</div>}
      {testResult && (
        <div style={{ padding: 10, background: testResult.status === "running" ? "var(--ok-weak)" : "var(--err-weak)", color: testResult.status === "running" ? "var(--ok)" : "var(--err)", borderRadius: 8, fontSize: 12, marginBottom: 8 }}>
          测试: status=<b>{testResult.status}</b>, action_needed=<b>{testResult.action_needed}</b> — {testResult.message}
        </div>
      )}
      <div style={{ display: "flex", gap: 8, justifyContent: "flex-end" }}>
        <Button onClick={doTest} disabled={testing || saving} loading={testing}>
          测试连通性
        </Button>
        <Button type="primary" onClick={doSave} disabled={saving || testing} loading={saving}>
          保存并切换
        </Button>
      </div>
    </Drawer>
  );
}

function Field({ label, value, onChange, placeholder, multiline }: {
  label: string; value: string; onChange: (v: string) => void; placeholder?: string; multiline?: boolean;
}) {
  return (
    <div>
      <div style={{ fontSize: 11.5, color: "var(--text-3)", marginBottom: 3 }}>{label}</div>
      {multiline ? (
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          rows={3}
          style={{ width: "100%", padding: "7px 10px", border: "1px solid var(--border)", borderRadius: 8, fontSize: 12, fontFamily: "var(--font-mono)", resize: "vertical" }}
        />
      ) : (
        <input
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          style={{ width: "100%", padding: "7px 10px", border: "1px solid var(--border)", borderRadius: 8, fontSize: 12, fontFamily: "var(--font-mono)" }}
        />
      )}
    </div>
  );
}

function ToolConfigRow({ label, info, draft, setDraft, saving, onSave }: {
  label: string;
  info: { found: boolean; path: string | null; source: string | null };
  draft: string; setDraft: (s: string) => void;
  saving: boolean; onSave: (p: string) => void;
}) {
  const isManual = info.source === "manual";
  return (
    <div style={{ marginTop: 14, padding: 14, border: "1px solid var(--border)", borderRadius: 10 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 9, marginBottom: 8 }}>
        <span style={{ fontWeight: 650 }}>{label}</span>
        <ToolChip name={label} info={info as any} />
        {isManual && <span style={{ fontSize: 11, color: "var(--text-3)" }}>手动配置</span>}
      </div>
      <div style={{ display: "flex", gap: 8 }}>
        <input className="sys-input" style={{ flex: 1, fontSize: 12 }}
          placeholder={info.path || "请输入可执行文件绝对路径"}
          value={draft} onChange={(e) => setDraft(e.target.value)} />
        <button className="mini-btn accent" disabled={saving || !draft} onClick={() => onSave(draft)}>
          {saving ? "保存中…" : "保存"}
        </button>
        {isManual && <button className="mini-btn" onClick={() => onSave("")}>清除</button>}
      </div>
      {info.path && (
        <div style={{ fontSize: 11, color: "var(--text-3)", marginTop: 6, fontFamily: "var(--font-mono)", wordBreak: "break-all" }}>
          当前: {info.path}
        </div>
      )}
    </div>
  );
}

function InstallHintRow({ tool }: { tool: "vmd" | "vesta" }) {
  const [url, setUrl] = useState<string>("");
  useEffect(() => {
    api.localToolsInstallHint(tool).then((r) => setUrl(r.url)).catch(() => setUrl(""));
  }, [tool]);
  if (!url) return null;
  return (
    <div style={{ marginTop: 10, fontSize: 12, color: "var(--text-2)" }}>
      {tool} 官网: <a href={url} target="_blank" rel="noreferrer">{url}</a>
    </div>
  );
}

function LocalToolsDrawer({ open, onClose, tools, onConfigured }: {
  open: boolean; onClose: () => void; tools: LocalToolsDetect | null;
  onConfigured: (t: LocalToolsDetect) => void;
}) {
  const [vmdDraft, setVmdDraft] = useState("");
  const [vestaDraft, setVestaDraft] = useState("");
  const [saving, setSaving] = useState<"" | "vmd" | "vesta">("");
  useEffect(() => { setVmdDraft(""); setVestaDraft(""); }, [open]);
  const save = async (tool: "vmd" | "vesta", path: string) => {
    setSaving(tool);
    try {
      const t = await api.configureLocalTool(tool, path);
      onConfigured(t);
      message.success(path ? `已配置 ${tool} 路径` : `已清除 ${tool} 配置`);
    } catch (e) {
      message.error(`配置失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setSaving(""); }
  };
  return (
    <Drawer title="本地可视化工具" open={open} onClose={onClose} width={520}>
      <Typography.Paragraph type="secondary" style={{ fontSize: 12.5, marginTop: 0 }}>
        工作台可在任务详情和体系配置页生成「一键启动脚本」打开本机可视化工具。
        下方自动检测常见安装路径; 检测失败时手动填入路径即可, 不会修改系统 PATH 或防火墙。
      </Typography.Paragraph>
      {!tools && <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>检测中…</div>}
      {tools && (<>
        <ToolConfigRow label="VMD" info={tools.vmd} draft={vmdDraft} setDraft={setVmdDraft}
          saving={saving === "vmd"} onSave={(p) => save("vmd", p)} />
        <ToolConfigRow label="Vesta" info={tools.vesta} draft={vestaDraft} setDraft={setVestaDraft}
          saving={saving === "vesta"} onSave={(p) => save("vesta", p)} />
        <InstallHintRow tool="vmd" />
        <InstallHintRow tool="vesta" />
      </>)}
    </Drawer>
  );
}

/** 最近任务 (Plane 行内密度 + filter chips): 单行 [状态点] [项目] [脚本] [创建] [耗时]
 *  10 行, filter chips: 全部 / 今天 / 本周。点击进入任务列表。 */
function RecentJobs({ jobs, onOpenJobs }: { jobs: Job[]; onOpenJobs: () => void }) {
  const [filter, setFilter] = useState<"all" | "today" | "week">("all");

  const filtered = useMemo(() => {
    const now = new Date();
    const today = new Date(now); today.setHours(0, 0, 0, 0);
    const weekAgo = new Date(today); weekAgo.setDate(weekAgo.getDate() - 7);
    return [...jobs]
      .filter((j) => {
        if (filter === "all") return true;
        const t = j.created_at ? new Date(j.created_at) : null;
        if (!t) return false;
        if (filter === "today") return t >= today;
        return t >= weekAgo;
      })
      .sort((a, b) => (b.created_at || "").localeCompare(a.created_at || ""))
      .slice(0, 10);
  }, [jobs, filter]);

  const counts = useMemo(() => {
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

  const fmtDuration = (s: string | null) => {
    if (!s) return "—";
    const d = new Date(s);
    const ago = Math.floor((Date.now() - d.getTime()) / 60000);
    if (ago < 1) return "刚刚";
    if (ago < 60) return `${ago} 分钟前`;
    if (ago < 1440) return `${Math.floor(ago / 60)} 小时前`;
    return `${Math.floor(ago / 1440)} 天前`;
  };

  return (
    <section className="card" style={{ overflow: "hidden" }}>
      <div className="section-header" style={{ padding: "16px 20px 0", marginBottom: 12 }}>
        <span>最近任务</span>
        <span style={{ display: "inline-flex", gap: 6 }}>
          <button
            className={"filter-chip " + (filter === "all" ? "active" : "")}
            onClick={() => setFilter("all")}
          >
            全部 <span className="count">{counts.all}</span>
          </button>
          <button
            className={"filter-chip " + (filter === "today" ? "active" : "")}
            onClick={() => setFilter("today")}
          >
            今天 <span className="count">{counts.today}</span>
          </button>
          <button
            className={"filter-chip " + (filter === "week" ? "active" : "")}
            onClick={() => setFilter("week")}
          >
            本周 <span className="count">{counts.week}</span>
          </button>
        </span>
      </div>
      {filtered.length === 0 ? (
        <div style={{ color: "var(--text-3)", fontSize: 12.5, padding: "20px 24px 24px" }}>
          暂无任务。点击右上角「运行演示模拟」或在「项目与脚本」页发起正式任务。
        </div>
      ) : (
        <table className="row-table" style={{ tableLayout: "fixed" }}>
          <thead>
            <tr>
              <th style={{ width: "28%" }}>项目</th>
              <th>脚本</th>
              <th style={{ width: 110 }}>类型</th>
              <th style={{ width: 130 }}>创建</th>
              <th style={{ width: 110 }}>状态</th>
              <th style={{ width: 90 }} />
            </tr>
          </thead>
          <tbody>
            {filtered.map((j) => (
              <tr key={j.id} onClick={onOpenJobs}>
                <td style={{ overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  <span style={{ fontWeight: 540 }}>{j.project_name}</span>
                </td>
                <td style={{ overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  <span className="mono-cell" style={{ fontSize: 12, color: "var(--text-2)" }}>{j.script}</span>
                </td>
                <td style={{ color: "var(--text-3)", fontSize: 11.5 }}>{j.kind}</td>
                <td style={{ color: "var(--text-3)", fontSize: 11.5 }}>{fmtDuration(j.created_at)}</td>
                <td><StatusChip status={j.status} /></td>
                <td style={{ color: "var(--text-3)", fontSize: 10.5 }}>
                  <span className="mono-cell">{j.id.slice(0, 8)}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}
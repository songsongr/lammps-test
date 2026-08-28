import {
  CheckCircleOutlined,
  CloseCircleOutlined,
  CloudServerOutlined,
  FolderOpenOutlined,
  InfoCircleOutlined,
  PlayCircleOutlined,
  PoweroffOutlined,
  ThunderboltOutlined,
} from "@ant-design/icons";
import { useCallback, useEffect, useState } from "react";
import { Drawer, Modal, Typography, message } from "antd";
import type { PageKey } from "../App";
import { api, type Health, type Job, type LocalToolsDetect } from "../api/client";
import { StatCard, StatusDot } from "../components/ui";

/** 仪表盘: 环境概览 + 任务统计 + 快速操作 + 工作台控制 (health/jobs 由 App 统一轮询注入) */
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

  const docker = health?.docker;
  const containerOk = docker?.container_running ?? false;
  const runningJobs = liveJobs.filter((j) => j.status === "running");
  const running = runningJobs.length;
  const completed = liveJobs.filter((j) => j.status === "completed").length;
  const failed = liveJobs.filter((j) => j.status === "failed").length;
  const lmpProc = docker?.lmp_processes ?? null;
  const orphanProcs = lmpProc !== null && lmpProc > 0 && running === 0;

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
      message.success("结束指令已发出, 工作台进程即将退出");
    } else if (r.outcome === "blocked") {
      message.error(r.message);
      setConfirmOpen(false);
      api.jobs().then(setLiveJobs).catch(() => {});
    } else {
      message.error(`结束失败: ${r.message}`);
    }
    setShuttingDown(false);
  }, []);

  const blocked = running > 0;

  return (
    <div>
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

      <div className="stat-grid">
        <StatCard
          icon={<CloudServerOutlined />}
          tint={containerOk ? "accent" : "err"}
          label="lammpsd 容器"
        >
          <span style={{ display: "inline-flex", alignItems: "center", gap: 9 }}>
            <StatusDot status={containerOk ? "ok" : "bad"} />
            <span style={{ fontSize: 19 }}>{containerOk ? "运行中" : docker === null ? "检测中" : "不可用"}</span>
          </span>
        </StatCard>
        <StatCard icon={<ThunderboltOutlined />} tint="accent" label="运行中任务">
          {running}
          <span className="unit">个</span>
        </StatCard>
        <StatCard icon={<CheckCircleOutlined />} tint="ok" label="已完成任务">
          {completed}
          <span className="unit">个</span>
        </StatCard>
        <StatCard icon={<CloseCircleOutlined />} tint="err" label="失败任务">
          {failed}
          <span className="unit">个</span>
        </StatCard>
      </div>

      <div
        style={{ display: "grid", gridTemplateColumns: "1.35fr 1fr", gap: 16, marginTop: 16 }}
      >
        <section className="card card-pad">
          <div className="card-title" style={{ marginBottom: 4 }}>
            模拟环境
          </div>
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
              <span className="kv-label">容器内 LAMMPS 进程</span>
              <span className="kv-value">
                {lmpProc === null ? (
                  "未知"
                ) : (
                  <>
                    <StatusDot status={lmpProc === 0 ? "ok" : orphanProcs ? "bad" : "running"} />
                    {lmpProc === 0
                      ? "无"
                      : `${lmpProc} 个${orphanProcs ? " · 疑似孤儿 (无运行中任务)" : ""}`}
                  </>
                )}
              </span>
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

        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <section className="card card-pad" style={{ display: "flex", flexDirection: "column" }}>
            <div className="card-title" style={{ marginBottom: 14 }}>
              快速操作
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
                marginTop: "auto",
                paddingTop: 16,
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

          <section
            className="card card-pad"
            style={{ cursor: "pointer" }}
            onClick={() => setToolsDrawerOpen(true)}
            title="点击配置本地可视化工具 (VMD / Vesta)"
          >
            <div className="card-title" style={{ marginBottom: 10 }}>
              本地工具
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
            <p style={{ margin: "10px 0 0", fontSize: 11.8, lineHeight: 1.65, color: "var(--text-3)" }}>
              点击此处配置路径、查看安装指引; 配置后任务详情页与体系配置页可直接「用 VMD/Vesta 打开」。
            </p>
          </section>

          <section className="card card-pad">
            <div className="card-title" style={{ marginBottom: 10 }}>
              工作台控制
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
      </div>

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
import {
  ArrowLeftOutlined,
  CaretRightOutlined,
  EditOutlined,
  EyeOutlined,
  SaveOutlined,
  ThunderboltOutlined,
  ToolOutlined,
} from "@ant-design/icons";
import { Button, Drawer, Modal, Select, Spin, message } from "antd";
import { useCallback, useEffect, useRef, useState } from "react";
import { api, type Job, type SchemaField, type SystemConsistency, type SystemProfileTemplate } from "../api/client";

/** 一致性徽章: 体系构建 / 渲染脚本 与当前参数的同步状态 */
function ConsistencyBadge({ label, state }: { label: string; state: string }) {
  const meta: Record<string, { text: string; fg: string; bg: string }> = {
    built: { text: "与当前参数一致", fg: "var(--ok)", bg: "var(--ok-weak)" },
    stale: { text: "参数已改, 未重建", fg: "#d97706", bg: "rgba(217, 119, 6, 0.1)" },
    never: { text: "从未构建", fg: "var(--text-3)", bg: "var(--neutral-weak)" },
    sync: { text: "与体系同步", fg: "var(--ok)", bg: "var(--ok-weak)" },
    hand_edited: { text: "已被手改", fg: "#d97706", bg: "rgba(217, 119, 6, 0.1)" },
    missing: { text: "未渲染", fg: "var(--text-3)", bg: "var(--neutral-weak)" },
  };
  const m = meta[state] ?? { text: state, fg: "var(--text-3)", bg: "var(--neutral-weak)" };
  return (
    <span
      title={`${label}: ${m.text}`}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 6,
        fontSize: 12,
        fontWeight: 600,
        padding: "4px 12px",
        borderRadius: 999,
        color: m.fg,
        background: m.bg,
      }}
    >
      <span style={{ width: 6, height: 6, borderRadius: 999, background: m.fg }} />
      {label} · {m.text}
    </span>
  );
}

type Cfg = Record<string, unknown>;

function getPath(obj: unknown, dotted: string): unknown {
  let node: unknown = obj;
  for (const p of dotted.split(".")) {
    if (node === null || typeof node !== "object") return undefined;
    node = (node as Record<string, unknown>)[p];
  }
  return node;
}

function setPath(obj: Record<string, unknown>, dotted: string, value: unknown): void {
  const parts = dotted.split(".");
  let node: Record<string, unknown> = obj;
  for (const p of parts.slice(0, -1)) {
    if (typeof node[p] !== "object" || node[p] === null) node[p] = {};
    node = node[p] as Record<string, unknown>;
  }
  node[parts[parts.length - 1]] = value;
}

const clone = (v: unknown) => JSON.parse(JSON.stringify(v)) as Cfg;

const GROUP_LABELS: Record<string, string> = {
  surface: "表面",
  water: "水层 / 水分子",
  vacuum: "真空层",
  box: "盒子",
  ions: "离子组成",
  seed: "可复现性",
};

const CONF_COLORS: Record<string, string> = {
  高: "#12994e",
  中: "#d97706",
  低: "#e5484d",
};

/** 体系配置页: 几何/组成/力场 结构化查看与编辑, 重建体系, 渲染脚本 */
export default function ProjectSystem({
  projectId,
  onBack,
  onOpenJob,
}: {
  projectId: string;
  onBack: () => void;
  onOpenJob: (id: string) => void;
}) {
  const [cfg, setCfg] = useState<Cfg | null>(null);
  const [consistency, setConsistency] = useState<SystemConsistency | null>(null);
  const [errors, setErrors] = useState<string[]>([]);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [schema, setSchema] = useState<SystemProfileTemplate | null>(null);
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState<Cfg | null>(null);
  const [saving, setSaving] = useState(false);
  const [building, setBuilding] = useState(false);
  const [rendering, setRendering] = useState(false);
  const [previewOpen, setPreviewOpen] = useState(false);
  const [scanOpen, setScanOpen] = useState(false);
  const [scanParam, setScanParam] = useState("");
  const [scanValues, setScanValues] = useState("");
  const [scanning, setScanning] = useState(false);
  const [methodParams, setMethodParams] = useState<{ key: string; label: string }[]>([]);

  const load = useCallback(() => {
    let closed = false;  // 防跨项目竞态: 慢响应覆盖新项目
    api
      .getSystem(projectId)
      .then((d) => {
        if (closed) return;
        setCfg(d.config);
        if (closed) return;
        setConsistency(d.consistency ?? null);
        setErrors(d.errors);
        if (d.meta?.method_id) {
          api.templates().then((tp) => {
            const m = tp.methods.find((x) => x.id === d.meta.method_id);
            setMethodParams(m ? m.params.map((p2) => ({ key: p2.key, label: p2.label })) : []);
            setScanParam((prev) => prev || (m?.params[0]?.key ?? ""));
          }).catch(() => {});
        }
      })
      .catch((e) => { if (!closed) setLoadError(e instanceof Error ? e.message : String(e)); });
    return () => { closed = true; };
  }, [projectId]);

  useEffect(() => {
    const cleanup = load();
    return cleanup;
  }, [load]);

  // cfg 载入后按 profile 取对应 schema (用于表单标签)
  useEffect(() => {
    if (!cfg?.profile) return;
    api
      .templates()
      .then((t) => setSchema(t.system_profiles.find((p) => p.id === (cfg as { profile: string }).profile) ?? null))
      .catch(() => {});
  }, [cfg?.profile]);

  if (loadError) {
    return (
      <div className="card card-pad" style={{ textAlign: "center", padding: 48 }}>
        <div style={{ fontSize: 15, fontWeight: 620, marginBottom: 6 }}>该项目无体系配置</div>
        <div style={{ fontSize: 13, color: "var(--text-2)", marginBottom: 18 }}>{loadError}</div>
        <button className="mini-btn" onClick={onBack}>
          返回
        </button>
      </div>
    );
  }
  if (!cfg) return <Spin />;

  const startEdit = () => {
    setDraft(clone(cfg));
    setEditing(true);
  };
  const save = async () => {
    if (!draft) return;
    setSaving(true);
    try {
      await api.putSystem(projectId, draft);
      message.success("体系配置已保存; 请「重建体系」生成新 system.data, 再「重新渲染」同步脚本");
      setCfg(draft);
      setEditing(false);
      load();
    } catch (e) {
      message.error(`保存失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setSaving(false);
    }
  };
  const handleOpenVesta = async (dataPath: string) => {
    if (!dataPath) { message.error("无 system.data 路径"); return; }
    // 走真一键: 后端 spawn vesta + 自动 .data→.xyz 临时文件转换
    const hide = message.loading("正在启动 Vesta…", 0);
    try {
      const result = await api.openWithTool("vesta", dataPath.split("\\").join("/"), true);
      hide();
      if (result.ok && result.spawned) {
        message.success(`已启动 Vesta (pid ${result.pid ?? "?"})`);
        return;
      }
      if (result.fallback === "launcher" && result.content) {
        const blob = new Blob([result.content], { type: "text/plain;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url; a.download = result.filename || "open-vesta.bat";
        document.body.appendChild(a); a.click(); a.remove();
        URL.revokeObjectURL(url);
        message.warning(result.message || "已下载启动器, 请双击运行");
      } else {
        message.error(result.message || "启动失败");
      }
    } catch (e) {
      hide();
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  };

  const runScan = async () => {
    const tokens = scanValues.split(/[,\s]+/).filter(Boolean);
    const bad = tokens.filter((tk) => Number.isNaN(Number(tk)));
    if (bad.length) { message.error(`这些值不是数字: ${bad.join(", ")}`); return; }
    const values = tokens.map(Number);
    if (!scanParam || values.length === 0) { message.error("请填写参数与值列表 (如 320, 340, 360)"); return; }
    if (values.length > 20) { message.error("单次最多 20 个值"); return; }
    setScanning(true);
    try {
      const r = await api.scanProject(projectId, scanParam, values, 8);
      message.success(`扫描批次 ${r.batch}: ${r.jobs.length} 个任务已入队 (${r.param} = ${r.values.join(", ")})`);
      setScanOpen(false);
      onOpenJob(r.jobs[0].id);
    } catch (e) {
      message.error(`扫描失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally { setScanning(false); }
  };

  const rebuild = async () => {
    setBuilding(true);
    try {
      const job: Job = await api.createJob(projectId, "", "build");
      message.success(`体系构建任务 ${job.id} 已启动`);
      onOpenJob(job.id);
    } catch (e) {
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setBuilding(false);
    }
  };
  const render = async (force = false) => {
    setRendering(true);
    try {
      const r = await api.renderRunLmp(projectId, { force });
      message.success(`已渲染 ${r.file} (${fmtKB(r.bytes)})`);
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      if (msg.includes("手改")) {
        Modal.confirm({
          title: "run.lmp 被手改过, 确认覆盖？",
          content: "重新渲染将覆盖你的手动修改; 建议先另存副本。",
          okText: "覆盖渲染",
          okButtonProps: { danger: true },
          onOk: () => render(true),
        });
      } else {
        message.error(`渲染失败: ${msg}`);
      }
    } finally {
      setRendering(false);
    }
  };

  const current = editing && draft ? draft : cfg;
  const view = editing ? "编辑模式" : "查看模式";
  const fields: SchemaField[] = schema?.fields ?? [];
  const groups = new Map<string, SchemaField[]>();
  for (const f of fields) {
    const g = f.key.split(".")[0];
    groups.set(g, [...(groups.get(g) ?? []), f]);
  }

  const numInput = (f: SchemaField) => {
    const value = Number(getPath(current, f.key) ?? 0);
    return (
      <input
        className="sys-input"
        type={f.type === "int" ? "number" : "number"}
        step="any"
        value={value}
        onChange={(e) => {
          const v = f.type === "int" ? parseInt(e.target.value || "0", 10) : parseFloat(e.target.value || "0");
          const next = clone(current);
          setPath(next, f.key, Number.isNaN(v) ? 0 : v);
          setDraft(next);
        }}
      />
    );
  };

  const atomTypes = (current.atom_types as Array<Record<string, unknown>>) ?? [];

  return (
    <div>
      <div className="detail-head">
        <button className="back-btn" onClick={onBack} title="返回项目列表">
          <ArrowLeftOutlined />
        </button>
        <div className="detail-title">
          体系配置 <span className="topbar-sub">{projectId}</span>
        </div>
        <div style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
          {editing ? (
            <>
              <button className="mini-btn" onClick={() => setEditing(false)} disabled={saving}>
                取消
              </button>
              <button className="mini-btn accent" onClick={save} disabled={saving}>
                <SaveOutlined style={{ marginRight: 5 }} />
                {saving ? "保存中…" : "保存配置"}
              </button>
            </>
          ) : (
            <>
              <button className="mini-btn" onClick={startEdit}>
                <EditOutlined style={{ marginRight: 5 }} />
                编辑参数
              </button>
              <button className="mini-btn accent" onClick={rebuild} disabled={building} title="从 system.json 生成 system.data">
                <ThunderboltOutlined style={{ marginRight: 5 }} />
                {building ? "构建中…" : "重建体系"}
              </button>
              <button className="mini-btn accent" onClick={() => render(false)} disabled={rendering} title="从 system.json + 方法参数生成运行脚本">
                <CaretRightOutlined style={{ marginRight: 5 }} />
                {rendering ? "渲染中…" : "重新渲染脚本"}
              </button>
              <button className="mini-btn" onClick={() => setPreviewOpen(true)} title="浏览器内 3D 预览 + 一键启动 Vesta">
                <EyeOutlined style={{ marginRight: 5 }} />
                预览 3D 结构
              </button>
              <button className="mini-btn accent" disabled={methodParams.length === 0}
                onClick={() => setScanOpen(true)}
                title="对一个方法参数取多个值, 批量渲染脚本并排队执行">
                参数扫描
              </button>
            </>
          )}
        </div>
      </div>

      {consistency && (
        <div style={{ display: "flex", gap: 8, marginBottom: 16, flexWrap: "wrap" }}>
          <ConsistencyBadge label="体系构建" state={consistency.built_state} />
          <ConsistencyBadge label="渲染脚本" state={consistency.script_state} />
        </div>
      )}

      {errors.length > 0 && (
        <div className="card card-pad failure-card" style={{ marginBottom: 16 }}>
          <div className="card-title">配置校验未通过</div>
          {errors.map((e, i) => (
            <div key={i} style={{ fontSize: 13, marginTop: 4 }}>
              - {e}
            </div>
          ))}
        </div>
      )}

      {/* 几何/组成 (schema 驱动) */}
      <section className="card card-pad" style={{ marginBottom: 16 }}>
        <div className="card-title" style={{ marginBottom: 6 }}>
          体系参数
          <span className="topbar-sub" style={{ marginLeft: 10 }}>
            {view} · 数据源 system.json (单一真相源)
          </span>
        </div>
        {[...groups.entries()].map(([group, fs]) => (
          <div key={group} style={{ marginTop: 10 }}>
            <div className="meta-label" style={{ fontSize: 12, color: "var(--accent)", marginBottom: 2 }}>
              {GROUP_LABELS[group] ?? group}
            </div>
            <div className="kv-grid">
              {fs.map((f) => (
                <div className="kv-row" key={f.key}>
                  <span className="kv-label" title={f.note}>
                    {f.label}
                    {f.note ? " ⓘ" : ""}
                  </span>
                  {editing ? (
                    <span className="kv-value">{numInput(f)}</span>
                  ) : (
                    <span className="kv-value">
                      <span className="mono">{String(getPath(current, f.key) ?? "-")}</span>
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
        <div className="kv-row" style={{ borderTop: "1px dashed var(--border)", marginTop: 8 }}>
          <span className="kv-label">水模型</span>
          {editing ? (
            <Select
              size="small"
              style={{ width: 120 }}
              value={String(current.water_model ?? "SPCE")}
              onChange={(v) => {
                const next = clone(current);
                next.water_model = v;
                setDraft(next);
              }}
              options={(["SPCE", "SPC"] as string[]).map((m) => ({ value: m, label: m }))}
            />
          ) : (
            <span className="kv-value">
              <span className="mono">{String(current.water_model ?? "-")}</span>
            </span>
          )}
        </div>
      </section>

      {/* 力场表 */}
      <section className="card card-pad">
        <div className="card-title" style={{ marginBottom: 10 }}>
          力场参数表
          <span className="topbar-sub" style={{ marginLeft: 10 }}>
            pair_coeff 单一真相源 — 渲染脚本时由此表生成, 来源/置信度随行标注
          </span>
        </div>
        <div style={{ overflowX: "auto" }}>
          <table className="ff-table">
            <thead>
              <tr>
                <th>type</th>
                <th>名称</th>
                <th>电荷 (e)</th>
                <th>质量</th>
                <th>ε (kcal/mol)</th>
                <th>σ (Å)</th>
                <th>来源</th>
                <th>置信度</th>
              </tr>
            </thead>
            <tbody>
              {atomTypes.map((t, idx) => {
                const tid = Number(t.id);
                const upd = (key: string, value: unknown) => {
                  const next = clone(current);
                  (next.atom_types as Array<Record<string, unknown>>)[idx][key] = value;
                  setDraft(next);
                };
                const conf = String(t.confidence ?? "");
                return (
                  <tr key={tid} className={t.warning ? "warn-row" : ""}>
                    <td className="mono-cell">{tid}</td>
                    <td className="mono-cell">{String(t.name)}</td>
                    <td>
                      {editing ? (
                        <input
                          className="sys-input sm"
                          type="number"
                          step="any"
                          defaultValue={String(t.charge)}
                          onBlur={(e) => upd("charge", parseFloat(e.target.value || "0"))}
                        />
                      ) : (
                        String(t.charge)
                      )}
                    </td>
                    <td>{String(t.mass)}</td>
                    <td>
                      {editing ? (
                        <input
                          className="sys-input sm"
                          type="number"
                          step="any"
                          defaultValue={String(t.eps)}
                          onBlur={(e) => upd("eps", parseFloat(e.target.value || "0"))}
                        />
                      ) : (
                        String(t.eps)
                      )}
                    </td>
                    <td>
                      {editing ? (
                        <input
                          className="sys-input sm"
                          type="number"
                          step="any"
                          defaultValue={String(t.sigma)}
                          onBlur={(e) => upd("sigma", parseFloat(e.target.value || "0"))}
                        />
                      ) : (
                        String(t.sigma)
                      )}
                    </td>
                    <td style={{ maxWidth: 260 }}>
                      {editing ? (
                        <input
                          className="sys-input sm"
                          style={{ width: 220 }}
                          defaultValue={String(t.source ?? "")}
                          onBlur={(e) => upd("source", e.target.value)}
                        />
                      ) : (
                        <>
                          {String(t.source ?? "")}
                          {t.warning && (
                            <div style={{ color: "var(--err)", fontSize: 11.5, marginTop: 2 }}>
                              ⚠ {String(t.warning)}
                            </div>
                          )}
                          {t.ref && (
                            <div style={{ color: "var(--text-3)", fontSize: 11.5 }}>{String(t.ref)}</div>
                          )}
                        </>
                      )}
                    </td>
                    <td>
                      {editing ? (
                        <Select
                          size="small"
                          style={{ width: 76 }}
                          value={conf}
                          onChange={(v) => upd("confidence", v)}
                          options={["高", "中", "低"].map((c) => ({ value: c, label: c }))}
                        />
                      ) : (
                        <span style={{ color: CONF_COLORS[conf] ?? "var(--text-2)", fontWeight: 600 }}>{conf}</span>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>
      <System3DPreview
        projectId={projectId}
        open={previewOpen}
        onClose={() => setPreviewOpen(false)}
        onOpenVesta={handleOpenVesta}
      />
      <Modal
        title="参数扫描"
        open={scanOpen}
        onCancel={() => setScanOpen(false)}
        onOk={runScan}
        confirmLoading={scanning}
        okText={`发车 (${scanValues.split(/[\s,]+/).filter(Boolean).length} 个任务)`}
        cancelText="取消"
      >
        <div style={{ display: "grid", gap: 12 }}>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 4 }}>扫描参数</div>
            <select
              className="sys-input"
              value={scanParam}
              onChange={(e) => setScanParam(e.target.value)}
              style={{ width: "100%" }}
            >
              {methodParams.map((p) => (
                <option key={p.key} value={p.key}>{p.label} ({p.key})</option>
              ))}
            </select>
          </div>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 4 }}>
              值列表 (逗号/空格分隔, 最多 20 个)
            </div>
            <input className="sys-input" style={{ width: "100%" }}
              placeholder="320, 340, 360"
              value={scanValues}
              onChange={(e) => setScanValues(e.target.value)} />
          </div>
          <div style={{ fontSize: 12, color: "var(--text-3)", lineHeight: 1.7 }}>
            每个值渲染一份脚本副本 (仅写入任务工作区, 项目文件不动), 任务进入队列串行执行;
            完成后在任务记录页勾选同批次任务点「对比」可叠加 thermo 曲线。
          </div>
        </div>
      </Modal>
    </div>
  );
}

function System3DPreview({ projectId, open, onClose, onOpenVesta }: {
  projectId: string; open: boolean; onClose: () => void; onOpenVesta: (path: string) => void;
}) {
  const viewerRef = useRef<HTMLDivElement>(null);
  const viewerInst = useRef<any>(null);
  const [status, setStatus] = useState<"loading" | "ready" | "missing" | "error">("loading");
  const [dataPath, setDataPath] = useState<string>("");
  const [error, setError] = useState<string>("");
  useEffect(() => {
    if (!open) return;
    setStatus("loading"); setError("");
    const w = window as any;
    const loadData = () => {
      fetch("/api/projects/" + encodeURIComponent(projectId) + "/system-data")
        .then(r => r.ok ? r.json() : r.json().then(b => Promise.reject(new Error(b?.detail || "无 system.data — 请先「重建体系」"))))
        .then(d => {
          if (d.xyz_error) throw new Error("结构转换失败: " + d.xyz_error);
          if (!d.xyz) throw new Error("system.data 为空");
          setDataPath(d.path);
          // 3Dmol 不支持 LAMMPS data 格式 — 后端已转为 XYZ
          setTimeout(() => render(d.xyz), 60);
        })
        .catch(e => { setStatus("missing"); setError(e instanceof Error ? e.message : String(e)); });
    };
    const render = (xyz: string) => {
      if (!viewerRef.current || !w.$3Dmol) return;
      try {
        // 复用 viewer 实例 (GLContext 有浏览器上限); clear 保留本体
        if (!viewerInst.current) {
          viewerInst.current = w.$3Dmol.createViewer(viewerRef.current, { backgroundColor: "#fcfcfa" });
        }
        const viewer = viewerInst.current;
        viewer.clear();
        viewer.addModel(xyz, "xyz");
        viewer.setStyle({}, { stick: { radius: 0.18 }, sphere: { scale: 0.25 } });
        viewer.zoomTo();
        viewer.render();
        setStatus("ready");
      } catch (e) {
        setStatus("error"); setError("3Dmol 渲染失败: " + (e instanceof Error ? e.message : String(e)));
      }
    };
    if (!w.$3Dmol) {
      const s = document.createElement("script");
      s.src = "https://cdn.jsdelivr.net/npm/3dmol@2.5.5/build/3Dmol-min.js";
      s.onload = () => loadData();
      s.onerror = () => { setStatus("error"); setError("3Dmol CDN 加载失败 (网络问题)"); };
      document.head.appendChild(s);
    } else { loadData(); }
  }, [open, projectId]);

  return (
    <Drawer title="3D 结构预览" open={open} onClose={onClose} width={680}>
      <div style={{ marginBottom: 10, display: "flex", alignItems: "center", gap: 9 }}>
        <span style={{ fontSize: 12.5, color: "var(--text-2)" }}>
          基于 3Dmol.js 的快速预览 (只读); 如需完整功能请「用 Vesta 打开」。
        </span>
        <span style={{ flex: 1 }} />
        <Button icon={<ToolOutlined />} size="small" onClick={() => onOpenVesta(dataPath)} disabled={!dataPath}>
          用 Vesta 打开
        </Button>
      </div>
      {status === "loading" && <div style={{ color: "var(--text-3)", fontSize: 13 }}>加载 3Dmol 与 system.data…</div>}
      {status === "missing" && (
        <div style={{ padding: 18, background: "var(--err-weak)", borderRadius: 10, fontSize: 13 }}>
          <b>system.data 暂不可用</b>
          <div style={{ marginTop: 6, color: "var(--text-2)" }}>{error}</div>
        </div>
      )}
      {status === "error" && (
        <div style={{ padding: 18, background: "var(--err-weak)", borderRadius: 10, fontSize: 13 }}>{error}</div>
      )}
      <div
        ref={viewerRef}
        id={`sys3d-viewer-${projectId}`}
        style={{
          height: 480, border: "1px solid var(--border)", borderRadius: 12, marginTop: 10,
          display: status === "ready" ? "block" : "none",
        }}
      />
    </Drawer>
  );
}

function fmtKB(bytes: number): string {
  return bytes < 1024 ? `${bytes} B` : `${(bytes / 1024).toFixed(1)} KB`;
}

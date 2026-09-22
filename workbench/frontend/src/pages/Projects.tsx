import {
  BookOutlined,
  DeleteOutlined,
  PlayCircleOutlined,
  PlusOutlined,
} from "@ant-design/icons";
import {
  Button,
  Card,
  Checkbox,
  Col,
  Drawer,
  Input,
  List,
  Modal,
  Popconfirm,
  Row,
  Select,
  Spin,
  Steps,
  Tag,
  Typography,
  message,
} from "antd";
import { useCallback, useEffect, useState } from "react";
import type { ReactNode } from "react";
import {
  api,
  type CreateProjectRequest,
  type InboxItem,
  type JobKind,
  type MethodTemplate,
  type Project,
  type ProjectScript,
  type SchemaField,
  type SystemProfileTemplate,
  type TemplatesResponse,
} from "../api/client";
import { KindChip } from "../components/ui";
import { fmtSize } from "../utils";
import { copyToClipboard } from "../utils/aiPrompt";

const TINTS = ["var(--accent-weak)", "var(--teal-weak)", "var(--neutral-weak)"];
const TINT_ICONS = ["var(--accent)", "var(--teal)", "var(--text-2)"];

/** 项目与脚本页: 浏览子项目 / 在线新建项目 / 对脚本发起任务 */
export default function Projects({
  onOpenJob,
  onOpenSystem,
}: {
  onOpenJob: (id: string) => void;
  onOpenSystem: (id: string) => void;
}) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [confirming, setConfirming] = useState<{ project: Project; script: ProjectScript; ompThreads: number } | null>(null);
  const [starting, setStarting] = useState(false);
  const [wizardOpen, setWizardOpen] = useState(false);
  const [guideOpen, setGuideOpen] = useState(false);

  const load = useCallback(() => {
    setLoading(true);
    api
      .projects()
      .then(setProjects)
      .catch((e) => message.error(`加载项目失败: ${e instanceof Error ? e.message : e}`))
      .finally(() => setLoading(false));
  }, []);

  useEffect(load, [load]);

  const run = async () => {
    if (!confirming) return;
    setStarting(true);
    try {
      const job = await api.createJob(
        confirming.project.id,
        confirming.script.name,
        confirming.script.kind,
        confirming.ompThreads,
      );
      message.success(`任务 ${job.id} 已启动`);
      setConfirming(null);
      onOpenJob(job.id);
    } catch (e) {
      message.error(`启动失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setStarting(false);
    }
  };

  return (
    <div>
      <div className="page-hero" style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div>
          <h1 className="hero-title">项目与脚本</h1>
          <div className="hero-sub">选择脚本发起任务, 或从模板创建全新体系</div>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          <Button icon={<BookOutlined />} onClick={() => setGuideOpen(true)}>
            手动创建指南
          </Button>
          <Button type="primary" icon={<PlusOutlined />} onClick={() => setWizardOpen(true)}>
            新建项目
          </Button>
        </div>
      </div>

      <Spin spinning={loading}>
        <Row gutter={[16, 16]}>
          {projects.map((p) => (
            <Col span={8} key={p.id}>
              <Card
                title={p.name}
                extra={
                  p.builtin ? (
                    <Tag>内置</Tag>
                  ) : p.unregistered ? (
                    <Tag color="warning">未注册</Tag>
                  ) : (
                    <Tag>自建</Tag>
                  )
                }
              >
                {p.unregistered ? (
                  <div
                    style={{
                      minHeight: 44,
                      fontSize: 12.3,
                      lineHeight: 1.7,
                      color: "var(--text-2)",
                      background: "var(--neutral-weak)",
                      borderRadius: 10,
                      padding: "9px 12px",
                    }}
                  >
                    目录缺少 <Typography.Text code>project.json</Typography.Text>
                    , 已按目录名注册。脚本可直接运行; 补上 manifest 后刷新即获完整卡片 (
                    <Typography.Text
                      style={{ color: "var(--accent)", cursor: "pointer" }}
                      onClick={() => setGuideOpen(true)}
                    >
                      查看指南
                    </Typography.Text>
                    )。
                  </div>
                ) : (
                  <Typography.Paragraph type="secondary" style={{ minHeight: 44 }}>
                    {p.description}
                  </Typography.Paragraph>
                )}
                <List
                  size="small"
                  dataSource={p.scripts}
                  locale={{ emptyText: "无可运行脚本" }}
                  renderItem={(s) => (
                    <List.Item
                      actions={[
                        <Button
                          key="run"
                          size="small"
                          type="primary"
                          ghost
                          icon={<PlayCircleOutlined />}
                          onClick={() => setConfirming({ project: p, script: s, ompThreads: 8 })}
                        >
                          运行
                        </Button>,
                      ]}
                    >
                      <List.Item.Meta
                        title={
                          <Typography.Text code>
                            {s.name} <KindChip kind={s.kind as JobKind} />
                          </Typography.Text>
                        }
                        description={`${fmtSize(s.size)} · 更新于 ${s.mtime}`}
                      />
                    </List.Item>
                  )}
                />
                <div style={{ display: "flex", gap: 8, marginTop: 8 }}>
                  {p.has_system && (
                    <Button size="small" onClick={() => onOpenSystem(p.id)}>
                      体系配置
                    </Button>
                  )}
                  {!p.builtin && (
                    <Popconfirm
                      title="删除该项目目录？"
                      description="projects/ 下的全部文件将被移除"
                      onConfirm={async () => {
                        try {
                          await api.deleteProject(p.id);
                          message.success(`项目 ${p.id} 已删除`);
                          load();
                        } catch (e) {
                          message.error(`删除失败: ${e instanceof Error ? e.message : String(e)}`);
                        }
                      }}
                    >
                      <Button size="small" danger icon={<DeleteOutlined />}>
                        删除项目
                      </Button>
                    </Popconfirm>
                  )}
                </div>
              </Card>
            </Col>
          ))}
        </Row>
      </Spin>

      <Modal
        title="确认发起任务"
        open={!!confirming}
        onOk={run}
        confirmLoading={starting}
        onCancel={() => setConfirming(null)}
        okText="启动任务"
        cancelText="取消"
      >
        {confirming && (
          <p>
            项目:<b>{confirming.project.name}</b>
            <br />
            脚本:
            <Typography.Text code>{confirming.script.name}</Typography.Text>
            <br />
            方式:
            {confirming.script.kind === "lmp"
              ? "容器内 LAMMPS (docker exec lammpsd)"
              : confirming.script.kind === "build"
                ? "体系构建 (python -m common.build)"
                : "本地 Python (uv run)"}
            {confirming.script.kind === "lmp" && (
              <>
                <br />
                <span style={{ display: "inline-flex", alignItems: "center", gap: 8, marginTop: 6 }}>
                  OMP 线程数:
                  <Input
                    size="small"
                    type="number"
                    style={{ width: 80 }}
                    min={1}
                    max={64}
                    value={confirming.ompThreads}
                    onChange={(e) => {
                      const v = parseInt(e.target.value || "8", 10);
                      setConfirming({ ...confirming, ompThreads: Number.isNaN(v) ? 8 : Math.min(64, Math.max(1, v)) });
                    }}
                  />
                </span>
              </>
            )}
          </p>
        )}
      </Modal>

      <NewProjectWizard
        open={wizardOpen}
        onClose={() => setWizardOpen(false)}
        onCreated={(id) => {
          setWizardOpen(false);
          load();
          onOpenSystem(id);
        }}
        onOpenGuide={() => {
          setWizardOpen(false);
          setGuideOpen(true);
        }}
      />

      <ManualGuideDrawer open={guideOpen} onClose={() => setGuideOpen(false)} onChanged={load} />
    </div>
  );
}

/* ---------------- 新建项目向导 ---------------- */

const ID_RE = /^[a-z0-9][a-z0-9-]{1,39}$/;

function NewProjectWizard({
  open,
  onClose,
  onCreated,
  onOpenGuide,
}: {
  open: boolean;
  onClose: () => void;
  onCreated: (id: string) => void;
  onOpenGuide: () => void;
}) {
  const [tpl, setTpl] = useState<TemplatesResponse | null>(null);
  const [step, setStep] = useState(0);
  const [id_, setId_] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [profile, setProfile] = useState<SystemProfileTemplate | null>(null);
  const [waterModel, setWaterModel] = useState("SPCE");
  const [systemOverrides, setSystemOverrides] = useState<Record<string, number>>({});
  const [method, setMethod] = useState<MethodTemplate | null>(null);
  const [methodParams, setMethodParams] = useState<Record<string, number | boolean>>({});
  const [creating, setCreating] = useState(false);

  useEffect(() => {
    if (open) {
      api
        .templates()
        .then(setTpl)
        .catch((e) => message.error(`模板加载失败: ${e instanceof Error ? e.message : e}`));
    } else {
      setStep(0);
      setId_(""); setName(""); setDescription("");
      setProfile(null); setWaterModel("SPCE"); setSystemOverrides({});
      setMethod(null); setMethodParams({});
    }
  }, [open]);

  const numField = (f: SchemaField, value: number | undefined, onChange: (v: number) => void) => (
    <div key={f.key} style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12, padding: "7px 0" }}>
      <span style={{ fontSize: 12.5, color: "var(--text-2)" }} title={f.note}>
        {f.label}
        {f.note ? " ⓘ" : ""}
      </span>
      <Input
        size="small"
        style={{ width: 120 }}
        type="number"
        step="any"
        value={value ?? (f.default as number)}
        onChange={(e) => {
          const v = f.type === "int" ? parseInt(e.target.value || "0", 10) : parseFloat(e.target.value || "0");
          onChange(Number.isNaN(v) ? 0 : v);
        }}
      />
    </div>
  );

  const canNext =
    (step === 0 && ID_RE.test(id_) && name.trim().length > 0 && !!profile) ||
    step === 1 ||
    step === 2;

  const create = async () => {
    setCreating(true);
    try {
      const body: CreateProjectRequest = {
        id: id_,
        name: name.trim(),
        description: description.trim(),
        profile: profile!.id,
        water_model: waterModel,
        system_overrides: systemOverrides,
        method_id: method!.id,
        method_params: methodParams,
      };
      const r = await api.createProject(body);
      message.success(`项目 ${r.name} 已创建 (${r.dir}/)`);
      onCreated(r.id);
    } catch (e) {
      message.error(`创建失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setCreating(false);
    }
  };

  return (
    <Drawer
      title="新建计算项目"
      width={560}
      open={open}
      onClose={onClose}
      footer={
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <Button onClick={() => setStep(Math.max(0, step - 1))} disabled={step === 0}>
            上一步
          </Button>
          {step < 2 ? (
            <Button type="primary" disabled={!canNext} onClick={() => setStep(step + 1)}>
              下一步
            </Button>
          ) : (
            <Button type="primary" loading={creating} onClick={create}>
              创建项目
            </Button>
          )}
        </div>
      }
    >
      <Steps
        size="small"
        current={step}
        items={[{ title: "基本信息" }, { title: "体系参数" }, { title: "模拟方法" }]}
        style={{ marginBottom: 20 }}
      />
      {!tpl && <Spin />}
      {tpl && step === 0 && (
        <div style={{ display: "grid", gap: 12 }}>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 4 }}>项目 ID (小写字母/数字/连字符)</div>
            <Input value={id_} onChange={(e) => setId_(e.target.value)} placeholder="my-tensile" />
          </div>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 4 }}>项目名称</div>
            <Input value={name} onChange={(e) => setName(e.target.value)} placeholder="我的拉伸模拟" />
          </div>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 4 }}>描述 (可选)</div>
            <Input.TextArea rows={2} value={description} onChange={(e) => setDescription(e.target.value)} />
          </div>
          <div>
            <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 6 }}>体系类型</div>
            {tpl.system_profiles.map((p) => (
              <Card
                key={p.id}
                size="small"
                onClick={() => setProfile(p)}
                style={{
                  marginBottom: 8,
                  cursor: "pointer",
                  borderColor: profile?.id === p.id ? "var(--accent)" : undefined,
                  background: profile?.id === p.id ? "var(--accent-weak)" : undefined,
                }}
              >
                <b>{p.name}</b>
                <div style={{ fontSize: 12, color: "var(--text-2)" }}>{p.description}</div>
              </Card>
            ))}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <span style={{ fontSize: 12.5, color: "var(--text-2)" }}>水模型</span>
            <Select style={{ width: 120 }} value={waterModel} onChange={setWaterModel}
              options={tpl.water_models.map((m) => ({ value: m, label: m }))} />
          </div>
          <div style={{ fontSize: 12.3, color: "var(--text-3)", borderTop: "1px solid var(--border)", paddingTop: 10 }}>
            想绕过向导、直接在文件系统里建目录写脚本?{" "}
            <Typography.Text style={{ color: "var(--accent)", cursor: "pointer" }} onClick={onOpenGuide}>
              查看手动创建指南
            </Typography.Text>
          </div>
        </div>
      )}
      {tpl && step === 1 && profile && (
        <div>
          <Typography.Paragraph type="secondary" style={{ fontSize: 12.5 }}>
            以下参数写入 system.json (体系单一真相源), 构建引擎据此生成 system.data。
          </Typography.Paragraph>
          {profile.fields.map((f) =>
            numField(
              f,
              systemOverrides[f.key],
              (v) => setSystemOverrides((prev) => ({ ...prev, [f.key]: v })),
            ),
          )}
        </div>
      )}
      {tpl && step === 2 && (
        <div>
          <div style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 6 }}>模拟方法模板</div>
          {tpl.methods.map((m) => (
            <Card
              key={m.id}
              size="small"
              onClick={() => {
                setMethod(m);
                setMethodParams({});
              }}
              style={{
                marginBottom: 8,
                cursor: "pointer",
                borderColor: method?.id === m.id ? "var(--accent)" : undefined,
                background: method?.id === m.id ? "var(--accent-weak)" : undefined,
              }}
            >
              <b>{m.name}</b>
              <div style={{ fontSize: 12, color: "var(--text-2)" }}>{m.description}</div>
            </Card>
          ))}
          {method &&
            method.params.map((f) =>
              f.type === "bool" ? (
                <Checkbox
                  key={f.key}
                  checked={(methodParams[f.key] as boolean) ?? (f.default as boolean)}
                  onChange={(e) => setMethodParams((prev) => ({ ...prev, [f.key]: e.target.checked }))}
                >
                  {f.label}
                </Checkbox>
              ) : (
                numField(
                  f,
                  methodParams[f.key] as number | undefined,
                  (v) => setMethodParams((prev) => ({ ...prev, [f.key]: v })),
                )
              ),
            )}
        </div>
      )}
    </Drawer>
  );
}

/* ---------------- 手动创建指南 ---------------- */

const GUIDE_MANIFEST = `{
  "id": "my-tensile",
  "name": "我的拉伸模拟",
  "description": "一句话描述研究体系"
}`;

/** 历史研究迁移用的标准版提示词 (带占位符注释) */
const MIGRATION_PROMPT = `我的 LAMMPS 历史研究需要迁入本工作台, 完整文件都在:

  <旧资料根目录绝对路径>           ← 必填: 例 D:\\\\research\\\\clay-md-2024 或 ~/work/strontium

目录里大致有:                       ← 可选: 你记得的文件类型 (帮助 agent 识别)
  - LAMMPS 输入脚本 (run.lmp / in.* 等)
  - system.data / *.data (体系数据)
  - Python 分析脚本 (analyze.py / plot_*.py 等)
  - 轨迹 / 日志 (prod.lammpstrj / log.lammps 等)
  - 散落的输出 (xlsx / png / csv / txt 等)

请按本工作台规则完成以下工作:
  1. 扫描旧目录, 分类列出所有文件 (不要读大轨迹/日志全文)
  2. 按角色归类 (run / analyze / system_data / artifact) 并识别研究主题
  3. 在 projects/_inbox/<project_id>/ 下建立结构化副本:
     - project.json (id / name / description)
     - run.lmp / analyze.py 等 (按角色复制)
     - README.md (引用映射清单)
     - migration_manifest.md (逐条 原路径 → 新路径 → 角色 → 备注)
  4. 不要修改我原路径的任何文件, 工作台内副本可自由改
  5. 完成后告诉我待入库项目 id, 我在抽屉的「待入库清单」里确认`;

const GUIDE_TREE = `lammps-test/                     ← 仓库根
├─ projects/                     ← 手动项目放这里 (文件夹即项目)
│  └─ my-tensile/                ← 刷新页面自动注册, 零重启
│     ├─ project.json            ← 必需·项目身份 (右侧最小模板)
│     ├─ run.lmp                 ← 顶层 *.lmp → LAMMPS 任务
│     ├─ analyze.py              ← 顶层 *.py → Python 分析任务
│     ├─ system.json             ← 可选·体系配置 (体系配置页数据层)
│     ├─ system.data             ← 可选·构建产物 (「重建体系」生成)
│     └─ ff.field                ← 脚本 include/read_data 引用的依赖
└─ lammps-data-docker/jobs/<id>/ ← 任务工作区 (自动暂存+产物, 勿手改)`;

function GuideSection({ title, children }: { title: string; children: ReactNode }) {
  return (
    <div style={{ marginBottom: 18 }}>
      <div style={{ fontWeight: 650, fontSize: 13.5, marginBottom: 7 }}>{title}</div>
      {children}
    </div>
  );
}

function GuideItem({ k, children }: { k: string; children: ReactNode }) {
  return (
    <div style={{ display: "flex", gap: 10, padding: "5px 0", fontSize: 12.6, lineHeight: 1.7 }}>
      <span style={{ color: "var(--text-2)", flex: "none", minWidth: 92, fontWeight: 550 }}>{k}</span>
      <span style={{ color: "var(--text-1)", minWidth: 0 }}>{children}</span>
    </div>
  );
}

/** 手动创建项目指南: 文件系统直建目录的规范与平台自动行为 (与 docs/workflows.md 同源) */
function ManualGuideDrawer({
  open,
  onClose,
  onChanged,
}: {
  open: boolean;
  onClose: () => void;
  /** 入库/丢弃后通知父级刷新项目列表 */
  onChanged?: () => void;
}) {
  const [inbox, setInbox] = useState<InboxItem[] | null>(null);
  const [inboxError, setInboxError] = useState<string | null>(null);
  const [inboxBusy, setInboxBusy] = useState<Set<string>>(new Set());

  const loadInbox = useCallback(() => {
    api
      .projectsInbox()
      .then((r) => {
        setInbox(r.items);
        setInboxError(null);
      })
      .catch((e) => setInboxError(e instanceof Error ? e.message : String(e)));
  }, []);

  useEffect(() => {
    if (open) loadInbox();
  }, [open, loadInbox]);

  const setItemBusy = (id: string, busy: boolean) => {
    setInboxBusy((prev) => {
      const next = new Set(prev);
      if (busy) next.add(id);
      else next.delete(id);
      return next;
    });
  };

  const confirmIn = async (item: InboxItem) => {
    setItemBusy(item.id, true);
    try {
      const r = await api.confirmInbox(item.id);
      message.success(`已入库 ${r.id} → ${r.dir}${r.manifest_backfilled ? " (自动补最小 manifest)" : ""}`);
      loadInbox();
      onChanged?.();
    } catch (e) {
      message.error(`入库失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setItemBusy(item.id, false);
    }
  };

  const discardStaged = async (item: InboxItem) => {
    setItemBusy(item.id, true);
    try {
      await api.discardInbox(item.id);
      message.success("已丢弃暂存副本 (你的旧路径文件不受影响)");
      loadInbox();
    } catch (e) {
      message.error(`丢弃失败: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setItemBusy(item.id, false);
    }
  };

  const copyPrompt = async (text: string, label: string) => {
    try {
      await copyToClipboard(text);
      message.success(`${label}已复制到剪贴板`);
    } catch {
      message.error("复制失败, 请手动选择文本复制");
    }
  };

  return (
    <Drawer title="手动创建项目指南" width={600} open={open} onClose={onClose}>
      <Typography.Paragraph type="secondary" style={{ fontSize: 12.6, marginTop: 0 }}>
        向导适合从模板起步; 任意体系都可以直接在文件系统里建目录、写脚本 — 平台按约定自动发现,
        无需注册代码、无需重启。
      </Typography.Paragraph>

      <GuideSection title="0. 从历史散落研究迁移进来">
        <div style={{ fontSize: 12.6, color: "var(--text-1)", lineHeight: 1.75, marginBottom: 10 }}>
          适用: 你之前跑过 LAMMPS, 文件散落在自己电脑某处 (可能根本没接触过本工作台),
          现在想用本工作台继续推进。
        </div>
        <GuideItem k="你要做的事">
          <ol style={{ margin: 0, paddingLeft: 18, lineHeight: 1.85 }}>
            <li>复制下方「标准版提示词」, 按你自己的情况填实占位符</li>
            <li>把填好的提示词 + 旧资料路径告诉 agent (我)</li>
            <li>agent 会扫描 → 识别 → 结构化迁移, 并给你一份映射清单待你确认</li>
          </ol>
        </GuideItem>
        <GuideItem k="硬约束">
          你的旧路径文件 <Typography.Text strong>不会被修改</Typography.Text>;
          agent 只读取、识别、复制副本到本工作台空间。副本可以自由改动。
        </GuideItem>
        <GuideItem k="迁移去向">
          产物先到 <Typography.Text code>projects/_inbox/&lt;id&gt;/</Typography.Text>{" "}
          (暂存, 不入库), 抽屉底部的「待入库清单」会列出;
          你点「确认入库」后才正式注册到项目库, 与新建项目走同一发现机制。
        </GuideItem>
        <div style={{ marginTop: 12 }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              marginBottom: 6,
            }}
          >
            <span style={{ fontWeight: 600, fontSize: 12.6, color: "var(--text-1)" }}>
              📋 标准版提示词 (可复制)
            </span>
            <Typography.Paragraph
              copyable={{ text: MIGRATION_PROMPT, tooltips: ["复制模板", "已复制"] }}
              style={{ margin: 0 }}
            >
              <Button size="small" type="primary" ghost onClick={() => copyPrompt(MIGRATION_PROMPT, "迁移提示词模板")}>
                复制模板
              </Button>
            </Typography.Paragraph>
          </div>
          <pre
            style={{
              margin: 0,
              padding: "12px 14px",
              borderRadius: 10,
              background: "var(--neutral-weak)",
              border: "1px dashed var(--border)",
              fontFamily: "var(--font-mono)",
              fontSize: 11.6,
              lineHeight: 1.75,
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
            }}
          >
            {MIGRATION_PROMPT}
          </pre>
          <div style={{ fontSize: 11.8, color: "var(--text-2)", marginTop: 7, lineHeight: 1.7 }}>
            填好后发给 agent 即可。agent 完成扫描后会先告诉你扫描到的文件清单,
            再开始复制 — 你可以随时叫停。
          </div>
        </div>
      </GuideSection>

      <GuideSection title="① 目录放在哪里">
        <pre
          style={{
            margin: 0,
            padding: "12px 14px",
            borderRadius: 10,
            background: "var(--neutral-weak)",
            fontFamily: "var(--font-mono)",
            fontSize: 11.8,
            lineHeight: 1.75,
            overflowX: "auto",
          }}
        >
          {GUIDE_TREE}
        </pre>
      </GuideSection>

      <GuideSection title="② project.json 最小模板 (可复制)">
        <Typography.Paragraph
          copyable={{ text: GUIDE_MANIFEST, tooltips: ["复制模板", "已复制"] }}
          style={{ margin: 0 }}
        >
          <pre
            style={{
              margin: 0,
              padding: "12px 14px",
              borderRadius: 10,
              border: "1px solid var(--border)",
              fontFamily: "var(--font-mono)",
              fontSize: 11.8,
              lineHeight: 1.75,
            }}
          >
            {GUIDE_MANIFEST}
          </pre>
        </Typography.Paragraph>
        <div style={{ fontSize: 12.3, color: "var(--text-2)", marginTop: 7, lineHeight: 1.7 }}>
          <Typography.Text code>id</Typography.Text> 必须与目录名一致。缺 manifest
          的非空目录也会被兜底注册 (卡片带「未注册」角标), 但建议补上以获得名称与描述。
          需要体系数据层 (重建/渲染) 时, 推荐用向导生成完整 manifest。
        </div>
      </GuideSection>

      <GuideSection title="③ 平台的自动行为">
        <GuideItem k="脚本发现">
          项目顶层 <Typography.Text code>*.lmp</Typography.Text> /{" "}
          <Typography.Text code>*.py</Typography.Text> 按扩展名判型, 自动出现在卡片列表, 直接「运行」。
        </GuideItem>
        <GuideItem k="依赖暂存">
          发起 LAMMPS 任务时, 脚本 <Typography.Text code>include</Typography.Text> /{" "}
          <Typography.Text code>read_data</Typography.Text> 引用的同目录文件自动闭包拷入工作区;
          顶层 <Typography.Text code>*.data</Typography.Text> 全量兜底 — 引用同目录相对路径即可。
        </GuideItem>
        <GuideItem k="体系层可选">
          <Typography.Text code>system.json</Typography.Text> (体系参数真相源) +
          <Typography.Text code> system.data</Typography.Text> (构建产物)
          启用「体系配置」页与模板渲染; 纯脚本项目没有也完全合法。
        </GuideItem>
        <GuideItem k="产物去向">
          LAMMPS 任务产物写入 <Typography.Text code>lammps-data-docker/jobs/&lt;任务id&gt;/</Typography.Text>{" "}
          (详情页可浏览/下载); Python 分析脚本输出约定为脚本同目录, 刷新后仍从原卡片发起。
        </GuideItem>
        <GuideItem k="在线编辑">
          卡片脚本可在线保存, 仅限既有的 <Typography.Text code>.lmp / .py</Typography.Text>;
          新文件在文件系统创建后刷新页面即见。
        </GuideItem>
      </GuideSection>

      <GuideSection title="④ 手动跑模拟与任务记录">
        <GuideItem k="CLI 同源">
          命令行 (<Typography.Text code>uv run run-sr-sim</Typography.Text> 等)
          与工作台共用同一执行契约 (common.runner), 结果一致。
        </GuideItem>
        <GuideItem k="记录边界">
          「任务记录」仅收录工作台发起的任务; 手动 CLI 执行暂不入库
          (曲线/失败解析请改从工作台发起, 或关注后续版本)。体系构建类手动命令:{" "}
          <Typography.Text code>uv run python -m common.build &lt;项目目录&gt;</Typography.Text>。
        </GuideItem>
      </GuideSection>

      <GuideSection title="⑤ 待入库清单 (迁移暂存区)">
        <div style={{ fontSize: 12.3, color: "var(--text-2)", marginBottom: 8, lineHeight: 1.7 }}>
          agent 按「0.」的提示词迁移的历史研究会先暂存在{" "}
          <Typography.Text code>projects/_inbox/&lt;id&gt;/</Typography.Text>, 审阅后逐条入库;
          暂存产物不会出现在项目卡片列表。
        </div>
        {inbox === null && !inboxError ? (
          <Spin size="small" />
        ) : inboxError ? (
          <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "6px 0 2px" }}>
            <span style={{ fontSize: 12.3, color: "var(--err)", lineHeight: 1.6 }}>
              ⚠ 待入库清单加载失败: {inboxError}
            </span>
            <Button size="small" onClick={loadInbox}>
              重试
            </Button>
          </div>
        ) : inbox && inbox.length === 0 ? (
          <div style={{ fontSize: 12.3, color: "var(--text-3)", padding: "6px 0 2px" }}>
            暂无待入库迁移。
          </div>
        ) : (
          <List
            size="small"
            dataSource={inbox ?? []}
            renderItem={(item) => (
              <List.Item
                style={{
                  display: "block",
                  padding: "10px 12px",
                  marginBottom: 8,
                  border: "1px solid var(--border)",
                  borderRadius: 10,
                  background: "var(--neutral-weak)",
                }}
              >
                <div style={{ display: "flex", alignItems: "baseline", gap: 8, flexWrap: "wrap" }}>
                  <span style={{ fontWeight: 600, fontSize: 12.8, color: "var(--text-1)" }}>
                    {item.name}
                  </span>
                  <Typography.Text code style={{ fontSize: 11.4 }}>
                    {item.target_id}
                  </Typography.Text>
                  <span style={{ fontSize: 11.6, color: "var(--text-2)" }}>
                    {item.file_count} 个文件 · {fmtSize(item.total_bytes)}
                  </span>
                </div>
                {item.description && (
                  <div style={{ fontSize: 11.8, color: "var(--text-2)", marginTop: 3, lineHeight: 1.6 }}>
                    {item.description}
                  </div>
                )}
                <div style={{ fontSize: 11.4, marginTop: 5, lineHeight: 1.8 }}>
                  {item.has_manifest ? (
                    <span style={{ color: "var(--text-2)" }}>✓ project.json</span>
                  ) : (
                    <span style={{ color: "var(--text-2)" }}>缺 project.json (确认时自动补最小 manifest)</span>
                  )}
                  {" · "}
                  {item.has_migration_manifest ? (
                    <span style={{ color: "var(--text-2)" }}>✓ 映射说明</span>
                  ) : (
                    <span style={{ color: "var(--text-2)" }}>缺 migration_manifest.md</span>
                  )}
                  {item.target_conflict && (
                    <span style={{ color: "var(--err)", marginLeft: 6 }}>
                      ⚠ 目标 id 已被占用, 不可入库
                    </span>
                  )}
                </div>
                <div style={{ display: "flex", gap: 8, marginTop: 8 }}>
                  <Popconfirm
                    title={`确认入库为 projects/${item.target_id}/?`}
                    description="目录将移动到项目库并自动注册, 与新建项目同一机制。"
                    okText="确认入库"
                    cancelText="取消"
                    disabled={item.target_conflict}
                    onConfirm={() => confirmIn(item)}
                  >
                    <Button
                      size="small"
                      type="primary"
                      disabled={item.target_conflict}
                      loading={inboxBusy.has(item.id)}
                    >
                      确认入库
                    </Button>
                  </Popconfirm>
                  <Popconfirm
                    title="丢弃这份暂存副本?"
                    description="仅删除工作台内 _inbox 副本; 你的旧路径文件不受影响。"
                    okText="丢弃"
                    okButtonProps={{ danger: true }}
                    cancelText="取消"
                    onConfirm={() => discardStaged(item)}
                  >
                    <Button size="small" danger loading={inboxBusy.has(item.id)}>
                      丢弃
                    </Button>
                  </Popconfirm>
                </div>
              </List.Item>
            )}
          />
        )}
      </GuideSection>
    </Drawer>
  );
}

/** 后端 API 客户端与类型定义 */

export type JobStatus = "queued" | "running" | "completed" | "failed" | "canceled" | "interrupted";
export type JobKind = "lmp" | "python" | "build";

export interface Job {
  id: string;
  project_id: string;
  project_name: string;
  script: string;
  kind: JobKind;
  command: string;
  status: JobStatus;
  exit_code: number | null;
  created_at: string | null;
  started_at: string | null;
  finished_at: string | null;
  log_path: string | null;
  /** LAMMPS 任务的工作区 (数据目录 jobs/<id>/); Python 任务为 null */
  workspace: string | null;
  /** OMP 线程数 (LAMMPS 任务) */
  omp_threads: number;
  /** 来源: workbench (默认) | cli (终端 runner) */
  source: "workbench" | "cli";
  /** 参数扫描批次 id */
  batch: string | null;
}

export interface JobDetail extends Job {
  log_tail: string[];
  /** 热力学样本 (最近 500 行): columns + rows 与 LAMMPS thermo 表头对应 */
  thermo: ThermoData;
  /** 失败任务的简要解析 (仅 failed 状态) */
  failure: FailureInfo | null;
  /** 平衡判据 (仅 LAMMPS 且有 thermo 数据) */
  equilibrium: Equilibrium | null;
  /** 环境指纹 (system.json sha + 镜像 + LAMMPS 版本) */
  fingerprint: JobFingerprint | null;
}

export interface ThermoData {
  columns: string[];
  rows: number[][];
}

export interface FailureInfo {
  summary: string;
  error_line: string | null;
  detail_line: string | null;
  hint: string;
  /** high=结果不可信必须修 / medium=可调参重跑 / low=环境性 */
  severity: "high" | "medium" | "low";
  /** 建议修复动作 (有序) */
  actions: string[];
  /** 是否存在从既有状态续跑的策略 */
  can_resume: boolean;
}

/** 体系一致性链 (system.json ↔ 构建产物 ↔ 渲染脚本) */
export interface SystemConsistency {
  built_state: "built" | "stale" | "never";
  script_state: "sync" | "hand_edited" | "missing";
  system_sha: string;
  built_system_sha: string | null;
  run_lmp_sha: string | null;
  rendered_sha: string | null;
}

/** 平衡判据 (RadonPy 思想: 末窗口线性漂移检验) */
export interface EquilibriumCheck {
  quantity: string;
  drift: number;
  threshold: number;
  verdict: 'pass' | 'fair' | 'poor';
  samples: number;
}
export interface Equilibrium {
  status: 'good' | 'fair' | 'poor' | 'unknown';
  checks: EquilibriumCheck[];
  note?: string;
  samples?: number;
}

/** 任务环境指纹 (可比性) */
export interface JobFingerprint {
  system_sha?: string;
  image_id?: string | null;
  image?: string | null;
  lmp_version?: string | null;
}

/** 轨迹统计在线分析结果 */
export interface FrameAtom { id: number; type: number; x: number; y: number; z: number }
export interface TrajectoryAnalysis {
  summary: { frames: number; atoms: number; types: Record<string, number> };
  z_profile: { type: string; label?: string; bins: { z: number; freq: number }[] }[];
  msd: {
    type: string;
    label?: string;
    points: { step: number; lag: number; value: number }[];
    /** MSD 末窗线性拟合: 斜率 Å²/step (物理换算需 dt) + R² + 拟合窗口 */
    diffusion?: { slope_a2_per_step: number; r2: number; window: [number, number] } | null;
  }[];
  frames_3d?: {
    first: FrameAtom[];
    last: FrameAtom[];
    timestep_first: number;
    timestep_last: number;
  };
}

export interface MsdCompareEntry {
  id: string;
  script?: string;
  project_name?: string;
  status: "done" | "idle" | "running" | "none" | "error" | "missing";
  note?: string;
  msd?: TrajectoryAnalysis["msd"][number];
}
export interface MsdComparison { series: MsdCompareEntry[] }

/** lint 结果 (errors 阻止发车, warnings 放行提示) */
export interface LintResult {
  errors: string[];
  warnings: string[];
}

export interface ToolInfo {
  found: boolean;
  path: string | null;
  version_hint: string | null;
  source: 'env' | 'known' | 'fallback' | 'manual' | null;
}

export interface LocalToolsDetect {
  platform: string;
  vmd: ToolInfo;
  vesta: ToolInfo;
}

export interface LauncherResult {
  filename: string;
  content: string;
  exe: string | null;
  found: boolean;
}

export interface WorkspaceFile {
  path: string;
  size: number;
  mtime: number;
}

export interface ProjectScript {
  name: string;
  kind: JobKind;
  size: number;
  mtime: string;
}

export interface Project {
  id: string;
  name: string;
  dir: string;
  description: string;
  builtin: boolean;
  has_system: boolean;
  /** 手动直建且缺 project.json (兜底按目录名注册) */
  unregistered?: boolean;
  scripts: ProjectScript[];
}

/** 迁移暂存区条目 (projects/_inbox/<id>/, 手动创建指南抽屉「待入库清单」用) */
export interface InboxItem {
  id: string; // 暂存目录名
  name: string; // manifest.name 或目录名
  description: string;
  has_manifest: boolean;
  has_migration_manifest: boolean; // 文件映射转换说明
  files: { name: string; size: number }[];
  file_count: number;
  total_bytes: number;
  target_id: string; // 入库后的项目 id
  target_conflict: boolean; // 目标 id 已被占用
  mtime: string;
}

export interface SchemaField {
  key: string; // 点分路径, 如 geometry.surface.a
  label: string;
  type: "number" | "int" | "bool" | "string";
  default: number | boolean | string;
  note?: string;
}

export interface SystemProfileTemplate {
  id: string;
  name: string;
  description: string;
  fields: SchemaField[];
}

export interface MethodTemplate {
  id: string;
  name: string;
  description: string;
  params: SchemaField[];
}

export interface TemplatesResponse {
  system_profiles: SystemProfileTemplate[];
  methods: MethodTemplate[];
  water_models: string[];
}

export interface CreateProjectRequest {
  id: string;
  name: string;
  description: string;
  profile: string;
  water_model: string;
  system_overrides: Record<string, number | boolean | string>;
  method_id: string;
  method_params: Record<string, number | boolean | string>;
}

export interface DockerInfo {
  available: boolean;
  container_running: boolean;
  container_status: string | null;
  image: string | null;
  error: string | null;
  data_mount_host: string | null;
  data_mount_ok: boolean;
  /** 容器内真实 LAMMPS 进程数 (pgrep 实测; null = 未知) */
  lmp_processes: number | null;
}

export interface Health {
  ok: boolean;
  time: string;
  python: string;
  docker: DockerInfo;
  /** v1.8.5: 当前执行后端摘要 (LocalDocker / RemoteHPC 等) */
  backend: BackendSummary;
}

/** v1.8.5: 执行后端摘要 (仪表盘状态卡 / 配置抽屉共用) */
export interface BackendSummary {
  type: string;
  name: string;
  status: string;
  action_needed: string;
  available: boolean;
}

/** v1.8.5: 后端配置项 (frontend 抽屉编辑用) */
export interface BackendConfig {
  type: string;
  ssh_host?: string;
  ssh_user?: string;
  ssh_key_path?: string;
  ssh_port?: number;
  hpc_workdir?: string;
  hpc_sbatch_template?: string;
  hpc_modules?: string[];
}

/** v1.8.5: 后端详细探测结果 (含 details / error 等冗余字段) */
export interface BackendInfo extends BackendSummary {
  error?: string | null;
  details?: Record<string, unknown>;
  [key: string]: unknown;
}

/** v1.8.5: 已注册 backend 列表项 (供下拉) */
export interface BackendListItem {
  type: string;
  name: string;
  status: string;
  action_needed: string;
  available: boolean;
  error?: string;
}

/** v1.8.5: 一键启动结果 (与 BackendStartResult 对齐) */
export interface BackendStartResult {
  ok: boolean;
  stage: string;
  message: string;
  hint_url: string | null;
}

export type WsMessage =
  | { type: "log"; line: string }
  | { type: "status"; status: JobStatus; exit_code?: number | null }
  | { type: "thermo"; columns?: string[]; rows?: number[][]; row?: number[] }
  | { type: "ping" };

/** 结束工作台进程的结果 (blocked = 后端互锁: 有运行中任务) */
export type ShutdownResult =
  | { outcome: "shutting_down"; orphan_processes_cleaned: number }
  | {
      outcome: "blocked";
      message: string;
      jobs: { id: string; project_name: string | null; script: string | null }[];
    }
  | { outcome: "error"; message: string };

async function http<T>(url: string, init?: RequestInit): Promise<T> {
  const resp = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!resp.ok) {
    let detail = `HTTP ${resp.status}`;
    try {
      const body = await resp.json();
      if (body?.detail) detail = body.detail;
    } catch {
      /* 非 JSON 错误体, 保留状态码 */
    }
    throw new Error(detail);
  }
  return resp.json() as Promise<T>;
}

export const api = {
  health: () => http<Health>("/api/health"),
  /** 容器资源监测: CPU% / 内存 / 数据目录大小 + 5 分钟趋势 ring buffer */
  dockerMetrics: () => http<{
    current: { cpu_pct: number; mem_used_bytes: number; mem_pct: number } | null;
    history: { t: number; cpu_pct: number; mem_used_bytes: number; mem_pct: number }[];
    data_dir_size_bytes: number | null;
    data_dir_path: string;
  }>("/api/docker/metrics"),
  /** 一键启动 lammpsd 容器 (容器停止时) */
  dockerStart: () => http<{ ok: boolean; message: string; status: string | null; stage: string; hint_url: string | null }>(
    "/api/docker/start", { method: "POST" }
  ),
  /** 执行后端: 当前配置 + 状态 */
  backendGet: () => http<{ config_path: string; config: BackendConfig; info: BackendInfo }>(
    "/api/backend"),
  /** 执行后端: 已注册列表 (Local Docker / Remote HPC 等) */
  backendList: () => http<{ backends: BackendListItem[] }>("/api/backend/list"),
  /** 执行后端: 切换并持久化 */
  backendPut: (cfg: BackendConfig) =>
    http<{ config: BackendConfig; info: BackendInfo }>("/api/backend", {
      method: "PUT", body: JSON.stringify(cfg),
    }),
  /** 执行后端: 连通性测试 (不持久化) */
  backendTest: (cfg?: Partial<BackendConfig>) =>
    http<{ info: BackendInfo }>("/api/backend/test", {
      method: "POST", body: JSON.stringify(cfg ?? {}),
    }),
  projects: () => http<Project[]>("/api/projects"),
  jobs: () => http<Job[]>("/api/jobs"),
  job: (id: string) => http<JobDetail>(`/api/jobs/${id}`),
  createJob: (projectId: string, script: string, kind: JobKind, ompThreads = 8) =>
    http<Job>("/api/jobs", {
      method: "POST",
      body: JSON.stringify({ project_id: projectId, script, kind, omp_threads: ompThreads }),
    }),
  cancelJob: (id: string) => http<Job>(`/api/jobs/${id}/cancel`, { method: "POST" }),
  /** 删除终态任务及其全部产物 (工作区+日志+记录) */
  deleteJob: (id: string) =>
    http<{ deleted: boolean; id: string; freed_bytes: number }>(`/api/jobs/${id}`, {
      method: "DELETE",
    }),
  /** 任务工作区产物列表 */
  jobFiles: (id: string) =>
    http<{ files: WorkspaceFile[]; truncated: boolean }>(`/api/jobs/${id}/files`),
  /** 工作区文本文件内容 (预览用) */
  jobFileContent: (id: string, path: string) =>
    http<{ path: string; size: number; text: string }>(
      `/api/jobs/${id}/files/content?path=${encodeURIComponent(path)}`,
    ),
  /** 参数扫描: 对每个值渲染脚本副本并批量发车 (进队列) */
  scanProject: (id: string, paramKey: string, values: number[], ompThreads: number) =>
    http<{ batch: string; param: string; values: number[]; jobs: { id: string; value: number; status: string }[] }>(
      `/api/projects/${id}/scan`,
      { method: "POST", body: JSON.stringify({ param_key: paramKey, values, omp_threads: ompThreads }) },
    ),
  /** 多任务 thermo 对比数据 */
  compareJobs: (ids: string[]) =>
    http<{ series: { id: string; script: string; project_name: string; status: string; batch: string | null; thermo: ThermoData }[] }>(
      `/api/jobs/compare?ids=${ids.join(",")}`),
  /** 多任务全原子 MSD 对比，使用现有轨迹分析缓存 */
  compareMsd: (ids: string[]) =>
    http<MsdComparison>(`/api/jobs/compare-msd?ids=${encodeURIComponent(ids.join(","))}`),
  /** 任务工作区检查点列表 */
  getRestarts: (id: string) =>
    http<{ restarts: { name: string; size: number; mtime: number }[] }>(`/api/jobs/${id}/restarts`),
  /** 从最新检查点续跑 — 重载区分返回 */
  resumeJob: (id: string, steps: number, ompThreads: number) =>
    http<{ id: string; source_restart?: string }>(`/api/jobs/${id}/resume`,
      { method: "POST", body: JSON.stringify({ steps, omp_threads: ompThreads }) }),
  /** 轨迹统计: 获取 (idle=待触发/running/done/error/none) */
  getAnalysis: (id: string) =>
    http<{ status: string; result?: TrajectoryAnalysis; note?: string; error?: string }>(
      `/api/jobs/${id}/analysis`),
  /** 轨迹统计: 触发后台计算 */
  runAnalysis: (id: string) =>
    http<{ status: string; cached: boolean }>(`/api/jobs/${id}/analysis`, { method: "POST" }),

  /** 工作区文件下载地址 (<a href> 直用) */
  jobFileDownloadUrl: (id: string, path: string) =>
    `/api/jobs/${id}/files/content?path=${encodeURIComponent(path)}&download=true`,
  // ---- 项目 / 体系配置 / 模板 ----
  templates: () => http<TemplatesResponse>("/api/templates"),
  createProject: (body: CreateProjectRequest) =>
    http<{ id: string; dir: string; name: string }>("/api/projects", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  getSystem: (id: string) =>
    http<{
      config: Record<string, unknown>;
      errors: string[];
      consistency: SystemConsistency;
      meta: { method_id: string | null; method_params: Record<string, number | boolean> };
    }>(`/api/projects/${id}/system`),
  putSystem: (id: string, config: Record<string, unknown>) =>
    http<{ saved: boolean; note: string }>(`/api/projects/${id}/system`, {
      method: "PUT",
      body: JSON.stringify(config),
    }),
  renderRunLmp: (
    id: string,
    params: { method_id?: string; params?: Record<string, unknown>; force?: boolean },
  ) =>
    http<{ file: string; manual_edits_detected: boolean; bytes: number; lint: LintResult }>(
      `/api/projects/${id}/render`,
      { method: "POST", body: JSON.stringify(params) },
    ),
  saveFile: (id: string, name: string, content: string) =>
    http<{ saved: boolean; file: string; bytes: number }>(
      `/api/projects/${id}/files/${name}`,
      { method: "PUT", body: JSON.stringify({ content }) },
    ),
  /** 删除用户自建项目 (projects/ 目录) */
  deleteProject: (id: string) =>
    http<{ deleted: boolean; id: string }>(`/api/projects/${id}`, { method: "DELETE" }),
  /** 迁移暂存区: 待入库清单 (手动创建指南抽屉) */
  projectsInbox: () =>
    http<{ dir: string; items: InboxItem[] }>("/api/projects/inbox"),
  /** 确认入库: 暂存目录移动为 projects/<target_id>/ 并自动注册 */
  confirmInbox: (id: string) =>
    http<{ confirmed: boolean; id: string; dir: string; manifest_backfilled: boolean }>(
      `/api/projects/inbox/${id}/confirm`, { method: "POST" }),
  /** 丢弃暂存副本 (仅删工作台内副本, 用户旧路径文件不受影响) */
  discardInbox: (id: string) =>
    http<{ discarded: boolean; id: string }>(`/api/projects/inbox/${id}`, { method: "DELETE" }),
  /** 本地工具探测 (VMD / Vesta) — 仪表盘浮窗用 */
  localToolsDetect: () => http<LocalToolsDetect>("/api/local-tools/detect"),
  /** 手动配置工具路径 (path 传空字符串清除) */
  configureLocalTool: (tool: 'vmd' | 'vesta', path: string) =>
    http<LocalToolsDetect>("/api/local-tools/configure", {
      method: "POST", body: JSON.stringify({ tool, path }),
    }),
  /** 安装指引 (自动配置失败时展示) */
  localToolsInstallHint: (tool: 'vmd' | 'vesta') =>
    http<{ tool: string; platform: string; url: string }>(
      `/api/local-tools/install-hint?tool=${tool}`),
  /** 启动器: 返回 {filename, content}, 前端用 blob 下载 (降级路径) */
  localToolLauncher: async (tool: 'vmd' | 'vesta', filePath: string): Promise<LauncherResult> => {
    const r = await http<LauncherResult>(
      `/api/local-tools/launcher?tool=${tool}&path=${encodeURIComponent(filePath)}`);
    return r;
  },
  /** 真一键: 后端 spawn 本机 .exe; 不可用时返回 {ok:false, fallback:"launcher", content/filename} 供下载 */
  openWithTool: async (tool: 'vmd' | 'vesta', filePath: string, autoConvertData = true) => {
    return http<{
      ok: boolean; spawned: boolean; pid?: string; path?: string;
      fallback?: string; message?: string;
      filename?: string; content?: string;
    }>("/api/local-tools/open", {
      method: "POST",
      body: JSON.stringify({ tool, path: filePath, auto_convert_data: autoConvertData }),
    });
  },

  /** 结束工作台后端进程 (受控退出; 409 = 有运行中任务被互锁) */
  shutdownWorkbench: async (): Promise<ShutdownResult> => {
    try {
      const resp = await fetch("/api/workbench/shutdown", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      });
      const body = await resp.json().catch(() => null);
      if (resp.ok) {
        return {
          outcome: "shutting_down",
          orphan_processes_cleaned: body?.orphan_processes_cleaned ?? 0,
        };
      }
      const d = body?.detail;
      if (d?.code === "active_jobs") {
        return { outcome: "blocked", message: d.message ?? "有运行中任务", jobs: d.jobs ?? [] };
      }
      return {
        outcome: "error",
        message: typeof d === "string" ? d : (d?.message ?? `HTTP ${resp.status}`),
      };
    } catch (e) {
      return { outcome: "error", message: e instanceof Error ? e.message : String(e) };
    }
  },
};

/** 订阅任务实时日志 (WebSocket); 组件卸载时需调用方 close */
export function openJobSocket(
  id: string,
  onMessage: (msg: WsMessage) => void,
): WebSocket {
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(`${proto}://${location.host}/ws/jobs/${id}`);
  ws.onmessage = (e) => {
    try {
      onMessage(JSON.parse(e.data) as WsMessage);
    } catch {
      /* 忽略非 JSON 帧 */
    }
  };
  return ws;
}

/** 后端 API 客户端与类型定义 */

export type JobStatus = "running" | "completed" | "failed" | "canceled" | "interrupted";
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
export interface TrajectoryAnalysis {
  summary: { frames: number; atoms: number; types: Record<string, number> };
  z_profile: { type: string; bins: { z: number; freq: number }[] }[];
  msd: { type: string; points: { step: number; lag: number; value: number }[] }[];
}

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
    http<{ config: Record<string, unknown>; errors: string[]; consistency: SystemConsistency }>(
      `/api/projects/${id}/system`,
    ),
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
  /** 启动器: 返回 {filename, content}, 前端用 blob 下载 */
  localToolLauncher: async (tool: 'vmd' | 'vesta', filePath: string): Promise<LauncherResult> => {
    const r = await http<LauncherResult>(
      `/api/local-tools/launcher?tool=${tool}&path=${encodeURIComponent(filePath)}`);
    return r;
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

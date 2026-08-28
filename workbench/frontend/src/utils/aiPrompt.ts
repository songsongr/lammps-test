/** AI 分析提示词构建器 (VASP DeepSeek Harness 的"桥梁"思想落地):
 *  把工作台的结构化诊断 (失败解析/平衡判据/环境指纹/日志尾部) 打包成
 *  可直接粘贴给 AI 编码代理 (ZCode 等) 的提示词 — agent 有仓库上下文, 即贴即开工。
 *  纯函数, 不发网络请求。 */

import type { Equilibrium, FailureInfo, JobDetail, ThermoData } from "../api/client";

const _line = "─".repeat(46);

function _header(job: JobDetail, purpose: string): string {
  const fp = job.fingerprint;
  const fpLine = fp
    ? [
        fp.system_sha ? `system.json sha:${fp.system_sha}` : null,
        fp.image ? `镜像 ${fp.image}` : null,
        fp.lmp_version ? `LAMMPS ${fp.lmp_version.replace(/^Large-scale Atomic\/Molecular Massively Parallel Simulator - /, "")}` : null,
      ].filter(Boolean).join(" · ")
    : "未记录";
  return [
    `你是 LAMMPS 分子动力学专家, 同时是本仓库 (lammps-test: LAMMPS 控制中心工作台) 的维护者 —`,
    `你已经在仓库工作目录内, 可以直接读写代码与项目文件。`,
    `请${purpose}。仓库规范见 AGENTS.md; 体系参数真相源是项目目录的 system.json;`,
    `修改 .lmp/参数后按工作台流程验证 (重建/渲染/发车)。`,
    "",
    _line,
    "## 任务上下文 (来自 LAMMPS 控制中心工作台)",
    `- 任务: ${job.id} · ${job.project_name} · 脚本 ${job.script} · 类型 ${job.kind}`,
    `- 状态: ${job.status}${job.exit_code != null ? ` (退出码 ${job.exit_code})` : ""}`,
    `- 项目目录: ${job.project_id}`,
    job.workspace ? `- 工作区: ${job.workspace}` : "",
    `- 环境指纹: ${fpLine}`,
  ].filter(Boolean).join("\n");
}

function _logTail(job: JobDetail, n = 40): string {
  const lines = (job.log_tail || []).slice(-n);
  if (lines.length === 0) return "(无日志)";
  return lines.join("\n");
}

/** 失败任务: 打包失败解析 + 案例库建议 + 日志尾部 */
export function buildFailurePrompt(job: JobDetail, failure: FailureInfo): string {
  const sev = { high: "高 (结果不可信, 必须修)", medium: "中 (可调参重跑)", low: "低 (环境性)" }[failure.severity] ?? failure.severity;
  return [
    _header(job, "分析下面这个失败任务的根因, 并直接修复脚本/参数 (给出具体 diff)"),
    "",
    "## 失败解析 (工作台案例库命中)",
    `- 摘要: ${failure.summary}`,
    failure.error_line ? `- 错误行: ${failure.error_line}` : "",
    failure.detail_line ? `- 末命令: ${failure.detail_line}` : "",
    `- 严重度: ${sev}`,
    `- 续跑策略: ${failure.can_resume ? "存在 (可从 restart 续跑)" : "无 (需修复后重跑)"}`,
    failure.actions?.length ? `- 建议动作:\n${failure.actions.map((a, i) => `  ${i + 1}. ${a}`).join("\n")}` : "",
    "",
    `## 日志尾部 (最后 40 行)`,
    "```",
    _logTail(job),
    "```",
  ].filter(Boolean).join("\n");
}

/** 平衡判据: 打包漂移检验结果 + thermo 尾部样本 */
export function buildEquilibriumPrompt(
  job: JobDetail,
  equil: Equilibrium,
  thermo: ThermoData,
): string {
  const verdict = { good: "已平衡", fair: "接近平衡", poor: "未收敛", unknown: "未知" }[equil.status];
  const checks = (equil.checks || [])
    .map((c) => `- ${c.quantity}: 相对漂移 ${(c.drift * 100).toFixed(4)}% (阈值 ${(c.threshold * 100).toFixed(3)}%, ${c.samples} 样本) → ${c.verdict}`)
    .join("\n");
  const tailRows = (thermo.rows || []).slice(-15);
  const thermoBlock = tailRows.length
    ? ["表头: " + thermo.columns.join("  "), ...tailRows.map((r) => r.map((v) => (typeof v === "number" ? v.toPrecision(8) : v)).join("  "))].join("\n")
    : "(无样本)";
  return [
    _header(job, "解读平衡判据结果并给出建议 (是否需要延长弛豫 / 调整步长 / 可否进入生产采样)"),
    "",
    "## 平衡判据 (末 20% 窗口线性漂移检验)",
    `- 总体判定: ${verdict}`,
    checks || "(无逐量检验结果)",
    "",
    "## thermo 尾部样本 (最后 15 行)",
    "```",
    thermoBlock,
    "```",
  ].filter(Boolean).join("\n");
}

/** 剪贴板写入 (IAB/非安全上下文 fallback execCommand); 两条路都失败时抛错 — 调用方须提示, 不静默 */
export async function copyToClipboard(text: string): Promise<void> {
  try {
    await navigator.clipboard.writeText(text);
    return;
  } catch {
    /* 页面失焦等 → 落到 execCommand */
  }
  const ta = document.createElement("textarea");
  ta.value = text;
  ta.style.position = "fixed";
  ta.style.opacity = "0";
  document.body.appendChild(ta);
  ta.select();
  const ok = document.execCommand("copy");
  ta.remove();
  if (!ok) throw new Error("剪贴板不可用 (页面未获得焦点) — 请点击页面后重试");
}

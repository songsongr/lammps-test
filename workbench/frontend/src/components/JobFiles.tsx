/** 工作区产物浏览: 文件列表 + 文本预览 + 下载 */
import { DownloadOutlined, EyeOutlined, FolderOpenOutlined, ToolOutlined } from "@ant-design/icons";
import { Dropdown } from "antd";
import { message } from "antd";
import { useEffect, useState } from "react";
import { api, type WorkspaceFile } from "../api/client";
import { fmtSize } from "../utils";

const PREVIEWABLE_EXT = new Set([
  ".log", ".txt", ".dat", ".lmp", ".in", ".mod", ".data", ".py",
  ".json", ".yaml", ".yml", ".csv", ".md",
]);

// 文件扩展 → 推荐的本地工具
const VMD_EXTS = new Set([".lammpstrj", ".dump", ".dcd", ".xyz"]);
const VESTA_EXTS = new Set([".data", ".cif", ".xsf", ".vesta"]);

/** 产物文件卡片 (内容区由父级渲染) */
export default function JobFiles({ jobId }: { jobId: string }) {
  const [files, setFiles] = useState<WorkspaceFile[] | null>(null);
  const [truncated, setTruncated] = useState(false);
  const [preview, setPreview] = useState<{ path: string; text: string } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let closed = false;
    setLoading(true);
    api
      .jobFiles(jobId)
      .then((d) => {
        if (closed) return;
        setFiles(d.files);
        setTruncated(d.truncated);
      })
      .catch(() => setFiles([]))
      .finally(() => setLoading(false));
    return () => {
      closed = true;
    };
  }, [jobId]);

  const openPreview = async (f: WorkspaceFile) => {
    const ext = f.path.slice(f.path.lastIndexOf(".")).toLowerCase();
    if (!PREVIEWABLE_EXT.has(ext) || f.size > 256_000) {
      message.info("该文件不支持在线预览, 请下载查看");
      return;
    }
    try {
      const d = await api.jobFileContent(jobId, f.path);
      setPreview({ path: f.path, text: d.text });
    } catch (e) {
      message.error(`预览失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  };

  if (loading) return <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>读取文件列表…</div>;
  if (!files || files.length === 0)
    return <div style={{ color: "var(--text-3)", fontSize: 12.5 }}>工作区为空或已清理</div>;

  return (
    <div>
      <div
        style={{
          border: "1px solid var(--border)",
          borderRadius: 12,
          overflow: "hidden",
          maxHeight: 240,
          overflowY: "auto",
        }}
      >
        {files.map((f) => {
          const ext = f.path.slice(f.path.lastIndexOf(".")).toLowerCase();
          const previewable = PREVIEWABLE_EXT.has(ext) && f.size <= 256_000;
          return (
            <div
              key={f.path}
              className="script-row"
              style={{ padding: "8px 14px", borderBottom: "1px solid var(--border)" }}
            >
              <FolderOpenOutlined style={{ color: "var(--text-3)", fontSize: 13 }} />
              <span
                className="script-name"
                style={{ cursor: previewable ? "pointer" : "default" }}
                onClick={() => previewable && openPreview(f)}
                title={f.path}
              >
                {f.path}
                {previewable && (
                  <EyeOutlined style={{ color: "var(--text-3)", marginLeft: 7, fontSize: 11 }} />
                )}
              </span>
              <span className="script-meta">{fmtSize(f.size)}</span>
              <OpenWithTool jobId={jobId} path={f.path} ext={ext} />
              <a
                className="row-run"
                style={{ textDecoration: "none" }}
                href={api.jobFileDownloadUrl(jobId, f.path)}
                download
                title="下载"
              >
                <DownloadOutlined />
              </a>
            </div>
          );
        })}
      </div>
      {truncated && (
        <div style={{ fontSize: 11.5, color: "var(--text-3)", marginTop: 6 }}>
          文件过多, 仅显示前 {files.length} 个
        </div>
      )}
      {preview && (
        <div style={{ marginTop: 12 }}>
          <div className="log-toolbar" style={{ margin: "0 0 8px" }}>
            <span className="label">
              <span className="mono-cell">{preview.path}</span>
            </span>
            <button className="mini-btn" onClick={() => setPreview(null)}>
              关闭预览
            </button>
          </div>
          <pre
            className="log-viewer"
            style={{ height: 260, borderRadius: 12, fontSize: 12 }}
          >
            {preview.text}
          </pre>
        </div>
      )}
    </div>
  );
}

function OpenWithTool({ jobId, path, ext }: { jobId: string; path: string; ext: string }) {
  const items: { key: string; label: string; tool: 'vmd' | 'vesta' }[] = [];
  if (VMD_EXTS.has(ext)) items.push({ key: "vmd", label: "用 VMD 打开", tool: "vmd" });
  if (VESTA_EXTS.has(ext)) items.push({ key: "vesta", label: "用 Vesta 打开", tool: "vesta" });
  if (items.length === 0) return null;

  const launch = async (tool: 'vmd' | 'vesta') => {
    try {
      const r = await fetch("/api/jobs/" + encodeURIComponent(jobId)).then(x => x.json());
      const ws = r.workspace as string | null;
      if (!ws) { message.error("任务工作区不可用"); return; }
      const abs = ws.split("\\").join("/") + "/" + path;
      const launcher = await api.localToolLauncher(tool, abs);
      const blob = new Blob([launcher.content], { type: "text/plain;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url; a.download = launcher.filename;
      document.body.appendChild(a); a.click(); a.remove();
      URL.revokeObjectURL(url);
      if (!launcher.found) {
        message.warning(`未检测到 ${tool.toUpperCase()} 可执行文件; 下载的启动器会提示, 请先在仪表盘「本地工具」浮窗配置路径`);
      } else {
        message.success(`已下载 ${launcher.filename} — 双击运行即可打开 ${tool.toUpperCase()}`);
      }
    } catch (e) {
      message.error(`启动器生成失败: ${e instanceof Error ? e.message : String(e)}`);
    }
  };

  return (
    <Dropdown
      menu={{ items: items.map(it => ({ key: it.key, label: it.label, onClick: () => launch(it.tool) })) }}
      trigger={["click"]}
    >
      <button className="row-run" title="用本地工具打开 (下载一键启动器)" type="button">
        <ToolOutlined />
      </button>
    </Dropdown>
  );
}

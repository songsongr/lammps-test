"""Patch Dashboard.tsx: 本地工具状态行 + Drawer 浮窗。"""
from pathlib import Path

p = Path("src/pages/Dashboard.tsx")
t = p.read_text(encoding="utf-8")

# 1) import Drawer
old = 'import { Modal, Typography, message } from "antd";'
new = 'import { Drawer, Modal, Typography, message } from "antd";'
assert old in t, "1"
t = t.replace(old, new, 1)

# 2) 类型 + 状态
old = "import { api, type Health, type Job } from \"../api/client\";"
new = "import { api, type Health, type Job, type LocalToolsDetect } from \"../api/client\";"
assert old in t, "2"
t = t.replace(old, new, 1)

old = """  const [confirmOpen, setConfirmOpen] = useState(false);
  const [shuttingDown, setShuttingDown] = useState(false);"""
new = """  const [confirmOpen, setConfirmOpen] = useState(false);
  const [shuttingDown, setShuttingDown] = useState(false);
  const [tools, setTools] = useState<LocalToolsDetect | null>(null);
  const [toolsDrawerOpen, setToolsDrawerOpen] = useState(false);"""
assert old in t, "3"
t = t.replace(old, new, 1)

# 3) 探测 hooks
old = "  useEffect(() => {\n    const load = () => {\n      api.health()"
new = """  useEffect(() => {
    api.localToolsDetect().then(setTools).catch(() => setTools(null));
    const t = setInterval(() => api.localToolsDetect().then(setTools).catch(() => setTools(null)), 10000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => { if (backendDown) setTools(null); }, [backendDown]);

  useEffect(() => {
    const load = () => {
      api.health()"""
assert old in t, "4"
t = t.replace(old, new, 1)

# 4) "工作台控制" 卡片上方插入 "本地工具" 小卡
old = """          <section className="card card-pad">
            <div className="card-title" style={{ marginBottom: 10 }}>
              工作台控制
            </div>"""
new = """          <section
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
            </div>"""
assert old in t, "5"
t = t.replace(old, new, 1)

# 5) Modal 之后挂载 Drawer, 并在文件底部 (在末尾 } 前) 注入辅助组件
old = "        </Modal>\n      </div>\n  );\n}"
new = "        </Modal>\n        <LocalToolsDrawer\n          open={toolsDrawerOpen}\n          onClose={() => setToolsDrawerOpen(false)}\n          tools={tools}\n          onConfigured={setTools}\n        />\n      </div>\n  );\n}\n\nfunction ToolChip({ name, info }: {\n  name: string; info: { found: boolean; version_hint: string | null; source: string | null }\n}) {\n  const ok = info.found;\n  return (\n    <span\n      style={{\n        display: \"inline-flex\", alignItems: \"center\", gap: 6,\n        fontSize: 12, fontWeight: 600, padding: \"5px 11px\", borderRadius: 999,\n        color: ok ? \"var(--ok)\" : \"var(--err)\",\n        background: ok ? \"var(--ok-weak)\" : \"var(--err-weak)\",\n      }}\n    >\n      <span style={{ width: 6, height: 6, borderRadius: 999, background: ok ? \"var(--ok)\" : \"var(--err)\" }} />\n      {name}{ok ? (info.version_hint ? ` ${info.version_hint}` : \" · 已检测\") : \" · 未检测到\"}\n    </span>\n  );\n}\n\nfunction ToolConfigRow({ label, info, draft, setDraft, saving, onSave }: {\n  label: string;\n  info: { found: boolean; path: string | null; source: string | null };\n  draft: string; setDraft: (s: string) => void;\n  saving: boolean; onSave: (p: string) => void;\n}) {\n  const isManual = info.source === \"manual\";\n  return (\n    <div style={{ marginTop: 14, padding: 14, border: \"1px solid var(--border)\", borderRadius: 10 }}>\n      <div style={{ display: \"flex\", alignItems: \"center\", gap: 9, marginBottom: 8 }}>\n        <span style={{ fontWeight: 650 }}>{label}</span>\n        <ToolChip name={label} info={info as any} />\n        {isManual && <span style={{ fontSize: 11, color: \"var(--text-3)\" }}>手动配置</span>}\n      </div>\n      <div style={{ display: \"flex\", gap: 8 }}>\n        <input\n          className=\"sys-input\"\n          style={{ flex: 1, fontSize: 12 }}\n          placeholder={info.path || \"请输入可执行文件绝对路径\"}\n          value={draft}\n          onChange={(e) => setDraft(e.target.value)}\n        />\n        <button className=\"mini-btn accent\" disabled={saving || !draft} onClick={() => onSave(draft)}>\n          {saving ? \"保存中…\" : \"保存\"}\n        </button>\n        {isManual && (\n          <button className=\"mini-btn\" onClick={() => onSave(\"\")}>清除</button>\n        )}\n      </div>\n      {info.path && (\n        <div style={{ fontSize: 11, color: \"var(--text-3)\", marginTop: 6, fontFamily: \"var(--font-mono)\", wordBreak: \"break-all\" }}>\n          当前: {info.path}\n        </div>\n      )}\n    </div>\n  );\n}\n\nfunction InstallHintRow({ tool }: { tool: \"vmd\" | \"vesta\" }) {\n  const [url, setUrl] = useState<string>(\"\");\n  useEffect(() => {\n    api.localToolsInstallHint(tool).then((r) => setUrl(r.url)).catch(() => setUrl(\"\"));\n  }, [tool]);\n  if (!url) return null;\n  return (\n    <div style={{ marginTop: 10, fontSize: 12, color: \"var(--text-2)\" }}>\n      {tool} 官网: <a href={url} target=\"_blank\" rel=\"noreferrer\">{url}</a>\n    </div>\n  );\n}\n\nfunction LocalToolsDrawer({ open, onClose, tools, onConfigured }: {\n  open: boolean; onClose: () => void; tools: LocalToolsDetect | null;\n  onConfigured: (t: LocalToolsDetect) => void;\n}) {\n  const [vmdDraft, setVmdDraft] = useState(\"\");\n  const [vestaDraft, setVestaDraft] = useState(\"\");\n  const [saving, setSaving] = useState<\"\" | \"vmd\" | \"vesta\">(\"\");\n  useEffect(() => { setVmdDraft(\"\"); setVestaDraft(\"\"); }, [open]);\n\n  const save = async (tool: \"vmd\" | \"vesta\", path: string) => {\n    setSaving(tool);\n    try {\n      const t = await api.configureLocalTool(tool, path);\n      onConfigured(t);\n      message.success(path ? `已配置 ${tool} 路径` : `已清除 ${tool} 配置`);\n    } catch (e) {\n      message.error(`配置失败: ${e instanceof Error ? e.message : String(e)}`);\n    } finally { setSaving(\"\"); }\n  };\n\n  return (\n    <Drawer title=\"本地可视化工具\" open={open} onClose={onClose} width={520}>\n      <Typography.Paragraph type=\"secondary\" style={{ fontSize: 12.5, marginTop: 0 }}>\n        工作台可在任务详情和体系配置页生成「一键启动脚本」打开本机可视化工具。\n        下方自动检测常见安装路径; 检测失败时手动填入路径即可, 不会修改系统 PATH 或防火墙。\n      </Typography.Paragraph>\n      {!tools && <div style={{ color: \"var(--text-3)\", fontSize: 12.5 }}>检测中…</div>}\n      {tools && (\n        <>\n          <ToolConfigRow label=\"VMD\" info={tools.vmd} draft={vmdDraft} setDraft={setVmdDraft}\n            saving={saving === \"vmd\"} onSave={(p) => save(\"vmd\", p)} />\n          <ToolConfigRow label=\"Vesta\" info={tools.vesta} draft={vestaDraft} setDraft={setVestaDraft}\n            saving={saving === \"vesta\"} onSave={(p) => save(\"vesta\", p)} />\n          <InstallHintRow tool=\"vmd\" />\n          <InstallHintRow tool=\"vesta\" />\n        </>\n      )}\n    </Drawer>\n  );\n}"
assert old in t, "6"
t = t.replace(old, new, 1)

# 6) 修复 useState 闭包问题: hooks 中的 `t` 变量名与 setInterval 重名, 改 interval 标识
old = "    const t = setInterval(() => api.localToolsDetect().then(setTools).catch(() => setTools(null)), 10000);\n    return () => clearInterval(t);"
new = "    const iv = setInterval(() => api.localToolsDetect().then(setTools).catch(() => setTools(null)), 10000);\n    return () => clearInterval(iv);"
assert old in t, "7"
t = t.replace(old, new, 1)

# 7) 同样修复 useEffect 内 setInterval 名字 (App 原本就有) — 搜索并避免冲突
# 简单做法: 我们新增的 useEffect 用新名, 原有的不动
# 上一步已经做了

# 8) ToolConfigRow 用的 setDraft 改用 onChange — 已写; InstallHintRow 在 Drawer 内必须 hook, ok
# 9) 修复小问题: Drawer 闭包里 useState/Effect 也要 import
old = "import { useCallback, useEffect, useState } from \"react\";"
assert old in t
# 已有 useEffect + useState, 缺 useCallback — 但 Drawer 不需要 useCallback

p.write_text(t, encoding="utf-8")
print("Dashboard.tsx ok")

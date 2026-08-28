import { DeleteOutlined, ReloadOutlined } from "@ant-design/icons";
import { Button, Checkbox, Modal, Popconfirm, Table, message } from "antd";
import type { ColumnsType } from "antd/es/table";
import { useCallback, useEffect, useState } from "react";
import { api, type Job, type JobKind, type JobStatus } from "../api/client";
import { KindChip, StatusChip } from "../components/ui";
import { fmtDuration, fmtTime, fmtSize } from "../utils";

/** 任务记录页: 全部任务列表, 运行中可取消, 终态可删除 (双重确认) */
export default function Jobs({ onOpenJob }: { onOpenJob: (id: string) => void }) {
  const [jobs, setJobs] = useState<Job[]>([]);
  // 删除双重确认: 第一步 Popconfirm → 第二步本 Modal 内勾选后才可点删除
  const [pendingDelete, setPendingDelete] = useState<Job | null>(null);
  const [confirmed, setConfirmed] = useState(false);
  const [deleting, setDeleting] = useState(false);

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

  const columns: ColumnsType<Job> = [
    {
      title: "状态",
      dataIndex: "status",
      width: 110,
      render: (s: JobStatus) => <StatusChip status={s} />,
    },
    { title: "项目", dataIndex: "project_name", width: 175, ellipsis: true },
    {
      title: "脚本",
      dataIndex: "script",
      render: (v: string, j) => (
        <button className="link-cell" onClick={() => onOpenJob(j.id)} title={v}>
          {v}
        </button>
      ),
    },
    {
      title: "类型",
      dataIndex: "kind",
      width: 92,
      render: (k: JobKind) => <KindChip kind={k} />,
    },
    {
      title: "开始时间",
      dataIndex: "started_at",
      width: 135,
      render: (v: string | null) => <span className="muted nowrap">{fmtTime(v)}</span>,
    },
    {
      title: "耗时",
      key: "duration",
      width: 100,
      render: (_, j) => <span className="muted">{fmtDuration(j.started_at, j.finished_at)}</span>,
    },
    {
      title: "",
      key: "actions",
      width: 190,
      align: "right",
      render: (_, j) => (
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
      ),
    },
  ];

  return (
    <div>
      <section className="card" style={{ overflow: "hidden" }}>
        <div className="table-toolbar">
          <span className="card-title">全部任务</span>
          <span className="table-count">{jobs.length}</span>
          <button className="icon-btn" onClick={load} title="刷新">
            <ReloadOutlined />
          </button>
        </div>
        <Table
          className="jobs-table"
          rowKey="id"
          columns={columns}
          dataSource={jobs}
          pagination={{ pageSize: 14, showSizeChanger: false }}
        />
      </section>

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
    </div>
  );
}

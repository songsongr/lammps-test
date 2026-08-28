import {
  DashboardOutlined,
  ExperimentOutlined,
  HistoryOutlined,
  FolderOpenOutlined,
} from "@ant-design/icons";
import { useEffect, useRef, useState } from "react";
import { api, type Health, type Job } from "./api/client";
import { EnvChip } from "./components/ui";
import Dashboard from "./pages/Dashboard";
import JobDetail from "./pages/JobDetail";
import Jobs from "./pages/Jobs";
import ProjectSystem from "./pages/ProjectSystem";
import Projects from "./pages/Projects";

export type PageKey = "dashboard" | "projects" | "jobs";
export type Route =
  | { page: PageKey }
  | { page: "job"; jobId: string }
  | { page: "system"; projectId: string };

const NAV: { key: PageKey; icon: JSX.Element; label: string; title: string }[] = [
  { key: "dashboard", icon: <DashboardOutlined />, label: "仪表盘", title: "控制中心" },
  { key: "projects", icon: <FolderOpenOutlined />, label: "项目与脚本", title: "项目与脚本" },
  { key: "jobs", icon: <HistoryOutlined />, label: "任务记录", title: "任务记录" },
];

export default function App() {
  const [route, setRoute] = useState<Route>({ page: "dashboard" });
  const [health, setHealth] = useState<Health | null>(null);
  const [jobs, setJobs] = useState<Job[]>([]);
  const [backendDown, setBackendDown] = useState(false);
  const everOk = useRef(false);

  useEffect(() => {
    const load = () => {
      api.health()
        .then((h) => {
          everOk.current = true;
          setBackendDown(false);
          setHealth(h);
        })
        .catch(() => {
          // 曾连通过才判定"已停止", 首次加载失败仍视为检测中
          if (everOk.current) setBackendDown(true);
          setHealth(null);
        });
      api.jobs().then(setJobs).catch(() => {});
    };
    load();
    const t = setInterval(load, 5000);
    return () => clearInterval(t);
  }, []);

  const navKey: PageKey =
    route.page === "job" ? "jobs" : route.page === "system" ? "projects" : route.page;
  const activeNav = NAV.find((n) => n.key === navKey)!;
  const subtitle =
    route.page === "job"
      ? "执行历史与实时日志"
      : ({
          dashboard: "模拟任务编排与实时监控",
          projects: "选择脚本发起任务, 或从模板创建全新体系",
          jobs: "全部任务的执行历史与日志",
          system: "体系参数配置 (单一真相源)",
        } as Record<string, string>)[route.page];

  return (
    <div className="shell">
      <aside className="sider">
        <div className="brand">
          <div className="brand-mark">
            <ExperimentOutlined />
          </div>
          <div>
            <div className="brand-name">LAMMPS 控制中心</div>
            <div className="brand-sub">SIMULATION WORKBENCH</div>
          </div>
        </div>
        <nav className="nav">
          {NAV.map((n) => (
            <button
              key={n.key}
              className={`nav-item ${navKey === n.key ? "active" : ""}`}
              onClick={() => setRoute({ page: n.key })}
            >
              {n.icon}
              {n.label}
            </button>
          ))}
        </nav>
        <div className="sider-foot">
          workbench v0.1
          <br />
          LAMMPS · Docker · FastAPI
        </div>
      </aside>

      <div className="main">
        <header className="topbar">
          <div className="topbar-title">
            {route.page === "job" ? "任务详情" : activeNav.title}
            <span className="topbar-sub">
              {route.page === "job" ? (route as { jobId: string }).jobId : subtitle}
            </span>
          </div>
          <div className="topbar-right">
            <EnvChip health={health} backendDown={backendDown} />
          </div>
        </header>
        <main className="content">
          {route.page === "dashboard" && (
            <Dashboard
              health={health}
              jobs={jobs}
              backendDown={backendDown}
              onNav={(p) => setRoute({ page: p })}
            />
          )}
          {route.page === "projects" && (
            <Projects
              onOpenJob={(id) => setRoute({ page: "job", jobId: id })}
              onOpenSystem={(id) => setRoute({ page: "system", projectId: id })}
            />
          )}
          {route.page === "jobs" && (
            <Jobs onOpenJob={(id) => setRoute({ page: "job", jobId: id })} />
          )}
          {route.page === "system" && (
            <ProjectSystem
              projectId={route.projectId}
              onBack={() => setRoute({ page: "projects" })}
              onOpenJob={(id) => setRoute({ page: "job", jobId: id })}
            />
          )}
          {route.page === "job" && (
            <JobDetail
              jobId={(route as { jobId: string }).jobId}
              onBack={() => setRoute({ page: "jobs" })}
              onOpenJob={(id) => setRoute({ page: "job", jobId: id })}
            />
          )}
        </main>
      </div>
    </div>
  );
}

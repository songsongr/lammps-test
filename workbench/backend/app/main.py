"""LAMMPS 控制中心 — 后端入口。

启动方式:
    uv run workbench                # 生产: 后端 + 静态托管前端 (http://127.0.0.1:8000)
    uv run uvicorn workbench.backend.app.main:app --reload   # 后端开发模式
"""
import argparse
import asyncio
import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import store, workspace
from .config import FRONTEND_DIST
from .job_manager import manager
from .routers import jobs, local_tools, projects, system

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

store.init()


@asynccontextmanager
async def lifespan(_: FastAPI):
    await manager.recover_orphans()  # 上次退出遗留的 running 任务 → interrupted
    await workspace.start_sweeper()  # 工作区过期清理后台任务
    asyncio.create_task(manager.queue_sweeper())  # 队列自愈调度 (CLI 任务完成等外部事件兜底)
    yield


app = FastAPI(title="LAMMPS 控制中心", version="0.1.1", lifespan=lifespan)
app.include_router(system.router)
app.include_router(projects.router)
app.include_router(jobs.router)
app.include_router(jobs.ws_router)
app.include_router(local_tools.router)

# 前端构建产物存在时托管 SPA (前端使用 hash 路由, html=True 即可覆盖刷新)
if os.path.isdir(FRONTEND_DIST):
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="web")


def main() -> None:
    parser = argparse.ArgumentParser(description="LAMMPS 控制中心 (后端 + 静态前端)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    if not os.path.isdir(FRONTEND_DIST):
        print("[workbench] 未找到前端构建产物 workbench/frontend/dist, 当前仅提供 API。"
              "构建方法见 workbench/README.md")
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()

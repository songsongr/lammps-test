# 环境与工具链

## 终端与 Shell

- 用户使用 **PowerShell**（不是 Git Bash）
- 本文档命令均以 PowerShell 为准

## Python（uv 管理）

- 项目根目录有 `.venv`（uv 创建）
- 所有 Python 脚本用 `uv run python <script>.py` 执行，**不要用裸 `python`**
- Docker 容器内**没有 Python**（apt-get 需要 root 权限，不要装）
- 项目配置在 `pyproject.toml`（依赖 + 一键命令入口，见 [workflows.md](workflows.md)）

### ⚠️ 修复记录：.venv 失效后重建

项目目录移动后 `.venv` 内的 uv trampoline 会找不到原始 Python（报 `os error 448`）。
修复方式：删除 `.venv` 后用 `uv sync` 重建（uv 会按 `pyproject.toml` 自动恢复依赖与命令入口）。

## Docker 容器 lammpsd

LAMMPS 运行在 Docker 容器 `lammpsd`（镜像 `lammps/lammps:latest`）中。

### 容器配置

- 可执行文件：`/usr/bin/lmp_mpi`
- **volume 映射：`/data` → 数据目录 `lammps-data-docker/`**（2026-08-28 起，不再挂项目根）
  - Windows 下挂小目录性能远好于挂整个项目根（.venv 数万小文件）
  - 容器不会写入项目目录
- LAMMPS 任务采用**暂存-运行-回收**：每个任务在 `lammps-data-docker/jobs/<id>/`
  建独立工作区（脚本与依赖由 workbench / common.runner 自动拷入），
  容器内 `-w /data/jobs/<id>` 运行，产物天然留在宿主机工作区
- 挂载校验：workbench 启动时通过 `docker inspect` 校验挂载源，仪表盘显示 ✓/✗

### 模拟任务的正确姿势（二选一）

```powershell
# 方式一 (推荐): 控制中心工作台 — 自动暂存/实时日志/曲线/失败解析
uv run workbench        # http://127.0.0.1:8000

# 方式二: CLI (与 workbench 同一执行契约 common.runner)
uv run run-sr-sim       # 运行 systems/strontium_adsorption/run.lmp
uv run build-mmt        # 构建 systems/Montmorillonite-test/system.data
```

### 容器管理

```powershell
docker start lammpsd                      # 启动容器（可能处于停止状态）
docker ps --filter name=lammpsd           # 状态检查
```

> 直接 `docker exec -w /data/...` 手动跑 LAMMPS 已不适用（/data 下没有项目文件）；
> 如需手动干预请进入任务工作区 `lammps-data-docker/jobs/<任务id>/`。

### 远程运行（Tailscale + SSH）

本地 Docker 不可用时，可经远程机运行（远程机需同样的 lammpsd 容器与数据目录约定）：

```powershell
ssh 23653@100.95.102.42 docker exec -w /data/jobs/<id> lammpsd /usr/bin/lmp_mpi -in run.lmp
```

## 执行后端配置（v1.8.5 起）

v1.8.5 把"拼装 docker exec 命令"抽象成了 **Backend 协议**（`common/backends/`），
现在有 2 个实现：

| 后端类型 | 说明 | 状态 |
|---|---|---|
| `local_docker` | 本地 Docker 容器（默认；零配置开箱即用） | ✅ 完成 |
| `remote_hpc` | 远程 HPC（sbatch 任务提交模式；ssh + rsync + sbatch） | ✅ 骨架 |
| `remote_docker` | 远程 Docker 主机 | ⏳ v1.8.6 占位 |

切换是**配置驱动**的：写入 `workbench/data/backend.json`，下次启动或调用 `get_backend()`
时自动生效，不需要改代码。

### 默认（本地 Docker）

`backend.json` 不存在时，**默认走 LocalDockerBackend，行为与 v1.8.5 之前完全一致**——
所有现有任务（CLI 与 workbench）均透明运行，不需要任何配置。

### 远程 HPC

```json
// workbench/data/backend.json
{
  "type": "remote_hpc",
  "ssh_host": "hpc.univ.edu",
  "ssh_user": "alice",
  "ssh_key_path": "/home/alice/.ssh/id_rsa",
  "ssh_port": 22,
  "hpc_workdir": "/home/alice/lammps",
  "hpc_modules": ["openmpi/4.1", "lammps/20240328"],
  "hpc_sbatch_template": "#!/bin/bash\n#SBATCH --job-name=lammps-$script\n#SBATCH --cpus-per-task=$omp\n...\n"
}
```

字段说明：

- `ssh_host` / `ssh_user`：必填，远程 HPC 入口
- `ssh_key_path`：可选，默认走 ssh-agent / `~/.ssh/id_rsa`
- `hpc_workdir`：远程提交根目录，每个任务建 `jobs/<id>/` 子目录
- `hpc_modules`：`module load` 列表（远程 .bashrc 没有 module 时跳过）
- `hpc_sbatch_template`：sbatch 脚本模板（`string.Template` 语法，可选变量
  `$script` / `$omp` / `$workdir` / `$modules`）；不填用内置默认模板

REST API（前端配置抽屉用）：

- `GET  /api/backend` — 当前配置 + 探测结果
- `GET  /api/backend/list` — 所有已注册 backend 列表（local_docker / remote_hpc）
- `PUT  /api/backend` — 切换 backend（持久化）
- `POST /api/backend/test` — 连通性测试（不持久化）

### 远程 Docker

留作 **v1.8.6**。骨架接口已就绪（Backend 协议满足），实现类是
`common/backends/remote_docker.py`，逻辑类似 LocalDockerBackend 但 ssh 到远程主机
后再 `docker exec`，等价于把现成的"远程 SSH 跑 docker"手动流程自动化。

## Workbench（控制中心）

- 启动：`uv run workbench` → http://127.0.0.1:8000（后端 + 静态托管前端）
- 能力：任务编排 / 实时日志 / thermo 曲线 / 失败解析 / 体系配置 / 新建项目向导
- 详细说明：[workbench/README.md](../workbench/README.md)
- 当前架构总览：[ARCHITECTURE.md](../ARCHITECTURE.md)

## VMD（轨迹可视化）

```powershell
& "C:\Program Files\VMD\vmd.exe" C:\Users\23653\Desktop\cc-proj\lammps-test\strontium_adsorption\prod.lammpstrj
```

推荐设置：

- 查看 Sr²⁺：`Graphics → Representations → Selected Atoms: type 4`，绘图方法 `VDW`/`CPK`
  （避免 `Lines` 产生周期边界假键）
- 查看水：`type 2 3`，用 `Lines` 或 `Licorice`

## 硬件

- GPU：RTX 3050，但容器内无 CUDA；5K 原子规模不值得用 GPU
- 加速基准数据见 [work-log.md](work-log.md)

## 文件约定

- 轨迹/日志（`*.lammpstrj`、`log.lammps`、`*.dump`、`*.restart`）已被根目录 `.gitignore` 排除，不入版本控制
- Python 脚本输出路径与脚本保持同目录（`os.path.dirname(os.path.abspath(__file__))`）
- LAMMPS 任务产物保留在任务工作区 `lammps-data-docker/jobs/<id>/`（14 天自动清理）

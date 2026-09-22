"""API 数据模型 (pydantic)。"""
import re
from typing import Literal, Optional

from pydantic import BaseModel, field_validator


class JobCreate(BaseModel):
    project_id: str
    script: str = ""
    kind: Literal["lmp", "python", "build"] = "lmp"
    omp_threads: int = 8  # 仅 LAMMPS 任务生效 (1-64)


class ProjectCreate(BaseModel):
    id: str
    name: str
    description: str = ""
    profile: Literal["surface_adsorption", "solution"]
    water_model: str = "SPCE"
    system_overrides: dict = {}
    method_id: str = "nvt_production"
    method_params: dict = {}

    @field_validator("id")
    @classmethod
    def id_format(cls, v: str) -> str:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,39}", v):
            raise ValueError("项目 ID 仅允许小写字母/数字/连字符, 2-40 位")
        return v


class RenderRequest(BaseModel):
    method_id: Optional[str] = None
    params: dict = {}
    force: bool = False


class FileSaveRequest(BaseModel):
    content: str


class ScanRequest(BaseModel):
    param_key: str  # 方法模板参数键 (如 temperature)
    values: list[float]
    omp_threads: int = 8


class JobOut(BaseModel):
    id: str
    project_id: str
    project_name: str
    script: str
    kind: str
    command: str
    status: str
    exit_code: Optional[int] = None
    created_at: Optional[str] = None
    started_at: Optional[str] = None
    finished_at: Optional[str] = None
    log_path: Optional[str] = None
    workspace: Optional[str] = None
    omp_threads: int = 8
    source: str = "workbench"
    batch: Optional[str] = None


class JobResumeOut(JobOut):
    source_restart: Optional[str] = None


class JobDetailOut(JobOut):
    log_tail: list[str] = []
    thermo: dict = {}  # {columns: [str], rows: [[float]]} (最近 500 行)
    failure: Optional[dict] = None  # 失败解析 {summary, error_line, detail_line, hint, severity, actions, can_resume}
    equilibrium: Optional[dict] = None  # 平衡判据 {status: good|fair|poor|unknown, checks: [...]}
    fingerprint: Optional[dict] = None  # 环境指纹 {system_sha, image_id, image, lmp_version}

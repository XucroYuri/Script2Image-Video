from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class Project(BaseModel):
    project_id: str = Field(..., description="项目唯一ID")
    name: str = Field(..., description="项目名称")
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = Field(default="pending", description="项目状态")

class NanoBananaPrompts(BaseModel):
    start: str = Field(..., description="起始帧提示词")
    middle: str = Field(..., description="中间帧提示词")
    end: str = Field(..., description="结束帧提示词")

class Shot(BaseModel):
    shot_id: str = Field(..., description="镜头唯一ID")
    scene_id: str = Field(..., description="所属场景ID")
    name: Optional[str] = Field(None, description="镜头名称")
    order_index: int = Field(0, description="镜头顺序")
    description: Optional[str] = Field(None, description="镜头描述")
    nano_banana_pro_prompts: Optional[NanoBananaPrompts] = None
    veo_3_1_prompt: Optional[str] = Field(None, description="视频生成提示词")
    
    # 允许额外的字段，因为JSON结构可能包含其他信息
    model_config = {
        "extra": "ignore"
    }

class Scene(BaseModel):
    scene_id: str = Field(..., description="场景唯一ID")
    project_id: Optional[str] = Field(None, description="所属项目ID")
    scene_title: Optional[str] = Field(None, description="场景标题")
    timestamp: Optional[str] = Field(None, description="时间戳")
    shots: List[Shot] = Field(default_factory=list, description="镜头列表")
    
    model_config = {
        "extra": "ignore"
    }

class ProjectData(BaseModel):
    project: str = Field(..., description="项目名称")
    core_style: Optional[Dict[str, Any]] = Field(None, description="核心风格定义")
    character_references: Optional[Dict[str, str]] = Field(None, description="角色引用")
    scenes: List[Scene] = Field(default_factory=list, description="场景列表")

class GeneratedFile(BaseModel):
    file_id: str = Field(..., description="文件唯一ID")
    shot_id: str = Field(..., description="所属镜头ID")
    file_type: str = Field(..., description="文件类型(image/video)")
    file_path: str = Field(..., description="文件完整路径")
    file_name: str = Field(..., description="文件名")
    created_at: datetime = Field(default_factory=datetime.now)
    file_size: int = Field(..., description="文件大小(字节)")

class TaskStatus(BaseModel):
    task_id: str = Field(..., description="任务ID")
    status: str = Field(..., description="任务状态")
    progress: float = Field(0.0, description="进度百分比")
    result: Optional[Dict] = Field(None, description="任务结果")
    error: Optional[str] = Field(None, description="错误信息")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.veo_client import VeoClient
from app.services.file_storage import FileStorageService
from app.models.schemas import GeneratedFile
from app.core.config import settings
import uuid
import os

router = APIRouter()

class VideoGenRequest(BaseModel):
    project_name: str
    scene_id: str
    shot_id: str
    prompt: str
    start_image_path: str = None # Optional path to start frame

@router.post("/generate-video", response_model=GeneratedFile)
async def generate_video(request: VideoGenRequest):
    """
    Generate a video based on prompt and save it
    """
    client = VeoClient()
    storage = FileStorageService()
    
    try:
        # 1. Generate Video
        video_data = await client.generate_video(
            prompt=request.prompt,
            image_url=None # TODO: Handle local file upload to Veo if supported
        )
        
        # 2. Save File
        filename = f"{request.scene_id}_{request.shot_id}_video.mp4"
        file_path = storage.save_file(
            content=video_data,
            project_name=request.project_name,
            scene_id=request.scene_id,
            shot_id=request.shot_id,
            filename=filename
        )
        
        # 3. Return Result
        rel_path = os.path.relpath(file_path, settings.OUTPUT_DIR)
        file_url = f"/files/{rel_path.replace(os.sep, '/')}"

        return GeneratedFile(
            file_id=str(uuid.uuid4()),
            shot_id=request.shot_id,
            file_type="video",
            file_path=file_path,
            file_url=file_url,
            file_name=filename,
            file_size=os.path.getsize(file_path)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

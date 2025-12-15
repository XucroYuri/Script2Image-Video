from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.services.gemini_client import GeminiClient
from app.services.file_storage import FileStorageService
from app.models.schemas import GeneratedFile
import uuid
import os

router = APIRouter()

class ImageGenRequest(BaseModel):
    project_name: str
    scene_id: str
    shot_id: str
    prompt: str
    frame_type: str  # start/middle/end

@router.post("/generate-image", response_model=GeneratedFile)
async def generate_image(request: ImageGenRequest):
    """
    Generate an image based on prompt and save it
    """
    client = GeminiClient()
    storage = FileStorageService()
    
    try:
        # 1. Generate Image
        image_data = await client.generate_image(request.prompt)
        
        # 2. Save File
        filename = f"{request.scene_id}_{request.shot_id}_{request.frame_type}.png"
        file_path = storage.save_file(
            content=image_data,
            project_name=request.project_name,
            scene_id=request.scene_id,
            shot_id=request.shot_id,
            filename=filename
        )
        
        # 3. Return Result
        return GeneratedFile(
            file_id=str(uuid.uuid4()),
            shot_id=request.shot_id,
            file_type="image",
            file_path=file_path,
            file_name=filename,
            file_size=os.path.getsize(file_path)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

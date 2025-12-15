from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.models.schemas import ProjectData
from app.services.json_parser import JSONParserService
from app.api import image_routes, video_routes
import shutil
import os
import uuid
from loguru import logger

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 设置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(image_routes.router, prefix=f"{settings.API_V1_STR}", tags=["images"])
app.include_router(video_routes.router, prefix=f"{settings.API_V1_STR}", tags=["videos"])

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

@app.post(f"{settings.API_V1_STR}/upload-json", response_model=ProjectData)
async def upload_json(file: UploadFile = File(...)):
    """
    上传并解析JSON文件
    """
    if not file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Only JSON files are allowed")
    
    # 确保临时目录存在
    temp_dir = os.path.join(settings.OUTPUT_DIR, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    # 保存文件
    file_id = str(uuid.uuid4())
    file_path = os.path.join(temp_dir, f"{file_id}_{file.filename}")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # 解析JSON
        parser = JSONParserService()
        project_data = parser.parse_project_json(file_path)
        
        # 处理Prompts
        processed_project = parser.process_all_prompts(project_data)
        
        logger.info(f"Successfully processed JSON file: {file.filename}")
        return processed_project
        
    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    finally:
        # 清理临时文件 (可选，或者保留用于调试)
        # if os.path.exists(file_path):
        #     os.remove(file_path)
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import os
from app.core.config import settings
from loguru import logger

class FileStorageService:
    """Service to handle file storage with structured paths"""
    
    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or settings.OUTPUT_DIR
        
    def get_output_path(self, project_name: str, scene_id: str, shot_id: str, filename: str) -> str:
        """
        Construct and ensure path exists: 
        output/project_name/scene_id/shot_id/filename
        """
        # Sanitize names to be safe directory names
        safe_project = self._sanitize(project_name)
        safe_scene = self._sanitize(scene_id)
        safe_shot = self._sanitize(shot_id)
        
        dir_path = os.path.join(self.base_dir, safe_project, safe_scene, safe_shot)
        os.makedirs(dir_path, exist_ok=True)
        
        return os.path.join(dir_path, filename)
    
    def save_file(self, content: bytes, project_name: str, scene_id: str, shot_id: str, filename: str) -> str:
        """Save binary content to file"""
        file_path = self.get_output_path(project_name, scene_id, shot_id, filename)
        
        try:
            with open(file_path, "wb") as f:
                f.write(content)
            logger.info(f"File saved: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save file {file_path}: {e}")
            raise e

    def _sanitize(self, name: str) -> str:
        """Simple sanitization for directory names"""
        # Replace common unsafe chars
        keepcharacters = (' ','.','_','-')
        return "".join(c for c in name if c.isalnum() or c in keepcharacters).strip().replace(' ', '_')

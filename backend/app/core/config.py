import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Image Video Generator"
    API_V1_STR: str = "/api"
    
    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    VEO_API_KEY: str = os.getenv("VEO_API_KEY", "")
    
    # System Config
    MAX_CONCURRENT_TASKS: int = int(os.getenv("MAX_CONCURRENT_TASKS", 5))
    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", 500 * 1024 * 1024)) # 500MB
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "./output")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Model Config
    GEMINI_MODEL: str = "models/gemini-3-pro-image-preview"
    VEO_MODEL: str = "models/veo-2.0-generate-001"

    class Config:
        env_file = ".env"

settings = Settings()

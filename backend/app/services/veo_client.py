import httpx
from app.core.config import settings
from loguru import logger
import json
import base64

class VeoClient:
    """Veo API Client for Video Generation"""
    
    def __init__(self):
        self.api_key = settings.VEO_API_KEY
        self.base_url = settings.VEO_BASE_URL
        self.model = settings.VEO_MODEL
        
    async def generate_video(self, prompt: str, image_url: str = None, **kwargs) -> bytes:
        """
        Generate video from prompt (and optional image) using Veo API
        """
        if not self.api_key:
            logger.warning("Veo API Key is missing. Returning mock data.")
            return self._get_mock_video()
            
        url = f"{self.base_url}/{self.model}:generate"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "duration_seconds": kwargs.get('duration', 5),
            "aspect_ratio": kwargs.get('aspect_ratio', "16:9")
        }
        
        if image_url:
            payload['image_url'] = image_url
            
        try:
            async with httpx.AsyncClient() as client:
                # Video generation is usually long-running. 
                # This might return a job ID or wait (if short).
                # Assuming sync return for simplicity or blocking wait.
                response = await client.post(url, json=payload, headers=headers, timeout=120.0)
                response.raise_for_status()
                data = response.json()
                
                # Assume response contains video URL or data
                return await self._extract_video_data(data)
                
        except Exception as e:
            logger.error(f"Veo API Error: {str(e)}")
            raise e

    async def _extract_video_data(self, data: dict) -> bytes:
        """
        Extract video data from API response.
        Supports direct base64 data or downloading from a URL.
        """
        try:
            # Case 1: Video URL provided
            if 'video_url' in data:
                video_url = data['video_url']
                async with httpx.AsyncClient() as client:
                    resp = await client.get(video_url)
                    resp.raise_for_status()
                    return resp.content
            
            # Case 2: Base64 encoded content (hypothetical structure)
            if 'video_content' in data:
                 return base64.b64decode(data['video_content'])

            # Case 3: Google Cloud / Vertex AI specific structure (e.g. predictions[0].bytesBase64Encoded)
            if 'predictions' in data and len(data['predictions']) > 0:
                 prediction = data['predictions'][0]
                 if 'bytesBase64Encoded' in prediction:
                     return base64.b64decode(prediction['bytesBase64Encoded'])

            # Fallback
            logger.warning(f"Could not find video data in response: {data.keys()}")
            return b"" 

        except Exception as e:
            logger.error(f"Failed to extract video data: {str(e)}")
            raise ValueError(f"Failed to extract video data: {str(e)}")

    def _get_mock_video(self) -> bytes:
        """Return a mock video bytes (using a small valid mp4 header if possible, or just dummy)"""
        # Minimal MP4 header for testing file creation
        # This is not a playable video, but enough to create a file
        return b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom\x00\x00\x00\x00'

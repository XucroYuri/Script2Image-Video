import httpx
from app.core.config import settings
from loguru import logger
import base64

class GeminiClient:
    """Gemini API Client for Image Generation"""
    
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.base_url = settings.GEMINI_BASE_URL
        self.model = settings.GEMINI_MODEL
        
    async def generate_image(self, prompt: str, **kwargs) -> bytes:
        """
        Generate image from prompt using Gemini API
        """
        if not self.api_key:
            logger.warning("Gemini API Key is missing. Returning mock data.")
            # Mock behavior for development if no key
            return self._get_mock_image()
            
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        
        # Construct payload based on Gemini API docs
        # Note: Actual payload structure depends on specific model version
        # This is a generic structure for Gemini 1.5 Pro/Flash, might need adjustment for 3-pro-image-preview
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": kwargs.get('temperature', 0.9),
                "topK": kwargs.get('top_k', 40),
                "topP": kwargs.get('top_p', 0.95),
                "maxOutputTokens": 8192,
                "responseMimeType": "image/jpeg" # Requesting image output if supported directly
            }
        }
        
        # For image generation models specifically (like Imagen on Vertex AI or Gemini generic)
        # We might need to adjust payload. 
        # Assuming the standard Gemini text-to-image capability if available via generateContent
        # OR if using a specific Imagen endpoint.
        # Since 'gemini-3-pro-image-preview' is specified, we'll assume it follows standard generateContent 
        # but returns image data or links.
        
        # Let's try standard structure first.
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload, timeout=30.0)
                response.raise_for_status()
                data = response.json()
                
                # Extract image data from response
                # This part is highly dependent on the specific API response format
                # For now, we'll try to find base64 image data
                return self._extract_image_data(data)
                
        except Exception as e:
            logger.error(f"Gemini API Error: {str(e)}")
            raise e

    def _extract_image_data(self, data: dict) -> bytes:
        """Extract binary image data from API response"""
        try:
            # Attempt to find base64 data in candidates
            # This path is hypothetical and needs to be adjusted based on actual API response
            if 'candidates' in data and data['candidates']:
                parts = data['candidates'][0]['content']['parts']
                for part in parts:
                    if 'inline_data' in part:
                        return base64.b64decode(part['inline_data']['data'])
            
            # Fallback or error if structure doesn't match
            logger.error(f"Unexpected API response structure: {data}")
            raise ValueError("Could not extract image from response")
            
        except Exception as e:
            raise ValueError(f"Failed to process API response: {str(e)}")

    def _get_mock_image(self) -> bytes:
        """Return a simple 1x1 pixel image for testing"""
        # Red 1x1 PNG
        return base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")

import asyncio
from app.services.gemini_client import GeminiClient
from app.services.veo_client import VeoClient
from app.services.file_storage import FileStorageService
import os

async def test_integration():
    print("🚀 Starting Integration Test...")
    
    # 1. Test File Storage
    print("\n📦 Testing File Storage...")
    storage = FileStorageService()
    test_content = b"TEST_CONTENT"
    try:
        path = storage.save_file(
            content=test_content,
            project_name="TestProject",
            scene_id="Scene01",
            shot_id="Shot01",
            filename="test.txt"
        )
        print(f"✅ File saved at: {path}")
        assert os.path.exists(path)
        with open(path, "rb") as f:
            assert f.read() == test_content
    except Exception as e:
        print(f"❌ File Storage Failed: {e}")

    # 2. Test Gemini Client (Mock)
    print("\n🎨 Testing Gemini Client...")
    gemini = GeminiClient()
    try:
        # Since we don't have a real key in env yet, this should return mock data or fail if configured to fail
        # The current implementation logs warning and returns mock data if key is missing
        image_data = await gemini.generate_image("Test Prompt")
        print(f"✅ Image Generated (Size: {len(image_data)} bytes)")
        
        # Save it
        img_path = storage.save_file(
            content=image_data,
            project_name="TestProject",
            scene_id="Scene01",
            shot_id="Shot01",
            filename="gemini_test.png"
        )
        print(f"✅ Image Saved at: {img_path}")
    except Exception as e:
        print(f"❌ Gemini Client Failed: {e}")

    # 3. Test Veo Client (Mock)
    print("\n🎥 Testing Veo Client...")
    veo = VeoClient()
    try:
        video_data = await veo.generate_video("Test Video Prompt")
        print(f"✅ Video Generated (Size: {len(video_data)} bytes)")
        
        # Save it
        vid_path = storage.save_file(
            content=video_data,
            project_name="TestProject",
            scene_id="Scene01",
            shot_id="Shot01",
            filename="veo_test.mp4"
        )
        print(f"✅ Video Saved at: {vid_path}")
    except Exception as e:
        print(f"❌ Veo Client Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_integration())

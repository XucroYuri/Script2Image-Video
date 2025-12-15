import sys
import os
# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.services.json_parser import JSONParserService
from app.models.schemas import ProjectData

def test_parser():
    # Path to the actual JSON file provided by user
    json_path = "/Volumes/SSD/Video_Cut/信与账/App/Input/Visual_Development_Prompts_Nano_Veo.json"
    
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    parser = JSONParserService()
    try:
        # 1. Parse
        print("Parsing JSON...")
        project_data = parser.parse_project_json(json_path)
        print(f"Project Name: {project_data.project}")
        print(f"Scenes count: {len(project_data.scenes)}")
        
        # 2. Process Prompts
        print("\nProcessing Prompts...")
        processed_data = parser.process_all_prompts(project_data)
        
        # Check a sample shot
        first_scene = processed_data.scenes[0]
        first_shot = first_scene.shots[0]
        
        print(f"\nSample Shot ID: {first_shot.shot_id}")
        print(f"Start Prompt (Processed): {first_shot.nano_banana_pro_prompts.start[:100]}...")
        
        # Verify placeholder replacement
        if "[Universal Style Block]" in first_shot.nano_banana_pro_prompts.start:
            print("❌ Error: [Universal Style Block] placeholder still exists!")
        else:
            print("✅ Success: [Universal Style Block] placeholder replaced.")
            
        # Verify reference replacement
        if "[Ref: Murata]" in first_shot.nano_banana_pro_prompts.start:
             print("❌ Error: [Ref: Murata] placeholder still exists!")
        else:
             print("✅ Success: [Ref: Murata] reference replaced.")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_parser()

import json
from typing import Dict, Any, List
from app.models.schemas import ProjectData, Scene, Shot, NanoBananaPrompts
from app.services.prompt_processor import PromptProcessorService

class JSONParserService:
    """JSON文件解析服务"""
    
    def parse_project_json(self, file_path: str) -> ProjectData:
        """解析项目JSON文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 手动构建 ProjectData 以处理结构差异
        
        # 1. 提取基础信息
        project_name = data.get('project', 'Untitled Project')
        core_style = data.get('core_style', {})
        character_references = data.get('character_references', {})
        
        # 2. 构建场景列表
        scenes_list = []
        raw_scenes = data.get('scenes', [])
        
        for scene_idx, raw_scene in enumerate(raw_scenes):
            scene_id = raw_scene.get('scene_id')
            
            # 构建镜头列表
            shots_list = []
            raw_shots = raw_scene.get('shots', [])
            
            for shot_idx, raw_shot in enumerate(raw_shots):
                # 处理 nano_banana_pro_prompts 列表转对象
                prompts_list = raw_shot.get('nano_banana_pro_prompts', [])
                prompts_dict = {}
                if isinstance(prompts_list, list):
                    for p in prompts_list:
                        frame = p.get('frame')
                        text = p.get('prompt')
                        if frame and text:
                            prompts_dict[frame] = text
                elif isinstance(prompts_list, dict):
                    prompts_dict = prompts_list
                
                # 确保有 start/middle/end
                nano_prompts = NanoBananaPrompts(
                    start=prompts_dict.get('start', ''),
                    middle=prompts_dict.get('middle', ''),
                    end=prompts_dict.get('end', '')
                )
                
                shot = Shot(
                    shot_id=raw_shot.get('shot_id'),
                    scene_id=scene_id, # 注入 scene_id
                    name=raw_shot.get('description', ''), # description 映射到 name
                    description=raw_shot.get('description'),
                    order_index=shot_idx + 1,
                    nano_banana_pro_prompts=nano_prompts,
                    veo_3_1_prompt=raw_shot.get('veo_3_1_prompt')
                )
                shots_list.append(shot)
            
            scene = Scene(
                scene_id=scene_id,
                project_id="project_001", # 默认ID，实际可能需要生成
                scene_title=raw_scene.get('scene_title'),
                timestamp=raw_scene.get('timestamp'),
                shots=shots_list
            )
            scenes_list.append(scene)
            
        project_data = ProjectData(
            project=project_name,
            core_style=core_style,
            character_references=character_references,
            scenes=scenes_list
        )
        
        return project_data
    
    def process_all_prompts(self, project_data: ProjectData) -> ProjectData:
        """
        处理项目中的所有Prompt
        返回一个新的ProjectData对象，其中的prompts已经被处理
        """
        # 初始化处理器
        processor = PromptProcessorService(
            core_style=project_data.core_style,
            character_references=project_data.character_references
        )
        
        # 遍历所有场景和镜头
        for scene in project_data.scenes:
            for shot in scene.shots:
                # 处理 nano_banana_pro_prompts
                if shot.nano_banana_pro_prompts:
                    shot.nano_banana_pro_prompts.start = processor.process_prompt(shot.nano_banana_pro_prompts.start)
                    shot.nano_banana_pro_prompts.middle = processor.process_prompt(shot.nano_banana_pro_prompts.middle)
                    shot.nano_banana_pro_prompts.end = processor.process_prompt(shot.nano_banana_pro_prompts.end)
                
                # 处理 veo_3_1_prompt
                if shot.veo_3_1_prompt:
                    shot.veo_3_1_prompt = processor.process_prompt(shot.veo_3_1_prompt)
                    
        return project_data

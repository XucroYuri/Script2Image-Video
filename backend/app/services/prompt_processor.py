import re
from typing import Dict, Any

class PromptProcessorService:
    """提示词处理服务"""
    
    def __init__(self, core_style: Dict[str, Any] = None, character_references: Dict[str, str] = None):
        self.core_style = core_style or {}
        self.character_references = character_references or {}
        self.style_blocks = self._flatten_style_blocks(self.core_style)
    
    def _flatten_style_blocks(self, core_style: Dict[str, Any]) -> Dict[str, str]:
        """
        将嵌套的风格块展平，并生成替换内容。
        例如 universal_style_block 会被替换为该block下所有属性的组合字符串。
        """
        blocks = {}
        for block_name, content in core_style.items():
            if isinstance(content, dict):
                # 将字典内容拼接成字符串
                style_desc = ", ".join([f"{k}: {v}" for k, v in content.items()])
                blocks[block_name] = style_desc
                
                # 同时也支持 [Universal Style Block] 这种格式 (首字母大写或带空格)
                # 简单的归一化处理
                normalized_name = block_name.replace("_", " ").title() # universal_style_block -> Universal Style Block
                blocks[normalized_name] = style_desc
            else:
                blocks[block_name] = str(content)
        return blocks
    
    def process_prompt(self, prompt: str) -> str:
        """处理单个提示词"""
        if not prompt:
            return ""
            
        # 1. 替换样式块占位符
        prompt = self.replace_style_blocks(prompt)
        
        # 2. 替换引用映射
        prompt = self.replace_references(prompt)
        
        return prompt
    
    def replace_style_blocks(self, prompt: str) -> str:
        """
        替换样式块占位符，支持多种格式：
        [universal_style_block]
        [Universal Style Block]
        """
        # 简单的字符串替换可能不够灵活，但对于明确的占位符通常足够
        # 先尝试直接替换 keys
        for key, value in self.style_blocks.items():
            # Case insensitive replace for brackets
            # e.g. [universal_style_block]
            pattern = re.compile(re.escape(f"[{key}]"), re.IGNORECASE)
            prompt = pattern.sub(value, prompt)
            
            # 同时也处理下划线和空格的差异
            # 如果 key 是 universal_style_block，我们也要匹配 [Universal Style Block]
            if "_" in key:
                alt_key = key.replace("_", " ")
                pattern_alt = re.compile(re.escape(f"[{alt_key}]"), re.IGNORECASE)
                prompt = pattern_alt.sub(value, prompt)

        return prompt
    
    def replace_references(self, prompt: str) -> str:
        """替换引用结构 ([Ref: Name])"""
        # 匹配 ([Ref: Name]) 格式的引用
        pattern = r'\(\[Ref:\s*([^\]]+)\]\)'
        
        def replace_match(match):
            ref_name = match.group(1).strip()
            # 尝试直接匹配
            if ref_name in self.character_references:
                return self.character_references[ref_name]
            
            # 尝试转小写匹配 (JSON key 通常是小写 snake_case, 但引用可能是 Title Case)
            ref_lower = ref_name.lower().replace(" ", "_")
            if ref_lower in self.character_references:
                return self.character_references[ref_lower]
                
            return match.group(0) # 如果没找到，保持原样
        
        return re.sub(pattern, replace_match, prompt)


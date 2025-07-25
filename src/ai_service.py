"""
AI Service for character interactions
使用OpenAI Python SDK规范，支持多种兼容的API服务
"""
import asyncio
from typing import Optional, Dict, Any

try:
    import config
except ImportError:
    print("错误: 未找到 config.py 文件。请复制 config.example.py 为 config.py 并设置您的API密钥。")
    exit(1)

try:
    import openai
except ImportError:
    print("错误: OpenAI库未安装。运行: pip install openai")
    exit(1)


class AIService:
    """使用OpenAI SDK规范处理AI API交互"""
    
    def __init__(self):
        self.provider = config.AI_PROVIDER
        self.api_key = config.API_KEY
        self.model = config.MODEL
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """根据提供商初始化OpenAI兼容的客户端"""
        
        # API端点配置
        api_configs = {
            "openai": {
                "base_url": None,  # 使用默认
                "description": "OpenAI官方API"
            },
            "kimi": {
                "base_url": "https://api.moonshot.cn/v1",
                "description": "Kimi (月之暗面) API"
            },
            "deepseek": {
                "base_url": "https://api.deepseek.com/v1",
                "description": "DeepSeek API"
            },
            "zhipu": {
                "base_url": "https://open.bigmodel.cn/api/paas/v4",
                "description": "智谱AI API"
            },
            "qwen": {
                "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
                "description": "通义千问 API"
            }
        }
        
        if self.provider not in api_configs:
            print(f"错误: 不支持的AI提供商: {self.provider}")
            print(f"支持的提供商: {', '.join(api_configs.keys())}")
            exit(1)
        
        config_info = api_configs[self.provider]
        
        try:
            # 使用OpenAI SDK创建客户端
            client_args = {"api_key": self.api_key}
            if config_info["base_url"]:
                client_args["base_url"] = config_info["base_url"]
            
            self.client = openai.OpenAI(**client_args)
            
            if config.DEBUG_MODE:
                print(f"✅ 已初始化 {config_info['description']} 客户端")
                print(f"   模型: {self.model}")
                if config_info["base_url"]:
                    print(f"   端点: {config_info['base_url']}")
                
        except Exception as e:
            print(f"错误: 客户端初始化失败: {e}")
            exit(1)
    
    async def get_character_response(self, character_name: str, character_personality: str, 
                                   player_message: str, context: str = "") -> str:
        """
        使用OpenAI SDK规范获取AI角色回复
        
        Args:
            character_name: 角色名称
            character_personality: 角色个性描述
            player_message: 玩家消息
            context: 额外上下文信息
            
        Returns:
            角色的回复
        """
        try:
            system_prompt = self._build_character_prompt(character_name, character_personality, context)
            
            # 使用统一的OpenAI SDK调用方式
            response = await self._get_openai_compatible_response(system_prompt, player_message)
            
            # 确保回复不会太长
            if len(response) > config.MAX_RESPONSE_LENGTH:
                response = response[:config.MAX_RESPONSE_LENGTH] + "..."
            
            return response
            
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"AI服务错误: {e}")
                print(f"错误类型: {type(e)}")
            return f"{character_name} 看起来心不在焉，现在无法回应。"
    
    def _build_character_prompt(self, name: str, personality: str, context: str) -> str:
        """构建角色系统提示词"""
        prompt = f"""你是 {name}，一个文字RPG游戏中的角色。

个性: {personality}

你需要:
- 始终保持角色身份
- 像 {name} 一样回应
- 保持对话的趣味性和吸引力
- 在适当的时候帮助玩家
- 为回复增添个性和风格
- 回复保持在 {config.MAX_RESPONSE_LENGTH} 字符以内
- 使用中文回复

当前情况: {context if context else "你在你的常驻地点。"}

请自然地以 {name} 的身份说话。"""
        
        return prompt
    
    async def _get_openai_compatible_response(self, system_prompt: str, user_message: str) -> str:
        """使用OpenAI SDK规范获取回复"""
        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=150,
                temperature=0.8
            )
            
            if response.choices and response.choices[0].message.content:
                return response.choices[0].message.content.strip()
            else:
                return "抱歉，我现在无法生成回复。"
                
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"API调用错误详情: {e}")
                print(f"错误类型: {type(e)}")
            
            # 处理常见错误
            error_msg = str(e).lower()
            if "404" in error_msg or "not found" in error_msg:
                return "模型不可用，请检查模型名称是否正确。"
            elif "401" in error_msg or "403" in error_msg or "permission" in error_msg:
                return "API密钥无效，请检查密钥是否正确。"
            elif "quota" in error_msg or "limit" in error_msg:
                return "API配额已用完，请稍后再试。"
            elif "connection" in error_msg or "timeout" in error_msg:
                return "网络连接问题，请稍后再试。"
            else:
                return "AI服务暂时不可用，请稍后再试。"

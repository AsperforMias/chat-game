# 配置模板 (OpenAI SDK规范)
# 复制此文件为 config.py 并设置您的实际值

# AI提供商配置 (所有提供商都使用OpenAI SDK规范)
AI_PROVIDER = "openai"  # 选项: "openai", "kimi", "deepseek", "zhipu", "qwen"
API_KEY = "your-api-key-here"  # 在这里填入您的API密钥
MODEL = "gpt-3.5-turbo"  # 根据提供商选择合适的模型

# 常用模型配置示例:
# OpenAI:    MODEL = "gpt-3.5-turbo" 或 "gpt-4"
# Kimi:      MODEL = "moonshot-v1-8k" 或 "moonshot-v1-32k"  
# DeepSeek:  MODEL = "deepseek-chat"
# 智谱AI:    MODEL = "glm-4" 或 "glm-3-turbo"
# 通义千问:   MODEL = "qwen-turbo" 或 "qwen-plus"

# AI提供商配置
AI_PROVIDER = "gemini"  # 选项: "openai", "anthropic", "gemini"
API_KEY = ""  # 在这里填入您的API密钥
MODEL = "gpt-3.5-turbo"  # OpenAI: "gpt-3.5-turbo", Anthropic: "claude-3-haiku-20240307", Gemini: "gemini-pro"

# 游戏设置
GAME_TITLE = "AI RPG 聊天游戏"
MAX_RESPONSE_LENGTH = 200  # AI回复的最大长度
DEBUG_MODE = False  # 生产环境请设为False

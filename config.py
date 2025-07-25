# AI RPG 聊天游戏配置
# 这是工作配置文件 - 请替换为您的实际API密钥

# AI提供商配置 (使用OpenAI SDK规范)
AI_PROVIDER = "kimi"  # 选项: "openai", "kimi", "deepseek", "zhipu", "qwen"
API_KEY = "sk-aNLlWGcgecl96airHqY1NrxYPht7yRWT9pNdXYrbaHSye3nG"  # 您的API密钥
MODEL = "moonshot-v1-8k"  # 根据提供商选择: openai(gpt-3.5-turbo), kimi(moonshot-v1-8k), deepseek(deepseek-chat), 等

# 游戏设置
GAME_TITLE = "AI RPG 聊天游戏"
MAX_RESPONSE_LENGTH = 200
DEBUG_MODE = True  # 生产环境请设为False

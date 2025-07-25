# AI RPG 聊天游戏

一个简洁的AI驱动RPG探索游戏，您可以探索世界并与AI角色互动。

## 特色功能

- **世界探索**: 在不同地点间穿行
- **AI角色互动**: 与能动态回应的AI NPC角色聊天
- **简洁架构**: 干净、最小化的代码库，易于理解和扩展
- **可配置AI**: 使用您自己的API密钥进行角色对话

## 快速开始

1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 配置您的AI API密钥:
   ```bash
   cp config.example.py config.py
   # 编辑 config.py 文件，设置您的API密钥
   ```

3. 运行游戏:
   ```bash
   python main.py
   ```

## 配置说明

本项目采用 **OpenAI Python SDK 规范**，支持所有兼容OpenAI API格式的AI服务商。

复制 `config.example.py` 为 `config.py` 并设置您的API配置:

- `AI_PROVIDER`: 选择AI提供商
- `API_KEY`: 您的API密钥  
- `MODEL`: 用于角色对话的模型名称

### 支持的AI提供商

| 提供商 | AI_PROVIDER | 推荐模型 | API密钥获取 |
|--------|-------------|----------|-------------|
| **OpenAI** | `openai` | `gpt-3.5-turbo`, `gpt-4` | [OpenAI API](https://platform.openai.com/api-keys) |
| **Kimi (月之暗面)** | `kimi` | `moonshot-v1-8k`, `moonshot-v1-32k` | [Kimi API](https://platform.moonshot.cn/console/api-keys) |
| **DeepSeek** | `deepseek` | `deepseek-chat` | [DeepSeek API](https://platform.deepseek.com/api_keys) |
| **智谱AI** | `zhipu` | `glm-4`, `glm-3-turbo` | [智谱AI](https://open.bigmodel.cn/usercenter/apikeys) |
| **通义千问** | `qwen` | `qwen-turbo`, `qwen-plus` | [阿里云](https://dashscope.console.aliyun.com/apiKey) |

### 配置示例

```python
# 使用 Kimi
AI_PROVIDER = "kimi"
API_KEY = "sk-your-kimi-api-key"
MODEL = "moonshot-v1-8k"

# 使用 OpenAI
AI_PROVIDER = "openai"  
API_KEY = "sk-your-openai-key"
MODEL = "gpt-3.5-turbo"

# 使用 DeepSeek
AI_PROVIDER = "deepseek"
API_KEY = "sk-your-deepseek-key"
MODEL = "deepseek-chat"
```

## 游戏命令

- `look` - 查看当前位置
- `go <方向>` - 移动 (north/south/east/west 或 北/南/东/西)
- `talk <角色> <消息>` - 与AI角色聊天
- `characters` - 列出当前位置的角色
- `help` - 显示可用命令
- `quit` - 退出游戏

## 项目结构

```
├── main.py           # 游戏入口和主循环
├── world.py          # 世界和地点管理  
├── character.py      # AI角色系统
├── ai_service.py     # AI API集成
├── config.py         # 配置文件 (从示例复制创建)
├── config.example.py # 配置模板
├── requirements.txt  # 依赖项
└── README.md         # 本文件
```

## 扩展游戏

代码库设计简洁且易于扩展:

- 在 `world.py` 中添加新地点
- 创建具有独特个性的新AI角色
- 在 `ai_service.py` 中集成更多AI提供商
- 在 `main.py` 中添加新的游戏命令

## 许可证

MIT 许可证

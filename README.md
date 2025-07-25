# AI RPG 聊天游戏

一个AI驱动的文本冒险游戏，你可以探索世界并与AI角色进行对话。

## ✨ 特性

- 🤖 使用OpenAI SDK标准化的AI角色交互
- 🌍 可探索的世界，包含不同的地点
- 💬 与独特AI个性的动态对话
- 🎭 多种角色类型（村长、商人、守护者、学者）
- 🔧 支持多个AI提供商（OpenAI、Kimi、DeepSeek、智谱AI、阿里云等）
- 🐍 使用 pyenv + venv 的干净环境管理
- 🧪 完整的测试套件和代码质量工具

## 📁 项目结构

```
chat-game/
├── src/                    # 源代码
│   ├── __init__.py        # 包初始化
│   ├── main.py            # 主程序入口
│   ├── ai_service.py      # AI服务模块
│   ├── character.py       # 角色系统
│   ├── world.py           # 世界管理
│   ├── config.py          # 配置文件
│   └── config.example.py  # 配置示例
├── tests/                  # 测试文件
├── scripts/               # 脚本工具
├── docs/                  # 文档
├── venv/                  # 虚拟环境
├── Makefile              # 便捷命令
├── pyproject.toml        # 项目配置
├── requirements.txt      # 生产依赖
└── requirements-dev.txt  # 开发依赖
```

## 🚀 快速开始

### 环境要求
- Python 3.10+
- pyenv (推荐)

### 1. 克隆项目
```bash
git clone https://github.com/AsperforMias/chat-game.git
cd chat-game
```

### 2. 设置开发环境
```bash
# 使用便捷脚本
source scripts/setup_env.sh

# 或者使用 Makefile
make setup

# 或者手动设置
pyenv local 3.12.11
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3. 配置API密钥
```bash
cp src/config.example.py src/config.py
# 编辑 src/config.py 添加你的API密钥
```

### 4. 运行游戏
```bash
# 使用 Makefile
make run

# 或者使用脚本
./scripts/run_game.sh

# 或者直接运行
source venv/bin/activate
python src/main.py
```

## 🛠️ 开发命令

```bash
make help     # 查看所有可用命令
make setup    # 设置开发环境
make run      # 运行游戏
make test     # 运行测试
make lint     # 代码检查
make format   # 代码格式化
make clean    # 清理临时文件
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

# Chat Game 开发文档

## 目录结构

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
└── requirements.txt       # 依赖列表
```

## 开发环境设置

### 1. 环境准备
- Python 3.10+
- pyenv (Python 版本管理)
- venv (虚拟环境)

### 2. 快速开始
```bash
# 克隆项目
git clone https://github.com/AsperforMias/chat-game.git
cd chat-game

# 设置环境
source scripts/setup_env.sh

# 配置 API 密钥
cp src/config.example.py src/config.py
# 编辑 src/config.py 添加你的 API 密钥

# 运行游戏
make run
# 或者
./scripts/run_game.sh
```

### 3. 开发命令

```bash
make setup    # 设置开发环境
make run      # 运行游戏
make test     # 运行测试
make lint     # 代码检查
make format   # 代码格式化
make clean    # 清理临时文件
```

## 架构设计

### AI 服务层
- 统一的 OpenAI SDK 接口
- 支持多个 AI 提供商
- 异步处理保证响应性

### 角色系统
- 可扩展的角色管理
- 对话历史记录
- 个性化 AI 响应

### 世界管理
- 基于位置的交互
- 动态场景描述
- 探索系统

## 支持的 AI 提供商

- OpenAI (GPT-3.5/4)
- Kimi (月之暗面)
- DeepSeek
- 智谱 AI (GLM)
- 阿里云通义千问

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 创建 Pull Request

## 许可证

MIT License

#!/bin/bash

# Chat Game 快速启动脚本

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "❌ 虚拟环境不存在，请先运行: source scripts/setup_env.sh"
    exit 1
fi

# 激活虚拟环境
source venv/bin/activate

# 检查配置文件
if [ ! -f "src/config.py" ]; then
    echo "❌ 配置文件不存在，请复制 src/config.example.py 为 src/config.py 并配置 API 密钥"
    exit 1
fi

# 启动游戏
echo "🎮 启动 Chat Game..."
python src/main.py

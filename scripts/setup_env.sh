#!/bin/bash

# Chat Game 环境设置脚本
# 使用方法: source scripts/setup_env.sh

echo "🎮 正在设置 Chat Game 开发环境..."

# 检查是否在项目根目录
if [ ! -f "requirements.txt" ]; then
    echo "❌ 错误：请在项目根目录运行此脚本"
    return 1
fi

# 检查 pyenv
if ! command -v pyenv &> /dev/null; then
    echo "❌ pyenv 未安装，请先安装 pyenv"
    echo "   macOS: brew install pyenv"
    echo "   Ubuntu/Debian: curl https://pyenv.run | bash"
    return 1
fi

# 设置 Python 版本
echo "🐍 设置 Python 版本..."
pyenv local 3.12.11

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python -m venv venv
else
    echo "📦 虚拟环境已存在"
fi

# 激活虚拟环境
echo "🔄 激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo "⬆️  升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "📚 安装项目依赖..."
pip install -r requirements.txt

# 安装开发依赖
echo "🛠️  安装开发依赖..."
pip install pytest pytest-cov black flake8 mypy

echo "✅ 环境设置完成！"
echo ""
echo "🎯 下一步："
echo "   1. 复制 src/config.example.py 为 src/config.py"
echo "   2. 在 src/config.py 中配置你的 AI API 密钥"
echo "   3. 运行游戏: python src/main.py"
echo "   4. 运行测试: pytest tests/"
echo ""
echo "💡 提示："
echo "   - 使用 'deactivate' 退出虚拟环境"
echo "   - 下次开发时只需运行: source venv/bin/activate"

#!/bin/bash

# Chat Game 测试脚本

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "❌ 虚拟环境不存在，请先运行: source scripts/setup_env.sh"
    exit 1
fi

# 激活虚拟环境
source venv/bin/activate

echo "🧪 运行测试..."

# 运行所有测试
pytest tests/ -v

# 运行代码覆盖率测试
echo ""
echo "📊 生成覆盖率报告..."
pytest tests/ --cov=src --cov-report=html --cov-report=term

echo ""
echo "✅ 测试完成！"
echo "📝 详细覆盖率报告: htmlcov/index.html"

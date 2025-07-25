# Chat Game Makefile

.PHONY: help setup run test clean lint format

# 默认目标
help:
	@echo "🎮 Chat Game 命令帮助"
	@echo ""
	@echo "可用命令:"
	@echo "  setup   - 设置开发环境"
	@echo "  run     - 运行游戏"
	@echo "  test    - 运行测试"
	@echo "  lint    - 代码检查"
	@echo "  format  - 代码格式化"
	@echo "  clean   - 清理临时文件"

# 设置开发环境
setup:
	@echo "🛠️  设置开发环境..."
	@bash scripts/setup_env.sh

# 运行游戏
run:
	@bash scripts/run_game.sh

# 运行测试
test:
	@bash scripts/run_tests.sh

# 代码检查
lint:
	@echo "🔍 运行代码检查..."
	@source venv/bin/activate && flake8 src/ tests/
	@source venv/bin/activate && mypy src/

# 代码格式化
format:
	@echo "✨ 格式化代码..."
	@source venv/bin/activate && black src/ tests/
	@source venv/bin/activate && isort src/ tests/

# 清理临时文件
clean:
	@echo "🧹 清理临时文件..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@rm -rf htmlcov/
	@rm -rf .coverage
	@rm -rf .pytest_cache/

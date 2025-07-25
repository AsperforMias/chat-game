#!/usr/bin/env python3
"""
测试AI服务支持的所有提供商
"""

def test_ai_providers():
    """测试所有AI提供商的配置"""
    print("🧪 测试AI提供商支持...")
    print()
    
    # 测试配置文件加载
    try:
        import config
        print(f"✅ 配置文件加载成功")
        print(f"   当前提供商: {config.AI_PROVIDER}")
        print(f"   当前模型: {config.MODEL}")
        print()
    except ImportError:
        print("❌ 配置文件未找到，请复制 config.example.py 为 config.py")
        return
    
    # 测试AI服务初始化
    try:
        from ai_service import AIService
        ai_service = AIService()
        print(f"✅ AI服务初始化成功")
        print(f"   提供商: {ai_service.provider}")
        print(f"   模型: {ai_service.model}")
        print()
    except Exception as e:
        print(f"❌ AI服务初始化失败: {e}")
        return
    
    # 显示支持的提供商
    print("📋 支持的AI提供商:")
    print("   • OpenAI (openai)")
    print("     - 模型: gpt-3.5-turbo, gpt-4, gpt-4-turbo")
    print("     - 获取密钥: https://platform.openai.com/api-keys")
    print()
    print("   • Anthropic (anthropic)")  
    print("     - 模型: claude-3-haiku-20240307, claude-3-sonnet-20240229")
    print("     - 获取密钥: https://console.anthropic.com/")
    print()
    print("   • Google Gemini (gemini)")
    print("     - 模型: gemini-pro, gemini-1.5-flash, gemini-1.5-pro")
    print("     - 获取密钥: https://makersuite.google.com/app/apikey")
    print()
    print("   • Kimi 月之暗面 (kimi)")
    print("     - 模型: moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k")
    print("     - 获取密钥: https://platform.moonshot.cn/console/api-keys")
    print()
    
    print("💡 使用说明:")
    print("   1. 在 config.py 中设置 AI_PROVIDER")
    print("   2. 设置对应的 API_KEY")  
    print("   3. 选择合适的 MODEL")
    print("   4. 运行游戏: python main.py")

if __name__ == "__main__":
    test_ai_providers()

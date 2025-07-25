#!/usr/bin/env python3
"""
Kimi API 测试和诊断工具
"""
import asyncio
import sys

def test_kimi_api():
    """测试Kimi API连接和配置"""
    print("🌙 Kimi API 诊断工具")
    print("=" * 50)
    
    # 1. 检查配置
    try:
        import config
        print(f"✅ 配置加载成功")
        print(f"   提供商: {config.AI_PROVIDER}")
        print(f"   模型: {config.MODEL}")
        print(f"   API密钥: {config.API_KEY[:20]}...")
        print()
    except ImportError:
        print("❌ 配置文件未找到")
        return False
    
    # 2. 检查库安装
    try:
        import openai
        print("✅ openai 库已安装")
        print()
    except ImportError:
        print("❌ openai 库未安装")
        print("   请运行: pip install openai")
        return False
    
    # 3. 测试API连接
    try:
        print("🧪 测试API连接...")
        client = openai.OpenAI(
            api_key=config.API_KEY,
            base_url="https://api.moonshot.cn/v1"
        )
        
        # 测试简单对话
        response = client.chat.completions.create(
            model=config.MODEL,
            messages=[
                {"role": "system", "content": "你是一个友善的助手，请简短回复。"},
                {"role": "user", "content": "你好，请简单介绍一下自己。"}
            ],
            max_tokens=50,
            temperature=0.7
        )
        
        if response.choices and response.choices[0].message.content:
            print("✅ API连接测试成功!")
            print(f"   回复: {response.choices[0].message.content.strip()}")
        else:
            print("⚠️  API连接成功但无有效回复")
            print(f"   响应: {response}")
        print()
        
    except Exception as e:
        print(f"❌ API连接测试失败: {e}")
        print(f"   错误类型: {type(e)}")
        
        # 分析常见错误
        error_msg = str(e).lower()
        if "401" in error_msg:
            print("   💡 建议: API密钥无效，请检查密钥是否正确")
        elif "403" in error_msg:
            print("   💡 建议: API密钥权限不足或已过期")
        elif "404" in error_msg:
            print("   💡 建议: 检查模型名称是否正确")
            print("       可用模型: moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k")
        elif "quota" in error_msg or "limit" in error_msg:
            print("   💡 建议: API配额已用完，请检查账户余额")
        elif "connection" in error_msg:
            print("   💡 建议: 网络连接问题，请检查网络设置")
        
        return False
    
    # 4. 模型信息
    print("📋 Kimi 可用模型:")
    print("   • moonshot-v1-8k    - 8K上下文窗口")
    print("   • moonshot-v1-32k   - 32K上下文窗口") 
    print("   • moonshot-v1-128k  - 128K上下文窗口")
    print()
    
    current_model = config.MODEL
    if current_model in ["moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"]:
        print(f"✅ 当前模型 '{current_model}' 是有效的Kimi模型")
    else:
        print(f"⚠️  当前模型 '{current_model}' 可能不是有效的Kimi模型")
        print("   建议使用: moonshot-v1-8k")
    print()
    
    print("🎉 Kimi API 测试完成!")
    return True

async def test_ai_service():
    """测试AI服务集成"""
    print("\n🧪 测试AI服务集成...")
    
    try:
        from ai_service import AIService
        ai_service = AIService()
        
        # 测试角色回复
        response = await ai_service.get_character_response(
            "村长",
            "你是一个友善的村长，说话简洁明了，关心村民。",
            "你好，村长",
            "你在村庄中心，周围有很多村民。"
        )
        
        print(f"✅ AI服务测试成功!")
        print(f"   村长回复: {response}")
        
    except Exception as e:
        print(f"❌ AI服务测试失败: {e}")
        return False
    
    return True

async def main():
    """主函数"""
    success = test_kimi_api()
    
    if success:
        await test_ai_service()
        print("\n🎉 所有测试通过! 您可以开始游戏了。")
        print("\n💡 配置示例:")
        print("   AI_PROVIDER = 'kimi'")
        print("   API_KEY = 'sk-...'  # 您的Kimi API密钥")
        print("   MODEL = 'moonshot-v1-8k'")
    else:
        print("\n⚠️  请解决上述问题后重新测试。")
        print("\n📖 获取Kimi API密钥:")
        print("   1. 访问 https://platform.moonshot.cn/")
        print("   2. 注册/登录账户")
        print("   3. 在控制台创建API密钥")
        print("   4. 确保账户有足够余额")

if __name__ == "__main__":
    asyncio.run(main())

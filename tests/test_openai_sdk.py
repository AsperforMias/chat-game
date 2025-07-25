#!/usr/bin/env python3
"""
统一AI API测试工具 (OpenAI SDK规范)
"""
import asyncio
import sys

def test_openai_compatible_api():
    """测试OpenAI兼容的API配置"""
    print("🤖 OpenAI SDK规范 - AI API 测试工具")
    print("=" * 60)
    
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
    
    # 2. 检查OpenAI库
    try:
        import openai
        print("✅ OpenAI SDK 已安装")
        print()
    except ImportError:
        print("❌ OpenAI SDK 未安装")
        print("   请运行: pip install openai")
        return False
    
    # 3. API端点配置
    api_configs = {
        "openai": {
            "base_url": None,
            "description": "OpenAI 官方API",
            "models": ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
        },
        "kimi": {
            "base_url": "https://api.moonshot.cn/v1",
            "description": "Kimi (月之暗面) API",
            "models": ["moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"]
        },
        "deepseek": {
            "base_url": "https://api.deepseek.com/v1", 
            "description": "DeepSeek API",
            "models": ["deepseek-chat", "deepseek-coder"]
        },
        "zhipu": {
            "base_url": "https://open.bigmodel.cn/api/paas/v4",
            "description": "智谱AI API",
            "models": ["glm-4", "glm-3-turbo"]
        },
        "qwen": {
            "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "description": "通义千问 API", 
            "models": ["qwen-turbo", "qwen-plus", "qwen-max"]
        }
    }
    
    if config.AI_PROVIDER not in api_configs:
        print(f"❌ 不支持的提供商: {config.AI_PROVIDER}")
        print(f"   支持的提供商: {', '.join(api_configs.keys())}")
        return False
    
    provider_config = api_configs[config.AI_PROVIDER]
    print(f"🔧 使用提供商: {provider_config['description']}")
    if provider_config['base_url']:
        print(f"   API端点: {provider_config['base_url']}")
    print(f"   推荐模型: {', '.join(provider_config['models'])}")
    print()
    
    # 4. 测试API连接
    try:
        print("🧪 测试API连接...")
        
        client_args = {"api_key": config.API_KEY}
        if provider_config["base_url"]:
            client_args["base_url"] = provider_config["base_url"]
        
        client = openai.OpenAI(**client_args)
        
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
            print(f"   AI回复: {response.choices[0].message.content.strip()}")
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
            print(f"       推荐模型: {', '.join(provider_config['models'])}")
        elif "quota" in error_msg or "limit" in error_msg:
            print("   💡 建议: API配额已用完，请检查账户余额")
        elif "connection" in error_msg:
            print("   💡 建议: 网络连接问题，请检查网络设置")
        
        return False
    
    # 5. 模型验证
    if config.MODEL in provider_config["models"]:
        print(f"✅ 模型 '{config.MODEL}' 是该提供商的推荐模型")
    else:
        print(f"⚠️  模型 '{config.MODEL}' 不在推荐列表中")
        print(f"   推荐模型: {', '.join(provider_config['models'])}")
    print()
    
    print("🎉 API测试完成!")
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
            "你好，村长！",
            "你在村庄中心，周围有很多村民在活动。"
        )
        
        print(f"✅ AI服务测试成功!")
        print(f"   村长回复: {response}")
        
    except Exception as e:
        print(f"❌ AI服务测试失败: {e}")
        return False
    
    return True

async def main():
    """主函数"""
    success = test_openai_compatible_api()
    
    if success:
        await test_ai_service()
        print("\n🎉 所有测试通过! 您可以开始游戏了。")
        print("\n🚀 启动游戏: python main.py")
    else:
        print("\n⚠️  请解决上述问题后重新测试。")

if __name__ == "__main__":
    asyncio.run(main())

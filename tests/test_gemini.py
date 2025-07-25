#!/usr/bin/env python3
"""
Gemini API 测试和诊断工具
"""
import asyncio
import sys

def test_gemini_api():
    """测试Gemini API连接和配置"""
    print("🧪 Gemini API 诊断工具")
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
        import google.generativeai as genai
        print("✅ google-generativeai 库已安装")
        print()
    except ImportError:
        print("❌ google-generativeai 库未安装")
        print("   请运行: pip install google-generativeai")
        return False
    
    # 3. 配置API
    try:
        genai.configure(api_key=config.API_KEY)
        print("✅ API密钥配置成功")
    except Exception as e:
        print(f"❌ API密钥配置失败: {e}")
        return False
    
    # 4. 列出可用模型
    try:
        print("📋 正在检查可用模型...")
        models = list(genai.list_models())
        print(f"✅ 找到 {len(models)} 个可用模型:")
        
        gemini_models = []
        for model in models:
            if 'gemini' in model.name.lower():
                model_name = model.name.split('/')[-1]  # 提取模型名称
                gemini_models.append(model_name)
                print(f"   • {model_name}")
        
        print()
        
        # 检查配置的模型是否可用
        if config.MODEL in gemini_models:
            print(f"✅ 配置的模型 '{config.MODEL}' 可用")
        else:
            print(f"⚠️  配置的模型 '{config.MODEL}' 不在可用列表中")
            print("   建议使用以下模型之一:")
            for model in gemini_models[:3]:  # 显示前3个
                print(f"     - {model}")
        print()
            
    except Exception as e:
        print(f"❌ 无法获取模型列表: {e}")
        print("   这通常表示API密钥无效或网络问题")
        return False
    
    # 5. 测试简单生成
    try:
        print("🧪 测试文本生成...")
        model = genai.GenerativeModel(config.MODEL)
        response = model.generate_content(
            "请简单说一句话介绍自己。",
            generation_config={
                'max_output_tokens': 50,
                'temperature': 0.7,
            }
        )
        
        if hasattr(response, 'text') and response.text:
            print(f"✅ 生成测试成功!")
            print(f"   回复: {response.text.strip()}")
        else:
            print("⚠️  生成请求成功但无文本回复")
            print(f"   响应对象: {response}")
            if hasattr(response, 'candidates'):
                print(f"   候选回复: {response.candidates}")
        print()
        
    except Exception as e:
        print(f"❌ 文本生成测试失败: {e}")
        print(f"   错误类型: {type(e)}")
        
        # 分析常见错误
        error_msg = str(e).lower()
        if "404" in error_msg:
            print("   💡 建议: 检查模型名称是否正确")
        elif "403" in error_msg:
            print("   💡 建议: 检查API密钥权限和配额")
        elif "invalid argument" in error_msg:
            print("   💡 建议: 检查请求参数格式")
        
        return False
    
    print("🎉 Gemini API 测试完成!")
    return True

async def test_ai_service():
    """测试AI服务集成"""
    print("\n🧪 测试AI服务集成...")
    
    try:
        from ai_service import AIService
        ai_service = AIService()
        
        # 测试角色回复
        response = await ai_service.get_character_response(
            "测试角色",
            "你是一个友善的测试角色，喜欢简短回复。",
            "你好",
            "这是一个测试环境。"
        )
        
        print(f"✅ AI服务测试成功!")
        print(f"   角色回复: {response}")
        
    except Exception as e:
        print(f"❌ AI服务测试失败: {e}")
        return False
    
    return True

async def main():
    """主函数"""
    success = test_gemini_api()
    
    if success:
        await test_ai_service()
        print("\n🎉 所有测试通过! 您可以开始游戏了。")
    else:
        print("\n⚠️  请解决上述问题后重新测试。")

if __name__ == "__main__":
    asyncio.run(main())

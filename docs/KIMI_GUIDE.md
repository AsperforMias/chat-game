# Kimi API 配置指南

## 🌙 如何获取Kimi API密钥

1. **访问官网**: 打开 [https://platform.moonshot.cn/](https://platform.moonshot.cn/)

2. **注册/登录**: 
   - 如果没有账户，请先注册
   - 如果已有账户，直接登录

3. **获取API密钥**:
   - 登录后进入控制台
   - 找到 "API密钥" 或 "API Keys" 选项
   - 创建新的API密钥
   - 复制生成的密钥（通常以 `sk-` 开头）

4. **充值余额**:
   - 确保账户有足够余额使用API
   - 在控制台充值页面进行充值

## ⚙️ 配置游戏

在 `config.py` 文件中设置：

```python
# AI提供商配置
AI_PROVIDER = "kimi"
API_KEY = "sk-your-actual-kimi-api-key"  # 替换为您的真实密钥
MODEL = "moonshot-v1-8k"  # 或 moonshot-v1-32k, moonshot-v1-128k
```

## 📋 Kimi 模型选择

- **moonshot-v1-8k**: 8K上下文，适合日常对话
- **moonshot-v1-32k**: 32K上下文，适合长文档处理  
- **moonshot-v1-128k**: 128K上下文，适合超长文本

## 🧪 测试配置

配置完成后运行测试：

```bash
python test_ai.py
```

## 🎮 开始游戏

配置无误后运行游戏：

```bash
python main.py
```

## ⚠️ 常见问题

### API密钥无效 (401错误)
- 检查密钥是否正确复制
- 确保密钥没有过期
- 验证账户是否正常

### 配额不足 (quota错误)  
- 检查账户余额
- 确认API调用次数未超限

### 模型不存在 (404错误)
- 确认模型名称拼写正确
- 使用推荐的模型名称

## 💡 优势特点

- **中文优化**: Kimi对中文理解和生成能力很强
- **长上下文**: 支持超长对话历史
- **成本合理**: 相比国外API服务更经济
- **响应速度**: 国内访问速度较快

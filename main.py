from openai import OpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL
)


# =====================================
# 1. 初始化 API 客户端
# =====================================

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)


# =====================================
# 2. 发送 API 请求
# =====================================

response = client.chat.completions.create(

    model=DEEPSEEK_MODEL,

    messages=[
        {
            "role": "system",
            "content": "你是一名专业的 Python 编程助手。"
        },
        {
            "role": "user",
            "content": "请用中文解释什么是transform架构。"
        }
    ],

    stream=False,

    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)


# =====================================
# 3. 获取模型回答
# =====================================

answer = response.choices[0].message.content

print("\nDeepSeek 回答：\n")
print(answer)


# =====================================
# 4. 查看 Token 使用情况
# =====================================

print("\nToken 使用情况：")
print("输入 Token：", response.usage.prompt_tokens)
print("输出 Token：", response.usage.completion_tokens)
print("总 Token：", response.usage.total_tokens)


import gradio as gr
from openai import OpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL
)


# ==================================================
# 1. 初始化 DeepSeek API 客户端
# ==================================================

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    timeout=60.0
)


# ==================================================
# 2. 定义聊天处理函数
# ==================================================

def chat(message, history):

    # 初始化系统提示词
    messages = [
        {
            "role": "system",
            "content": "你是一名专业、友好的 AI 助手，请使用中文回答。"
        }
    ]

    # 加入历史对话
    for item in history:

        role = item.get("role")
        content = item.get("content")

        if role in ("user", "assistant") and isinstance(content, str):
            messages.append({
                "role": role,
                "content": content
            })

    # 加入当前用户问题
    messages.append({
        "role": "user",
        "content": message
    })

    try:
        # 调用 DeepSeek API
        response = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=messages,
            stream=False
        )

        # 提取模型回答
        answer = response.choices[0].message.content

        return answer or "模型没有返回文本，请重试。"

    except Exception as e:

        print("API 调用失败:", type(e).__name__, str(e))

        return f"API 调用失败：{type(e).__name__}，请检查配置或网络。"


# ==================================================
# 3. 创建 Gradio 聊天界面
# ==================================================

demo = gr.ChatInterface(
    fn=chat,
    title="DeepSeek AI Assistant",
    description="基于 DeepSeek API 构建的智能对话助手。",
    examples=[
        "请解释卷积神经网络的工作原理。",
        "什么是 Transformer？",
        "介绍一下 Agent 的开发流程。",
        "帮我写一个 Python 文件读取程序。"
    ],
    textbox=gr.Textbox(
        placeholder="请输入你的问题……",
        container=True
    )
)


# ==================================================
# 4. 启动 Web 服务
# ==================================================

if __name__ == "__main__":

    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=True,
        inbrowser=True
    )

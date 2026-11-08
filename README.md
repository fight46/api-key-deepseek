
# DeepSeek API Learning Project

基于 Python、DeepSeek API 和 Gradio 构建的 AI Chat WebUI。

本项目从零实现 DeepSeek API 接入、API Key 安全管理，以及基于 Gradio 的 Web 聊天界面。

## 1. Project Introduction

本项目主要用于学习和实践：

- Python 项目环境管理
- API Key 配置与安全管理
- OpenAI Python SDK
- DeepSeek API 调用
- Gradio WebUI 开发
- HTTP 代理与公网分享

## 2. Features

- DeepSeek API integration
- Environment variable management
- Secure API Key configuration
- Chat interface with Gradio
- Multi-turn conversation history
- Gradio public sharing

## 3. Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| DeepSeek API | Large language model |
| OpenAI SDK | API client |
| Gradio | Web UI |
| python-dotenv | Environment configuration |
| HTTPX | HTTP communication |

## 4. Project Structure

```text
api-key-deepseek/
│
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── config.py
├── main.py
└── app.py
```

## 5. Installation

### Step 1: Clone repository

```bash
git clone YOUR_REPOSITORY_URL
cd api-key-deepseek
```

### Step 2: Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure API Key

Create a `.env` file in the project root directory.

Configure:

```env
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=your_supported_model
```

请使用 DeepSeek 官方文档中当前支持的模型名称。

### Step 5: Run the application

```bash
python app.py
```

Open your browser:

http://127.0.0.1:7860

## 6. Security

- Never commit your real `.env` file.
- Never expose your API Key in frontend code.
- Keep API credentials on the backend.
- Configure authentication before public deployment.

## 7. Future Improvements

- Streaming responses
- User authentication
- Conversation management
- API usage statistics
- FastAPI backend
- Docker deployment
- Agent and MCP integration

## 8. License

MIT


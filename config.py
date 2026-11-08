import os
from pathlib import Path
from dotenv import load_dotenv


# 1. 获取当前文件所在目录
BASE_DIR = Path(__file__).resolve().parent

# 2. 加载项目根目录下的 .env 文件
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# 3. 读取环境变量
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

DEEPSEEK_BASE_URL = os.getenv(
    "DEEPSEEK_BASE_URL",
    "https://api.deepseek.com"
)

DEEPSEEK_MODEL = os.getenv(
    "DEEPSEEK_MODEL",
    "deepseek-flash"
)

# 4. 检查必要配置
if not DEEPSEEK_API_KEY:
    raise ValueError("缺少 DEEPSEEK_API_KEY，请检查 .env 文件")

if not DEEPSEEK_BASE_URL:
    raise ValueError("缺少 DEEPSEEK_BASE_URL")

if not DEEPSEEK_MODEL:
    raise ValueError("缺少 DEEPSEEK_MODEL")

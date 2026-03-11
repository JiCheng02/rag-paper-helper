import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
API_KEY = os.getenv('API_KEY')

# 模型配置
MODEL_CONFIG = {
    "model": "Qwen/Qwen3-8B",
    "model_provider": "openai",
    "base_url": "https://api.siliconflow.cn/v1",
    "temperature": 0.0
}

# 嵌入模型配置
EMBEDDING_CONFIG = {
    "base_url": "https://api.siliconflow.cn/v1",
    "model": "BAAI/bge-m3"
}

# 文本切分配置
TEXT_SPLIT_CONFIG = {
    "chunk_size": 500,
    "chunk_overlap": 50,
    "separators": ["\n\n", "\n", "。", "!", "?", " "]
}

# 路径配置
PDF_DIR = "./docs"
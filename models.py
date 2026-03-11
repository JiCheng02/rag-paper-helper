from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import init_chat_model
from config import MODEL_CONFIG,EMBEDDING_CONFIG

def init_llm_model(api_key: str):
    """初始化大语言模型"""
    if not api_key:
        raise ValueError("API_KEY未配置,请检查.env文件")
    return init_chat_model(
        MODEL_CONFIG["model"],
        model_provider=MODEL_CONFIG["model_provider"],
        base_url=MODEL_CONFIG["base_url"],
        api_key= api_key,
        temperature=MODEL_CONFIG["temperature"]
)

def init_embedding_model(api_key: str) -> OpenAIEmbeddings:
    """初始化嵌入模型"""
    return OpenAIEmbeddings(
        base_url=EMBEDDING_CONFIG["base_url"],
        api_key=api_key,
        model=EMBEDDING_CONFIG["model"]
    )
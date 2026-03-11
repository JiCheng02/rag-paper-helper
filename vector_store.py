from typing import List
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def build_vector_store(doc_chunks: List[Document], embeddings: OpenAIEmbeddings) -> FAISS:
    """构建FAISS向量库"""
    vector_store = FAISS.from_documents(doc_chunks, embeddings)
    print("√ 向量库构建完成！")
    return vector_store


def get_retriever(vector_store: FAISS, k: int = 5) -> object:
    """获取检索器"""
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )


def format_retrieved_docs(docs: List[Document]) -> str:
    """格式化检索到的文档"""
    return "\n\n".join([f"文档{i+1}:\n{doc.page_content}" for i, doc in enumerate(docs)])
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from vector_store import get_retriever,format_retrieved_docs

def build_rag_chain(model: object, vector_store: FAISS) -> object:
    """构建完整的RAG问答链"""
    retriever = get_retriever(vector_store)
    
    prompt_template = ChatPromptTemplate.from_template("""
    你是一个论文阅读助手，请基于上下文回答问题。
    上下文:{context}
    
    问题:{question}
    要求：
    1. 仅基于上下文回答，不要编造任何不在上下文中的信息；
    2. 回答要准确、简洁，只保留核心信息，避免冗余铺垫。
    
    答案:""")
    
    rag_chain = (
        {"context": retriever | format_retrieved_docs, "question": RunnablePassthrough()}
        | prompt_template
        | model
        | StrOutputParser()
    )
    return rag_chain
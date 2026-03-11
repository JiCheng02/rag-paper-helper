import os
from typing import List

from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import TEXT_SPLIT_CONFIG


def load_and_split_pdfs(pdf_dir: str) -> List[Document]:
    """加载并切分PDF"""
    if not os.path.exists(pdf_dir):
        raise FileNotFoundError(f"PDF目录不存在: {pdf_dir}")
    
    loader = DirectoryLoader(
        path=pdf_dir,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )
    documents = loader.load()
    
    if not documents:
        print("知识库为空！")
        return []
    
    print(f"√ 加载完成！总计{len(documents)}页PDF内容")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=TEXT_SPLIT_CONFIG["chunk_size"],
        chunk_overlap=TEXT_SPLIT_CONFIG["chunk_overlap"],
        separators=TEXT_SPLIT_CONFIG["separators"]
    )
    pdf_chunks = text_splitter.split_documents(documents)
    return pdf_chunks


from config import API_KEY, PDF_DIR
from document import load_and_split_pdfs
from models import init_embedding_model, init_llm_model
from rag_chain import build_rag_chain
from vector_store import build_vector_store


def main():
    """主函数：循环问答"""
    try:
        # 初始化模型
        print("🔧 正在初始化模型...")
        llm_model = init_llm_model(API_KEY)
        embedding_model = init_embedding_model(API_KEY)
        
        # 加载PDF
        print("\n📄 正在加载PDF文档...")
        pdf_chunks = load_and_split_pdfs(PDF_DIR)
        
        # 构建向量库
        print("\n🧠 正在构建向量库...")
        vector_store = build_vector_store(pdf_chunks, embedding_model)
        
        # 构建RAG链
        rag_chain = build_rag_chain(llm_model, vector_store)
        
        # 循环问答
        print("\n=====================================")
        print("🎉 RAG论文阅读助手已就绪！")
        print("💡 输入/quit可退出程序")
        print("=====================================\n")
        
        while True:
            question = input("请输入问题(输入/quit以结束程序)：").strip()
            if question == "/quit":
                print("\n👋 程序已结束，感谢使用！")
                break
            if not question:
                print("⚠️  问题不能为空，请重新输入！")
                continue
            try:
                print(f"\n🔍 正在检索并生成回答...")
                answer = rag_chain.invoke(question)
                print(f"📝 回答：{answer}\n")
            except Exception as e:
                print(f"❌ 回答生成失败：{str(e)}\n")
    
    except Exception as e:
        print(f"\n❌ 程序初始化出错：{str(e)}")


if __name__ == "__main__":
    main()
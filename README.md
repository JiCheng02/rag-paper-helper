# rag-paper-helper
基于检索增强生成 (RAG) 的论文阅读助手，支持 PDF 文档加载、向量库构建，通过 Qwen3-8B 模型基于文档内容精准回答问题


### 快速开始
1. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 修改.env.example文件：
   ```bash
   mv .env.example .env
   ```
3. 编辑 `.env` 文件，将其中的 `api_key` 替换为[硅基流动](https://siliconflow.cn/)密钥。
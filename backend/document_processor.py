# backend/document_processor.py
import os
import hashlib
from typing import List
from langchain_community.document_loaders import UnstructuredMarkdownLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

DOCUMENTS_DIR = "./knowledge_base"  # 存放你笔记的目录
CHROMA_PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "my_notes_collection"

# 1. 确保你有 DashScope 的 API Key (在 .env 文件中)
embedding_model = DashScopeEmbeddings()


# --- 辅助函数：计算文件哈希，用于去重[cite: 6] ---
def calculate_file_hash(file_path: str) -> str:
    """计算文件的 MD5 哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# --- 步骤 1: 读取所有 Markdown 文档[cite: 6] ---
def load_all_documents(directory: str) -> List[Document]:
    all_docs = []
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在，请创建并放入文档。")
        return all_docs

    for root, _, files in os.walk(directory):
        for file in files:
            # 你的笔记主要是 Markdown[cite: 3, 4, 9]
            if file.endswith(('.md', '.txt')):
                file_path = os.path.join(root, file)
                print(f"正在加载: {file_path}")
                try:
                    # 使用对应的加载器[cite: 6]
                    if file.endswith('.md'):
                        loader = UnstructuredMarkdownLoader(file_path)
                    else:
                        loader = TextLoader(file_path, encoding='utf-8')

                    documents = loader.load()
                    # 为每个文档添加哈希值和来源信息[cite: 6]
                    for doc in documents:
                        doc.metadata["source"] = file
                        doc.metadata["file_hash"] = calculate_file_hash(file_path)
                    all_docs.extend(documents)
                except Exception as e:
                    print(f"加载文件失败 {file_path}: {e}")
    return all_docs


# --- 步骤 2: 文档分割[cite: 6] ---
def split_documents(documents: List[Document]) -> List[Document]:
    """将文档切分为适合嵌入的块"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # 每个块大约 500 字符[cite: 6]
        chunk_overlap=50,  # 重叠 50 字符保持上下文[cite: 6]
        separators=["\n## ", "\n# ", "\n\n", "\n", "。", "！", "？", " ", ""],  # 针对 Markdown 优化
        length_function=len,
    )
    return text_splitter.split_documents(documents)


# --- 步骤 3: 存入向量数据库 (Chroma)[cite: 6] ---
def build_or_update_vectorstore():
    raw_documents = load_all_documents(DOCUMENTS_DIR)
    if not raw_documents:
        print("没有找到文档，请检查目录。")
        return

    print(f"共加载 {len(raw_documents)} 个原始文档对象。")
    split_docs = split_documents(raw_documents)
    print(f"分割后得到 {len(split_docs)} 个文本块。")

    # 判断向量库是否已存在[cite: 6]
    if os.path.exists(CHROMA_PERSIST_DIR) and os.listdir(CHROMA_PERSIST_DIR):
        print("向量库已存在，检查更新...")
        vectorstore = Chroma(
            persist_directory=CHROMA_PERSIST_DIR,
            embedding_function=embedding_model,
            collection_name=COLLECTION_NAME
        )

        # 获取已有哈希进行去重[cite: 6]
        existing_data = vectorstore.get(include=["metadatas"])
        existing_hashes = set()
        if existing_data and existing_data["metadatas"]:
            for meta in existing_data["metadatas"]:
                if meta and "file_hash" in meta:
                    existing_hashes.add(meta["file_hash"])

        new_docs = [doc for doc in split_docs if doc.metadata.get("file_hash") not in existing_hashes]

        if new_docs:
            vectorstore.add_documents(new_docs)
            print(f"已向现有库中添加 {len(new_docs)} 个新文本块。")
        else:
            print("没有新内容需要添加。")

    else:
        print("创建新的向量库...")
        vectorstore = Chroma.from_documents(
            documents=split_docs,
            embedding=embedding_model,
            collection_name=COLLECTION_NAME,
            persist_directory=CHROMA_PERSIST_DIR
        )
        print("向量库创建完成。")


if __name__ == "__main__":
    build_or_update_vectorstore()
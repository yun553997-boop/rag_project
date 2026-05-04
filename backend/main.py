# backend/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# LangChain 核心与扩展组件[cite: 6, 11]
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 加载环境变量 (需要 DASHSCOPE_API_KEY)
load_dotenv()

app = FastAPI(title="个人知识库 RAG API")

# 1. 配置 CORS：允许跨域请求
# 这是前后端分离的必经之路，允许你的 Vue 项目 (比如运行在 5173 端口) 访问这个 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发阶段允许所有源，实际部署时建议改为 Vue 部署的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 初始化模型与检索器[cite: 6]
# 确保你已经跑过前面的脚本，生成了 chroma_db 文件夹
llm = ChatTongyi(model="qwen-plus")  # 使用千问 plus 模型[cite: 6]
embedding_model = DashScopeEmbeddings()

CHROMA_PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "my_notes_collection"
CHAT_HISTORY_DIR = "./chat_histories"

os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)

# 加载本地 Chroma 向量库[cite: 6]
vectorstore = Chroma(
    persist_directory=CHROMA_PERSIST_DIR,
    embedding_function=embedding_model,
    collection_name=COLLECTION_NAME
)
# 将向量库包装为检索器，每次返回 k=4 个相关片段[cite: 6]
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 3. 构造 RAG 提示词与 LCEL 链[cite: 6]
system_prompt = """你是一个专业的知识问答助手。请严格基于以下【上下文】信息回答【问题】。
如果上下文中没有相关信息，请直接说“我知识库中暂时没有相关信息”，不要自己编造答案。
【上下文】：
{context}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),  # 注入历史对话[cite: 6]
    ("human", "{question}")
])


def format_docs(docs):
    """将检索到的多个 Document 对象拼接成一个大字符串[cite: 6]"""
    return "\n\n".join(doc.page_content for doc in docs)


# 声明式组合 LCEL 链[cite: 6]
rag_chain = (
        {
            "context": (lambda x: x["question"]) | retriever | format_docs,
            "question": lambda x: x["question"],
            "history": lambda x: x["history"]
        }
        | prompt
        | llm
        | StrOutputParser()  # 提取纯文本[cite: 6]
)


# 4. 组装历史记忆[cite: 6]
def get_session_history(session_id: str) -> FileChatMessageHistory:
    """使用本地文件存储会话记忆，替代数据库[cite: 6]"""
    file_path = os.path.join(CHAT_HISTORY_DIR, f"{session_id}.json")
    return FileChatMessageHistory(file_path)


chain_with_history = RunnableWithMessageHistory(
    runnable=rag_chain,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)


# 5. 定义前端请求体模型
class ChatRequest(BaseModel):
    session_id: str
    query: str


# 6. 定义接口
@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    """
    核心问答接口。
    采用 StreamingResponse 返回流式数据，为前端的“打字机效果”提供支持。
    """

    async def generate():
        config = {"configurable": {"session_id": request.session_id}}
        # 调用 stream 方法逐块生成回答[cite: 6]
        for chunk in chain_with_history.stream({"question": request.query}, config=config):
            yield chunk

    # media_type 设置为 text/event-stream，契合 Server-Sent Events (SSE) 规范
    return StreamingResponse(generate(), media_type="text/event-stream")


@app.get("/api/ping")
async def ping():
    """用于前端测试前后端连通性"""
    return {"message": "pong! API 服务运行正常 🟢"}
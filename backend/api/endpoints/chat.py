# 聊天与测试接口
import os
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# 导入原来的 LangChain 组件
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

router = APIRouter()

# --- 暂时保留原来的模型与链初始化代码 ---
llm = ChatTongyi(model="qwen-plus", streaming=True)
embedding_model = DashScopeEmbeddings()
CHROMA_PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "my_notes_collection"
CHAT_HISTORY_DIR = "./chat_histories"

vectorstore = Chroma(
    persist_directory=CHROMA_PERSIST_DIR,
    embedding_function=embedding_model,
    collection_name=COLLECTION_NAME
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

system_prompt = """你是一个专业的知识问答助手。请严格基于以下【上下文】信息回答【问题】。
如果上下文中没有相关信息，请直接说“我知识库中暂时没有相关信息”，不要编造。
【上下文】：\n{context}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": (lambda x: x["question"]) | retriever | format_docs,
        "question": lambda x: x["question"],
        "history": lambda x: x["history"]
    }
    | prompt | llm | StrOutputParser()
)

def get_session_history(session_id: str) -> FileChatMessageHistory:
    file_path = os.path.join(CHAT_HISTORY_DIR, f"{session_id}.json")
    return FileChatMessageHistory(file_path)

chain_with_history = RunnableWithMessageHistory(
    runnable=rag_chain,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)
# ----------------------------------

class ChatRequest(BaseModel):
    session_id: str
    query: str

@router.get("/ping")
async def ping():
    return {"message": "pong! API 服务运行正常 🟢"}

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    async def generate():
        config = {"configurable": {"session_id": request.session_id}}
        async for chunk in chain_with_history.astream({"question": request.query}, config=config):
            yield chunk
    return StreamingResponse(generate(), media_type="text/event-stream")
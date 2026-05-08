# 路由汇总文件
from fastapi import APIRouter
from api.endpoints import chat, document

api_router = APIRouter()

# 注册子路由 (这样写能保证前端原有的 /api/chat, /api/upload 路径完全不变)
api_router.include_router(chat.router, tags=["Chat 对话模块"])
api_router.include_router(document.router, tags=["Document 文档模块"])
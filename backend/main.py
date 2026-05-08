# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router
from core.config import settings

# 使用 core/config.py 中的全局配置
app = FastAPI(title=settings.PROJECT_NAME)

# 1. 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 挂载所有 API 路由
# 这里统一加上 /api 前缀，里面的接口就会变成 /api/chat, /api/upload 等
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
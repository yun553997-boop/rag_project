from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 初始化 FastAPI 应用
app = FastAPI(
    title="AI Study Copilot API",
    description="AI 辅助学习工作站后端接口",
    version="1.0.0"
)

# 配置 CORS (跨域资源共享)
# 这非常重要，因为前端 (Vue) 和后端 (FastAPI) 本地开发时通常在不同的端口
# 必须允许跨域，前端才能调得通后端的接口
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（开发环境下方便，生产环境需限制）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法 (GET, POST 等)
    allow_headers=["*"],  # 允许所有请求头
)

# 定义一个基础的 GET 路由，用于测试服务是否存活 (Health Check)
@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to AI Study Copilot API! 🚀",
        "docs_url": "/docs"  # 提示查看 API 文档的地址
    }



# 环境变量与全局配置加载
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 项目基本信息
    PROJECT_NAME: str = "RAG Fullstack Assistant"

    # 数据库配置 (优先从 .env 读取，如果没有则使用默认值)
    DATABASE_URL: str = "postgresql+asyncpg://rag_user:rag_password@postgres:5432/rag_db"

    # 大模型 API Key
    DASHSCOPE_API_KEY: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"  # 忽略多余的环境变量


# 实例化全局配置对象
settings = Settings()
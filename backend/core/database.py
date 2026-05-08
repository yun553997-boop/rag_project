#数据库连接池与会话管理
# backend/core/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from core.config import settings

# 1. 创建异步引擎
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # 生产环境建议设为 False，避免打印过多 SQL 日志
    pool_size=10,
    max_overflow=20,
)

# 2. 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# 3. 定义声明式基类
class Base(DeclarativeBase):
    pass

# 4. 获取数据库会话的依赖函数 (供 FastAPI 路由层使用)
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
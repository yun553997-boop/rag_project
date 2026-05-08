# backend/models/__init__.py
from core.database import Base
from models.document import Document
from models.chat import ChatSession, ChatMessage

# 暴露出 Base 供 Alembic 使用
__all__ = ["Base", "Document", "ChatSession", "ChatMessage"]
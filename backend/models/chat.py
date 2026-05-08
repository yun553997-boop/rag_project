# 这里设计了主从表：ChatSession 是会话主题，ChatMessage 是每一条对话记录
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    # 使用前端生成的字符串作为 ID
    id: Mapped[str] = mapped_column(String(100), primary_key=True, index=True, comment="会话ID")
    title: Mapped[str] = mapped_column(String(255), default="新会话", comment="会话标题")
    create_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="创建时间"
    )

    # 定义与消息表的一对多关系，级联删除
    messages = relationship("ChatMessage", back_populates="session", cascade="all, delete-orphan")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment="消息ID")
    session_id: Mapped[str] = mapped_column(ForeignKey("chat_sessions.id", ondelete="CASCADE"), index=True)
    role: Mapped[str] = mapped_column(String(20), comment="角色 (user 或 ai)")
    content: Mapped[str] = mapped_column(Text, comment="消息内容")
    create_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="产生时间"
    )

    # 反向关联
    session = relationship("ChatSession", back_populates="messages")
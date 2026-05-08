# backend/models/document.py
from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, comment="主键ID")
    filename: Mapped[str] = mapped_column(String(255), index=True, comment="文件名")
    file_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True, comment="文件哈希去重")
    upload_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="上传时间"
    )
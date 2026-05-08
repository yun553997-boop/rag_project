# 这个文件处理 chat_sessions（会话列表）和 chat_messages（具体的聊天消息记录）
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.chat import ChatSession, ChatMessage

# ================= 会话管理 (Session) =================
async def create_chat_session(db: AsyncSession, session_id: str, title: str = "新会话"):
    """创建一个新的聊天会话"""
    db_session = ChatSession(id=session_id, title=title)
    db.add(db_session)
    await db.commit()
    await db.refresh(db_session)
    return db_session

async def get_session_by_id(db: AsyncSession, session_id: str):
    """获取指定的会话信息"""
    result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
    return result.scalar_one_or_none()

async def get_all_sessions(db: AsyncSession):
    """获取所有历史会话列表 (按时间倒序，最新的在上面)"""
    result = await db.execute(select(ChatSession).order_by(ChatSession.create_time.desc()))
    return result.scalars().all()

async def delete_session(db: AsyncSession, session_id: str):
    """删除指定会话 (借助模型的 cascade 级联属性，会自动删除该会话下的所有消息)"""
    session = await get_session_by_id(db, session_id)
    if session:
        await db.delete(session)
        await db.commit()
        return True
    return False


# ================= 消息记录 (Messages) =================
async def create_chat_message(db: AsyncSession, session_id: str, role: str, content: str):
    """保存一条新的聊天消息"""
    db_message = ChatMessage(session_id=session_id, role=role, content=content)
    db.add(db_message)
    await db.commit()
    await db.refresh(db_message)
    return db_message

async def get_messages_by_session(db: AsyncSession, session_id: str):
    """获取指定会话下的所有历史消息 (按时间正序，最早的在上面)"""
    result = await db.execute(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.create_time.asc())
    )
    return result.scalars().all()
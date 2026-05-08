# 这个文件专门处理对 documents 表的增删改查
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.document import Document

async def create_document(db: AsyncSession, filename: str, file_hash: str):
    """新增一条文档记录"""
    db_document = Document(filename=filename, file_hash=file_hash)
    db.add(db_document)
    await db.commit()
    await db.refresh(db_document)
    return db_document

async def get_document_by_hash(db: AsyncSession, file_hash: str):
    """通过哈希值查找文档（用于判断是否重复上传）"""
    result = await db.execute(select(Document).where(Document.file_hash == file_hash))
    return result.scalar_one_or_none()

async def get_all_documents(db: AsyncSession):
    """获取所有已上传的文档列表"""
    result = await db.execute(select(Document).order_by(Document.upload_time.desc()))
    return result.scalars().all()

async def delete_document(db: AsyncSession, document_id: int):
    """删除指定的文档记录"""
    result = await db.execute(select(Document).where(Document.id == document_id))
    document = result.scalar_one_or_none()
    if document:
        await db.delete(document)
        await db.commit()
        return True
    return False
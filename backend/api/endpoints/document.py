# backend/api/endpoints/document.py
import os
import shutil
from fastapi import APIRouter, UploadFile, File
from document_processor import DOCUMENTS_DIR, build_or_update_vectorstore

# 创建当前模块的路由实例
router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """处理文件上传并入库"""
    try:
        os.makedirs(DOCUMENTS_DIR, exist_ok=True)
        file_path = os.path.join(DOCUMENTS_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 触发知识库更新
        build_or_update_vectorstore()

        return {"message": f"文件 {file.filename} 上传并入库成功！🚀"}
    except Exception as e:
        return {"error": f"上传处理失败: {str(e)}"}
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, UploadFile, File, Query

router = APIRouter(tags=["Ответы"])


@router.post(
    "/questions/{id}/answers/",
    summary="Добавить ответ к вопросу",
)
async def add_answer():
    pass

@router.get(
    "/answers/{id}",
    summary="Получить конкретный ответ",
)
async def get_answer_by_id():
    pass

@router.delete(
    "/answers/{id}",
    summary="Удалить ответ"
)
async def delete_answer():
    pass
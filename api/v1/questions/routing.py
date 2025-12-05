from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, UploadFile, File, Query

router = APIRouter(tags=["Вопросы"])


@router.get(
    "/questions",
    summary="Список всех вопросов",
)
async def get_all_questions():
    pass

@router.post(
    "/questions",
    summary="Создать новый вопрос",
)
async def create_question():
    pass

@router.get(
    "/questions/{id}",
    summary="Получить вопрос и все ответы на него"
)
async def get_question_answers():
    pass

@router.delete(
    "/questions/{id}",
    summary="Удалить вопрос (вместе с ответами)"
)
async def delete_question_cascade():
    pass

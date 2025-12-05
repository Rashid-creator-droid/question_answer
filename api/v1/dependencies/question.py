from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.repositories.question import QuestionRepository
from core.db_helper import db_helper
from models import Question


async def get_question_by_id(
    question_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Question:
    question = await QuestionRepository().get_with_answers(session, question_id)
    if not question:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Вопрос не найден")
    return question
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.repositories.answer import AnswerRepository
from core.db_helper import db_helper

from models import Answer


async def get_answer_by_id(
    answer_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Answer:
    answer = await AnswerRepository().get_by_id(session, answer_id)
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ответ не найден"
        )
    return answer
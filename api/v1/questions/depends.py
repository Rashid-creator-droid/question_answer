from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from core.db_helper import db_helper
from models import Question


async def get_question_by_id(
    question_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Question:
    result = await session.execute(
        select(Question)
        .options(selectinload(Question.answers))
        .where(Question.id == question_id)
    )
    question = result.scalars().first()
    if not question:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Вопрос не найден")
    return question
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.db_helper import db_helper
from models import Answer


async def get_answer_by_id(
    answer_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
) -> Answer:
    result = await session.execute(select(Answer).where(Answer.id == answer_id))
    answer = result.scalars().first()
    if not answer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Ответ не найден")
    return answer

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Question
from .base import BaseRepository


class QuestionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Question)

    @staticmethod
    async def get_with_answers(session: AsyncSession, question_id: int) -> Question | None:
        result = await session.execute(
            select(Question)
            .options(selectinload(Question.answers))
            .where(Question.id == question_id)
        )
        return result.scalars().first()

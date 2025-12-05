from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseRepository
from models import Question
from sqlalchemy.orm import selectinload
from sqlalchemy import select


class QuestionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Question)

    async def get_with_answers(self, session: AsyncSession, question_id: int) -> Question | None:
        result = await session.execute(
            select(Question)
            .options(selectinload(Question.answers))
            .where(Question.id == question_id)
        )
        return result.scalars().first()

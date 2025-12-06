from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Answer
from .base import BaseRepository


class AnswerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Answer)

    @staticmethod
    async def get_by_id(session: AsyncSession, answer_id: int) -> Answer | None:
        result = await session.execute(select(Answer).where(Answer.id == answer_id))
        return result.scalars().first()
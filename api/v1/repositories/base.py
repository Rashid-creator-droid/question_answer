from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, model):
        self.model = model

    async def create(self, session: AsyncSession, **kwargs):
        obj = self.model(**kwargs)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    @staticmethod
    async def delete(session: AsyncSession, obj):
        await session.delete(obj)
        await session.commit()

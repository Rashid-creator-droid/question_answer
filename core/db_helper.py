from asyncio import current_task

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from models.users import User
from .config import settings, logger


class DatabaseHelper:

    def __init__(self, url: str, echo: bool = False):
        logger.info(f"Инициализация подключения к базе Postgres")
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
        logger.info("Движок и фабрика сессий созданы")

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        logger.info("Создана scoped сессия")
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            logger.info("Создана новая сессия (dependency)")
            yield session
            logger.info("Сессия закрыта (dependency)")

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        logger.info("Начата scoped сессия (dependency)")
        yield session
        logger.info("Scoped сессия завершена")

    async def get_user_db(self) -> AsyncSession:
        async with self.session_factory() as session:
            logger.info("Создан SQLAlchemyUserDatabase")
            yield SQLAlchemyUserDatabase(session, User)
            logger.info("SQLAlchemyUserDatabase завершён")


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)

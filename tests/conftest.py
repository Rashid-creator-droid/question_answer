import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool
from faker import Faker

from main import app
from models import Base, User
from core.config import settings
from core.db_helper import db_helper
from core.auth import get_current_user


@pytest.fixture(scope="session")
def faker():
    return Faker()

@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(
        settings.db_url,
        echo=False,
        future=True,
        poolclass=NullPool,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield engine
    await engine.dispose()

@pytest.fixture(scope="function")
async def db_session(engine):
    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        yield session
        await session.rollback()

@pytest.fixture(scope="function")
async def test_user(db_session, faker):
    plain_password = "password123"
    hashed_password = "aboba_pass"

    user = User(
        email=faker.unique.email(),
        username=faker.unique.user_name(),
        hashed_password=hashed_password,
        is_active=True,
        is_verified=True,
        is_superuser=False,
    )

    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    user.plain_password = plain_password
    return user

@pytest.fixture(scope="function")
async def async_client(db_session: AsyncSession, test_user: User):
    async def get_session_override():
        yield db_session

    async def current_user_override():
        return test_user

    app.dependency_overrides[db_helper.session_dependency] = get_session_override
    app.dependency_overrides[get_current_user] = current_user_override

    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client

    app.dependency_overrides.clear()

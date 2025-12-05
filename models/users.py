from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, TIMESTAMP, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import Base

if TYPE_CHECKING:
    from models.answers import Answer
    from models.questions import Question


class User(SQLAlchemyBaseUserTable[int], Base):
    """User model"""

    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    registered_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.utcnow
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    questions: Mapped[list["Question"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    answers: Mapped[list["Answer"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.repositories.question import QuestionRepository
from api.v1.schemas.question import QuestionCreate

from models import User, Question


question_repo = QuestionRepository()

async def create_question_service(session: AsyncSession, quest_data: QuestionCreate, user: User) -> Question:
    question = await question_repo.create(
        session,
        text=quest_data.text,
        user_id=user.id,
    )
    return question

async def delete_question_service(session: AsyncSession, question: Question, user: User):
    if question.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Нельзя удалить чужой вопрос",
        )
    await question_repo.delete(session, question)

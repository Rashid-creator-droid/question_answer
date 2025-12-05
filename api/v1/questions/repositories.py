from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from models import Question, User
from api.v1.questions.schemas import QuestionCreate


async def create_question_service(
    session: AsyncSession, question_data: QuestionCreate, user: User
) -> Question:
    new_question = Question(text=question_data.text, user_id=user.id)
    session.add(new_question)
    await session.commit()
    await session.refresh(new_question)
    return new_question


async def delete_question_service(session: AsyncSession, question: Question, user: User):
    if question.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не можете удалить этот вопрос, так как вы не являетесь автором",
        )
    await session.delete(question)
    await session.commit()
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.repositories.answer import AnswerRepository
from api.v1.schemas.answer import AnswerCreate
from models import Answer, Question, User


answer_repo = AnswerRepository()

async def create_answer_service(
    session: AsyncSession, question: Question, answer_data: AnswerCreate, user: User
) -> Answer:
    answer = await answer_repo.create(
        session,
        text=answer_data.text,
        question_id=question.id,
        user_id=user.id,
    )
    return answer

async def delete_answer_service(session: AsyncSession, answer: Answer, user: User):
    if answer.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не можете удалить этот ответ, так как вы не являетесь автором",
        )
    await answer_repo.delete(session, answer)

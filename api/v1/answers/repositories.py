from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

from models import Answer, Question, User
from api.v1.answers.schemas import AnswerCreate


async def create_answer_service(
    session: AsyncSession, question: Question, answer_data: AnswerCreate, user: User
) -> Answer:
    new_answer = Answer(text=answer_data.text, question_id=question.id, user_id=user.id)
    session.add(new_answer)
    await session.commit()
    await session.refresh(new_answer)
    return new_answer


async def get_answer_service(session: AsyncSession, answer_id: int) -> Answer:
    result = await session.execute(select(Answer).where(Answer.id == answer_id))
    answer = result.scalars().first()
    if not answer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Ответ не найден")
    return answer



async def delete_answer_service(session: AsyncSession, answer: Answer, user: User):
    if answer.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не можете удалить этот ответ, так как вы не являетесь автором",
        )
    await session.delete(answer)
    await session.commit()
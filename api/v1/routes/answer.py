from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.v1.dependencies.answer import get_answer_by_id
from api.v1.services.answer import create_answer_service, delete_answer_service
from api.v1.schemas.answer import AnswerCreate, AnswerRead
from api.v1.dependencies.question import get_question_by_id
from core.auth import get_current_user
from core.db_helper import db_helper
from models import Answer, Question, User


router = APIRouter(tags=["Ответы"])


@router.post("/questions/{question_id}/answers/", response_model=AnswerRead, summary="Создать овет")
async def create_answer(
    question: Question = Depends(get_question_by_id),
    answer: AnswerCreate = ...,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await create_answer_service(session, question, answer, current_user)


@router.get("/answers/{answer_id}", response_model=AnswerRead, summary="Получить ответ с ID")
async def get_answer(answer: Answer = Depends(get_answer_by_id)):
    return answer


@router.delete("/answers/{answer_id}", status_code=204, summary="Удалить ответ с  ID")
async def delete_answer(
    answer: Answer = Depends(get_answer_by_id),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await delete_answer_service(session, answer, current_user)
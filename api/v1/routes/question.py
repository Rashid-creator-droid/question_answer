from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.v1.dependencies.question import get_question_by_id
from api.v1.services.question import create_question_service, delete_question_service
from core.config import logger
from core.db_helper import db_helper
from core.auth import get_current_user
from models import User, Question
from api.v1.schemas.question import QuestionRead, QuestionReadWithAnswers, QuestionCreate


router = APIRouter(prefix="/questions", tags=["Вопросы"])

@router.get("/", response_model=list[QuestionRead], summary="Получить все вопросы")
async def list_questions(session: AsyncSession = Depends(db_helper.session_dependency)):
    result = await session.execute(select(Question))
    questions = result.scalars().all()
    logger.info(f"Получен список всех вопросов, всего {len(questions)}")
    return questions


@router.post("/", response_model=QuestionRead, status_code=status.HTTP_201_CREATED, summary="Создать вопрос")
async def create_question(
    question: QuestionCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    new_question = await create_question_service(session, question, current_user)
    logger.info(f"Создан вопрос id={new_question.id} пользователем id={current_user.id}")
    return new_question


@router.get("/{question_id}", response_model=QuestionReadWithAnswers, summary="Получить вопрос по ID")
async def get_question(
    question: Question = Depends(get_question_by_id)
):
    logger.info(f"Получен вопрос id={question.id} пользователем")
    return QuestionReadWithAnswers.from_orm(question)


@router.delete("/{question_id}", status_code=204, summary="Удалить вопрос с ID")
async def delete_question(
    question: Question = Depends(get_question_by_id),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await delete_question_service(session, question, current_user)
    logger.info(f"Удалён вопрос id={question.id} пользователем id={current_user.id}")
from fastapi import APIRouter

from .questions.routing import router as questions_router
from .answers.routing import router as answers_router

router = APIRouter(prefix="/v1")
router.include_router(router=questions_router)
router.include_router(router=answers_router)
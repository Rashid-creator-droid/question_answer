from fastapi import APIRouter

from api.v1.routes.answer import router as answers_router
from api.v1.routes.question import router as questions_router

router = APIRouter(prefix="/v1")
router.include_router(router=questions_router)
router.include_router(router=answers_router)
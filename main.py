import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1 import router as router_v1
from api.v1.schemas.user import UserRead, UserCreate, UserUpdate
from core.auth import auth_backend, fastapi_users
from core.config import settings


app = FastAPI(
    title="Тестовое задание вопрос-ответы",
    description="Создание вопросов, ответы на них",
    openapi_url="/vq/openapi.json",
    docs_url="/docs/v1",
    version="v1",
)

app.include_router(
    router=router_v1,
    prefix=settings.api_prefix,
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["Аутентификация"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["Аутентификация"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/api/users",
    tags=["Пользователь"],
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
import uvicorn
from fastapi import FastAPI, Depends
from api.v1 import router as router_v1


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
    dependencies=[Depends(current_user)]
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
@app.get("/")
def hello_index():
    return  {
        "message": "Hello index",
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
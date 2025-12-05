from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class AnswerCreate(BaseModel):
    text: str

    @field_validator("text", mode="before")
    def text_must_not_be_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Текст вопроса не может быть пустым")
        return v


class AnswerRead(BaseModel):
    id: int
    text: str
    user_id: int
    question_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
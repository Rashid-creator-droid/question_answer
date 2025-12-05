from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import List

from api.v1.schemas.answer import AnswerRead


class QuestionCreate(BaseModel):
    text: str

    @field_validator("text", mode="before")
    def text_must_not_be_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Текст вопроса не может быть пустым")
        return v


class QuestionRead(BaseModel):
    id: int
    text: str
    created_at: datetime


class QuestionReadWithAnswers(QuestionRead):
    answers: List[AnswerRead] = []

    model_config = {
        "from_attributes": True
    }
from datetime import datetime
from pydantic import BaseModel
from typing import List

from api.v1.answers.schemas import AnswerRead


class QuestionCreate(BaseModel):
    text: str

class QuestionRead(BaseModel):
    id: int
    text: str
    created_at: datetime

class QuestionReadWithAnswers(QuestionRead):
    answers: List[AnswerRead] = []

    model_config = {
        "from_attributes": True
    }
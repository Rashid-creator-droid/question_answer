from datetime import datetime
from pydantic import BaseModel

class AnswerCreate(BaseModel):
    text: str

class AnswerRead(BaseModel):
    id: int
    text: str
    user_id: int
    question_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
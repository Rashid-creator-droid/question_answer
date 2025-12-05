from pydantic import  BaseModel
from datetime import datetime


class Answers(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

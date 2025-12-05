from pydantic import BaseModel
from datetime import datetime


class Questions(BaseModel):
    id: int
    text: str
    created_at: datetime
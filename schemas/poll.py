from pydantic import BaseModel
from typing import Optional

class Poll(BaseModel):
    id: Optional[int] = None
    title: str
    description: str

class Question(BaseModel):
    id: Optional[int] = None
    poll_id: int
    question_number: int
    text: str

class Answer(BaseModel):
    id: Optional[int] = None
    question_id: int
    answer_number: int
    answer_text: str
    votes: int = 0


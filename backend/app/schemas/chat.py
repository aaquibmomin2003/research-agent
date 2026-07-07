from pydantic import BaseModel
from typing import List


class Source(BaseModel):
    file: str
    score: float


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source] = []
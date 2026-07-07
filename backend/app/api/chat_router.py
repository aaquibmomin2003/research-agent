from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_chat_service
from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    answer = chat_service.chat(request.question)

    return ChatResponse(
        answer=answer,
        sources=[],
    )
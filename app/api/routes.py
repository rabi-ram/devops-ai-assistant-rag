from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import rag_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = rag_service.ask(request.question)

    return ChatResponse(**response)

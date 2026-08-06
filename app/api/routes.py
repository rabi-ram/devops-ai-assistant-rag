from uuid import uuid4

from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import rag_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    conversation_id = request.conversation_id or str(uuid4())

    response = rag_service.ask(
        conversation_id=conversation_id,
        question=request.question,
    )

    return ChatResponse(
        conversation_id=conversation_id,
        answer=response["answer"],
        sources=response["sources"],
    )

    
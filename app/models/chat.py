from typing import Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for chat endpoint.
    """

    conversation_id: Optional[str] = Field(
        default=None,
        description="Conversation ID. If omitted, a new conversation will be created.",
    )

    question: str = Field(
        ...,
        description="User question.",
    )


class Source(BaseModel):
    """
    Source document information returned with the answer.
    """

    file: str
    page: int


class ChatResponse(BaseModel):
    """
    Response returned by the chat endpoint.
    """

    conversation_id: str

    answer: str

    sources: list[Source]
    
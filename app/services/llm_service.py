from langchain_ollama import ChatOllama

from app.core.config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)


class LLMService:
    """
    Service responsible for communicating with the LLM.
    """

    def __init__(self):
        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.2,
        )

    def ask(self, question: str) -> str:
        """
        Send a question to the LLM and return the response.
        """
        response = self.llm.invoke(question)

        return response.content


llm_service = LLMService()

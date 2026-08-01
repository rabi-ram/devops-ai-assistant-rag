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

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the LLM and return the generated response.
        """
        response = self.llm.invoke(prompt)

        return response.content


llm_service = LLMService()

import time

from langchain_ollama import ChatOllama

from app.core.config import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
    LLM_TEMPERATURE,
)
from app.utils.logger import logger


class LLMService:
    """
    Service responsible for communicating with the LLM.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
             temperature=LLM_TEMPERATURE,
        )

    def ask(self, prompt: str) -> str:

        logger.info(
            "Calling Ollama model: %s",
            OLLAMA_MODEL,
        )

        start = time.perf_counter()

        response = self.llm.invoke(prompt)

        elapsed = time.perf_counter() - start

        logger.info(
            "LLM response time: %.2f seconds",
            elapsed,
        )

        logger.info("Received response from Ollama")

        return response.content


llm_service = LLMService()

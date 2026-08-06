from pathlib import Path

from fastapi import HTTPException

from app.prompts.rag_prompt import rag_prompt
from app.services.conversation_service import conversation_service
from app.services.llm_service import llm_service
from app.services.retrieval_service import retrieval_service
from app.utils.logger import logger


class RAGService:
    """
    Combines retrieval, conversation history,
    and LLM generation.
    """

    def ask(
        self,
        conversation_id: str,
        question: str,
    ):

        try:

            logger.info(
                "Conversation=%s Question=%s",
                conversation_id,
                question,
            )

            docs = retrieval_service.retrieve(question)

            logger.info(
                "Retrieved %d documents",
                len(docs),
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            history = conversation_service.get_history(
                conversation_id
            )

            prompt = rag_prompt.format(
                history=history,
                context=context,
                question=question,
            )

            logger.info("Calling LLM")

            answer = llm_service.ask(prompt)

            conversation_service.add_message(
                conversation_id,
                question,
                answer,
            )

            logger.info(
                "Conversation updated"
            )

            sources = []

            for doc in docs:

                sources.append(
                    {
                        "file": Path(
                            doc.metadata["source"]
                        ).name,
                        "page": doc.metadata.get(
                            "page",
                            0,
                        )
                        + 1,
                    }
                )

            return {
                "answer": answer,
                "sources": sources,
            }

        except Exception:

            logger.exception("RAG failed")

            raise HTTPException(
                status_code=500,
                detail="Unable to process request.",
            )


rag_service = RAGService()

from pathlib import Path

from app.prompts.rag_prompt import rag_prompt
from app.services.llm_service import llm_service
from app.services.retrieval_service import retrieval_service


class RAGService:
    """
    Combines retrieval and generation.
    """

    def ask(self, question: str):

        docs = retrieval_service.retrieve(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = rag_prompt.format(
            context=context,
            question=question,
        )

        answer = llm_service.ask(prompt)

        sources = []

        for doc in docs:

            sources.append(
                {
                    "file": Path(doc.metadata["source"]).name,
                    "page": doc.metadata.get("page", 0) + 1,
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }


rag_service = RAGService()

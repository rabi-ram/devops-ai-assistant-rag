from app.services.llm_service import llm_service
from app.vectorstore.chroma_store import chroma_store


class RAGService:
    """
    Combines retrieval and generation.
    """

    def ask(self, question: str):

        docs = chroma_store.similarity_search(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are an expert DevOps AI assistant.

Answer the user's question using ONLY the context below.

If the answer is not found in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

        return llm_service.ask(prompt)


rag_service = RAGService()

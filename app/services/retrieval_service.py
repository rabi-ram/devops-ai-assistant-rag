from app.core.config import TOP_K
from app.vectorstore.chroma_store import chroma_store
from app.utils.logger import logger


class RetrievalService:
    """
    Handles retrieval of relevant document chunks.
    """

    def retrieve(self, question: str, k: int = TOP_K):

        logger.info("Searching ChromaDB (k=%d)", k)

        retriever = chroma_store.as_retriever(k)

        results = retriever.invoke(question)

        logger.info(
            "Retrieved %d document chunks",
            len(results),
        )

        return results

    def retrieve_with_score(self, question: str, k: int = TOP_K):

        logger.info(
            "Searching ChromaDB with similarity scores (k=%d)",
            k,
        )

        results = chroma_store.similarity_search_with_score(
            query=question,
            k=k,
        )

        filtered_docs = []

        for document, score in results:

            if score < 0.80:
                filtered_docs.append(document)

        logger.info(
            "Filtered %d relevant chunks",
            len(filtered_docs),
        )

        return filtered_docs


retrieval_service = RetrievalService()

from app.vectorstore.chroma_store import chroma_store


class RetrievalService:
    """
    Handles retrieval of relevant document chunks from ChromaDB.
    """

    def retrieve(self, question: str, k: int = 5):
        """
        Retrieve relevant document chunks using a LangChain Retriever.
        """

        retriever = chroma_store.as_retriever(k)

        return retriever.invoke(question)

    def retrieve_with_score(self, question: str, k: int = 5):
        """
        Retrieve the top-k relevant document chunks and filter
        out low-quality matches based on distance score.
        """

        results = chroma_store.similarity_search_with_score(
            query=question,
            k=k,
        )

        filtered_docs = []

        for document, score in results:

            # Lower score = better match
            if score < 0.80:
                filtered_docs.append(document)

        return filtered_docs


retrieval_service = RetrievalService()

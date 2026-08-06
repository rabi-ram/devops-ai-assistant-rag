from langchain_chroma import Chroma

from app.services.embedding_service import embedding_service


class ChromaStore:
    """
    Handles interaction with the Chroma vector database.
    """

    def __init__(self):
        self.vectorstore = Chroma(
            collection_name="devops-ai-knowledge",
            embedding_function=embedding_service.get_embeddings(),
            persist_directory="data/chroma",
        )

    def add_documents(self, documents):
        self.vectorstore.add_documents(documents)


    def similarity_search(self, query, k=5):
        """
        Retrieve the most relevant document chunks.
        """
        return self.vectorstore.similarity_search(
            query=query,
            k=k,
        )


    def similarity_search_with_score(self, query, k=5):
        """
        Retrieve the most relevant document chunks along with their similarity scores.
        """
        return self.vectorstore.similarity_search_with_score(
            query=query,
            k=k,
        )

    def reset(self):
        """
        Delete all documents from the collection.

        Useful during development when rebuilding the vector database.
        """
        self.vectorstore.delete_collection()

        self.vectorstore = Chroma(
            collection_name="devops-ai-knowledge",
            embedding_function=embedding_service.get_embeddings(),
            persist_directory="data/chroma",
        )

    def as_retriever(self, k=5):
        """
        Return a LangChain retriever.
        """
        return self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

chroma_store = ChromaStore()

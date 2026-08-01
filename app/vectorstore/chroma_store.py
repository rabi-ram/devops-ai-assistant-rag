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

    def similarity_search(self, query, k=3):
        return self.vectorstore.similarity_search(query, k=k)


chroma_store = ChromaStore()

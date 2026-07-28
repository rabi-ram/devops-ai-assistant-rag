from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingService:
    """
    Generates vector embeddings for documents.
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def get_embeddings(self):
        return self.embeddings


embedding_service = EmbeddingService()

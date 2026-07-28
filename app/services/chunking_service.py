from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingService:
    """
    Splits documents into smaller chunks for embedding.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )

    def split_documents(self, documents):
        return self.splitter.split_documents(documents)


chunking_service = ChunkingService()

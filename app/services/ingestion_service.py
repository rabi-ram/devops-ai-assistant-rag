from pathlib import Path

from app.loaders.pdf_loader import document_loader
from app.services.chunking_service import chunking_service
from app.vectorstore.chroma_store import chroma_store


class IngestionService:
    """
    Loads documents and stores them in Chroma.
    """

    def ingest_directory(self, directory: str):

        directory = Path(directory)

        for file in directory.iterdir():

            if file.is_file():

                documents = document_loader.load(str(file))

                chunks = chunking_service.split_documents(documents)

                chroma_store.add_documents(chunks)

                print(f"Ingested {file.name} ({len(chunks)} chunks)")


ingestion_service = IngestionService()

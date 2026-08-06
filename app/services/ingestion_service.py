from pathlib import Path

from app.loaders.pdf_loader import document_loader
from app.services.chunking_service import chunking_service
from app.vectorstore.chroma_store import chroma_store
from app.utils.logger import logger


class IngestionService:
    """
    Loads documents, splits them into chunks,
    and stores them in ChromaDB.
    """

    def ingest_file(self, file_path: str):

        path = Path(file_path)

        logger.info("Processing file: %s", path.name)

        documents = document_loader.load(str(path))

        logger.info("Loaded %d pages", len(documents))

        chunks = chunking_service.split_documents(documents)

        logger.info("Created %d chunks", len(chunks))

        chroma_store.add_documents(chunks)

        logger.info("Stored vectors in ChromaDB")

        return len(chunks)

    def ingest_directory(self, directory: str, reset_db=False):

        if reset_db:

            logger.info("Resetting Chroma database")

            chroma_store.reset()

        directory = Path(directory)

        total_files = 0
        total_chunks = 0

        logger.info("Starting document ingestion")

        for file in sorted(directory.iterdir()):

            if not file.is_file():
                continue

            chunks = self.ingest_file(file)

            total_files += 1
            total_chunks += chunks

        logger.info(
            "Ingestion completed | Files=%d Chunks=%d",
            total_files,
            total_chunks,
        )


ingestion_service = IngestionService()

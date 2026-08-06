from pathlib import Path

from app.loaders.pdf_loader import document_loader
from app.services.chunking_service import chunking_service
from app.vectorstore.chroma_store import chroma_store


class IngestionService:
    """
    Loads documents, splits them into chunks,
    and stores them in ChromaDB.
    """

    def ingest_file(self, file_path: str):

        path = Path(file_path)

        print(f"\nProcessing: {path.name}")

        documents = document_loader.load(str(path))

        chunks = chunking_service.split_documents(documents)

        chroma_store.add_documents(chunks)

        print(f"Pages Loaded  : {len(documents)}")
        print(f"Chunks Created: {len(chunks)}")

        return len(chunks)

    def ingest_directory(self, directory: str, reset_db=False):

        if reset_db:
            print("\nResetting Chroma database...\n")
            chroma_store.reset()

        directory = Path(directory)

        total_files = 0
        total_chunks = 0

        print("=" * 60)
        print("Starting document ingestion")
        print("=" * 60)

        for file in sorted(directory.iterdir()):

            if not file.is_file():
                continue

            chunks = self.ingest_file(file)

            total_files += 1
            total_chunks += chunks

        print("\n" + "=" * 60)
        print("Ingestion Summary")
        print("=" * 60)

        print(f"Files Processed : {total_files}")
        print(f"Total Chunks    : {total_chunks}")

        print("=" * 60)


ingestion_service = IngestionService()

from app.loaders.pdf_loader import document_loader
from app.services.chunking_service import chunking_service

documents = document_loader.load("data/documents/kubernetes.txt")

chunks = chunking_service.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(chunk.page_content)
    
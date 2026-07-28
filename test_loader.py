from app.loaders.pdf_loader import document_loader

documents = document_loader.load("data/documents/kubernetes.txt")

print(documents)

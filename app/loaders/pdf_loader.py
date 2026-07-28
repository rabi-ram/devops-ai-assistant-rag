from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)


class DocumentLoader:
    """
    Loads documents from the data/documents directory.
    """

    def load(self, file_path: str):
        path = Path(file_path)

        if path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(file_path)

        elif path.suffix.lower() == ".txt":
            loader = TextLoader(file_path)

        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")

        return loader.load()


document_loader = DocumentLoader()

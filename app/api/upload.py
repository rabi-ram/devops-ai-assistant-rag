from pathlib import Path
import shutil

from fastapi import APIRouter, File, UploadFile

from app.services.ingestion_service import ingestion_service

router = APIRouter()

DOCUMENT_DIR = Path("data/documents")


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    destination = DOCUMENT_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingestion_service.ingest_file(destination)

    return {
        "message": f"{file.filename} uploaded successfully.",
        "chunks_created": chunks,
    }

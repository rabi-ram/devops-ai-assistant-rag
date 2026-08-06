from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.ingestion_service import ingestion_service
from app.utils.logger import logger

router = APIRouter()

DOCUMENT_DIR = Path("data/documents")


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    try:

        logger.info("Uploading file: %s", file.filename)

        destination = DOCUMENT_DIR / file.filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        chunks = ingestion_service.ingest_file(destination)

        logger.info(
            "Successfully indexed %s (%d chunks)",
            file.filename,
            chunks,
        )

        return {
            "message": f"{file.filename} uploaded successfully.",
            "chunks_created": chunks,
        }

    except Exception:

        logger.exception("Failed to upload document")

        raise HTTPException(
            status_code=500,
            detail="Document upload failed.",
        )

        
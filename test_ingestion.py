from app.services.ingestion_service import ingestion_service

ingestion_service.ingest_directory(
    "data/documents",
    reset_db=True
)

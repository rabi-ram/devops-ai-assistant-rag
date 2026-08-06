from fastapi import FastAPI

from app.api.routes import router
from app.api.upload import router as upload_router
from app.core.config import APP_NAME
from app.utils.logger import logger

app = FastAPI(title=APP_NAME)


@app.on_event("startup")
async def startup():

    logger.info("Application started")


@app.on_event("shutdown")
async def shutdown():

    logger.info("Application stopped")


@app.get("/")
def home():

    logger.info("Home endpoint called")

    return {
        "message": f"Welcome to {APP_NAME}!"
    }


@app.get("/health")
def health():

    logger.info("Health endpoint called")

    return {
        "status": "healthy"
    }


app.include_router(
    router,
    prefix="/api/v1",
    tags=["Chat"],
)

app.include_router(
    upload_router,
    prefix="/api/v1",
    tags=["Upload"],
)

    
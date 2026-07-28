from fastapi import FastAPI

from app.api.routes import router
from app.core.config import APP_NAME

app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME}!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    router,
    prefix="/api/v1",
    tags=["Chat"],
)


    
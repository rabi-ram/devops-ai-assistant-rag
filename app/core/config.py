from dotenv import load_dotenv
import os

load_dotenv()

# Application
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

# Ollama
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))

# Retrieval
TOP_K = int(os.getenv("TOP_K", "5"))

# ChromaDB
CHROMA_COLLECTION = os.getenv(
    "CHROMA_COLLECTION",
    "devops-ai-knowledge",
)

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "data/chroma",
)

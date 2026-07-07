from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
        "vector_store": "ready",
        "llm": "ollama",
    }
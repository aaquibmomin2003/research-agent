from llama_index.embeddings.huggingface import (
    HuggingFaceEmbedding,
)

from app.core.config import settings


_embedding = None


def get_embedding():

    global _embedding

    if _embedding is None:

        _embedding = HuggingFaceEmbedding(

            model_name=settings.EMBED_MODEL

        )

    return _embedding
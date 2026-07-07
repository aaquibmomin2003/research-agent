import chromadb

from llama_index.vector_stores.chroma import (
    ChromaVectorStore,
)

from app.core.config import settings


_vector_store = None


def get_vector_store():

    global _vector_store

    if _vector_store is None:

        client = chromadb.PersistentClient(

            path=settings.CHROMA_PATH

        )

        collection = client.get_or_create_collection(

            "documents"

        )

        _vector_store = ChromaVectorStore(

            chroma_collection=collection

        )

    return _vector_store
"""
LlamaIndex Ingestion Pipeline

This module creates a singleton ingestion pipeline responsible for:

1. Splitting documents into chunks
2. Generating embeddings
3. Storing vectors in ChromaDB
"""

from functools import lru_cache

from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

from app.rag.embedding import get_embedding
from app.rag.vector_store import get_vector_store


@lru_cache(maxsize=1)
def get_ingestion_pipeline() -> IngestionPipeline:
    """
    Returns a singleton LlamaIndex ingestion pipeline.

    The pipeline:
    - Splits documents into chunks
    - Generates embeddings
    - Stores embeddings inside ChromaDB
    """

    return IngestionPipeline(
        transformations=[
            SentenceSplitter(
                chunk_size=512,
                chunk_overlap=50,
            ),
            get_embedding(),
        ],
        vector_store=get_vector_store(),
    )
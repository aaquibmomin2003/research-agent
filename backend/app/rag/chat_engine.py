from functools import lru_cache

from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama

from app.core.config import settings
from app.rag.embedding import get_embedding
from app.rag.vector_store import get_vector_store


@lru_cache(maxsize=1)
def get_chat_engine():

    llm = Ollama(
        model=settings.OLLAMA_MODEL,
        request_timeout=300,
        context_window=2048,
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store=get_vector_store(),
        embed_model=get_embedding(),
    )

    return index.as_query_engine(
        llm=llm,
        similarity_top_k=5,
        response_mode="compact",
    )
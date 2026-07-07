from llama_index.core import VectorStoreIndex

from app.rag.embedding import get_embedding

from app.rag.vector_store import (
    get_vector_store,
)


_index = None


def get_index():

    global _index

    if _index is None:

        _index = VectorStoreIndex.from_vector_store(

            vector_store=get_vector_store(),

            embed_model=get_embedding(),

        )

    return _index
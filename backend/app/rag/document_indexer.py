from pathlib import Path

from llama_index.core import SimpleDirectoryReader

from app.rag.ingestion import get_ingestion_pipeline


class DocumentIndexer:
    def __init__(self):
        self.pipeline = get_ingestion_pipeline()

    async def index_file(self, file_path: str) -> int:
        """
        Read a document, split it into nodes,
        generate embeddings, and store them in ChromaDB.

        Returns:
            Number of indexed chunks.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {path}"
            )

        documents = SimpleDirectoryReader(
            input_files=[path]
        ).load_data()

        nodes = await self.pipeline.arun(
            documents=documents
        )

        return len(nodes)
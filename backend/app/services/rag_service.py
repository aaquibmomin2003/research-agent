from pathlib import Path

from llama_index.core import SimpleDirectoryReader

from app.core.logger import logger
from app.rag.chat_engine import get_chat_engine
from app.rag.ingestion import get_ingestion_pipeline


class RAGService:

    @property
    def pipeline(self):
        return get_ingestion_pipeline()

    @property
    def chat_engine(self):
        return get_chat_engine()

    async def ingest(self, file_path: str):

        logger.info(f"Indexing {file_path}")

        docs = SimpleDirectoryReader(
            input_files=[Path(file_path)]
        ).load_data()

        nodes = await self.pipeline.arun(
            documents=docs,
        )

        logger.info(f"Indexed {len(nodes)} chunks")

        return len(nodes)

    def ask(self, question: str):

        logger.info(f"Question: {question}")

        response = self.chat_engine.query(question)

        return str(response)
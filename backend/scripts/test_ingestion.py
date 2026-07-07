import asyncio
from pathlib import Path

from app.rag.document_indexer import DocumentIndexer


async def main():
    storage = Path("storage/documents")

    pdfs = list(storage.glob("*.pdf"))

    if not pdfs:
        raise FileNotFoundError(
            "No PDF found in storage/documents"
        )

    file_path = pdfs[0]

    print(f"Indexing: {file_path.name}")

    indexer = DocumentIndexer()

    chunks = await indexer.index_file(str(file_path))

    print(f"Indexed {chunks} chunks")


if __name__ == "__main__":
    asyncio.run(main())
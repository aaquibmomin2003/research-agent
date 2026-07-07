from app.services.rag_service import RAGService


class ChatService:

    def __init__(
        self,
        rag: RAGService | None = None,
    ):

        self.rag = rag or RAGService()

    def chat(
        self,
        question: str,
    ) -> str:

        return self.rag.ask(question)
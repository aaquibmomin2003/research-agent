import asyncio

from app.rag.query_engine import get_query_engine


async def main():

    engine = get_query_engine()

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        response = engine.query(question)

        print("\nAssistant:\n")

        print(response)


if __name__ == "__main__":

    asyncio.run(main())
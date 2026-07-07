from fastapi import FastAPI
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def exception_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(exc),
            },
        )
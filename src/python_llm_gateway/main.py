from fastapi import FastAPI

from python_llm_gateway.api.router import api_router
from python_llm_gateway.core.config import get_app_settings


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application instance.
    """

    app_settings = get_app_settings()

    fastapi_app = FastAPI(
        title=app_settings.app_name,
        version="0.1.0",
    )

    fastapi_app.include_router(api_router)

    return fastapi_app


app = create_app()
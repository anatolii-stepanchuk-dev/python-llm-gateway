from typing import Annotated

from fastapi.params import Depends

from python_llm_gateway.core.config import AppSettings, get_app_settings
from python_llm_gateway.services.health_service import HealthService


def get_health_service(
    settings: Annotated[AppSettings, Depends(get_app_settings)],
) -> HealthService:
    """
    Create a health service for the current request.

    Args:
        settings: Application settings dependency.

    Returns:
        Health service instance.
    """

    return HealthService(app_settings=settings)

from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from python_llm_gateway.api.dependencies.health_dependencies import get_health_service
from python_llm_gateway.api.schemas.health_models import HealthResponse
from python_llm_gateway.services.health_service import HealthService

health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get("", response_model=HealthResponse)
async def get_health(
    health_service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    """
    Return application health status.

    Args:
        health_service: Service used to resolve health status.

    Returns:
        Current application health status.
    """

    return health_service.get_health()
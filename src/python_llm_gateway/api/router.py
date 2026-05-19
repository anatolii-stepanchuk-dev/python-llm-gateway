from fastapi import APIRouter

from python_llm_gateway.api.endpoints.health_endpoints import health_router

api_router = APIRouter()
api_router.include_router(health_router)
from python_llm_gateway.api.schemas.health_models import HealthResponse
from python_llm_gateway.core.config import AppSettings


class HealthService:
    """Service responsible for reporting application health."""

    def __init__(self, app_settings: AppSettings) -> None:
        """
        Initialize the health service.

        Args:
            app_settings: Application settings.
        """

        self._app_settings = app_settings

    def get_health(self) -> HealthResponse:
        """
        Return current application health.

        Returns:
            Health response with application status metadata.
        """

        return HealthResponse(
            app_name=self._app_settings.app_name,
            status="ok",
            environment=self._app_settings.app_env,
        )
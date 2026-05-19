from pydantic import BaseModel


class HealthResponse(BaseModel):
    """
    Response returned by the health endpoint.

    Attributes:
        app_name: Public application name.
        status: Current application status.
        environment: Runtime environment name.
    """

    app_name: str
    status: str
    environment: str
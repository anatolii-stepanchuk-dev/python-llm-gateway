from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Application configuration loaded from environment variables.

    Attributes:
        app_name: Public application name.
        app_env: Runtime environment name.
        log_level: Minimum application log level.
    """

    app_name: str = "python_llm_gateway"
    app_env: str = "local"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_app_settings() -> AppSettings:
    """
    Return cached application settings.

    Returns:
        Application settings loaded from environment variables and defaults.
    """

    return AppSettings()
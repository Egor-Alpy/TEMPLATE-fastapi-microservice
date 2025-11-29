from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentMode(str, Enum):
    """Режимы окружения приложения"""
    DEV = "DEV"
    PROD = "PROD"


class Settings(BaseSettings):
    """Конфигурация приложения с загрузкой из переменных окружения"""
    model_config = SettingsConfigDict(env_file="../.env")

    # Режим окружения
    ENV_MODE: EnvironmentMode = EnvironmentMode.DEV

    @property
    def is_production_mode(self) -> bool:
        """Проверка на production режим."""
        return self.ENV_MODE == EnvironmentMode.PROD

    @property
    def is_development_mode(self) -> bool:
        """Проверка на development режим."""
        return self.ENV_MODE == EnvironmentMode.DEV

    # Общие настройки
    PROJECT_NAME: str = "TEMPLATE FASTAPI SERVICE"
    PROJECT_DESCRIPTION: str = "by Alpy"
    PROJECT_VERSION: str = "0.0.0"

    # Настройка логирования
    LOG_LEVEL: str = "INFO"  # Доступные уровни логирования - DEBUG, INFO, WARNING, ERROR, FATAL
    LOG_FORMAT: str = "%(asctime).19s | %(levelname).3s | %(message)s"

    # Настройки FastAPI
    API_HOST: str = "localhost"
    API_PORT: int = 8000


settings = Settings()

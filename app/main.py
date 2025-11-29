
#      ___      __
#     /   |    / /  ____    __  __
#    / /| |   / /  / __ \  / / / /
#   / ___ |  / /  / /_/ / / /_/ /
#  /_/  |_| /_/  / .___/  \__, /
#              /_/      /____/

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core.logger import get_logger
from app.core.settings import settings

from app.api.router import router


logger = get_logger(name=__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения"""
    try:
        logger.info(f"🚀 Запуск {settings.PROJECT_NAME} сервиса...")
        logger.info(f" - Режим: {settings.ENV_MODE.upper()}")
        logger.info(f' - Уровень логирования: {settings.LOG_LEVEL}')

        if settings.is_production_mode:
            pass
        else:
            pass

        yield

    except Exception as e:
        logger.error(f"💥 Ошибка при запуске приложения: {e}")
        raise
    finally:
        logger.info("✅ Все соединения закрыты")


# Создание FastAPI приложения
app = FastAPI(
    title=f"{settings.PROJECT_NAME} API",
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        log_level="info"
    )

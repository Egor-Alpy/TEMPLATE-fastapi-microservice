from fastapi import APIRouter

from app.core.settings import settings

from app.api.v1 import router as v1_router


# Главный роутер приложения
router = APIRouter()

# Роутер для корневого эндпоинта
router_root = APIRouter(tags=['Root'])

@router_root.get("/", summary="Корневой эндпоинт")
async def root():
    """Корневой эндпоинт API"""
    return {
        "service": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "docs": "/docs",
        "status": "running"
    }

# Роутер для всех версий API
router_api = APIRouter(prefix="/api")
router_api.include_router(v1_router.api_router)

# Подключение всех роутеров
router.include_router(router_api)
router.include_router(router_root)

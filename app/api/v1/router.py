from fastapi import APIRouter

from app.api.v1.endpoints import health


api_router = APIRouter(prefix='/v1')

# Список всех роутеров версии v1
routers = [health.router]

# Подключение роутеров
for router in routers:
    api_router.include_router(router)

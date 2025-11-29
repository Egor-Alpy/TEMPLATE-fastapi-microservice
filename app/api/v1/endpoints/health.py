from fastapi import APIRouter


router = APIRouter(tags=['Monitoring'])

@router.get("/healthz")
async def health_check():
    """Проверка здоровья сервиса"""
    return {"status": "healthy"}

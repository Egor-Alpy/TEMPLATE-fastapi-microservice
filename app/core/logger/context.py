from contextvars import ContextVar
from typing import Optional

# Context variables для хранения идентификаторов
user_id_ctx: ContextVar[Optional[int]] = ContextVar('user_id', default=None)
company_id_ctx: ContextVar[Optional[int]] = ContextVar('company_id', default=None)
tender_id_ctx: ContextVar[Optional[int]] = ContextVar('tender_id', default=None)


def set_logging_context(
    user_id: Optional[int] = None,
    company_id: Optional[int] = None,
    tender_id: Optional[int] = None
) -> None:
    """Установить контекст для логирования"""
    if user_id is not None:
        user_id_ctx.set(user_id)
    if company_id is not None:
        company_id_ctx.set(company_id)
    if tender_id is not None:
        tender_id_ctx.set(tender_id)


def get_logging_prefix() -> str:
    """Получить префикс для логов из текущего контекста"""
    user_id = user_id_ctx.get()
    company_id = company_id_ctx.get()
    tender_id = tender_id_ctx.get()

    parts = []
    if user_id is not None:
        parts.append(f"USER_ID: {user_id}")
    if company_id is not None:
        parts.append(f"COMPANY_ID: {company_id}")
    if tender_id is not None:
        parts.append(f"TENDER_ID: {tender_id}")

    return " | ".join(parts) + (" | " if parts else "")


def clear_logging_context() -> None:
    """Очистить контекст логирования"""
    user_id_ctx.set(None)
    company_id_ctx.set(None)
    tender_id_ctx.set(None)
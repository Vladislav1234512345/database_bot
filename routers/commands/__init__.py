__all__ = ("router", )

from aiogram import Router

from .base_commands import router as base_commands_router
from .callback_commands import router as callback_commands_router
from .media_handlers import router as media_commands_router

router = Router(name=__name__)

router.include_routers(
    base_commands_router,
    callback_commands_router,
    media_commands_router,
)
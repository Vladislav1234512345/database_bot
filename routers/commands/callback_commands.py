from aiogram import Router, F, types

from routers.keyboards.action_keyboard import RegisterCallbackData, RegisterAction, Log_inCallbackData, Log_inAction
from config import access

router = Router(name=__name__)


@router.callback_query(
    RegisterCallbackData.filter(F.action == RegisterAction.register)
)
async def register_button_handle(callback_query: types.CallbackQuery):
    access.register = True
    await callback_query.message.edit_text(
        text="Create the new login:",
    )

@router.callback_query(
    Log_inCallbackData.filter(F.action == Log_inAction.log_in)
)
async def log_in_button_handle(callback_query: types.CallbackQuery):
    access.login = True
    await callback_query.message.edit_text(
        text="Enter your login:",
    )

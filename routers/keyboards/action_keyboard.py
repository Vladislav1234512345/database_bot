from enum import Enum, IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

class StartAction:
    register = "Register"
    log_in = "Log in"
class RegisterAction(IntEnum):
    register = auto()

class Log_inAction(IntEnum):
    log_in = auto()

class RegisterCallbackData(CallbackData, prefix="register"):
    action: RegisterAction

class Log_inCallbackData(CallbackData, prefix="log_in"):
    action: Log_inAction

def start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text=StartAction.log_in,
    )
    builder.button(
        text=StartAction.register,
    )
    builder.adjust(1)
    return builder.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True,
    )
def register_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Start registration",
        callback_data=RegisterCallbackData(action=RegisterAction.register).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()

def log_in_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Log in account",
        callback_data=Log_inCallbackData(action=Log_inAction.log_in).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()
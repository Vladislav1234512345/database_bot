from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from config import user
from routers.keyboards.action_keyboard import register_keyboard, log_in_keyboard, start_keyboard, StartAction

router = Router(name=__name__)

@router.message(CommandStart())
async def start_handle(message: types.Message):
    user.empty()
    await message.answer(
        text=f"Hello. {message.from_user.full_name}!\n"
             "Click /help to read about this bot.",
        reply_markup=start_keyboard(),
    )

@router.message(Command("help"))
async def help_message(message: types.Message):
    user.empty()
    await message.answer(
        "/start - enable the Bot\n"
        "/help - read all about Bot\n"
        "/register - create a new account\n"
        "/login - log in your account"
    )

@router.message(F.text == StartAction.register)
@router.message(Command("register"))
async def register_handle(message: types.Message):
    await message.answer(
        text="You can register down below:",
        reply_markup=register_keyboard()
    )

@router.message(F.text == StartAction.log_in)
@router.message(Command("login"))
async def log_in_handle(message: types.Message):
    await message.answer(
        text="You can log in down below:",
        reply_markup=log_in_keyboard()
    )



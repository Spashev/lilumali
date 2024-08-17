from aiogram import types

from app.telebot.keyboards import budget_kb
from app.telebot import engine


async def handle_start(message: types.Message) -> None:
    await message.answer(
        text=f"Добро пожаловать, {message.from_user.full_name}!\nВас приветствует бот помощник. Выберите компанию.",
        reply_markup=budget_kb.get_keyboard(engine)
    )

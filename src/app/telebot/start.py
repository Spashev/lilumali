import sys
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.bot import DefaultBotProperties

from app.core.config import settings
from app.telebot.handlers import commands
from app.telebot.handlers import bot_router

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def set_handlers():
    dp.message.register(commands.handle_start, CommandStart())
    dp.include_router(bot_router)


async def run_aiogram_bot() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await set_handlers()
    await dp.start_polling(bot)

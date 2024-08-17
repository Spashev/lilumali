import os
from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from sqlalchemy import select

from app.models.budget import Company, Budget
from app.telebot import engine
from app.telebot.keyboards import budget_kb
from app.telebot.utils.chart import create_budget_chart

bot_router = Router()


@bot_router.message()
async def handle_message(message: types.Message) -> None:
    try:
        company_name = message.text
        with engine.connect() as connection:
            result = connection.execute(select(Budget).join(Company).filter(Company.name == company_name))
            budgets = result.all()

            if not budgets:
                await message.answer("No budget data found for this company.")
                return

            tmp_folder = 'tmp'
            os.makedirs(tmp_folder, exist_ok=True)
            file_path = os.path.join(tmp_folder, 'budget_chart.jpg')

            create_budget_chart(budgets, file_path)

            photo = types.FSInputFile(file_path)
            await message.reply_photo(photo=photo, caption="Here is your chart.")

            os.remove(file_path)

    except TelegramBadRequest as e:
        await message.answer(f"Bad request error: {e}")
    except TelegramForbiddenError as e:
        await message.answer(f"Permission error: {e}")
    except Exception as e:
        await message.answer(f"An unexpected error occurred: {e}")

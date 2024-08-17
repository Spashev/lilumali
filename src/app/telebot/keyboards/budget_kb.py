from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from sqlalchemy import select

from app.models.budget import Company


def get_keyboard(engine) -> ReplyKeyboardMarkup:
    with engine.connect() as connection:
        result = connection.execute(select(Company))
        companies = result.mappings().all()
        keyboards = [KeyboardButton(text=company.name) for company in companies]
        return ReplyKeyboardMarkup(
            keyboard=[
                keyboards
            ],
            resize_keyboard=True
        )

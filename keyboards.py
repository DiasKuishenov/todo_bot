from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/add"),
            KeyboardButton(text="/show")
        ],
        [
            KeyboardButton(text="/delete"),
            KeyboardButton(text="/clear")
        ]
    ],
    resize_keyboard=True
)
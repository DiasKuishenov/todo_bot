from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio

from config import TOKEN
from keyboards import main_keyboard

from handlers import (
    add_task,
    save_task,
    show_tasks,
    delete_task,
    confirm_delete,
    clear_tasks,
    TaskStates
)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Welcome to To-Do Bot",
        reply_markup=main_keyboard
    )


dp.message.register(
    add_task,
    Command("add")
)

dp.message.register(
    show_tasks,
    Command("show")
)

dp.message.register(
    delete_task,
    Command("delete")
)

dp.message.register(
    clear_tasks,
    Command("clear")
)

dp.message.register(
    save_task,
    TaskStates.waiting_for_task
)

dp.message.register(
    confirm_delete,
    TaskStates.waiting_for_delete
)


async def main():
    await dp.start_polling(
        bot
    )


if __name__ == "__main__":
    asyncio.run(
        main()
    )
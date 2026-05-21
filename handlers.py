from aiogram.types import Message
from task_manager import TaskManager

manager = TaskManager()


async def add_task(message: Message):
    text = message.text.replace("/add ", "")

    if text == "/add" or text.strip() == "":
        await message.answer(
            "❌ Use: /add your task"
        )
        return

    manager.add_task(
        message.from_user.id,
        text
    )

    await message.answer(
        "✅ Task added"
    )


async def show_tasks(message: Message):
    tasks = manager.show_tasks(message.from_user.id)

    if not tasks:
        await message.answer(
            "📭 No tasks"
        )
        return

    result = "📋 Your tasks:\n\n"

    for i, task in enumerate(tasks, start=1):
        result += f"{i}. {task}\n"

    await message.answer(result)


async def delete_task(message: Message):
    try:
        index = int(
            message.text.replace(
                "/delete ",
                ""
            )
        ) - 1

        deleted = manager.delete_task(
            message.from_user.id,
            index
        )

        if deleted:
            await message.answer(
                "🗑 Task deleted"
            )

        else:
            await message.answer(
                "❌ Task not found"
            )

    except:
        await message.answer(
            "❌ Use: /delete number"
        )


async def clear_tasks(message: Message):
    manager.clear_tasks(
        message.from_user.id
    )

    await message.answer(
        "🗑 All tasks deleted"
    )
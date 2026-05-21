from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from task_manager import TaskManager

manager = TaskManager()


class TaskStates(StatesGroup):
    waiting_for_task = State()
    waiting_for_delete = State()


async def add_task(message: Message, state: FSMContext):
    await message.answer(
        "📝 What task do you want to add?"
    )

    await state.set_state(
        TaskStates.waiting_for_task
    )


async def save_task(message: Message, state: FSMContext):
    manager.add_task(
        message.from_user.id,
        message.text
    )

    await message.answer(
        "✅ Task added"
    )

    await state.clear()


async def show_tasks(message: Message):
    tasks = manager.show_tasks(
        message.from_user.id
    )

    if not tasks:
        await message.answer(
            "📭 No tasks"
        )
        return

    result = "📋 Your tasks:\n\n"

    for i, task in enumerate(
            tasks,
            start=1
    ):
        result += f"{i}. {task}\n"

    await message.answer(
        result
    )


async def delete_task(message: Message, state: FSMContext):
    tasks = manager.show_tasks(
        message.from_user.id
    )

    if not tasks:
        await message.answer(
            "📭 No tasks"
        )
        return

    result = "📋 Your tasks:\n"

    for i, task in enumerate(
            tasks,
            start=1
    ):
        result += f"{i}. {task}\n"

    result += "\n🗑 Enter task number:"

    await message.answer(
        result
    )

    await state.set_state(
        TaskStates.waiting_for_delete
    )


async def confirm_delete(
        message: Message,
        state: FSMContext
):
    try:
        index = int(
            message.text
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
            "❌ Enter only number"
        )

    await state.clear()


async def clear_tasks(message: Message):
    manager.clear_tasks(
        message.from_user.id
    )

    await message.answer(
        "🗑 All tasks deleted"
    )
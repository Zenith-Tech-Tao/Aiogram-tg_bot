from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
import aiosqlite

bot = Router()

data_base = "projekt.sql"

# -------- СОСТОЯНИЕ --------
user_states = {}


# --------------------БАЗА ДАННЫХ ------------------------#
async def db_init():
    async with aiosqlite.connect(data_base) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS info
        (
        id INTEGER,
        name TEXT,
        name_habits TEXT,
        habits TEXT
        )
        """)
        await db.commit()


async def add_user(name, id):
    async with aiosqlite.connect(data_base) as db:
        await db.execute("""
        INSERT INTO info (name, id) VALUES (?,?)
        """, (name, id))
        await db.commit()


async def print_get_users():
    async with aiosqlite.connect(data_base) as db:
        cursor = await db.execute("""SELECT * FROM info""")
        rows = await cursor.fetchall()
        return rows


# --------------------КНОПКИ------------------------#
def buton_main_Inline():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Добавить', callback_data='add_habit'),
             InlineKeyboardButton(text='Список привычек', callback_data='info_habit')],
            [InlineKeyboardButton(text='Статистика', callback_data='stats')]
        ]
    )
    return keyboard


# --------------------КОМАНДЫ ------------------------#
@bot.message(Command('start'))
async def start(messsage: Message):
    try:
        name = messsage.from_user.username
        await messsage.answer(f"Добро пожаловать {name}! \n\n"
                              f'Это Telegram-бот “Личный трекер привычек”')
        await messsage.answer("Выберите действие ниже 👇",
                              reply_markup=buton_main_Inline())

        await add_user(name, messsage.from_user.id)

    except Exception as e:
        print("Ошибка:")
        print(e)


# --------------------ДОБАВЛЕНИЕ ПРИВЫЧКИ------------------------#
@bot.callback_query(lambda c: c.data == 'add_habit')
async def callback(callback):
    user_states[callback.from_user.id] = {"step": "name_habits"}

    await callback.message.answer("Введи название привычки:")
    await callback.answer()


@bot.message()
async def handle_message(message: Message):
    user_id = message.from_user.id

    if user_id not in user_states:
        return

    state = user_states[user_id]

    # 1 шаг
    if state["step"] == "name_habits":
        state["name_habits"] = message.text
        state["step"] = "habits"

        await message.answer("Теперь введи цель/описание привычки:")
        return

    # 2 шаг
    if state["step"] == "habits":
        name_habits = state["name_habits"]
        habits = message.text

        async with aiosqlite.connect(data_base) as db:
            await db.execute("""
            INSERT INTO info (id, name_habits, habits)
            VALUES (?, ?, ?)
            """, (user_id, name_habits, habits))
            await db.commit()

        await message.answer("Привычка добавлена ✅",
                             reply_markup=buton_main_Inline())

        del user_states[user_id]


# --------------------СПИСОК ПРИВЫЧЕК------------------------#
@bot.callback_query(lambda c: c.data == 'info_habit')
async def callback(callback):
    async with aiosqlite.connect(data_base) as db:
        cursor = await db.execute("""
        SELECT name_habits, habits FROM info WHERE id = ?
        """, (callback.from_user.id,))
        rows = await cursor.fetchall()

    if not rows:
        await callback.message.answer("У тебя нет привычек")
    else:
        text = "Твои привычки:\n\n"
        for r in rows:
            text += f"{r[0]} — {r[1]}\n"

        await callback.message.answer(text)

    await callback.answer()
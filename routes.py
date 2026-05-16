from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import aiosqlite

bot = Router()

DB = "test.sql"

async def db_init():
    async with aiosqlite.connect(DB) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users 
        (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
        )
        ''')
        await db.commit()


async def add_user(name, age):
    async with aiosqlite.connect(DB) as db:
        await db.execute('''
            INSERT INTO users (name, age) VALUES(?,?)
        ''', (name, age))
        await db.commit()


async def get_user():
    async with aiosqlite.connect(DB) as db:
        cursor = await db.execute('''SELECT * FROM users''')
        result = await cursor.fetchall()
        return result


@bot.message(Command("start"))
async def start(message: Message):
    await message.answer("Hi aiogram, /reg")


@bot.message(Command("reg"))
async def start(message: Message):
    await message.answer("Привет!\n"
                         "Пропишите команду: /reg AGE")
    delenie = message.text.strip().split()

    if len(delenie) != 2 or not delenie[1].isdigit():
        await message.answer("Ошибка")
        return

    await add_user(message.from_user.full_name, int(delenie[1]))
    await message.answer("Все готово!")


@bot.message(Command("users"))
async def start(message: Message):
    user = await get_user()

    if not user:
        await message.answer("В БД пусто!")
        return

    info = "Пользователей в БД:\n\n"

    for user_id, full_name, age in user:
        info += f"- {full_name} - {age}\n"

    await message.answer(info)
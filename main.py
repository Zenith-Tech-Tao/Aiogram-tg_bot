from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher
from routes import bot, db_init

TOKEN = TOKEN
dp = Dispatcher()
dp.include_router(bot)


async def main():
    await db_init()  # ← ЭТО БЫЛО КРИТИЧНО

    bot_instance = Bot(token=TOKEN)

    print("Запущен")
    await dp.start_polling(bot_instance)


if __name__ == "__main__":
    asyncio.run(main())
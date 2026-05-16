Token = "7754010897:AAGh0Z-31eh0svRMm7ieo8VGFQouzYkv5P0"

from aiogram import Router
from aiogram import Bot, Dispatcher
import aiohttp
import asyncio
from aiogram.filters import Command
from aiogram.types import Message



TOKEN = Token

dp = Dispatcher()
bot = Router()
dp.include_router(bot)




async def func():
    url = 'https://official-joke-api.appspot.com/random_joke'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as zapros:

            info = await zapros.json()
            return info




@bot.message(Command('joke'))
async def www(message: Message):



    try:
       info_two = await func()
    except Exception:
        await message.answer("❌ Не удалось обратиться к серверу. Попробуй позже.")
        return

    setup = info_two['setup']
    punchline = info_two['punchline']

    await message.answer(f'🤣 {setup}\n'
                         f'👉 2{punchline}')



async def main():
    bot = Bot(token=TOKEN)

    print("Запущен")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

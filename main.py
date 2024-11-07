import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot_app.local_settings import TOKEN
from aiogram import Bot, Dispatcher
from bot_app import dp
from bot_app import commands


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

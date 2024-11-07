from aiogram import types, Dispatcher
from aiogram.filters import Command
from bot_app import dp
import aiohttp
from aiohttp import ClientSession
from bot_app.local_settings import HTTP
from .local_settings import admin_chat_id


async def patch_data(url, data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.patch(url, json=data) as response:
                return await response.json()
        except Exception as e:
            print(e)


@dp.message(Command('start'))
async def start(message: types.Message):
    # Получение уникального кода с URL
    verif_code = str(message.text)[7:]

    if verif_code:
        # Найти пользователя по уникальному коду.
        # Для этого делается запрос по API с использованием verif_code.

        url = f'{HTTP}/users/api/v1/user-data/{verif_code}/'

        data = {
            'telegram_chat_id': int(message.chat.id),
            'telegram_verif_code': None
        }

        response = await patch_data(url, data)

        # if data['telegram_chat_id'] == admin_chat_id:
        #     await message.answer(f"Вы авторизовались под админом!")
        # else:
        await message.answer(f"Вы авторизовались!")
    else:
        await message.answer(f"Вы уже авторизовались!")
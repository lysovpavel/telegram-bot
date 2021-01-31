import json
import logging

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
# from aiohttp import request

API_TOKEN = '1538457964:AAF6_vY4qfiEAFlZkli7sBEOpzkezS75dxc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['menu', ])
async def send_menu(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Menu:\nCoffee - 2$\nTea - 1$.")


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    print(message.text)
    url = f"http://127.0.0.1:5000/{message.text}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            print(response)
            json_data = await response.text()
    data = json.loads(json_data)
    if data:
        await message.answer(data['content'])
    else:
        await message.answer('Упс... что-то пошло не так)')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
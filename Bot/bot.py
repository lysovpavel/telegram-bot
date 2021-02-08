import json
import logging
import os
from config import TELEGRAM_API_TOKEN, FLASK_ADMIN_HOST, FLASK_ADMIN_PORT
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
# from aiohttp import request


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

flask_admin_endpoint = f'http://{FLASK_ADMIN_HOST}:{FLASK_ADMIN_PORT}'


async def get_request(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                json_data = await response.text()
        data = json.loads(json_data)
        return True, data
    except Exception as ex:
        print(str(ex))
        return False, str(ex)


@dp.message_handler(commands=['start', ])
async def send_welcome(message: types.Message):
    print(message)
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['help', 'info'])
async def info(message: types.Message):
    print(message)
    print(f"<--- {message.from_user.first_name} {message.from_user.last_name}:\n{message.text}")
    url = f"{flask_admin_endpoint}/commands"
    status, data = await get_request(url)
    if status and data:
        answer = '/info - Cписок команд'
        if data:
            for command in data:
                answer += f"\n/{command['key']} - {command['title']}"
        print(f"---> {message.from_user.first_name} {message.from_user.last_name}:\n{answer}")
        await message.answer(answer)
    else:
        await message.answer('Упс... что-то пошло не так)')


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    print(message.text)
    url = f"{flask_admin_endpoint}/{message.text}"
    status, data = await get_request(url)
    if status and data:
        await message.answer(data['content'])
    else:
        await message.answer('Упс... что-то пошло не так)')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
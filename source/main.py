import asyncio
import uvicorn

from bot.bot import dp
# from nats2 import nats_consume
from aiogram import executor
from fast_api.views.command import create_command, get_commands, get_command_by_id, count_commands

from fast_api.app import app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # asyncio.ensure_future(nats_consume(loop))
    # loop.run_until_complete(nats_consume(loop))
    # loop.run_until_complete(do_insert())
    # loop.run_forever()
    config = uvicorn.Config(app=app, port=8080, loop=loop)
    server = uvicorn.Server(config)
    loop.run_until_complete(server.serve())
    # asyncio.ensure_future(server.serve())
    # executor.start_polling(dp, skip_updates=True)
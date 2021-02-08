import asyncio

from bot import dp
from nats2 import nats_consume
from aiogram import executor

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    # asyncio.ensure_future(nats_consume(loop))
    # loop.run_until_complete(nats_consume(loop))
    # loop.run_forever()
    executor.start_polling(dp, skip_updates=True)

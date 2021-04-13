import asyncio

from bot import dp
# from nats2 import nats_consume
from aiogram import executor
from mongo import db, do_insert

if __name__ == '__main__':
    print(db.list_collection_names())
    loop = asyncio.get_event_loop()
    # asyncio.ensure_future(nats_consume(loop))
    # loop.run_until_complete(nats_consume(loop))
    # loop.run_until_complete(do_insert())
    # loop.run_forever()
    executor.start_polling(dp, skip_updates=True)

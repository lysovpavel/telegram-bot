from nats.aio.client import Client as NatsClient
import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
import aiohttp
from config import TELEGRAM_API_TOKEN


async def message_handler(msg):
    # subject = msg.subject
    # reply = msg.reply
    # if reply:
    #     await send_message(channel=reply, data={'received': True, 'subject': subject})
    try:
        data = json.loads(msg.data.decode())


        # await dispatch(data)
        print(data)
        await send_telegram(data['message'], data['user_telegram_id'])
    except Exception as e:
        print(str(e))


async def generator_task(msg):
    asyncio.ensure_future(message_handler(msg))


async def nats_consume(loop):
    nc = NatsClient()
    await nc.connect("localhost:4222", loop=loop)
    if nc.is_connected:
        await nc.subscribe('django_out', cb=generator_task)
    else:
        raise Exception('Cant reach broker!')


async def post_request(url, data):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                json_data = await response.text()
        data = json.loads(json_data)
        return True, data
    except Exception as ex:
        print(str(ex))
        return False, str(ex)

async def send_telegram(text, channel_id):
    token = TELEGRAM_API_TOKEN
    # url = "https://telegg.ru/orig/bot"
    url = "https://api.telegram.org/bot"
    # channel_id = "-1001401087596"
    url += token
    method = url + "/sendMessage"

    try:
        print(method)
        r = await post_request(method, data={
             "chat_id": channel_id,
             "text": text
              })
        print(r)
        # print(r.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(nats_consume(loop))
    loop.run_forever()
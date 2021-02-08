from nats.aio.client import Client as NatsClient
import asyncio
import json


async def message_handler(msg):
    # subject = msg.subject
    # reply = msg.reply
    # if reply:
    #     await send_message(channel=reply, data={'received': True, 'subject': subject})
    try:
        data = json.loads(msg.data.decode())
        # await dispatch(data)
        print(data)
    except Exception as e:
        print(str(e))


async def generator_task(msg):
    asyncio.ensure_future(message_handler(msg))


async def nats_consume(loop):
    nc = NatsClient()
    await nc.connect("localhost:4222", loop=loop)
    if nc.is_connected:
        await nc.subscribe('mafin_in', cb=generator_task)
    else:
        raise Exception('Cant reach broker!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(nats_consume(loop))
    loop.run_forever()
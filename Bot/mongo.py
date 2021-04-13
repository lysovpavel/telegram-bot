from motor.motor_asyncio import AsyncIOMotorClient


# client = MongoClient()
client = AsyncIOMotorClient('mongodb://user:password@localhost:27017/')

db = client.tg_bot

init_commands = [
    {'key': 'test', 'title': 'test_title', 'content': 'test_content'},
    {'key': 'test2', 'title': 'test_title2', 'content': 'test_content2'},
    {'key': 'test3', 'title': 'test_title3', 'content': 'test_content3'}
]

async def do_insert():
    result = await db.commands.insert_many(init_commands)
    print('inserted %d docs' % (len(result.inserted_ids),))

async def do_find_one(key):
    document = await db.commands.find_one({'key': key})
    return document


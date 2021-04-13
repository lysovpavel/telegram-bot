import json

from app import app
from models import Command


@app.route('/<key>')
def get_command(key):
    data = {}
    print(key)
    command = Command.query.filter(Command.key==key).first()
    if command:
        data = {
            'id': command.id,
            'key': command.key,
            'title': command.title,
            'content': command.content,
        }
    return json.dumps(data)

@app.route('/commands')
def get_commands():
    data = []
    commands = Command.query.all()
    for command in commands:
        data.append({
            'id': command.id,
            'key': command.key,
            'title': command.title,
            'content': command.content,
        })
    return json.dumps(data)

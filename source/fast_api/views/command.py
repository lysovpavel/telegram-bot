from typing import List

from fastapi import HTTPException
from odmantic import ObjectId

from ..app import app
from ..mongo import engine
from pydantic import BaseModel
from typing import Optional

from ..models.command import Command


@app.put("/commands/", response_model=Command)
async def create_command(command: Command):
    await engine.save(command)
    return command


@app.get("/commands/", response_model=List[Command])
async def get_commands():
    commands = await engine.find(Command)
    return commands


@app.get("/commands/count", response_model=int)
async def count_commands():
    count = await engine.count(Command)
    return count


@app.get("/commands/{id}", response_model=Command)
async def get_command_by_id(id: ObjectId):
    command = await engine.find_one(Command, Command.id == id)
    if command is None:
        raise HTTPException(404)
    return command


@app.delete("/commands/{id}", response_model=Command)
async def delete_command_by_id(id: ObjectId):
    command = await engine.find_one(Command, Command.id == id)
    if command is None:
        raise HTTPException(404)
    await engine.delete(command)
    return command


class CommandPatchSchema(BaseModel):
    key: Optional[str]
    title: Optional[str]
    content: Optional[str]


@app.patch("/commands/{id}", response_model=Command)
async def update_command_by_id(id: ObjectId, patch: CommandPatchSchema):
    command = await engine.find_one(Command, Command.id == id)
    if command is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(command, name, value)
    await engine.save(command)
    return command
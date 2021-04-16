from typing import Optional

from odmantic import Field, Model


class Command(Model):
    key: str
    title: str
    content: str
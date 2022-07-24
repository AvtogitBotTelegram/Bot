import os
from dataclasses import dataclass


@dataclass
class config:

    url: str
    key_bot: str


config = config(
    url=os.environ['BACKEND_URL'],
    key_bot=os.environ['KEY_BOT']
)

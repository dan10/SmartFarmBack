from typing import Optional

from beanie import Document

from model.Routine import Routine


class Pump(Document):
    name: str
    is_open: bool
    routine: Optional[Routine]

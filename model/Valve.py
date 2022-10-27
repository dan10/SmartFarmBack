from typing import Optional

from beanie import Document, Link

from model.Plant import Plant


class Valve(Document):
    open: bool
    active: bool
    plant: Optional[Link[Plant]]

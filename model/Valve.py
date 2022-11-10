from enum import Enum
from typing import Optional

from beanie import Document, Link

from model.Plant import Plant


class TypeValve(Enum):
    IRRIGATION = "IRRIGATION"
    SUPPLY = "SUPPLY"


class Valve(Document):
    open: bool
    active: bool
    type: TypeValve
    plant: Optional[Link[Plant]]

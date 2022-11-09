from typing import Optional

from beanie import Document
from fastapi.encoders import jsonable_encoder

from model.Routine import Routine


class Plant(Document):
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    irrigation_routine: Routine


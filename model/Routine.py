from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TypeRoutine(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class Routine(BaseModel):
    start_date: datetime
    end_date: Optional[datetime] = None
    type_routine: TypeRoutine

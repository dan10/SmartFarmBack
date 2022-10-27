from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from model.Pump import Pump

pump_router = APIRouter()


@pump_router.get("/")
async def getPumps():
    return Pump.find_all()


@pump_router.get('/{id}')
async def getPump(id: PydanticObjectId):
    return Pump.get(id)


@pump_router.post('/{id}/open')
async def openPump():
    pump = Pump.get(id)
    pump.is_open = True

    if not pump:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    return pump

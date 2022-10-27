from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from model.Valve import Valve

valve_router = APIRouter()


@valve_router.get("/")
async def getValves():
    return Valve.find_all()


@valve_router.get('/{id}')
async def getValve(id: PydanticObjectId):
    return Valve.get(id)


@valve_router.post('/{id}/open')
async def openValve():
    valve = Valve.get(id)
    valve.is_open = True

    if not valve:
        raise HTTPException(
            status_code=404,
            detail="Valve record not found!"
        )

    return valve

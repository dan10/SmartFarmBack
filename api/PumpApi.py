import logging

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import Response
from starlette import status

from model.Pump import Pump

pump_router = APIRouter()

log = logging.getLogger(__name__)


@pump_router.get("/", response_model=list[Pump])
async def get_pumps() -> list[Pump]:
    return await Pump.find_all().to_list()


@pump_router.get('/{pump_id}', response_model=Pump)
async def get_pump(pump_id: PydanticObjectId) -> Pump:
    pump = await Pump.get(pump_id)

    if pump is None:
        raise HTTPException(
            status_code=404,
            detail="Pump not found!"
        )

    return pump


@pump_router.patch('/{pump_id}/open')
async def open_pump(pump_id: PydanticObjectId) -> bool:
    pump = await Pump.get(pump_id)

    if pump is None:
        raise HTTPException(
            status_code=404,
            detail="Pump not found!"
        )

    pump.is_open = True

    return pump.is_open


@pump_router.patch('/{pump_id}/close')
async def close_pump(pump_id: PydanticObjectId) -> bool:
    pump = await Pump.get(pump_id)

    if pump is None:
        raise HTTPException(
            status_code=404,
            detail="Pump not found!"
        )

    pump.is_open = False

    return pump.is_open


@pump_router.post("/")
async def add_pump(pump: Pump = Body(...)):
    insert = await pump.insert()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

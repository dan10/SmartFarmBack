import logging

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

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


@pump_router.post('/{pump_id}/open')
async def open_pump(pump_id: PydanticObjectId) -> bool:
    pump = await Pump.get(pump_id)

    if pump is None:
        raise HTTPException(
            status_code=404,
            detail="Pump not found!"
        )

    pump.is_open = True

    return pump.is_open

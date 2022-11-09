from beanie import PydanticObjectId, WriteRules
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import Response
from starlette import status

from model.Valve import Valve

valve_router = APIRouter()


@valve_router.get("/", response_model=list[Valve])
async def get_valves():
    return await Valve.find_all().to_list()


@valve_router.get('/{valve_id}', response_model=Valve)
async def get_valve(valve_id: PydanticObjectId):
    valve = await Valve.get(valve_id)

    if valve is None:
        raise HTTPException(
            status_code=404,
            detail="Valve record not found!"
        )

    return valve


@valve_router.post('/{id}/open')
async def open_valve(id: PydanticObjectId):
    valve = await Valve.get(id)
    valve.is_open = True

    if valve is None:
        raise HTTPException(
            status_code=404,
            detail="Valve record not found!"
        )

    return valve


@valve_router.post("/")
async def add_valve(valve: Valve = Body(...)):
    insert = await valve.insert(link_rule=WriteRules.DO_NOTHING)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

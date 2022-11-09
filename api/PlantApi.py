from beanie import PydanticObjectId
from fastapi import APIRouter

from model.Plant import Plant

plant_router = APIRouter()


@plant_router.get("/", response_description="List all plants", response_model=list[Plant])
async def get_plants():
    return await Plant.find_all().to_list()


@plant_router.get("/{_id}", response_description="Get Specific Plant Through the plant id", response_model=Plant)
async def get_plant(_id: PydanticObjectId):
    return await Plant.get(_id)

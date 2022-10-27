from beanie import PydanticObjectId
from fastapi import APIRouter

from model.Plant import Plant

plant_router = APIRouter()


@plant_router.get("/", response_description="List all plants")
async def getPlants():
    return Plant.find_all()


@plant_router.get("/{id}", response_description="Get Specific Plant Through the plant id")
async def getPlant(id: PydanticObjectId):
    return Plant.get(id)

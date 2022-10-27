import uvicorn as uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from api.PlantApi import plant_router
from api.PumpApi import pump_router
from api.ValveApi import valve_router
from config import settings
from model.Plant import Plant
from model.Pump import Pump
from model.Valve import Valve

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    await init_beanie(database=mongodb_client[settings.DB_NAME], document_models=[Plant, Pump, Valve])


app.include_router(plant_router, tags=["plant"], prefix="/plant")
app.include_router(pump_router, tags=["pump"], prefix="/pump")
app.include_router(valve_router, tags=["valve"], prefix="/valve")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )

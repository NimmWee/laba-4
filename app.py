from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class TripInfo(BaseModel):
    destination: str
    duration: int
    price: float

trips = [
    TripInfo(destination="Paris", duration=5, price=1000.0),
    TripInfo(destination="London", duration=3, price=800.0),
    TripInfo(destination="Rome", duration=7, price=1200.0)
]

@app.get("/trips")
async def get_trips() -> List[TripInfo]:
    return trips

@app.post("/trips")
async def create_trip(trip: TripInfo) -> TripInfo:
    trips.append(trip)
    return trip

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class TripInfo(BaseModel):
    id: int
    destination: str
    duration: int
    price: float

trips = [
    TripInfo(id=0, destination="Paris", duration=5, price=1000.0),
    TripInfo(id=1, destination="London", duration=3, price=800.0),
    TripInfo(id=2, destination="Rome", duration=7, price=1200.0)
]

@app.get("/trips")
async def get_trips() -> List[TripInfo]:
    return trips

@app.post("/trips")
async def create_trip(trip: TripInfo) -> TripInfo:
    trip.id = len(trips)
    trips.append(trip)
    return trip

@app.get("/trips/{trip_id}")
async def get_trip(trip_id: int) -> TripInfo:
    for trip in trips:
        if trip.id == trip_id:
            return trip
    raise HTTPException(status_code=404, detail="Trip not found")

@app.delete("/trips/{trip_id}")
async def delete_trip(trip_id: int):
    for i, trip in enumerate(trips):
        if trip.id == trip_id:
            deleted_trip = trips.pop(i)
            return deleted_trip
    raise HTTPException(status_code=404, detail="Trip not found")

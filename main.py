from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from database import (
    save_location,
    get_latest_location,
    get_all_locations,
    delete_location,
    delete_all_locations,
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Location(BaseModel):
    latitude: float
    longitude: float


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.post("/location")
def receive_location(location: Location):

    save_location(
        location.latitude,
        location.longitude
    )

    return {
        "message": "Location saved successfully!",
        "latitude": location.latitude,
        "longitude": location.longitude
    }


@app.get("/location/latest")
def latest_location():

    location = get_latest_location()

    if location is None:
        return {
            "message": "No locations found."
        }

    return {
        "id": location["id"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timestamp": location["timestamp"]
    }


@app.get("/locations")
def all_locations():

    locations = get_all_locations()

    return [
        {
            "id": location["id"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "timestamp": location["timestamp"],
        }
        for location in locations
    ]
@app.delete("/location/{location_id}")
def remove_location(location_id: int):
    delete_location(location_id)

    return{
        "message": "Location delete successfully."
    }
@app.delete("/locations")
def clear_locations():

    delete_all_locations()

    return {
        "message": "All locations deleted."
    }

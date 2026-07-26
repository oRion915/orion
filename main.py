from datetime import datetime
from math import asin, cos, radians, sin, sqrt

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from core.storage import (
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
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


def haversine_distance_km(start, end):
    """Return the distance between two locations in kilometers."""
    earth_radius_km = 6371.0

    latitude_difference = radians(end["latitude"] - start["latitude"])
    longitude_difference = radians(end["longitude"] - start["longitude"])
    start_latitude = radians(start["latitude"])
    end_latitude = radians(end["latitude"])

    haversine_value = (
        sin(latitude_difference / 2) ** 2
        + cos(start_latitude)
        * cos(end_latitude)
        * sin(longitude_difference / 2) ** 2
    )

    return 2 * earth_radius_km * asin(sqrt(haversine_value))


def format_duration(total_seconds):
    """Format a non-negative duration as HH:MM:SS."""
    total_seconds = max(0, int(total_seconds))
    hours, remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"


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


@app.get("/analytics")
def analytics():
    locations = list(reversed(get_all_locations()))

    if len(locations) < 2:
        return {
            "distance": 0.0,
            "average_speed": 0.0,
            "duration": "00:00:00",
            "stops": 0,
        }

    total_distance_km = 0.0
    total_stops = 0

    for start, end in zip(locations, locations[1:]):
        segment_distance_km = haversine_distance_km(start, end)
        total_distance_km += segment_distance_km

        if segment_distance_km * 1000 < 5:
            total_stops += 1

    start_time = datetime.fromisoformat(locations[0]["timestamp"])
    end_time = datetime.fromisoformat(locations[-1]["timestamp"])
    duration_seconds = (end_time - start_time).total_seconds()
    duration_hours = duration_seconds / 3600
    average_speed_kmh = (
        total_distance_km / duration_hours if duration_hours > 0 else 0.0
    )

    return {
        "distance": round(total_distance_km, 3),
        "average_speed": round(average_speed_kmh, 3),
        "duration": format_duration(duration_seconds),
        "stops": total_stops,
    }


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

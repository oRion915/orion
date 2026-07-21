import pytest


def test_create_and_retrieve_location(client):
    payload = {"latitude": 14.5995, "longitude": 120.9842}

    create_response = client.post("/location", json=payload)
    latest_response = client.get("/location/latest")
    locations_response = client.get("/locations")

    assert create_response.status_code == 200
    assert create_response.json() == {
        "message": "Location saved successfully!",
        **payload,
    }
    assert latest_response.status_code == 200
    assert latest_response.json()["latitude"] == payload["latitude"]
    assert latest_response.json()["longitude"] == payload["longitude"]
    assert locations_response.status_code == 200
    assert len(locations_response.json()) == 1


@pytest.mark.parametrize(
    "payload, field",
    [
        ({"latitude": -90.1, "longitude": 0}, "latitude"),
        ({"latitude": 0, "longitude": 180.1}, "longitude"),
    ],
)
def test_rejects_out_of_range_coordinates(client, payload, field):
    response = client.post("/location", json=payload)

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", field]


def test_clear_history_removes_all_locations(client):
    client.post("/location", json={"latitude": 14.5995, "longitude": 120.9842})
    client.post("/location", json={"latitude": 14.6000, "longitude": 120.9850})

    response = client.delete("/locations")

    assert response.status_code == 200
    assert response.json() == {"message": "All locations deleted."}
    assert client.get("/locations").json() == []
    assert client.get("/location/latest").json() == {
        "message": "No locations found."
    }


def test_analytics_returns_zero_values_without_locations(client):
    response = client.get("/analytics")

    assert response.status_code == 200
    assert response.json() == {
        "distance": 0.0,
        "average_speed": 0.0,
        "duration": "00:00:00",
        "stops": 0,
    }

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import database
from main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Provide a client backed by a fresh temporary locations database."""
    database_path = tmp_path / "gps_tracker.db"
    monkeypatch.setattr(database, "DATABASE", str(database_path))

    connection = database.get_connection()
    connection.execute(
        """
        CREATE TABLE locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.commit()
    connection.close()

    yield TestClient(app)

import os

from .loader import get_boolean_setting

DATABASE_URL = os.getenv("DATABASE_URL", "gps_tracker.db")

API_HOST = os.getenv("API_HOST", "127.0.0.1")

API_PORT = int(os.getenv("API_PORT", "8000"))

DEBUG = get_boolean_setting("DEBUG", True)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CHANGE_ME_TO_A_LONG_RANDOM_SECRET",
)

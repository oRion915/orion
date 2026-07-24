import os

from dotenv import load_dotenv


load_dotenv()


def get_boolean_setting(name, default):
    """Return an environment setting as a boolean."""
    value = os.getenv(name, str(default))
    return value.strip().lower() in {"1", "true", "yes", "on"}


DATABASE_URL = os.getenv("DATABASE_URL", "gps_tracker.db")
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = get_boolean_setting("DEBUG", True)
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_TO_A_LONG_RANDOM_SECRET")

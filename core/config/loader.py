import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def get_boolean_setting(name: str, default: bool) -> bool:
    """
    Return an environment variable as a boolean.

    Accepted true values:
    1, true, yes, on
    """
    value = os.getenv(name, str(default))
    return value.strip().lower() in {"1", "true", "yes", "on"}

import os
from pathlib import Path
from dotenv import load_dotenv


# =========================================
# Load .env
# =========================================
BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / "default.env"

load_dotenv(ENV_FILE)


# =========================================
# Database Configuration
# =========================================

DB_SERVER = os.getenv(
    "DB_SERVER"
)

DB_NAME = os.getenv(
    "DB_NAME"
)

DB_USER = os.getenv(
    "DB_USER"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD"
)


# =========================================
# Validate Configuration
# =========================================

required_config = {
    "DB_SERVER": DB_SERVER,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD
}


for key, value in required_config.items():

    if not value:

        raise ValueError(
            f"Missing environment variable: {key}"
        )
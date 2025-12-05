import logging
from datetime import datetime

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os


load_dotenv()

# FastAPI Additional settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Env settings
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_NAME_TEST = os.environ.get("POSTGRES_DB_TEST")
SECRET = os.environ.get("SECRET")


# Base settings
class Settings(BaseSettings):
    api_prefix: str = "/api"
    db_url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    db_echo: bool = False
    secret: str = f"{SECRET}"


# Logging
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
log_file_path = f"test_log_{current_time}.log"
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
logs_dir = os.path.join(BASE_DIR, "logs", log_file_path)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=logs_dir,
)
logger = logging.getLogger("test_logs")


settings = Settings()
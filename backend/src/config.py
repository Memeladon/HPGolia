from dotenv import load_dotenv
import os

load_dotenv(".env")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = os.getenv("DATABASE_URL")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")

PROJECT_NAME = 'PPlay'
PROJECT_VERSION = '0.0.0'

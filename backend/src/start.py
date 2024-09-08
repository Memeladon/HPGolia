import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import PROJECT_VERSION, PROJECT_NAME

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not defined!")

app = FastAPI(title=PROJECT_NAME, version=PROJECT_VERSION)

# ---------- Middleware ---------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ Routing ------------ #
# app.include_router(users.router)
# app.include_router(games.router)


@app.get("/")
def home():
    return "Root page"



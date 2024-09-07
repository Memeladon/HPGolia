import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import PROJECT_VERSION, PROJECT_NAME
from database.register import init_db
from routers import hpg_map, hpg_players, hpg_description

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
app.include_router(hpg_map.router)
app.include_router(hpg_players.router)
app.include_router(hpg_description.router)


@app.get("/")
def home():
    return "Root page"


@app.on_event("startup")
def on_startup():
    print("Database initialization...")
    init_db()
    print("Initialization completed.")

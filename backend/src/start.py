import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import PROJECT_VERSION, PROJECT_NAME
from src.routers import storage
from src.routers import users, auth, items, players, games

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not defined!")

app = FastAPI(title=PROJECT_NAME, version=PROJECT_VERSION, root_path="/api")

# ---------- Middleware ---------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ Routing ------------ #
app.include_router(users.router)
app.include_router(storage.router)
app.include_router(auth.router)
# app.include_router(items.router)
# app.include_router(players.router)
# app.include_router(games.router)


@app.get("/")
def home():
    # health check
    return {"msg": "ok"}

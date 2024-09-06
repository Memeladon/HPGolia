from fastapi import APIRouter, HTTPException

from ..database.models import db_connect
from ..database.crud import create_player, get_player_stats, get_player_by_username, update_player
from ..database.initialize.populate_players import init_players

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/create_new_one")
def create_new_player(username: str, age: int, biography: str):
    db = next(db_connect.get_db())
    player = create_player(username, age, biography, db)
    return player


@router.post("/initialize")
def initialize_players():
    db = next(db_connect.get_db())
    init_players(db)
    return {"message": "Players initialized successfully"}


@router.get("/by_username/{username}")
async def read_player_by_username(username: str):
    db = next(db_connect.get_db())
    player = get_player_by_username(username, db)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/{player_id}")
async def read_player(player_id: int):
    db = next(db_connect.get_db())
    player = get_player_stats(player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.put("/{player_id}")
def update_player_info(player_id: int, age: int = None, biography: str = None):
    db = next(db_connect.get_db())
    updated_player = update_player(player_id, db, age=age, biography=biography)
    if updated_player:
        return {"status": "success", "player": updated_player}
    return {"status": "error", "message": "Player not found"}

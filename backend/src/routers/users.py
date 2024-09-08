from fastapi import APIRouter

from src.database.models import get_db
from src.database.repositories.player import create_player, update_player

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/create_new_one")
def create_new_player(username: str, age: int, biography: str):
    db = get_db()
    player = create_player(username, age, biography, db)
    return player


# @router.post("/initialize")
# def initialize_players():
#     db = next(db_connect.get_db())
#     init_players(db)
#     return {"message": "Players initialized successfully"}


@router.put("/{player_id}")
def update_player_info(player_id: int, **kwargs):
    db = get_db()
    updated_player = update_player(player_id, db, **kwargs)
    if updated_player:
        return {"status": "success", "player": updated_player}
    return {"status": "error", "message": "Player not found"}

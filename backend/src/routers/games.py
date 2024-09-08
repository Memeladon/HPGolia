from fastapi import APIRouter

from backend.src.database.models import db_connect
from backend.src.database.repositories.map import get_all_fields

router = APIRouter(prefix="/game", tags=["game"])


@router.get("/map")
def get_map():
    db = next(db_connect.get_db())
    all_fields = get_all_fields(db)
    return all_fields


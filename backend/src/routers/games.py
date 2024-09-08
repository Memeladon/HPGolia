from fastapi import APIRouter

from src.database.models import get_db
from src.database.repositories.map import get_all_fields

router = APIRouter(prefix="/game", tags=["game"])


@router.get("/map")
def get_map():
    db = get_db()
    all_fields = get_all_fields(db)
    return all_fields


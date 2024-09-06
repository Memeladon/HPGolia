from fastapi import APIRouter

from ..database.models import db_connect
from ..database.crud import get_field_by_id
from ..database.initialize.populate_fields import init_fields

router = APIRouter(prefix="/fields", tags=["fields"])


@router.post("/initialize")
def populate_fields():
    db = next(db_connect.get_db())
    init_fields(db)
    return {"message": "Fields initialized successfully"}


@router.get("/{field_id}")
async def get_field(field_id: int):
    db = next(db_connect.get_db())
    return get_field_by_id(field_id, db)

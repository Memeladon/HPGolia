from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.repositories.session_map import read_cells

router = APIRouter(tags=['session-map'], prefix='/session-map')


@router.get('/cells')
def get_all_games(db: Session = Depends(get_db)):
    return read_cells(db)

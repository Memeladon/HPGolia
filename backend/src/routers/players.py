from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.repositories.player import read_player, read_players, create_player, update_player, delete_player
from src.entities.player import PlayerCreate, PlayerUpdate

router = APIRouter(tags=['players'], prefix='/players')


@router.get('/')
def get_all_players(db: Session = Depends(get_db)):
    return read_players(db)


@router.get('/{id}')
def get_one_player(id: UUID, db: Session = Depends(get_db)):
    return read_player(db, id)


@router.post('/')
def create_one_player(data: PlayerCreate, db: Session = Depends(get_db)):
    return create_player(db, data.dict())


@router.put('/{id}')
def update_one_player(id, data: PlayerUpdate, db: Session = Depends(get_db)):
    return update_player(db, id, data.dict())


@router.delete('/{id}')
def delete_one_player(id, db: Session = Depends(get_db)):
    return delete_player(db, id)

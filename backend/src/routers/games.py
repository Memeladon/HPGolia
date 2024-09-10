from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.repositories.game import read_game, read_games, create_game, update_game, delete_game
from src.entities.game import GameUpdate, GameCreate

router = APIRouter(tags=['games'], prefix='/games')


@router.get('/')
def get_all_games(db: Session = Depends(get_db)):
    return read_games(db)


@router.get('/{id}')
def get_one_user(id: int, db: Session = Depends(get_db)):
    return read_game(db, id)


@router.post('/')
def create_one_game(data: GameCreate, db: Session = Depends(get_db)):
    return create_game(db, data.dict())


@router.put('/{id}')
def update_one_user(id, data: GameUpdate, db: Session = Depends(get_db)):
    return update_game(db, id, data.dict())


@router.delete('/{id}')
def delete_one_user(id, db: Session = Depends(get_db)):
    return delete_game(db, id)

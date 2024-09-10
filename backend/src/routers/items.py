from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.repositories.item import read_items, read_item, create_item, update_item, delete_item, \
    read_player_items, read_player_item, create_player_item, update_player_item, delete_player_item

from src.entities.item import ItemCreate, ItemUpdate
from src.entities.player_item import PlayerItemCreate

router = APIRouter(tags=['items'], prefix='/items')


@router.get('/')
def get_all_items(db: Session = Depends(get_db)):
    return read_items(db)


@router.get('/player_items/')
def get_all_players_items(db: Session = Depends(get_db)):
    return read_player_items(db)


@router.get('/{id}')
def get_one_items(id: UUID, db: Session = Depends(get_db)):
    return read_item(db, id)


@router.get('/player_items/{id}')
def get_one_players_item(id: UUID, db: Session = Depends(get_db)):
    return read_player_item(db, id)


@router.post('/')
def create_one_item(data: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, data.dict())


@router.post('/player_items/')
def create_one_players_item(data: PlayerItemCreate, db: Session = Depends(get_db)):
    return create_player_item(db, data.dict())


@router.put('/{id}')
def update_one_item(id, data: ItemUpdate, db: Session = Depends(get_db)):
    return update_item(db, id, data.dict())


@router.put('/player_items/{id}')
def update_one_players_item(id, data: ItemUpdate, db: Session = Depends(get_db)):
    return update_player_item(db, id, data.dict())


@router.delete('/{id}')
def delete_one_item(id, db: Session = Depends(get_db)):
    return delete_item(db, id)


@router.delete('/player_items/{id}')
def delete_one_players_item(id, db: Session = Depends(get_db)):
    return delete_player_item(db, id)

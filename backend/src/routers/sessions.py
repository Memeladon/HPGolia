from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.repositories.session import read_session, read_sessions, create_session, update_session, delete_session, \
     read_session_users, read_session_user, create_session_user, update_session_user, delete_session_user
from src.entities.session import SessionCreate, SessionUpdate

router = APIRouter(tags=['sessions'], prefix='/sessions')


# --------------- SESSIONS -------------- #

@router.get('/')
def get_all_sessions(db: Session = Depends(get_db)):
    return read_sessions(db)


@router.get('/{id}')
def get_one_game(id: UUID, db: Session = Depends(get_db)):
    return read_session(db, id)


@router.post('/')
def create_one_session(data: SessionCreate, db: Session = Depends(get_db)):
    return create_session(db, data.dict())


@router.put('/{id}')
def update_one_session(id, data: SessionUpdate, db: Session = Depends(get_db)):
    return update_session(db, id, data.dict())


@router.delete('/{id}')
def delete_one_game(id, db: Session = Depends(get_db)):
    return delete_session(db, id)


# ------------- SESSION_USER ------------ #

@router.get('/session_users/')
def get_all_session_users(db: Session = Depends(get_db)):
    return read_session_users(db)


@router.get('/session_users/{id}')
def get_one_game(id: UUID, db: Session = Depends(get_db)):
    return read_session_user(db, id)


@router.post('/session_users/')
def create_one_session(data: SessionCreate, db: Session = Depends(get_db)):
    return create_session_user(db, data.dict())


@router.put('/session_users/{id}')
def update_one_session(id, data: SessionUpdate, db: Session = Depends(get_db)):
    return update_session_user(db, id, data.dict())


@router.delete('/session_users/{id}')
def delete_one_game(id, db: Session = Depends(get_db)):
    return delete_session_user(db, id)
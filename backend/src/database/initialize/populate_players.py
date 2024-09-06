from sqlalchemy.orm import Session

from ..crud import create_players


def init_players(db: Session):
    players_data = [
        {"username": "memeladon", "age": 22, "biography": "desc1"},
        {"username": "Xlebyiiiek2322", "age": 22, "biography": "desc2"},
        {"username": "Gnida", "age": 22, "biography": "desc3"},
        {"username": "ARCV", "age": 22, "biography": "desc4"},
        {"username": "Drainculture", "age": 22, "biography": "desc5"},
    ]
    create_players(players_data, db)

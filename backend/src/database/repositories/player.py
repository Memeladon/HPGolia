# ============================================================================================================ #
# -------------------------------------------------- PLAYER -------------------------------------------------- #
# ============================================================================================================ #
from sqlalchemy.orm import Session

from src.database.models import Player, DiceRoll, PlayerFieldPosition


def create_player(username: str, age: int, biography: str, db: Session):
    existing_player = db.query(Player).filter(Player.username == username).first()
    if existing_player:
        raise ValueError("Username уже существует")

    new_player = Player(
        username=username,
        age=age,
        biography=biography,
    )
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


def create_players(players_data: list, db: Session):
    players = [Player(**data) for data in players_data]
    db.add_all(players)
    db.commit()


def update_player(player_id: int, db: Session, **kwargs):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        for key, value in kwargs.items():
            setattr(player, key, value)
        db.commit()
        db.refresh(player)
        return player
    return None


def delete_player(player_id: int, db: Session):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        db.query(DiceRoll).filter(DiceRoll.player_id == player_id).delete()
        db.delete(player)
        db.commit()
        return True
    return False



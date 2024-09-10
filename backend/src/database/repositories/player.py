from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Union, Dict, Any

from src.database.models import Player


# =================================================================================================================== #
# ------------------------------------------------------ PLAYER ----------------------------------------------------- #
# =================================================================================================================== #

def create_player(db: Session, player_data: Dict[str, Any]) -> Union[Player, None]:
    try:
        required_fields = ['user', 'cell', 'nickname', 'profile_image']
        if not all(field in player_data for field in required_fields):
            raise ValueError("Missing required fields: user, cell, nickname, profile_image")

        new_player = Player(**player_data)
        db.add(new_player)
        db.commit()
        db.refresh(new_player)
        return new_player
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE player: {str(e)}"
    finally:
        db.close()


def read_player(db: Session, player_id: UUID) -> Union[Player, None]:
    try:
        player = db.query(Player).filter(Player.id == player_id).first()
        return player
    except SQLAlchemyError as e:
        raise f"Error READ player: {str(e)}"
    finally:
        db.close()


def read_players(db: Session):
    players = db.query(Player).all()
    return players


def update_player(db: Session, player_id: UUID, player_data: Dict[str, Any]) -> bool:
    try:
        player = db.query(Player).filter(Player.id == player_id).first()
        if not player:
            raise ValueError("Player not found")

        for attr, value in player_data.items():
            setattr(player, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE player: {str(e)}"
    finally:
        db.close()


def delete_player(db: Session, player_id: UUID) -> bool:
    try:
        player = db.query(Player).filter(Player.id == player_id).first()
        if not player:
            raise ValueError("Player not found")

        db.delete(player)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE player: {str(e)}"
    finally:
        db.close()

from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError
from typing import Union, Dict, Any

from src.database.models import GamePlayer, Game


# =================================================================================================================== #
# ------------------------------------------------------- GAME ------------------------------------------------------ #
# =================================================================================================================== #

def create_game(db: Session, game_data: Dict[str, Any]) -> Union[Game, None]:
    try:
        required_fields = ['cell', 'link', 'condition_type']
        if not all(field in game_data for field in required_fields):
            raise ValueError("Missing required fields: cell, link, condition_type")

        new_game = Game(**game_data)
        db.add(new_game)
        db.commit()
        db.refresh(new_game)
        return new_game
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE game: {str(e)}"
    finally:
        db.close()


def read_game(db: Session, game_id: int) -> Union[Game, None]:
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        return game
    except SQLAlchemyError as e:
        raise f"Error UPDATE game: {str(e)}"
    finally:
        db.close()


def read_games(db: Session):
    games = db.query(Game).all()
    return games


def update_game(db: Session, game_id: int, game_data: Dict[str, Any]) -> bool:
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if not game:
            raise ValueError("Game not found")

        for attr, value in game_data.items():
            setattr(game, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE game: {str(e)}"
    finally:
        db.close()


def delete_game(db: Session, game_id: int) -> bool:
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if not game:
            raise ValueError("Game not found")

        db.delete(game)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE game: {str(e)}"
    finally:
        db.close()


# =================================================================================================================== #
# --------------------------------------------------- GAME PLAYER --------------------------------------------------- #
# =================================================================================================================== #

def create_game_player(db: Session, game_player_data: Dict[str, Any]) -> Union[GamePlayer, None]:
    try:
        required_fields = ['player', 'game', 'status']
        if not all(field in game_player_data for field in required_fields):
            raise ValueError("Missing required fields: player, game, status")

        new_game_player = GamePlayer(**game_player_data)
        db.add(new_game_player)
        db.commit()
        db.refresh(new_game_player)
        return new_game_player
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE game_player: {str(e)}"
    finally:
        db.close()


def read_game_player(db: Session, game_player_id: int) -> Union[GamePlayer, None]:
    try:
        game_player = db.query(GamePlayer).filter(GamePlayer.id == game_player_id).first()
        return game_player
    except SQLAlchemyError as e:
        raise f"Error READ game_player: {str(e)}"
    finally:
        db.close()


def read_game_players(db: Session):
    users = db.query(GamePlayer).all()
    return users


def update_game_player(db: Session, game_player_id: int, game_player_data: Dict[str, Any]) -> bool:
    try:
        game_player = db.query(GamePlayer).filter(GamePlayer.id == game_player_id).first()
        if not game_player:
            raise ValueError("Game_player not found")

        for attr, value in game_player_data.items():
            setattr(game_player, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE game_player: {str(e)}"
    finally:
        db.close()


def delete_game_player(db: Session, game_player_id: int) -> bool:
    try:
        game_player = db.query(GamePlayer).filter(GamePlayer.id == game_player_id).first()
        if not game_player:
            raise ValueError("Game_player not found")

        db.delete(game_player)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE game_player: {str(e)}"
    finally:
        db.close()

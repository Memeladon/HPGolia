from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Union, Dict, Any

from src.database.models import Item, PlayerItem


# =================================================================================================================== #
# ------------------------------------------------------- ITEM ------------------------------------------------------ #
# =================================================================================================================== #


def create_item(db: Session, item_data: Dict[str, Any]) -> Union[Item, None]:
    try:
        required_fields = ['title', 'description']
        if not all(field in item_data for field in required_fields):
            raise ValueError("Missing mandatory fields: title, description")

        new_item = Item(**item_data)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE item: {str(e)}"
    finally:
        db.close()


def read_item(db: Session, item_id: int) -> Union[Item, None]:
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        return item
    except SQLAlchemyError as e:
        raise f"Error READ item: {str(e)}"
    finally:
        db.close()


def update_item(db: Session, item_id: int, item_data: Dict[str, Any]) -> bool:
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            raise ValueError("Item not found")

        for attr, value in item_data.items():
            setattr(item, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE item: {str(e)}"
    finally:
        db.close()


def delete_item(db: Session, item_id: int) -> bool:
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            raise ValueError("Item not found")

        db.delete(item)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE item: {str(e)}"
    finally:
        db.close()


# =================================================================================================================== #
# --------------------------------------------------- PLAYER ITEM --------------------------------------------------- #
# =================================================================================================================== #


def create_player_item(db: Session, player_item_data: Dict[str, Any]) -> Union[PlayerItem, None]:
    try:
        required_fields = ['item', 'user']
        if not all(field in player_item_data for field in required_fields):
            raise ValueError("Missing mandatory fields: item, user")

        new_player_item = PlayerItem(**player_item_data)
        db.add(new_player_item)
        db.commit()
        db.refresh(new_player_item)
        return new_player_item
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE player_item: {str(e)}"
    finally:
        db.close()


def read_player_item(db: Session, player_item_id: int) -> Union[PlayerItem, None]:
    try:
        player_item = db.query(PlayerItem).filter(PlayerItem.id == player_item_id).first()
        return player_item
    except SQLAlchemyError as e:
        raise f"Error READ player_item: {str(e)}"
    finally:
        db.close()


def update_player_item(db: Session, player_item_id: int, player_item_data: Dict[str, Any]) -> bool:
    try:
        player_item = db.query(PlayerItem).filter(PlayerItem.id == player_item_id).first()
        if not player_item:
            raise ValueError("Player_item not found")

        for attr, value in player_item_data.items():
            setattr(player_item, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE player_item: {str(e)}"
    finally:
        db.close()


def delete_player_item(db: Session, player_item_id: int) -> bool:
    try:
        player_item = db.query(PlayerItem).filter(PlayerItem.id == player_item_id).first()
        if not player_item:
            raise ValueError("Player_item not found")

        db.delete(player_item)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE player_item:: {str(e)}"
    finally:
        db.close()

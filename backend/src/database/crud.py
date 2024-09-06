import random

from sqlalchemy import func
from sqlalchemy.orm import Session

from .models import DiceRoll, Field, Player, PlayerFieldPosition, InventoryItem, FieldType, db_connect


# ============================================================================================================ #
# -------------------------------------------------- PLAYER -------------------------------------------------- #
# ============================================================================================================ #

def create_player(username: str, age: int, biography: str, db: Session):
    existing_player = db.query(Player).filter(Player.username == username).first()
    if existing_player:
        raise ValueError("Username уже существует")

    new_player = Player(
        username=username,
        age=age,
        biography=biography,
        # Инвентарь будет управляться через relationship
    )
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


def create_players(players_data: list, db: Session):
    players = [Player(**data) for data in players_data]
    db.add_all(players)
    db.commit()


def get_player_stats(player_id: int, db: Session):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        inventory = {item.item.name: item.quantity for item in player.inventory_items}
        stats = {
            "username": player.username,
            "age": player.age,
            "biography": player.biography,
            "average_dice_roll": player.average_dice_roll,
            "completed_games_count": player.completed_games_count,
            "passed_fields_count": player.passed_fields_count,
            "dropped_count": player.dropped_count,
            "rounds_completed_count": player.rounds_completed_count,
            "dice_rolls_count": player.dice_rolls_count,
            "win_points": player.win_points,
            "inventory": inventory,
            "is_active": player.is_active
        }
        return stats
    return None


def get_player_by_username(username: str, db: Session):
    return db.query(Player).filter(Player.username == username).first()


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
        db.query(PlayerFieldPosition).filter(PlayerFieldPosition.player_id == player_id).delete()
        db.query(InventoryItem).filter(InventoryItem.player_id == player_id).delete()
        db.delete(player)
        db.commit()
        return True
    return False


def update_win_points(player_id: int, win_points: int, db: Session):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        player.win_points += win_points
        db.commit()
        return True
    return False


# ============================================================================================================ #
# -------------------------------------------------- FIELD --------------------------------------------------- #
# ============================================================================================================ #

def create_field(name: str, field_type: FieldType, rules: str, db: Session):
    existing_field = db.query(Field).filter(Field.name == name).first()
    if existing_field:
        raise ValueError("Поле с таким именем уже существует")

    new_field = Field(
        name=name,
        type=field_type,
        rules=rules
    )
    db.add(new_field)
    db.commit()
    db.refresh(new_field)
    return new_field


def create_fields(fields_data: list, db: Session):
    db.bulk_insert_mappings(Field, fields_data)
    db.commit()


def get_field_by_id(field_id: int, db: Session):
    return db.query(Field).filter(Field.id == field_id).first()


def print_fields(db: Session):
    all_fields = db.query(Field).all()
    for field in all_fields:
        print(f"\nПоле: {field.name}")
        print(f"Тип: {field.type.value}")
        print(f"ID: {field.id}")
        print(f"Правила: {field.rules}")  # Парсить JSON здесь =p


def delete_player_from_field(player_id: int, field_id: int, db: Session):
    position = db.query(PlayerFieldPosition).filter_by(player_id=player_id, field_id=field_id).first()
    if position:
        db.delete(position)
        db.commit()


def add_player_to_field(player_id: int, field_id: int, position: int, db: Session):
    existing_position = db.query(PlayerFieldPosition).filter_by(player_id=player_id).first()
    if existing_position:
        existing_position.field_id = field_id
        existing_position.position = position
    else:
        new_position = PlayerFieldPosition(player_id=player_id, field_id=field_id, position=position)
        db.add(new_position)
    db.commit()


def get_players_on_field(field_id: int, db: Session):
    players = db.query(Player).join(PlayerFieldPosition).filter(PlayerFieldPosition.field_id == field_id).all()
    return [p.username for p in players]


# ============================================================================================================ #
# --------------------------------------------------- DICE --------------------------------------------------- #
# ============================================================================================================ #

def roll_dice(player_id: int, db: Session):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        current_roll = first_dice + second_dice

        dice_roll = DiceRoll(
            player_id=player_id,
            roll_value1=first_dice,
            roll_value2=second_dice,
        )
        db.add(dice_roll)

        # player roll update
        player.dice_rolls_count += 1
        total_sum = db.query(func.sum(DiceRoll.roll_value1 + DiceRoll.roll_value2)).filter(
            DiceRoll.player_id == player_id).scalar() or 0
        player.average_dice_roll = round(total_sum / player.dice_rolls_count, 2)

        db.commit()
        db.refresh(player)
        return current_roll
    return None

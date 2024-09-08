# ============================================================================================================ #
# --------------------------------------------------- DICE --------------------------------------------------- #
# ============================================================================================================ #
import random

from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.src.database.models import Player, DiceRoll


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

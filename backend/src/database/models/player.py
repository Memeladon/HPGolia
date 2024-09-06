from .base import db_connect
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship


class Player(db_connect.Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    biography = Column(String)

    average_dice_roll = Column(Float, nullable=False, default=0.0)
    completed_games_count = Column(Integer, default=0)
    passed_fields_count = Column(Integer, default=0)
    dropped_count = Column(Integer, default=0)
    rounds_completed_count = Column(Integer, default=0)
    dice_rolls_count = Column(Integer, default=0)
    win_points = Column(Integer, default=0)

    is_active = Column(Boolean, default=True)

    inventory_items = relationship("InventoryItem", back_populates="player", cascade="all, delete-orphan")
    dice_rolls = relationship("DiceRoll", back_populates="player", cascade="all, delete-orphan")
    field_positions = relationship("PlayerFieldPosition", back_populates="player", cascade="all, delete-orphan")

    def __repr__(self):
        return (f"<Player(id={self.id}, username='{self.username}', age={self.age}, biography='{self.biography}', "
                f"avg_dice_roll={self.average_dice_roll:.2f}, games_completed={self.completed_games_count})>")

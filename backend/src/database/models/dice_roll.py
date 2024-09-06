from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import db_connect


class DiceRoll(db_connect.Base):
    __tablename__ = 'dice_rolls'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    roll_value1 = Column(Integer, nullable=False)
    roll_value2 = Column(Integer, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())

    player = relationship("Player", back_populates="dice_rolls")

    def __repr__(self):
        return (f"DiceRoll(id={self.id}, player_id={self.player_id}, "
                f"roll_value1={self.roll_value1}, roll_value2={self.roll_value2}")

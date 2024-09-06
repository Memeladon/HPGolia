from .base import db_connect
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class PlayerFieldPosition(db_connect.Base):
    __tablename__ = 'player_field_positions'

    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    field_id = Column(Integer, ForeignKey('fields.id'), primary_key=True)
    position = Column(Integer, nullable=False)

    player = relationship("Player", back_populates="field_positions")
    field = relationship("Field", back_populates="players")

    def __repr__(self):
        return (f"PlayerFieldPosition(player_id={self.player_id}, field_id={self.field_id}, "
                f"position={self.position})")

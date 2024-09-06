from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import db_connect


class InventoryItem(db_connect.Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

    player = relationship("Player", back_populates="inventory_items")
    item = relationship("Item")

    def __repr__(self):
        return f"InventoryItem(player_id={self.player_id}, item_id={self.item_id})"

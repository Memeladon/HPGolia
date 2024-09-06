from sqlalchemy import Column, Integer, String, Boolean, Enum
from enum import Enum as PyEnum
from .base import db_connect


class ItemType(PyEnum):
    BUFF = 'Бафф'
    DEBUFF = 'Дебафф'
    TRAP = 'Ловушка'
    NEUTRAL = 'Нейтралка'


class Item(db_connect.Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(Enum(ItemType))
    charges_count = Column(Integer, default=0)
    description = Column(String)

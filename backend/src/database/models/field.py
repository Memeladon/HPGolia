from .base import db_connect
from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum


class FieldType(PyEnum):
    START = 'Старт'
    AUCTION = 'Аукционная'
    LOTTERY = 'Лотерея'
    JAIL = 'Тюрьма'
    GAME = 'Игра'
    RANDOM = 'Случай'
    LUCKY_UNLUCKY = 'Повезет или не повезет'


class Field(db_connect.Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    type = Column(Enum(FieldType), nullable=False)
    rules = Column(JSON, nullable=True)  # TODO: Рассмотреть разбиение на таблицы

    players = relationship("PlayerFieldPosition", back_populates="field", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Field(id={self.id}, name='{self.name}', type='{self.type}')"

    '''
        Пример использования
    # Пока у пользователя нет "players"
     fieldname = Field(name='Kalowar', Type=FieldType.GAME, rules=json.dump('...'))
     fieldname.players  # Пустой список
     
     # Добавим адресов ему
     fieldname.players = [
                 Player(name='...'),
                 Player(name='...'),
                 Player(name='...')
            ]
    '''

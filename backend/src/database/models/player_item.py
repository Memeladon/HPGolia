from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class PlayerItem(Base):
    __tablename__ = "player_item"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item: Mapped[int] = mapped_column(ForeignKey("item.id"),
                                      nullable=False,
                                      index=True)
    user: Mapped[UUID] = mapped_column(ForeignKey("users.id"),
                                       nullable=False,
                                       index=True)

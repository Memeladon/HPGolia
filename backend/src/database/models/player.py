from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from src.database.models import Base


class Player(Base):
    __tablename__ = "player"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                       nullable=False,
                                       index=True)
    cell: Mapped[UUID] = mapped_column(ForeignKey("cell.id"),
                                       nullable=False,
                                       index=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    profile_image: Mapped[str] = mapped_column(nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)
    round: Mapped[int] = mapped_column(default=0, nullable=False)
    modifier_dice: Mapped[int] = mapped_column(nullable=True)
    modifier_game: Mapped[int] = mapped_column(nullable=True)

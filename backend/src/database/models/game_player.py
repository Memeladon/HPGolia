from uuid import UUID

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class GamePlayer(Base):
    __tablename__ = "game_player"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player: Mapped[UUID] = mapped_column(ForeignKey("player.id"),
                                         nullable=False,
                                         index=True)
    game: Mapped[int] = mapped_column(ForeignKey("game.id"),
                                      nullable=False,
                                      index=True)
    status: Mapped[str] = mapped_column(nullable=False)

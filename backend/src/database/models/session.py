from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from src.database.models import Base


class Session(Base):
    __tablename__ = "session"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(nullable=True)
    max_players: Mapped[int] = mapped_column(nullable=False)
    date_start: Mapped[DateTime] = mapped_column(nullable=False)
    date_end: Mapped[DateTime] = mapped_column(nullable=False)

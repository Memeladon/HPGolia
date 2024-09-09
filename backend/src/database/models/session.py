from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from src.database.models import Base


class Session(Base):
    __tablename__ = "session"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(nullable=True)
    max_players: Mapped[int] = mapped_column(nullable=False)
    date_start: Mapped[datetime] = mapped_column(nullable=False)
    date_end: Mapped[datetime] = mapped_column(nullable=False)

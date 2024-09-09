from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class Game(Base):
    __tablename__ = "game"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cell: Mapped[int] = mapped_column(ForeignKey("cell.id"),
                                      nullable=False,
                                      index=True)
    link: Mapped[str] = mapped_column(nullable=False)
    condition_type: Mapped[str] = mapped_column(nullable=False)


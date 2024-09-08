from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class Cell(Base):
    __tablename__ = "cell"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    position: Mapped[int] = mapped_column(unique=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)

    main_conditions: Mapped[text] = mapped_column(nullable=False)
    genre_conditions: Mapped[text] = mapped_column(nullable=False)

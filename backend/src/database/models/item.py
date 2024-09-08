from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[text] = mapped_column(nullable=False)
    uses: Mapped[int] = mapped_column(nullable=True)


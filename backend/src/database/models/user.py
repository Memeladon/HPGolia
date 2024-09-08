from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from src.database.models import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from uuid import UUID

from src.database.models import Base


class SessionUser(Base):
    __tablename__ = "session_user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session: Mapped[UUID] = mapped_column(ForeignKey("session.id"),
                                          nullable=False,
                                          index=True)
    user: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                       nullable=False,
                                       index=True)
    permission: Mapped[str] = mapped_column(nullable=False)


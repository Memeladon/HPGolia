import datetime
from uuid import UUID

from pydantic import BaseModel


class SessionUser(BaseModel):
    id: int
    session: UUID
    user: UUID
    permission: str


class SessionUserCreate(BaseModel):
    session: UUID
    user: UUID
    permission: str


class SessionUserUpdate(BaseModel):
    permission: str


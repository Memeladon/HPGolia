import datetime
from uuid import UUID

from pydantic import BaseModel


class Session(BaseModel):
    id: UUID
    status: str | None
    max_players: int
    date_start: datetime
    date_end: datetime


class SessionCreate(BaseModel):
    max_players: int
    date_start: datetime
    date_end: datetime


class SessionUpdate(BaseModel):
    status: str | None
    max_players: int
    date_start: datetime
    date_end: datetime


class SessionResponse(BaseModel):
    id: UUID
    status: str | None
    date_start: datetime
    date_end: datetime

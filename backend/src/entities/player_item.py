from uuid import UUID

from pydantic import BaseModel


class PlayerItem(BaseModel):
    id: int
    item: int
    user: UUID


class PlayerItemCreate(BaseModel):
    item: int
    user: UUID


class UpdatePlayerItem(BaseModel):
    item: int
    user: UUID

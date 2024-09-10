from uuid import UUID
from pydantic import BaseModel


class Player(BaseModel):
    id: UUID
    user: UUID
    cell: int
    nickname: str
    profile_image: str
    points: int
    round: int
    modifier_dice: int | None
    modifier_game: int | None


class PlayerCreate(BaseModel):
    user: UUID
    cell: int
    nickname: str
    profile_image: str


class PlayerUpdate(BaseModel):
    nickname: str
    profile_image: str
    points: int
    round: int
    modifier_dice: int | None
    modifier_game: int | None



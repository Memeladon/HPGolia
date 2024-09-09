from pydantic import BaseModel


class Game(BaseModel):
    id: int
    cell: int
    link: str
    condition_type: str


class GameCreate(BaseModel):
    cell: int
    link: str
    condition_type: str


class GameUpdate(GameCreate):
    pass

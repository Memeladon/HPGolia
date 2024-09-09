from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    username: str
    password: str
    role: str
    is_active: bool


class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    is_active: bool


class UserUpdate(UserCreate):
    pass

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    description: str
    uses: int | None


class ItemCreate(BaseModel):
    title: str
    description: str
    uses: int | None


class ItemUpdate(BaseModel):
    title: str
    description: str
    uses: int | None

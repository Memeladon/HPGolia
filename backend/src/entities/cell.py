from pydantic import BaseModel


class Cell:
    id: int
    position: str
    title: str
    type: str
    background_img: str | None

    main_conditions: str
    genre_conditions: str


class CreateCell:
    position: str
    title: str
    type: str
    background_img: str | None
    main_conditions: str
    genre_conditions: str


class UpdateCell:
    position: str
    title: str
    type: str
    background_img: str | None
    main_conditions: str
    genre_conditions: str

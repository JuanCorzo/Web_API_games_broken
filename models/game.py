from sqlmodel import SQLModel, Field


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    genre: str
    platform: str
    stock: int
    active: bool = True

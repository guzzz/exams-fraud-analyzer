
from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    surname: str
    age: int | None = None

    class Config:
        orm_mode = True


from pydantic import BaseModel


class Monitor(BaseModel):
    device: str
    version: str

    class Config:
        orm_mode = True

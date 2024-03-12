
from pydantic import BaseModel
from uuid import UUID


class Payload(BaseModel):
    hr: int
    hrt: int


class SamsungX1S(BaseModel):
    eui: UUID
    model: str
    version: str
    payload: Payload
    ts: float

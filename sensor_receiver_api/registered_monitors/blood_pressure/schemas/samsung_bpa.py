
from pydantic import BaseModel
from uuid import UUID


class Payload(BaseModel):
    bp_sys: int
    bp_dia: int


class SamsungBPA(BaseModel):
    eui: UUID
    model: str
    version: str
    payload: Payload
    ts: float

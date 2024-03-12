
from pydantic import BaseModel
from uuid import UUID


class PolarMX2(BaseModel):
    eui: UUID
    fw: str
    pulse: int
    ts: float

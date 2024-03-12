
from pydantic import BaseModel
from datetime import datetime


class BloodPressure(BaseModel):
    systolic_bp: int
    date: datetime

    class Config:
        orm_mode = True

class HeartRate(BaseModel):
    pulse: int
    date: datetime

    class Config:
        orm_mode = True

class Evidences(BaseModel):
    blood_pressure_evidences: list[BloodPressure]
    heart_rate_evidences: list[HeartRate]

    class Config:
        orm_mode = True


from pydantic import BaseModel
from datetime import datetime

from consultive_api.schemas.persons import Person
from consultive_api.schemas.monitors import Monitor


class FraudsByPerson(BaseModel):
    id: int
    title: str
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


class FraudsWithDetails(BaseModel):
    id: int
    title: str
    start_date: datetime
    end_date: datetime
    person: Person

    class Config:
        orm_mode = True

class FraudWithDetails(BaseModel):
    title: str
    base_blood_pressure: int
    base_heart_rate: int
    start_date: datetime
    end_date: datetime
    blood_pressure_monitor: Monitor
    heart_rate_monitor: Monitor
    person: Person

    class Config:
        orm_mode = True
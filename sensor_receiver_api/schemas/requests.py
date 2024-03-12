
from pydantic import BaseModel


class ProcessRequest(BaseModel):
    start_time: float
    end_time: float
    base_blood_pressure: int
    base_hearth_rate: int
    pressure_monitor_device: str
    pressure_monitor_version: str
    hearth_monitor_device: str
    hearth_monitor_version: str

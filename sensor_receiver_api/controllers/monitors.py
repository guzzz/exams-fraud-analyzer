
from fastapi import APIRouter, status
from structlog import get_logger

from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import SamsungBPA
from sensor_receiver_api.registered_monitors.heart_rate.schemas.polarmx2 import PolarMX2
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import SamsungX1S
from sensor_receiver_api.services.facade import ServiceFacade

router = APIRouter()
log = get_logger()
service = ServiceFacade()


@router.post("/heart-rate/samsung-x1s/", status_code=status.HTTP_201_CREATED)
async def register_samsung_x1s(request: SamsungX1S):
    service.create_heart_rate_record(request)
    return request

@router.post("/heart-rate/polar-mx2/", status_code=status.HTTP_201_CREATED)
async def register_polar_mx2(request: PolarMX2):    
    service.create_heart_rate_record(request)
    return request

@router.post("/blood-pressure/samsung-bpa/", status_code=status.HTTP_201_CREATED)
async def register_samsung_bpa(request: SamsungBPA):
    service.create_blood_pressure_record(request)
    return request

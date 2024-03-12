import uuid
import time
from fastapi import APIRouter, status
from datetime import datetime
from structlog import get_logger

from sensor_receiver_api.services.blood_pressure import BloodPressureService
from sensor_receiver_api.services.heart_rate import HeartRateService

from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import (
    SamsungBPA,
    Payload as BPAPayload
)
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import (
    SamsungX1S,
    Payload as X1SPayload
)


blood_pressure_service = BloodPressureService()
heart_rate_service = HeartRateService()
router = APIRouter()
log = get_logger()


def get_timestamp():
    date_time = datetime.now()
    return time.mktime(date_time.timetuple())

def create_SamsungX1S(hr: int, hrt: int, ts: float, repeat: int = 1) -> None:
    updated_ts = ts
    for _ in range(0, repeat):
        log.info(f"[MOCK] Creating SamsungX1S measure at timestamp: {updated_ts}")
        x1s = SamsungX1S(
            eui=uuid.uuid4(), 
            model="X1-S",
            version="1.1", 
            payload=X1SPayload(hr=hr, hrt=hrt), 
            ts=updated_ts
        )
        heart_rate_service.create(x1s)
        updated_ts = updated_ts + 30
    return updated_ts

def create_SamsungBPA(bp_sys: int, bp_dia: int, ts: float, repeat: int = 1) -> None:
    updated_ts = ts
    for _ in range(0, repeat):
        log.info(f"[MOCK] Creating SamsungBPA measure at timestamp: {updated_ts}")
        bpa = SamsungBPA(
            eui=uuid.uuid4(), 
            model="BPA", 
            version="1.3", 
            payload=BPAPayload(bp_sys=bp_sys, bp_dia=bp_dia), 
            ts=updated_ts
        )
        blood_pressure_service.create(bpa)
        updated_ts = updated_ts + 30
    return updated_ts


@router.post("/mock-success/", status_code=status.HTTP_201_CREATED)
def mock_success():
    ts_base = get_timestamp()
    
    create_SamsungBPA(10, 10, ts_base) # 1
    ts_base = create_SamsungX1S(10, 10, ts_base)
    
    create_SamsungBPA(11, 11, ts_base) # 2
    ts_base = create_SamsungX1S(10, 10, ts_base)

    create_SamsungBPA(10, 10, ts_base) # 3
    ts_base = create_SamsungX1S(9, 9, ts_base)

    create_SamsungBPA(11, 11, ts_base) # 4
    ts_base = create_SamsungX1S(11, 11, ts_base)

    create_SamsungBPA(12, 12, ts_base) # 5
    ts_base = create_SamsungX1S(13, 13, ts_base)

    create_SamsungBPA(9, 9, ts_base) # 6
    ts_base = create_SamsungX1S(12, 12, ts_base)
    
    create_SamsungBPA(10, 10, ts_base) # 7
    ts_base = create_SamsungX1S(13, 13, ts_base)

    create_SamsungBPA(10, 10, ts_base) # 8
    ts_base = create_SamsungX1S(10, 10, ts_base)

    return {"mock": "Finished!"} 

@router.post("/mock-fraud/", status_code=status.HTTP_201_CREATED)
def mock_fraud():
    ts_base = get_timestamp()
    
    create_SamsungBPA(10, 10, ts_base) # 1
    ts_base = create_SamsungX1S(10, 10, ts_base)
    
    create_SamsungBPA(12, 12, ts_base) # 2
    ts_base = create_SamsungX1S(10, 10, ts_base)

    create_SamsungBPA(12, 12, ts_base) # 3
    ts_base = create_SamsungX1S(10, 10, ts_base)

    create_SamsungBPA(12, 12, ts_base) # 4
    ts_base = create_SamsungX1S(13, 13, ts_base)

    create_SamsungBPA(12, 12, ts_base) # 5
    ts_base = create_SamsungX1S(13, 13, ts_base)

    create_SamsungBPA(10, 10, ts_base) # 6
    ts_base = create_SamsungX1S(13, 13, ts_base)
    
    create_SamsungBPA(10, 10, ts_base) # 7
    ts_base = create_SamsungX1S(10, 10, ts_base)

    return {"mock": "Finished!"} 

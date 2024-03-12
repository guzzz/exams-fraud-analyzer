from fastapi import FastAPI
from structlog import get_logger

from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import SamsungBPA
from sensor_receiver_api.registered_monitors.heart_rate.schemas.polarmx2 import PolarMX2
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import SamsungX1S

from sensor_receiver_api.schemas.requests import ProcessRequest
from sensor_receiver_api.schemas.responses import ProcessResponse
from sensor_receiver_api.services.facade import ServiceFacade

from sensor_receiver_api.controllers.mock import router as mock_router
from sensor_receiver_api.controllers.monitors import router as monitor_router

log = get_logger()

app = FastAPI(title="Sensor Receiver API")
app.include_router(
    mock_router,
    prefix="/v0",
    tags=["Mocks"]
)

app.include_router(
    monitor_router,
    prefix="/v0",
    tags=["Monitors"]
)

service = ServiceFacade()


@app.post("/v0/process/", response_model=ProcessResponse, tags=["Process"])
async def process(body: ProcessRequest):
    blood_pressures = service.get_blood_pressure_measures(body)
    bp_suspicious, bp_first_spike = service.check_blood_pressure_fraud(body, blood_pressures)

    heart_rates = service.get_heart_rate_measures(body)
    hr_suspicious, hr_first_spike = service.check_heart_rate_fraud(body, heart_rates)

    fraud_timing = service.check_spikes_fraud_timing(bp_first_spike, hr_first_spike)

    if bp_suspicious and hr_suspicious and fraud_timing:
        log.info("FRAUD_WARNING")
        return ProcessResponse.serialize(True, blood_pressures, heart_rates)
    else:
        log.info("[Result] NOT a fraud!")
        return ProcessResponse.serialize(False, blood_pressures, heart_rates)

@app.get("/health")
def health_check():
    return {"health": "OK!"}

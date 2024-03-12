
from sensor_receiver_api.registered_monitors.blood_pressure.adapters.samsung_bpa import SamsungBPAAdapter
from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import SamsungBPA
from sensor_receiver_api.registered_monitors.heart_rate.adapters.polarmx2 import PolarMX2Adapter
from sensor_receiver_api.registered_monitors.heart_rate.adapters.samsungx1s import SamsungX1SAdapter
from sensor_receiver_api.registered_monitors.heart_rate.schemas.polarmx2 import PolarMX2
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import SamsungX1S


BLOOD_PRESSURE_OPTIONS = (
    (SamsungBPA, lambda obj: SamsungBPAAdapter(obj)),
)

HEART_RATE_OPTIONS = (
    (SamsungX1S, lambda obj: SamsungX1SAdapter(obj)),
    (PolarMX2, lambda obj: PolarMX2Adapter(obj)),
)

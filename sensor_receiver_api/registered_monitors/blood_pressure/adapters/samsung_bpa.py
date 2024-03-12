
from sensor_receiver_api.models.blood_pressure import BloodPressure
from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import SamsungBPA


class SamsungBPAAdapter(BloodPressure):
    def __init__(self, samsung_bpa: SamsungBPA) -> None:
        self.device = samsung_bpa.model
        self.version = samsung_bpa.version
        self.systolic_bp = samsung_bpa.payload.bp_sys
        self.ts = samsung_bpa.ts

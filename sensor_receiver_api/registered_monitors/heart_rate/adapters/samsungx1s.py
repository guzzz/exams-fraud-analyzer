
from sensor_receiver_api.models.heart_rate import HeartRate
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import SamsungX1S


class SamsungX1SAdapter(HeartRate):
    def __init__(self, samsung_x1s: SamsungX1S) -> None:
        self.device = samsung_x1s.model
        self.version = samsung_x1s.version
        self.pulse = samsung_x1s.payload.hr
        self.ts = samsung_x1s.ts

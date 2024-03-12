
from sensor_receiver_api.models.heart_rate import HeartRate
from sensor_receiver_api.registered_monitors.heart_rate.schemas.polarmx2 import PolarMX2


def get_device(fw_received):
    try:
        return fw_received.split('/')[0]
    except:
        return fw_received
    
def get_version(fw_received):
    try:
        return fw_received.split('/')[1]
    except:
        return fw_received

class PolarMX2Adapter(HeartRate):
    def __init__(self, polar_mx2: PolarMX2) -> None:
        self.device = get_device(polar_mx2.fw)
        self.version = get_version(polar_mx2.fw)
        self.pulse = polar_mx2.pulse
        self.ts = polar_mx2.ts


from structlog import get_logger

from sensor_receiver_api.repositories.bpressure import BloodPressureRepository
from sensor_receiver_api.registered_monitors.workable_monitors import BLOOD_PRESSURE_OPTIONS
from sensor_receiver_api.services.fraud import FraudService

log = get_logger()


class BloodPressureService(FraudService):

    def __init__(self):
        self.__repository = BloodPressureRepository()

    def get_monitor_adapter(self, monitor):
        log.info("[Blood Pressure Service] Finding adapter...")
        return dict(BLOOD_PRESSURE_OPTIONS)[type(monitor)]

    def create(self, monitor_request):
        log.info("[Blood Pressure Service] Preparing to save measure...")
        adater = self.get_monitor_adapter(monitor_request)
        blood_pressure = adater(monitor_request)
        self.__repository.create(blood_pressure)
        return

    def check_fraud(self, data, blood_pressures):
        log.info("[Blood Pressure Service] Preparing analysis ...")
        baseline = data.base_blood_pressure
        monitor_key = "systolic_bp"
        increase_factor = 1.2
        max_spikes_sequence = 4
        return self.analysis(
            baseline, blood_pressures, monitor_key, increase_factor, max_spikes_sequence
        )

    def get_measures(self, data):
        log.info("[Blood Service Service] Setting searching params...")
        start_timestamp = data.start_time
        end_timestamp = data.end_time
        bp_monitor_device = data.pressure_monitor_device
        bp_monitor_version = data.pressure_monitor_version
        hr_monitor_device = data.hearth_monitor_device
        hr_monitor_version = data.hearth_monitor_version
        
        return self.__repository.find_between_timestamps(
            start_timestamp, 
            end_timestamp, 
            bp_monitor_device, 
            bp_monitor_version,
            hr_monitor_device,
            hr_monitor_version
        )
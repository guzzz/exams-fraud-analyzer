
from structlog import get_logger

from sensor_receiver_api.repositories.hrate import HearthRateRepository
from sensor_receiver_api.registered_monitors.workable_monitors import HEART_RATE_OPTIONS
from sensor_receiver_api.services.fraud import FraudService

log = get_logger()


class HeartRateService(FraudService):

    def __init__(self):
        self.__repository = HearthRateRepository()

    def get_monitor_adapter(self, monitor):
        log.info("[Heart Rate Service] Finding adapter...")
        return dict(HEART_RATE_OPTIONS)[type(monitor)]

    def create(self, monitor_request):
        log.info("[Heart Rate Service] Preparing to save measure...")
        adater = self.get_monitor_adapter(monitor_request)
        blood_pressure = adater(monitor_request)
        self.__repository.create(blood_pressure)
        return
    
    def check_fraud(self, data, hearth_rates):
        log.info("[Heart Rate Service] Preparing analysis ...")
        baseline = data.base_hearth_rate
        monitor_key = "pulse"
        increase_factor = 1.3
        max_spikes_sequence = 3
        
        return self.analysis(
            baseline, hearth_rates, monitor_key, increase_factor, max_spikes_sequence
        )
    
    def get_measures(self, data):
        log.info("[Heart Rate Service] Setting searching params...")
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

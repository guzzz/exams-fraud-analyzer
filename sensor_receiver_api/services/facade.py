
from structlog import get_logger

from sensor_receiver_api.services.blood_pressure import BloodPressureService
from sensor_receiver_api.services.heart_rate import HeartRateService

log = get_logger()


class ServiceFacade:
    def __init__(self) -> None:
        self._bp_service = BloodPressureService()
        self._hr_service = HeartRateService()

    def create_blood_pressure_record(self, monitor_request):
        return self._bp_service.create(monitor_request)

    def get_blood_pressure_measures(self, data):
        return self._bp_service.get_measures(data)
    
    def check_blood_pressure_fraud(self, data, blood_pressures):
        return self._bp_service.check_fraud(data, blood_pressures)
    
    def create_heart_rate_record(self, monitor_request):
        return self._hr_service.create(monitor_request)

    def get_heart_rate_measures(self, data):
        return self._hr_service.get_measures(data)
    
    def check_heart_rate_fraud(self, data, heart_rates):
        return self._hr_service.check_fraud(data, heart_rates)
    
    def check_spikes_fraud_timing(self, bp_first_spike, hr_first_spike):
        log.info("[Service] Checking time difference between spikes...")
        if not bp_first_spike or not hr_first_spike:
            return False
        hr_range_start = bp_first_spike + 60
        hr_range_end = bp_first_spike + 90

        return hr_range_start <= hr_first_spike < hr_range_end

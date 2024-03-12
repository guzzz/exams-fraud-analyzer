import pytz
from structlog import get_logger
from datetime import datetime

from events.models import Event
from evidences.models import BloodPressureEvidence, HeartRateEvidence
from sensor_integration.api import SensorAPI

log = get_logger()


class EventService:

    def __init__(self):
        self._sensor_api = SensorAPI()

    def get_event(self, id: int) -> Event: 
        return Event.objects.filter(id=id).first()
    
    def generate_bp_evidences(self, event: Event, blood_pressures: list):
        log.info("[Event Service] Generating Blood Pressure Evidence Infos...")
        datetime_converter = lambda item: datetime.fromtimestamp(item.get("ts"), tz=pytz.UTC)
        systolic_bp = lambda item: item.get("systolic_bp")        
        generate_bp = lambda item: BloodPressureEvidence(
            event=event, 
            systolic_bp=systolic_bp(item), 
            date=datetime_converter(item)
        )
        return [generate_bp(item) for item in blood_pressures]
    
    def generate_hr_evidences(self, event: Event, heart_rates: list):
        log.info("[Event Service] Generating Heart Rate Evidence Infos...")
        datetime_converter = lambda item: datetime.fromtimestamp(item.get("ts"), tz=pytz.UTC)
        pulse = lambda item: item.get("pulse")        
        generate_hr = lambda item: HeartRateEvidence(
            event=event, 
            pulse=pulse(item), 
            date=datetime_converter(item)
        )
        return [generate_hr(item) for item in heart_rates]
    
    def save_evidences(self, event_id: int, blood_pressures: list, heart_rates: list):
        event = self.get_event(event_id)

        bp_evidences = self.generate_bp_evidences(event, blood_pressures)
        hr_evidences = self.generate_hr_evidences(event, heart_rates)

        log.info("[Event Service] Saving evidences...")
        BloodPressureEvidence.objects.bulk_create(bp_evidences)
        HeartRateEvidence.objects.bulk_create(hr_evidences)
        return

    def process_integration(self, event):
        log.info("[Event Service] Process through integration...")
        result = self._sensor_api.process(event)
        is_fraud_result = result.get("is_fraud")

        bp_evidences = result.get("blood_pressure_evidences")
        hr_evidences = result.get("heart_rate_evidences")

        graph_data = self.get_graph_data(bp_evidences, hr_evidences)

        if is_fraud_result:
            bp_evidences = result.get("blood_pressure_evidences")
            hr_evidences = result.get("heart_rate_evidences")
            self.save_evidences(event.id, bp_evidences, hr_evidences)
            
        return is_fraud_result, graph_data

    def get_graph_data(self, bp_list, hr_list):
        log.info("[Event Service] Generating graph data...")
        bp_x, bp_y = self.generate_blood_pressure_graph(bp_list)
        hr_x, hr_y = self.generate_heart_rate_graph(hr_list)
        return {
            'bp_x': bp_x,
            'bp_y': bp_y,
            'hr_x': hr_x,
            'hr_y': hr_y
        }
    
    def generate_blood_pressure_graph(self, bp_list):
        bp_x = [str(i) for i in range(1, len(bp_list)+1)]
        bp_y = [i.get('systolic_bp') for i in bp_list]
        return bp_x, bp_y
    
    def generate_heart_rate_graph(self, hr_list):
        hr_x = [str(i) for i in range(1, len(hr_list)+1)]
        hr_y = [i.get('pulse') for i in hr_list]
        return hr_x, hr_y

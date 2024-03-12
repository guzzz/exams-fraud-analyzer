
import pytz
from django.test import TestCase

from events.models import Event
from events.services import EventService
from evidences.models import BloodPressureEvidence, HeartRateEvidence
from persons.models import Person
from monitors.models import Monitor
from datetime import datetime

def now():
    return datetime.now(tz=pytz.UTC)

class EventUnitTest(TestCase):
    event = None
    event_service = EventService()

    @classmethod
    def setUpClass(cls):
        super(EventUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Event SERVICE Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        bp_monitor = Monitor.objects.create(
            device='aa',
            version='aa',
            type='BLOOD_PRESSURE'
        )
        hr_monitor = Monitor.objects.create(
            device='aa',
            version='aa',
            type='HEART_RATE'
        )
        person = Person.objects.create(
            name = 'Daniel',
            surname = 'Guzman',
            age = 100
        )
        event = Event.objects.create(
            title = '',
            base_blood_pressure = 1,
            base_heart_rate = 1,
            start_date = now(),
            end_date = now(),
            is_fraud = None,
            person = person,
            blood_pressure_monitor = bp_monitor,
            heart_rate_monitor = hr_monitor
        )
        print("----------------------------------------------------------------------")

    def test_generate_bp_evidences_fail(self):
        print("==> generate_bp_evidences FAIL CASE")
        empty_list = self.event_service.generate_bp_evidences(self.event, [])
        self.assertEqual(empty_list, [])
        print("----------------------------------------------------------------------")

    def test_generate_bp_evidences_success(self):
        print("==> generate_bp_evidences SUCCESS CASE")
        test_timestamp = now().timestamp()
        blood_pressure = 10
        blood_pressures = [{"systolic_bp": blood_pressure, "ts": test_timestamp}]
        evidences = [BloodPressureEvidence(
            systolic_bp = blood_pressure,
            event = self.event,
            date = None
        )]
        bp_evidences = self.event_service.generate_bp_evidences(self.event, blood_pressures)
        self.assertEqual(len(bp_evidences), len(evidences))
        self.assertEqual(bp_evidences[0].systolic_bp, evidences[0].systolic_bp)
        print("----------------------------------------------------------------------")

    def test_generate_hr_evidences_fail(self):
        print("==> generate_hr_evidences FAIL CASE")
        empty_list = self.event_service.generate_hr_evidences(self.event, [])
        self.assertEqual(empty_list, [])
        print("----------------------------------------------------------------------")

    def test_generate_hr_evidences_success(self):
        print("==> generate_hr_evidences SUCCESS CASE")
        test_timestamp = now().timestamp()
        pulse = 10
        heart_rates = [{"pulse": pulse, "ts": test_timestamp}]
        evidences = [HeartRateEvidence(
            pulse = pulse,
            event = self.event,
            date = None
        )]
        hr_evidences = self.event_service.generate_hr_evidences(self.event, heart_rates)
        self.assertEqual(len(hr_evidences), len(evidences))
        self.assertEqual(hr_evidences[0].pulse, evidences[0].pulse)
        print("----------------------------------------------------------------------")


    def test_generate_blood_pressure_graph_fail(self):
        print("==> generate_blood_pressure_graph FAIL CASE")
        empty_list = self.event_service.generate_blood_pressure_graph([])
        self.assertEqual(empty_list, ([],[]))
        print("----------------------------------------------------------------------")

    def test_generate_blood_pressure_graph_success(self):
        print("==> generate_blood_pressure_graph SUCCESS CASE")
        initial_data = [{'systolic_bp': 10}]
        result = self.event_service.generate_blood_pressure_graph(initial_data)
        self.assertEqual(result, (['1'],[10]))
        print("----------------------------------------------------------------------")

    def test_generate_heart_rate_graph_fail(self):
        print("==> generate_heart_rate_graph FAIL CASE")
        empty_list = self.event_service.generate_heart_rate_graph([])
        self.assertEqual(empty_list, ([],[]))
        print("----------------------------------------------------------------------")

    def test_generate_heart_rate_graph_success(self):
        print("==> generate_heart_rate_graph SUCCESS CASE")
        initial_data = [{'pulse': 10}]
        result = self.event_service.generate_heart_rate_graph(initial_data)
        self.assertEqual(result, (['1'],[10]))
        print("----------------------------------------------------------------------")

    def test_get_graph_data_fail(self):
        print("==> get_graph_data FAIL CASE")
        response = self.event_service.get_graph_data([], [])
        expected_response = {
            'bp_x': [],
            'bp_y': [],
            'hr_x': [],
            'hr_y': []
        }
        self.assertEqual(response, expected_response)
        print("----------------------------------------------------------------------")

    def test_get_graph_data_success(self):
        print("==> get_graph_data SUCCESS CASE")
        test_timestamp = now().timestamp()
        param_1 = [{"systolic_bp": 10, "ts": test_timestamp}]
        param_2 = [{"pulse": 10, "ts": test_timestamp}]
        response = self.event_service.get_graph_data(param_1, param_2)
        expected_response = {
            'bp_x': ['1'],
            'bp_y': [10],
            'hr_x': ['1'],
            'hr_y': [10]
        }
        self.assertEqual(response, expected_response)
        print("----------------------------------------------------------------------")

import pytz

from django.test import TestCase
from datetime import datetime

from monitors.models import Monitor
from persons.models import Person
from events.models import Event


def now():
    return datetime.now(tz=pytz.UTC)

def get_monitor():
    return Monitor.objects.create(
        device='bp',
        version='1',
        type='BLOOD_PRESSURE'
    )
    
def get_person():
    return Person.objects.create(
        name = 'Jon',
        surname = 'Snow',
        age = 100
    )


class EventUnitTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(EventUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Event MODEL Tests...")
        print("======================================================================")

    def test_model_success(self):
        print("==> create_Event SUCCESS CASE")
        event = Event.objects.create(
            title = 'Some title',
            base_blood_pressure = 1,
            base_heart_rate = 1,
            start_date = now(),
            end_date = now(),
            is_fraud = None,
            person = get_person(),
            blood_pressure_monitor = get_monitor(),
            heart_rate_monitor = get_monitor()
        )
        self.assertEqual(event.title, 'Some title')
        print("----------------------------------------------------------------------")

    def test_model_little_error(self):
        print("==> create_Event FAIL CASE")
        with self.assertRaises(Exception):
            event = Event.objects.create(title='Little event')
        print("----------------------------------------------------------------------")

    def test_model_no_person_error(self):
        print("==> create_Event no person ERROR CASE")
        with self.assertRaises(Exception):
            event = Event.objects.create(
                title = 'Some title',
                base_blood_pressure = 1,
                base_heart_rate = 1,
                start_date = now(),
                end_date = now(),
                is_fraud = None,
                person = None,
                blood_pressure_monitor = get_monitor(),
                heart_rate_monitor = get_monitor()
            )
        print("----------------------------------------------------------------------")

    def test_model_no_bp_monitor_error(self):
        print("==> create_Event no blood pressure monitor ERROR CASE")
        with self.assertRaises(Exception):
            event = Event.objects.create(
                title = 'Some title',
                base_blood_pressure = 1,
                base_heart_rate = 1,
                start_date = now(),
                end_date = now(),
                is_fraud = None,
                person = get_person(),
                blood_pressure_monitor = None,
                heart_rate_monitor = get_monitor()
            )
        print("----------------------------------------------------------------------")

    def test_model_no_hr_monitor_error(self):
        print("==> create_Event no heart rate monitor ERROR CASE")
        with self.assertRaises(Exception):
            event = Event.objects.create(
                title = 'Some title',
                base_blood_pressure = 1,
                base_heart_rate = 1,
                start_date = now(),
                end_date = now(),
                is_fraud = None,
                person = get_person(),
                blood_pressure_monitor = get_monitor(),
                heart_rate_monitor = None
            )
        print("----------------------------------------------------------------------")



import pytz

from django.test import TestCase
from datetime import datetime

from evidences.models import BloodPressureEvidence, HeartRateEvidence
from monitors.models import Monitor
from persons.models import Person
from events.models import Event


def now():
    return datetime.now(tz=pytz.UTC)

def get_event():
    bp_monitor = Monitor.objects.create(
        device='bp',
        version='1',
        type='BLOOD_PRESSURE'
    )
    hr_monitor = Monitor.objects.create(
        device='hr',
        version='2',
        type='HEART_RATE'
    )
    person = Person.objects.create(
        name = 'Jon',
        surname = 'Snow',
        age = 100
    )
    return Event.objects.create(
            title = 'Some title',
            base_blood_pressure = 1,
            base_heart_rate = 1,
            start_date = now(),
            end_date = now(),
            is_fraud = None,
            person = person,
            blood_pressure_monitor = bp_monitor,
            heart_rate_monitor = hr_monitor
        )


class BloodPressureEvidenceUnitTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BloodPressureEvidenceUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING BloodPressureEvidence MODEL Tests...")
        print("======================================================================")

    def test_model_success(self):
        print("==> create_BloodPressureEvidence SUCCESS CASE")
        bp_evidence = BloodPressureEvidence.objects.create(systolic_bp=10, event=get_event(), date=now())
        self.assertEqual(bp_evidence.systolic_bp, 10)
        print("----------------------------------------------------------------------")

    def test_model_error(self):
        print("==> create_BloodPressureEvidence FAIL CASE")
        with self.assertRaises(Exception):
            bp_evidence = BloodPressureEvidence.objects.create(systolic_bp=10, event=None, date=now())
        print("----------------------------------------------------------------------")


class HeartRateEvidenceUnitTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(HeartRateEvidenceUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING HeartRateEvidence MODEL Tests...")
        print("======================================================================")

    def test_model_success(self):
        print("==> create_HeartRateEvidence SUCCESS CASE")
        hr_evidence = HeartRateEvidence.objects.create(pulse=10, event=get_event(), date=now())
        self.assertEqual(hr_evidence.pulse, 10)
        print("----------------------------------------------------------------------")

    def test_model_error(self):
        print("==> create_HeartRateEvidence FAIL CASE")
        with self.assertRaises(Exception):
            hr_evidence = HeartRateEvidence.objects.create(pulse=10, event=None, date=now())
        print("----------------------------------------------------------------------")

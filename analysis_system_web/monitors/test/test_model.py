
from django.test import TestCase
from monitors.models import Monitor


class MonitorUnitTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(MonitorUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Monitor MODEL Tests...")
        print("======================================================================")

    def test_model_success(self):
        print("==> create_monitor SUCCESS CASE")
        monitor = Monitor(device='Samsung', version='A', type='BLOOD_PRESSURE')
        self.assertEqual(monitor.device, 'Samsung')
        print("----------------------------------------------------------------------")

    def test_model_error(self):
        print("==> create_monitor FAIL CASE")
        with self.assertRaises(Exception):
            monitor = Monitor(device='Samsung', description='Good Monitor')
        print("----------------------------------------------------------------------")

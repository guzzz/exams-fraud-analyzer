
import uuid
from datetime import datetime 

from sensor_receiver_api.registered_monitors.heart_rate.adapters.samsungx1s import SamsungX1SAdapter 
from sensor_receiver_api.registered_monitors.heart_rate.schemas.samsungx1s import SamsungX1S, Payload as X1SPayload
from sensor_receiver_api.services.heart_rate import HeartRateService

from sensor_receiver_api.registered_monitors.blood_pressure.adapters.samsung_bpa import SamsungBPAAdapter
from sensor_receiver_api.registered_monitors.blood_pressure.schemas.samsung_bpa import SamsungBPA, Payload as BPAPayload
from sensor_receiver_api.services.blood_pressure import BloodPressureService

from sensor_receiver_api.services.facade import ServiceFacade

bp_service = BloodPressureService()
hr_service = HeartRateService()
service = ServiceFacade()


def now():
    return datetime.now().timestamp()

def test_get_bpa_monitor_adapter_success():
    bpa = SamsungBPA(
        eui=uuid.uuid4(), 
        model="BPA", 
        version="1.3", 
        payload=BPAPayload(bp_sys=1, bp_dia=1), 
        ts=now()
    )
    expected_response = lambda obj: SamsungBPAAdapter(obj)
    response = bp_service.get_monitor_adapter(bpa)
    assert type(response) == type(expected_response)

def test_get_bpa_monitor_adapter_error():
    bpa = ""
    try:
        bp_service.get_monitor_adapter(bpa)
    except Exception:
        assert True


def test_blood_pressure_suspicius_false():
    class Object(object):
        pass

    data = Object()
    data.base_blood_pressure = 10
    blood_pressures = [
         {'ts': 10, 'systolic_bp': 10},
         {'ts': 40, 'systolic_bp': 10},
         {'ts': 70, 'systolic_bp': 10},
         {'ts': 100, 'systolic_bp': 10},
         {'ts': 130, 'systolic_bp': 10},
         {'ts': 160, 'systolic_bp': 10}
    ]
    is_fraud, first_spike = bp_service.check_fraud(data, blood_pressures)
    assert is_fraud == False
    assert first_spike == None

def test_blood_pressure_suspicius_true():
    class Object(object):
        pass

    data = Object()
    data.base_blood_pressure = 10
    blood_pressures = [
         {'ts': 10, 'systolic_bp': 10},
         {'ts': 40, 'systolic_bp': 12},
         {'ts': 70, 'systolic_bp': 12},
         {'ts': 100, 'systolic_bp': 12},
         {'ts': 130, 'systolic_bp': 12},
         {'ts': 160, 'systolic_bp': 10}
    ]
    is_fraud, first_spike = bp_service.check_fraud(data, blood_pressures)
    assert is_fraud == True
    assert first_spike == 40

def test_get_x1s_monitor_adapter_success():
    x1s = SamsungX1S(
        eui=uuid.uuid4(), 
        model="X1-S",
        version="1.1", 
        payload=X1SPayload(hr=10, hrt=10), 
        ts=now()
    )
    expected_response = lambda obj: SamsungX1SAdapter(obj)
    response = hr_service.get_monitor_adapter(x1s)
    assert type(response) == type(expected_response)

def test_get_x1s_monitor_adapter_error():
    x1s = 1
    try:
        hr_service.get_monitor_adapter(x1s)
    except Exception:
        assert True


def test_heart_rate_suspicius_false():
    class Object(object):
        pass

    data = Object()
    data.base_hearth_rate = 10
    blood_pressures = [
         {'ts': 10, 'pulse': 10},
         {'ts': 40, 'pulse': 10},
         {'ts': 70, 'pulse': 10},
         {'ts': 100, 'pulse': 10},
         {'ts': 130, 'pulse': 10},
         {'ts': 160, 'pulse': 10}
    ]
    is_fraud, first_spike = hr_service.check_fraud(data, blood_pressures)
    assert is_fraud == False
    assert first_spike == None

def test_heart_rate_suspicius_true():
    class Object(object):
        pass

    data = Object()
    data.base_hearth_rate = 10
    blood_pressures = [
         {'ts': 10, 'pulse': 10},
         {'ts': 40, 'pulse': 10},
         {'ts': 70, 'pulse': 13},
         {'ts': 100, 'pulse': 13},
         {'ts': 130, 'pulse': 13},
         {'ts': 160, 'pulse': 10}
    ]
    is_fraud, first_spike = hr_service.check_fraud(data, blood_pressures)
    assert is_fraud == True
    assert first_spike == 70

def test_check_spikes_fraud_timing_is_fraud():
    resp = service.check_spikes_fraud_timing(1, 61)
    assert True == resp

def test_check_spikes_fraud_timing_is_not_fraud():
    resp = service.check_spikes_fraud_timing(1, 60)
    assert False == resp

def test_check_spikes_fraud_timing_is_not_fraud_waited_too_long():
    resp = service.check_spikes_fraud_timing(1, 120)
    assert False == resp

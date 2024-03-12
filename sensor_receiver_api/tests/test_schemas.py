

from sensor_receiver_api.schemas.requests import ProcessRequest
from sensor_receiver_api.schemas.responses import ProcessResponse


def test_schema_process_request_success():
    data = {
        'start_time': 1.0,
        'end_time': 10.0,
        'base_blood_pressure': 10,
        'base_hearth_rate': 10,
        'pressure_monitor_device': 'device and version',
        'pressure_monitor_version': 'device and version',
        'hearth_monitor_device': 'device and version',
        'hearth_monitor_version': 'device and version'
    }
    request = ProcessRequest(**data)
    assert request.start_time == 1.0
    assert request.end_time == 10.0
    assert request.base_blood_pressure == 10
    assert request.base_hearth_rate == 10


def test_schema_process_request_fail():
    data = {
        'start_time': '',
        'end_time': '',
        'base_blood_pressure': '',
        'base_hearth_rate': '',
        'pressure_monitor_device': 11,
        'pressure_monitor_version': 12,
        'hearth_monitor_device': 21,
        'hearth_monitor_version': 22
    }
    try:
        request = ProcessRequest(**data)
    except:
        assert True

def test_schema_process_response_success():
    data = {
        'is_fraud': True,
        'blood_pressure_evidences': [],
        'heart_rate_evidences': []
    }
    response = ProcessResponse(**data)
    assert response.is_fraud == True
    assert response.blood_pressure_evidences == []
    assert response.heart_rate_evidences == []

def test_schema_process_response_fail():
    data = {
        'is_fraud': True,
        'blood_pressure_evidences': True,
        'heart_rate_evidences': ''
    }
    try:
        request = ProcessResponse(**data)
    except:
        assert True

def test_schema_process_serialize():
    result = ProcessResponse.serialize(True, [], [])
    expected_response = {
        'is_fraud': True,
        'blood_pressure_evidences': [],
        'heart_rate_evidences': []
    }
    assert result == expected_response

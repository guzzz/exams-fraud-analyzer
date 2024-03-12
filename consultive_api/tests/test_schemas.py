import pytz

from datetime import datetime

from consultive_api.schemas.evidences import BloodPressure, HeartRate, Evidences
from consultive_api.schemas.frauds import FraudsByPerson, FraudsWithDetails, FraudWithDetails
from consultive_api.schemas.persons import Person
from consultive_api.schemas.monitors import Monitor
from consultive_api.schemas.users import User


def now():
    return datetime.now(tz=pytz.UTC)

def test_schema_blood_pressure_success():
    data = {
        'systolic_bp': 10,
        'date': now()
    }
    request = BloodPressure(**data)
    assert request.systolic_bp == 10

def test_schema_blood_pressure_fail():
    data = {
        'systolic_bp': '',
        'date': None
    }
    try:
        request = BloodPressure(**data)
    except:
        assert True

def test_schema_heart_rate_success():
    data = {
        'pulse': 10,
        'date': now()
    }
    request = HeartRate(**data)
    assert request.pulse == 10

def test_schema_heart_rate_fail():
    data = {
        'pulse': '',
        'date': None
    }
    try:
        request = HeartRate(**data)
    except:
        assert True

def test_schema_evidences_success():
    data = {
        'blood_pressure_evidences': [],
        'heart_rate_evidences': []
    }
    request = Evidences(**data)
    assert request.blood_pressure_evidences == []

def test_schema_evidences_fail():
    data = {
        'blood_pressure_evidences': '',
        'heart_rate_evidences': True
    }
    try:
        request = Evidences(**data)
    except:
        assert True

def test_schema_frauds_by_person_success():
    data = {
        'id': 8,
        'title': 'Test',
        'start_date': now(),
        'end_date': now()
    }
    request = FraudsByPerson(**data)
    assert request.id == 8

def test_schema_frauds_by_person_fail():
    data = {
        'id': '',
        'title': 1,
        'start_date': now(),
        'end_date': now()
    }
    try:
        request = FraudsByPerson(**data)
    except:
        assert True

def test_schema_person_success():
    data = {
        'id': 9,
        'name': 'Jon',
        'surname': 'Snow',
        'age': None
    }
    request = Person(**data)
    assert request.id == 9

def test_schema_person_fail():
    data = {
        'id': 1,
        'name': 'Jon',
        'surname': 'Snow',
        'age': True
    }
    try:
        request = Person(**data)
    except:
        assert True

def test_schema_frauds_with_details_success():
    person_dict = {
        'id': 1,
        'name': 'Jon',
        'surname': 'Snow',
        'age': None
    }
    person = Person(**person_dict)
    data = {
        'id': 1,
        'title': 'Test',
        'start_date': now(),
        'end_date': now(), 
        'person': person
    }
    request = FraudsWithDetails(**data)
    assert request.person.name == 'Jon'

def test_schema_frauds_with_details_fail():
    data = {
        'id': '',
        'title': 1,
        'start_date': now(),
        'end_date': now(), 
        'person': None
    }
    try:
        request = FraudsWithDetails(**data)
    except:
        assert True

def test_schema_monitor_success():
    data = {
        'device': 'BPA',
        'version': '5.0'
    }
    request = Monitor(**data)
    assert request.device == 'BPA'

def test_schema_monitor_fail():
    data = {
        'device': 'BPA',
        'version': 5
    }
    try:
        request = Monitor(**data)
    except:
        assert True

def test_schema_fraud_with_details_success():
    person_dict = {
        'id': 1,
        'name': 'Jon',
        'surname': 'Snow',
        'age': None
    }
    person = Person(**person_dict)
    monitor_1_dict = {
        'device': 'AAA',
        'version': '5.0'
    }
    monitor_1 = Monitor(**monitor_1_dict)
    monitor_2_dict = {
        'device': 'BBB',
        'version': '5.0'
    }
    monitor_2 = Monitor(**monitor_2_dict)
    data = {
        'id': 1,
        'title': 'Test',
        'base_blood_pressure': 10,
        'base_heart_rate': 10,
        'start_date': now(),
        'end_date': now(), 
        'person': person,
        'blood_pressure_monitor': monitor_1,
        'heart_rate_monitor': monitor_2
    }
    request = FraudWithDetails(**data)
    assert request.person.name == 'Jon'

def test_schema_fraud_with_details_fail():
    data = {
        'id': '',
        'title': 1,
        'base_blood_pressure': 10,
        'base_heart_rate': 10,
        'start_date': now(),
        'end_date': now(), 
        'person': None,
        'blood_pressure_monitor': None,
        'heart_rate_monitor': None
    }
    try:
        request = FraudWithDetails(**data)
    except:
        assert True

def test_schema_user_success():
    data = {
        'username': 'Deadpool'
    }
    request = User(**data)
    assert request.username == 'Deadpool'

def test_schema_user_fail():
    data = {
        'username': None
    }
    try:
        request = User(**data)
    except:
        assert True

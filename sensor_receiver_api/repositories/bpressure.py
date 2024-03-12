
from sensor_receiver_api.config.db import mongoclient
from sensor_receiver_api.repositories.sensor import SensorRepository


class BloodPressureRepository(SensorRepository):

    def __init__(self):
        database = mongoclient.local
        self._table = database.blood_pressure

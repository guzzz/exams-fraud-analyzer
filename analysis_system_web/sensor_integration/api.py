import os
import requests
from structlog import get_logger

from events.schemas import Requests

log = get_logger()


class SensorAPI:
    def __init__(self) -> None:
        self._url = os.getenv('SENSOR_API_URL')

    def __post(self, endpoint, body):
        try: 
            resp = requests.post(url=endpoint, json=body)
            log.info("[API Integration] Sucessful Request")
            return resp.json()
        except ConnectionError:
            log.info("[API Integration] Connection Error")
            raise ConnectionError

    def process(self, event):
        endpoint = f"{self._url}/v0/process/" 
        body = Requests.process_body(event)
        return self.__post(endpoint, body)

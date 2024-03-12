from fastapi.encoders import jsonable_encoder
from structlog import get_logger

log = get_logger()


class SensorRepository:

    def __init__(self):
        self._table = None

    def find_between_timestamps(self, start, end, bp_monit_device, bp_monit_version, hr_monit_device, hr_monit_version):
        log.info(f"[DB] Looking for data between timestamps: {start} and {end}")
        return self._find(start, end, bp_monit_device, bp_monit_version, hr_monit_device, hr_monit_version) 

    def _find(self, start, end, bp_monit_device, bp_monit_version, hr_monit_device, hr_monit_version):
        query = {
            "ts": {'$lte': end, '$gte': start},
            "$or": [
                {
                    'device': bp_monit_device,
                    'version': bp_monit_version
                },
                {
                    'device': hr_monit_device,
                    'version': hr_monit_version
                },
            ]
        }
        result = self._table.find(query, {'_id': False})
        return list(result)

    def create(self, data):
        log.info("[DB] Registering data...")
        data = jsonable_encoder(data)
        return self._table.insert_one(data)

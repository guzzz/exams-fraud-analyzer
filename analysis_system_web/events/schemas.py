
import time


class Requests:

    @staticmethod
    def process_body(event):
        return {
            'start_time': time.mktime(event.start_date.timetuple()),
            'end_time': time.mktime(event.end_date.timetuple()),
            'base_blood_pressure': event.base_blood_pressure,
            'base_hearth_rate': event.base_heart_rate,
            'pressure_monitor_device': event.blood_pressure_monitor.device,
            'pressure_monitor_version': event.blood_pressure_monitor.version,
            'hearth_monitor_device': event.heart_rate_monitor.device,
            'hearth_monitor_version': event.heart_rate_monitor.version
        }

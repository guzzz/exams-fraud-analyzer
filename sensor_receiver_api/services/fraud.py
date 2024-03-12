from structlog import get_logger

log = get_logger()


class FraudService:

    def __init__(self):
        pass

    def analysis(self, baseline: int, measure_data: list, monitor_key: str, increase_factor: float, max_spikes_sequence: int):
        spikes = 0
        spike_timestamp_records = []
        exceed_value = int(baseline * increase_factor)

        measure_analysis = lambda ts: add(ts) if measure >= exceed_value else sub()

        def add(timestamp):
            spike_timestamp_records.append(timestamp)
            return (spikes + 1)
        
        def sub():
            if spikes > 0:
                spike_timestamp_records[:-1]
                return (spikes - 1)
            return spikes
        
        for item in measure_data:
            timestamp = item.get('ts')
            measure = item.get(monitor_key)
            spikes = measure_analysis(timestamp)

            if spikes == max_spikes_sequence:
                log.info("[Fraud Service] Spikes are suspicious...")
                return True, spike_timestamp_records[0]

        log.info("[Fraud Service] Spikes are safe...")
        return False, None




from sqlalchemy.orm import Session
from structlog import get_logger

from consultive_api.models.evidences import BloodPressureEvidence, HeartRateEvidence

log = get_logger()


class EvidenceRepository:

    def __init__(self):
        pass

    def blood_pressure_list(self, db: Session, event_id: int):
        log.info("[DB] Listing Blood Pressure Evidences...")
        return db.query(BloodPressureEvidence).filter(BloodPressureEvidence.event_id == event_id).all()
    
    def heart_rate_list(self, db: Session, event_id: int):
        log.info("[DB] Listing Heart Rate Evidences...")
        return db.query(HeartRateEvidence).filter(HeartRateEvidence.event_id == event_id).all()

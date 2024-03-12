

from sqlalchemy.orm import Session
from structlog import get_logger
from sqlalchemy import and_

from consultive_api.models.events import Event

log = get_logger()


class FraudRepository:

    def __init__(self):
        pass

    def retrieve(self, db: Session, id: str):
        log.info("[DB] Searching Fraud...")
        return db.query(Event).filter(and_(Event.id == id, Event.is_fraud == True)).first()

    def list(self, db: Session, page, limit, person_id_filter):
        log.info(f"[DB] Listing Frauds page {page}, page_size: {limit}.")
        to_start = (page-1)*limit
        if person_id_filter:
            person_id = str(person_id_filter)
            return db.query(Event).filter(and_(Event.person_id == person_id, Event.is_fraud == True)).offset(to_start).limit(limit).all()
        else:
            return db.query(Event).filter(Event.is_fraud == True).offset(to_start).limit(limit).all()

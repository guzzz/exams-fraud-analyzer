

from sqlalchemy.orm import Session
from structlog import get_logger

from consultive_api.models.persons import Person

log = get_logger()


class PersonRepository:

    def __init__(self):
        pass

    def retrieve(self, db: Session, id: str):
        log.info("[DB] Searching Person...")
        return db.query(Person).filter(Person.id == id).first()

    def list(self, db: Session, page, limit):
        log.info(f"[DB] Listing Persons page {page}, page_size: {limit}.")
        to_start = (page-1)*limit
        return db.query(Person).offset(to_start).limit(limit).all()

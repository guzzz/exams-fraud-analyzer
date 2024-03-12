

from sqlalchemy.orm import Session
from structlog import get_logger
from sqlalchemy import and_

from consultive_api.models.users import User

log = get_logger()


class UserRepository:

    def __init__(self):
        pass

    def retrieve(self, db: Session, username: str):
        log.info("[DB] Searching User...")
        return db.query(User).filter(and_(User.username == username, User.is_active == True)).first()

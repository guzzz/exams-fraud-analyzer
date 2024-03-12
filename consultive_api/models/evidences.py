
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from consultive_api.config.database import Base
from consultive_api.models.events import Event


class BloodPressureEvidence(Base):
    __tablename__ = "evidences_bloodpressureevidence"

    id = Column(Integer, primary_key=True)
    systolic_bp = Column(Integer)
    date = Column(String)

    event_id = Column(Integer, ForeignKey("events_event.id"))
    event = relationship(Event, foreign_keys=[event_id])


class HeartRateEvidence(Base):
    __tablename__ = "evidences_heartrateevidence"

    id = Column(Integer, primary_key=True)
    pulse = Column(Integer)
    date = Column(String)

    event_id = Column(Integer, ForeignKey("events_event.id"))
    event = relationship(Event, foreign_keys=[event_id])

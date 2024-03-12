
from consultive_api.models.persons import Person
from consultive_api.models.monitors import Monitor
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from consultive_api.config.database import Base


class Event(Base):
    __tablename__ = "events_event"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    base_blood_pressure = Column(Integer)
    base_heart_rate = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    is_fraud = Column(Boolean)

    blood_pressure_monitor_id = Column(Integer, ForeignKey("monitors_monitor.id", ondelete='CASCADE'))
    blood_pressure_monitor = relationship(Monitor, foreign_keys=[blood_pressure_monitor_id])

    heart_rate_monitor_id = Column(Integer, ForeignKey("monitors_monitor.id", ondelete='CASCADE'))
    heart_rate_monitor = relationship(Monitor, foreign_keys=[heart_rate_monitor_id])

    person_id = Column(Integer, ForeignKey("persons_person.id", ondelete='CASCADE'), index=True)
    person = relationship(Person, back_populates="events")

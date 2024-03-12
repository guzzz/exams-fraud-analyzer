
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from consultive_api.config.database import Base


class Person(Base):
    __tablename__ = "persons_person"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(Integer)
    age = Column(Integer)

    events = relationship("Event", back_populates="person")

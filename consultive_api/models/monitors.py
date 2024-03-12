
from sqlalchemy import Column, Integer, String
from consultive_api.config.database import Base


class Monitor(Base):
    __tablename__ = "monitors_monitor"
    
    id = Column(Integer, primary_key=True)
    device = Column(String)
    version = Column(String)
    type = Column(String)

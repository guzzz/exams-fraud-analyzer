

from sqlalchemy import Column, Integer, String, Boolean
from consultive_api.config.database import Base


class User(Base):
    __tablename__ = "auth_user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean)

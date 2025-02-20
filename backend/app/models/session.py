from sqlalchemy import Column, Integer, String
from .base import Base

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String) 
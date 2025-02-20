from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String)
    place = Column(String)
    schedule = Column(String)
    description = Column(String)
    price = Column(Integer)
    available_spots = Column(Integer)

    professor = relationship("User") 
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base


class Correspondent(Base):
    __tablename__ = "correspondents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    country = Column(String(100))
    bio = Column(Text)

    reports = relationship("Report", back_populates="correspondent")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    data = Column(JSONB, default={})
    reports = relationship("Report", back_populates="event")
    category = Column(String, nullable=True)
    extra_data = Column(JSONB, default={}) 

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)

    correspondent_id = Column(Integer, ForeignKey("correspondents.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

    correspondent = relationship("Correspondent", back_populates="reports")
    event = relationship("Event", back_populates="reports")

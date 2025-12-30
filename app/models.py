from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Correspondent(Base):
    __tablename__ = "correspondents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    country = Column(String(100))
    bio = Column(Text)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    correspondent_id = Column(Integer, ForeignKey("correspondents.id"))

    correspondent = relationship("Correspondent", back_populates="events")
    reports = relationship("Report", back_populates="event")


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    correspondent_id = Column(Integer, ForeignKey("correspondents.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

    correspondent = relationship("Correspondent", back_populates="reports")
    event = relationship("Event", back_populates="reports")

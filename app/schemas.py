# app/schemas.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# -----------------------------
# Event Schemas
# -----------------------------

class EventBase(BaseModel):
    title: str
    location: str
    description: str

class EventCreate(EventBase):
    date: datetime = Field(default_factory=datetime.utcnow)

class Event(EventBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

# -----------------------------
# Correspondent Schemas
# -----------------------------

class CorrespondentBase(BaseModel):
    name: str
    email: str

class CorrespondentCreate(CorrespondentBase):
    pass

class Correspondent(CorrespondentBase):
    id: int

    class Config:
        orm_mode = True

# -----------------------------
# Report Schemas
# -----------------------------

class ReportBase(BaseModel):
    title: str
    content: str
    correspondent_id: int

class ReportCreate(ReportBase):
    date: datetime = Field(default_factory=datetime.utcnow)

class Report(ReportBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

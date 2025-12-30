from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ---------- Correspondent ----------

class CorrespondentBase(BaseModel):
    name: str
    email: str
    country: Optional[str] = None
    bio: Optional[str] = None


class CorrespondentCreate(CorrespondentBase):
    pass


class Correspondent(CorrespondentBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Event ----------

class EventBase(BaseModel):
    title: str
    location: Optional[str] = None
    description: Optional[str] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True


# ---------- Report ----------

class ReportBase(BaseModel):
    title: str
    content: Optional[str]
    correspondent_id: int
    event_id: int


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int

    class Config:
        from_attributes = True

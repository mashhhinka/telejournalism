# app/schemas.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from typing import  Dict

class EventBase(BaseModel):
    title: str
    location: str
    description: str

class EventCreate(BaseModel):
    title: str
    location: str
    description: str
    date: Optional[datetime] = None
    data: Optional[Dict] = {}

class Event(EventBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class CorrespondentBase(BaseModel):
    name: str
    email: str

class CorrespondentCreate(CorrespondentBase):
    pass

class Correspondent(CorrespondentBase):
    id: int

    class Config:
        orm_mode = True


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

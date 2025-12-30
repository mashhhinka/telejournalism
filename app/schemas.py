from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Correspondent Schemas
class CorrespondentBase(BaseModel):
    name: str
    email: str
    phone_number: Optional[str] = None
    country: Optional[str] = None
    bio: Optional[str] = None

class CorrespondentCreate(CorrespondentBase):
    pass

class Correspondent(CorrespondentBase):
    id: int

    class Config:
        from_attributes = True  
        

class EventBase(BaseModel):
    title: str
    date: Optional[datetime] = None
    correspondent_id: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True


class ReportBase(BaseModel):
    title: str
    content: str
    correspondent_id: int
    event_id: int

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int

    class Config:
        from_attributes = True

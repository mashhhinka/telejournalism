from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    date: datetime | None = None
    correspondent_id: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True


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
        orm_mode = True

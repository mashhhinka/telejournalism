from pydantic import BaseModel

class CorrespondentBase(BaseModel):
    name: str
    email: str

class CorrespondentCreate(CorrespondentBase):
    pass

class Correspondent(CorrespondentBase):
    id: int

    class Config:
        orm_mode = True

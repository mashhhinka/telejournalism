from sqlalchemy import Column, Integer, String
from .database import Base  # <- import Base from database.py

class Correspondent(Base):
    __tablename__ = "correspondents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

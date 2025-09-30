from ast import Index
from operator import index

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=True)
    hashed_password = Column(String)

    notes = relationship('Note', back_populates='owner')

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates='notes')

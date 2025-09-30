from pydantic import BaseModel

class NoteBase(BaseModel):
    content: str

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

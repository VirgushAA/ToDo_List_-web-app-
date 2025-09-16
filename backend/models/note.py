from pydantic import BaseModel

class NoteIn(BaseModel):
    user_id: int
    test: str

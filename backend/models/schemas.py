from pydantic import BaseModel

class NoteIn(BaseModel):
    user_id: int
    text: str

from fastapi import APIRouter, Depends, HTTPException

from backend.main import get_db
from backend.models import note

router = APIRouter(prefix='/notes', tags=['notes'])

@router.post('/add')
def add_note(note_: note.NoteIn, conn=Depends(get_db)):
    # adding note to db, return response by default i gues
    cur = conn.cursor()
    cur.execute(''' INSERT INTO notes (note)
                    VALUES (?)''',
                (note_.text,))
    conn.commit()

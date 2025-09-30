from xml.dom.minicompat import defproperty

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from backend.db.session import get_db
from backend.models import schemas
from backend.db import crud

pwd_context = CryptContext(schemas=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

router = APIRouter(prefix='/notes', tags=['notes'])

@router.post('/register')
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hp = hash_password(user.password)
    crud.create_user(db=db, user=user, hashed_password=hp)

@router.post('/add_note')
def add_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    crud.create_note(db=db, note=note, user_id=1)



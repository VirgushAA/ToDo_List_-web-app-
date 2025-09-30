from sqlalchemy.orm import Session
from backend.models import db_models, schemas

def get_user_by_username(db: Session,  username):
    return db.query(db_models.User).filter(db_models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    pass

def create_note(db: Session, note: schemas.NoteCreate, user_id: int):
    pass
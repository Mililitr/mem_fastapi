from sqlalchemy.orm import Session
from app.models import Meme
from app.schemas import MemeCreate, MemeUpdate

def get_memes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Meme).offset(skip).limit(limit).all()

def get_meme(db: Session, meme_id: int):
    return db.query(Meme).filter(Meme.id == meme_id).first()

def create_meme(db: Session, meme: MemeCreate):
    db_meme = Meme(**meme.model_dump())
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme

def update_meme(db: Session, meme_id: int, meme: MemeUpdate):
    db_meme = db.query(Meme).filter(Meme.id == meme_id).first()
    if db_meme:
        for key, value in meme.model_dump().items():
            setattr(db_meme, key, value)
        db.commit()
        db.refresh(db_meme)
    return db_meme

def delete_meme(db: Session, meme_id: int):
    db_meme = db.query(Meme).filter(Meme.id == meme_id).first()
    if db_meme:
        db.delete(db_meme)
        db.commit()
    return db_meme
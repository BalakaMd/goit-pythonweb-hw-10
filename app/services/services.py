from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import auth
from app.db.database import get_db
from app.models import models
from app.schemas import schemas


def get_user(db: Session, email):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_current_user(token: str = Depends(auth.oauth2_scheme), db: Session = Depends(get_db)):
    email = auth.decode_token(token)
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

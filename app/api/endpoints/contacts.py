from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta

from app.schemas import schemas
from app.models import models
from app.services.services import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Contact)
async def create_contact(
    contact: schemas.ContactCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_contact = models.Contact(**contact.model_dump(), owner_id=current_user.id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.get("/", response_model=List[schemas.Contact])
def read_contacts(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contacts = db.query(models.Contact).filter(models.Contact.owner_id == current_user.id).offset(skip).limit(limit).all()
    return contacts

@router.get("/{contact_id}", response_model=schemas.Contact)
def read_contact(
    contact_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id, models.Contact.owner_id == current_user.id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/{contact_id}", response_model=schemas.Contact)
def update_contact(
    contact_id: int,
    contact: schemas.ContactCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id, models.Contact.owner_id == current_user.id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.delete("/{contact_id}", response_model=schemas.Contact)
def delete_contact(
    contact_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id, models.Contact.owner_id == current_user.id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return contact

@router.get("/search/", response_model=List[schemas.Contact])
async def search_contacts(
    query: str,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contacts = db.query(models.Contact).filter(
        models.Contact.owner_id == current_user.id,
        (models.Contact.first_name.ilike(f"%{query}%") |
         models.Contact.last_name.ilike(f"%{query}%") |
         models.Contact.email.ilike(f"%{query}%"))
    ).all()
    return contacts

@router.get("/birthdays/", response_model=List[schemas.Contact])
def upcoming_birthdays(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    today = date.today()
    next_week = today + timedelta(days=7)
    contacts = db.query(models.Contact).filter(
        (models.Contact.birthday >= today) & (models.Contact.birthday <= next_week) &
        (models.Contact.owner_id == current_user.id)
    ).all()
    return contacts
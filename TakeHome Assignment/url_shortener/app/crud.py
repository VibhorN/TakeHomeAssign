from sqlalchemy.orm import Session
from app import models

def create_short_url(db: Session, long_url: str, code: str):
    db_url = models.URL(code=code, long_url=long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, code: str):
    return db.query(models.URL).filter(models.URL.code == code).first()

def increment_clicks(db: Session, code: str):
    url_obj = get_url_by_code(db, code)
    if url_obj:
        url_obj.clicks += 1
        db.commit()

from fastapi import HTTPException

def get_analytics(db: Session, code: str):
    url_obj = get_url_by_code(db, code)
    if not url_obj:
        raise HTTPException(status_code=404, detail="Short code not found")
    return {"code": code, "clicks": url_obj.clicks, "created_at": url_obj.created_at}
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import random, string

from . import models, crud, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=schemas.ShortURL)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return crud.create_short_url(db, url.long_url, code)

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url_obj = crud.get_url_by_code(db, short_code)
    if not url_obj:
        raise HTTPException(status_code=404, detail="Short code not found")
    crud.increment_clicks(db, short_code)
    return {"redirect_to": url_obj.long_url}

@app.get("/analytics/{short_code}", response_model=schemas.Analytics)
def get_analytics(short_code: str, db: Session = Depends(get_db)):
    return crud.get_analytics(db, short_code)

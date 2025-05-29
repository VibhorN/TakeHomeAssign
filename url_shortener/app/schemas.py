from pydantic import BaseModel
from datetime import datetime

class URLCreate(BaseModel):
    long_url: str

class ShortURL(BaseModel):
    code: str
    long_url: str

class Analytics(BaseModel):
    code: str
    clicks: int
    created_at: datetime

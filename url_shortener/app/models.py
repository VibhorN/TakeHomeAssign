from sqlalchemy import Column, String, Integer, DateTime, func
from .database import Base

class URL(Base):
    __tablename__ = "urls"
    code = Column(String, primary_key=True, index=True)
    long_url = Column(String, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
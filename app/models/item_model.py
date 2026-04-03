from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.databases.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True) 
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    # func.now() use karne se Database ka current time automatic mil jata hai
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
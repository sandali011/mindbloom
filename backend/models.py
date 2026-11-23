from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id= Column(Integer, primary_key=True , index=True)
    username= Column(String(50), unique=True, index=True, nullable=False)
    email= Column(String(50), unique= True, index= True , nullable =False)
    hashed_password= Column(String(255), nullable= False)
    created_at= Column(DateTime, default=datetime.utcnow)

    mood_logs= relationship("MoodLog", back_populates="owner",cascade="all, delete-orphan")

class MoodLog(Base):
    __tablename__="mood_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id= Column(Integer,Forignkey("users.id"), nullable=False)

    mood_score = Column(Integer, nullable= False)
    mood_name = Column(String(20),nullale=False)
    note = Column(Text, nullable=True)
    tags=Column(Json, default=list)
    recommendation = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="mood_logs")
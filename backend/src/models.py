from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100))
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    def __repr__(self):
        return f"<User(username='{self.username}', password='{self.password}')>"

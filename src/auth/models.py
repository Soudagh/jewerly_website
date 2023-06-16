from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer, Column, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.types import ARRAY

from database import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    role_id = Column(Integer, ForeignKey(Role.id))
    hashed_password = Column(String(length=1024), nullable=False)
    email = Column(String(length=1024), nullable=False)
    user_name = Column(Text, nullable=False)
    user_surname = Column(Text, nullable=False)
    favorite = Column(ARRAY(Integer), nullable=True)
    cart = Column(ARRAY(Integer), nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow())

    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

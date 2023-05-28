from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, JSON, MetaData
from sqlalchemy.types import ARRAY
from datetime import datetime

from database import Base

metadata = MetaData()


# class Role(Base):
#     __tablename__ = 'roles'
#
#     id = Column(Integer, primary_key=True)
#     role_name = Column(Text, nullable=False)
#     role_permissions = Column(JSON)

role = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("user_name", String, nullable=False),
    Column("user_surname", String, nullable=False),
    Column("registration_date", DateTime, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("favorite", ARRAY(Integer), nullable=True),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     role_id = Column(Integer, ForeignKey('roles.id'))
#     hashed_password = Column(String(length=1024), nullable=False)
#     email = Column(String(length=1024), unique=True, index=True, nullable=False)
#     user_name = Column(Text, nullable=False)
#     user_surname = Column(Text, nullable=False)
#     favorite = Column(ARRAY(Integer), nullable=True)
#     registration_date = Column(DateTime, default=datetime.utcnow())
#
#     is_active = Column(Boolean, default=True, nullable=False)
#     is_superuser = Column(Boolean, default=False, nullable=False)
#     is_verified = Column(Boolean, default=False, nullable=False)


class User_auth(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)

    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password = Column(String(length=1024), nullable=False)
    email = Column(String(length=1024), nullable=False)
    user_name = Column(Text, nullable=False)
    user_surname = Column(Text, nullable=False)
    favorite = Column(ARRAY(Integer), nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow())

    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

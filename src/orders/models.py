from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Integer, Column, Text, DateTime, Boolean, ForeignKey, JSON, MetaData
from sqlalchemy.types import ARRAY
from datetime import datetime

from database import Base

metadata = MetaData()

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Table, Integer, Column, Text, DateTime, Boolean, ForeignKey, JSON, MetaData
from sqlalchemy.types import ARRAY
from datetime import datetime

from sqlalchemy import String, Integer, Column, Text, DateTime, create_engine, ForeignKey, Boolean, JSON
from sqlalchemy.types import ARRAY
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config import DB_USER, DB_NAME, DB_PORT, DB_HOST, DB_PASS
from src.database import Base
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Base = declarative_base()
metadata = MetaData()

order = Table(
    "orders",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("products_id", ARRAY(Integer), nullable=False),
    Column("status", Text, nullable=False),
    Column("address", Text, nullable=False),
    Column("order_date", Integer, default=datetime.utcnow()),
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
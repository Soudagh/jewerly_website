from datetime import datetime

from auth.models import User
from database import Base
from database import metadata
from sqlalchemy import Table, Integer, Column, Text, DateTime, ForeignKey
from sqlalchemy.types import ARRAY


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    products_id = Column(ARRAY(Integer), nullable=False)
    status = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow())


order = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(User.id), nullable=False),
    Column("products_id", ARRAY(Integer), nullable=False),
    Column("status", Text, nullable=False),
    Column("address", Text, nullable=False),
    Column("order_date", DateTime, default=datetime.utcnow()),
)

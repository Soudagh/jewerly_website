from datetime import datetime

from sqlalchemy import Table, Integer, Column, Text, DateTime, ForeignKey
from sqlalchemy.types import ARRAY

from src.auth.models import User
from src.database import metadata

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

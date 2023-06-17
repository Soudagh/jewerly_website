from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel
from pydantic.types import List


class Order(BaseModel):
    id: int
    user_id: int
    products_id: list
    status: str
    address: str
    order_date: datetime

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    user_id: int
    products_id: list
    status: str
    address: str


class OrderFilter(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    status: Optional[str]
    address: Optional[str]
    order_date: Optional[datetime]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Order
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
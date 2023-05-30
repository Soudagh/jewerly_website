from datetime import datetime

from pydantic import BaseModel


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
    order_date: datetime

from datetime import datetime

from pydantic import BaseModel


class Order(BaseModel):
    order_id: int
    user_id: int
    products_id: list
    status: str
    address: str

    class Config:
        orm_mode = True


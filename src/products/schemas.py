from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    product_name: str
    brand: int
    category: int
    material: int
    material_color: int
    cutting: int | None
    stone: int | None
    weaving: int | None
    style: int | None
    image_url: str | None
    weight: int
    cost: int
    date_of_creation: datetime

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    product_name: str
    brand: int
    category: int
    material: int
    material_color: int
    cutting: int | None
    stone: int | None
    weaving: int | None
    style: int | None
    image_url: str | None
    weight: int
    cost: int
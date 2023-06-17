from __future__ import annotations

from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from products.models import Product as ProductModel
from pydantic import BaseModel
from pydantic.types import List


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


class ProductFilter(Filter):
    product_name: Optional[str]
    brand: Optional[int]
    category: Optional[int]
    material: Optional[int]
    material_color: Optional[int]
    cutting: Optional[int] | Optional[None]
    stone: Optional[int] | Optional[None]
    weaving: Optional[int] | Optional[None]
    style: Optional[int] | Optional[None]
    weight: Optional[int]
    cost: Optional[int]
    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = ProductModel
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["product_name"]
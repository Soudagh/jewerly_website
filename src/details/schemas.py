from typing import Optional, List

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel


class Brand(BaseModel):
    id: int
    brand_name: str

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand_name: str


class BrandFilter(Filter):
    brand_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Brand
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["brand_name"]


class Category(BaseModel):
    id: int
    category_name: str

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    category_name: str


class CategoryFilter(Filter):
    category_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Category
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["category_name"]


class Style(BaseModel):
    id: int
    style_name: str

    class Config:
        orm_mode = True


class StyleCreate(BaseModel):
    style_name: str


class StyleFilter(Filter):
    style_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Style
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["style_name"]


class Color(BaseModel):
    id: int
    color_name: str

    class Config:
        orm_mode = True


class ColorCreate(BaseModel):
    color_name: str


class ColorFilter(Filter):
    color_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Color
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["color_name"]


class Material(BaseModel):
    id: int
    material_name: str

    class Config:
        orm_mode = True


class MaterialCreate(BaseModel):
    material_name: str


class MaterialFilter(Filter):
    material_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Material
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["material_name"]


class Stone(BaseModel):
    id: int
    stone_name: str

    class Config:
        orm_mode = True


class StoneCreate(BaseModel):
    stone_name: str


class StoneFilter(Filter):
    stone_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Stone
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["stone_name"]


class Cutting(BaseModel):
    id: int
    cutting_name: str

    class Config:
        orm_mode = True


class CuttingCreate(BaseModel):
    cutting_name: str


class CuttingFilter(Filter):
    cutting_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Cutting
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["cutting_name"]


class Weaving(BaseModel):
    id: int
    weaving_name: str

    class Config:
        orm_mode = True


class WeavingCreate(BaseModel):
    weaving_name: str


class WeavingFilter(Filter):
    weaving_name: Optional[str]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = Weaving
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["weaving_name"]
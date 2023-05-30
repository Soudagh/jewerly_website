from pydantic import BaseModel


class Brand(BaseModel):
    id: int
    brand_name: str

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand_name: str


class Category(BaseModel):
    id: int
    category_name: str

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    category_name: str


class Style(BaseModel):
    id: int
    style_name: str

    class Config:
        orm_mode = True


class StyleCreate(BaseModel):
    style_name: str


class Color(BaseModel):
    id: int
    color_name: str

    class Config:
        orm_mode = True


class ColorCreate(BaseModel):
    color_name: str


class Material(BaseModel):
    id: int
    material_name: str

    class Config:
        orm_mode = True


class MaterialCreate(BaseModel):
    material_name: str


class Stone(BaseModel):
    id: int
    stone_name: str

    class Config:
        orm_mode = True


class StoneCreate(BaseModel):
    stone_name: str


class Cutting(BaseModel):
    id: int
    cutting_name: str

    class Config:
        orm_mode = True


class CuttingCreate(BaseModel):
    cutting_name: str


class Weaving(BaseModel):
    id: int
    weaving_name: str

    class Config:
        orm_mode = True


class WeavingCreate(BaseModel):
    weaving_name: str

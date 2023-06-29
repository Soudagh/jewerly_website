from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_users import schemas
from pydantic.types import List


class UserModel(schemas.BaseUser):
    id: int
    role_id: int
    email: str
    user_name: str
    user_surname: str
    favorite: list | None
    cart: list | None
    registration_date: datetime

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True


class UserRead(schemas.BaseUser):
    id: int
    email: str
    role_id: int
    user_name: str
    user_surname: str

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    role_id: int
    email: str
    password: str
    user_name: str
    user_surname: str

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserFilter(Filter):
    id: Optional[int]
    role_id: Optional[int]
    email: Optional[str]
    user_name: Optional[str]
    user_surname: Optional[str]
    registration_date: Optional[datetime]

    custom_order_by: Optional[List[str]]
    custom_search: Optional[str]

    class Constants(Filter.Constants):
        model = UserModel
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["id"]

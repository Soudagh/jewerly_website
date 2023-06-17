from datetime import datetime
from typing import Optional

from fastapi_users import schemas


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


class UserFilter(schemas.BaseUserUpdate):
    id: Optional[int]
    role_id: Optional[int]
    email: Optional[str]
    user_name: Optional[str]
    user_surname: Optional[str]
    favorite: Optional[list] | Optional[None]
    cart: Optional[list] | Optional[None]
    registration_date: Optional[datetime]

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True
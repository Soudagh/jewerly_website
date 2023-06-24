from auth.models import User
from database import get_async_session
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


def ids_initialize(obj_array):
    ids_array = []
    for cart_product in obj_array:
        for i in range(cart_product[1]):
            ids_array.append(cart_product[0].id)
    return ids_array
from fastapi import APIRouter, Depends
from pydantic.types import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas import UserModel
from src.database import get_async_session

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/get_user_by_id", response_model=UserModel)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(User, user_id)
    return query


@router.get("/get_all_users", response_model=List[UserModel])
async def get_user_by_id(session: AsyncSession = Depends(get_async_session)):
    query = select(User).order_by(User.id)
    result = await session.execute(query)
    rows = len(result.all())
    users: List[UserModel] = []
    for i in range(rows):
        user = await session.get(User, i + 1)
        print(user.id)
        users.append(user)
    return users

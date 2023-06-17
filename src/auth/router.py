from auth.models import User
from auth.schemas import UserModel
from database import get_async_session
from fastapi import APIRouter, Depends
from pydantic.types import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/get_user_by_id", response_model=UserModel)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(User, user_id)
    return query


@router.get("/get_all_users", response_model=List[UserModel])
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User).order_by(User.id)
    result = await session.execute(query)
    users: List[UserModel] = []
    for user in result.scalars():
        users.append(user)
    return users


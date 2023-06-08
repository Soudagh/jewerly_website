from fastapi import APIRouter, Depends
from pydantic.types import List
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.orders.models import order
from src.orders.schemas import Order, OrderCreate

router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/get_orders_by_user_id", response_model=List[Order])
async def get_orders_by_user_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.user_id == user_id)
    result = await session.execute(query)
    return result.all()


@router.post("/add_order")
async def add_order(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

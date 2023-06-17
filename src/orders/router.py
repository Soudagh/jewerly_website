from database import get_async_session
from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from orders.models import order
from orders.schemas import Order, OrderCreate
from orders.schemas import OrderFilter
from pydantic.types import List
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

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


@router.get("/get_orders", response_model=List[Order] | List[None])
async def get_orders(session: AsyncSession = Depends(get_async_session),
                     order_filter: OrderFilter = FilterDepends(OrderFilter)):
    query = select(order).order_by(order.c.id)
    query = order_filter.filter(query)
    query = order_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException
from fastapi_filter import FilterDepends
from fastapi_pagination import Page, paginate
from orders.models import Order as OrderModel
from orders.models import order
from orders.schemas import Order, OrderCreate, OrderUpdate, OrderFilter
from pydantic.types import List
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/get_orders_by_user_id", response_model=List[Order])
async def get_orders_by_user_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(OrderModel).where(OrderModel.user_id == user_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/get_order_by_id", response_model=Order)
async def get_order_by_id(order_id: int, session: AsyncSession = Depends(get_async_session)):
    curr_order = await session.get(OrderModel, order_id)
    if not curr_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return curr_order


@router.post("/add_order")
async def add_order(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.patch("/update_order", response_model=Order)
async def update_order(order_id: int, updated_order: OrderUpdate, session: AsyncSession = Depends(get_async_session)):
    cur_order = get_order_by_id(order_id, session)

    product_data = updated_order.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(cur_order, key, value)
    session.add(cur_order)
    await session.commit()
    await session.refresh(cur_order)
    return cur_order


@router.get("/get_orders", response_model=Page[Order])
async def get_orders(session: AsyncSession = Depends(get_async_session),
                     order_filter: OrderFilter = FilterDepends(OrderFilter)):
    query = select(OrderModel).order_by(OrderModel.id)
    query = order_filter.filter(query)
    query = order_filter.sort(query)
    result = await session.execute(query)
    return paginate(result.scalars().all())

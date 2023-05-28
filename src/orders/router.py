from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic.types import List


from src.orders.models import order
from src.database import get_async_session
from src.orders.schemas import Order
router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/", response_model=List[Order])
async def get_specific_orders(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.user_id == user_id)
    result = await session.execute(query)

    return result.all()

from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import Product as ProductModel
from src.products.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.post("/add_product")
async def add_order(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(ProductModel).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

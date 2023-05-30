from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from details.models import Brand
from src.database import get_async_session
from src.details.schemas import BrandCreate

router = APIRouter(
    prefix="/details",
    tags=["Detail"]
)


@router.post("/add_brand")
async def add_brand(new_brand: BrandCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Brand).values(**new_brand.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


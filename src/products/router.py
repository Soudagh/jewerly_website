from datetime import datetime, timedelta

from database import get_async_session
from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from fastapi_pagination import Page, paginate
from products.models import Product as ProductModel
from products.schemas import ProductCreate, Product
from products.schemas import ProductFilter
from pydantic.types import List
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.post("/add_product")
async def add_product(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(ProductModel).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_product_by_id", response_model=Product | None)
async def get_product_by_id(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(ProductModel, product_id)
    return query


@router.get("/get_products_by_id", response_model=List[Product] | List[None])
async def get_products_by_id(products_ids, session: AsyncSession = Depends(get_async_session)):
    products_ids = set(map(int, products_ids.split()))
    products = []
    for i in products_ids:
        query = await session.get(ProductModel, i)
        products.append(query)
    return products


@router.get("/get_all_products", response_model=Page[Product])
async def get_all_products(session: AsyncSession = Depends(get_async_session),
                           product_filter: ProductFilter = FilterDepends(ProductFilter)):
    query = select(ProductModel)
    query = product_filter.filter(query)
    query = product_filter.sort(query)
    result = await session.execute(query)
    return paginate(result.scalars().all())


@router.get("/get_new_products", response_model=Page[Product])
async def get_new_products(session: AsyncSession = Depends(get_async_session),
                           product_filter: ProductFilter = FilterDepends(ProductFilter)):
    query = select(ProductModel).filter(ProductModel.date_of_creation > datetime.utcnow() - timedelta(days=31))
    query = product_filter.filter(query)
    query = product_filter.sort(query)
    result = await session.execute(query)
    return paginate(result.scalars().all())

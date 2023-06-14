from fastapi import APIRouter, Depends
from pydantic.types import List
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import Product as ProductModel
from src.products.schemas import ProductCreate, Product

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


@router.get("/get_product_by_id", response_model=Product | None)
async def get_product_by_id(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(ProductModel, product_id)
    return query


@router.get("/get_products_by_id", response_model=List[Product] | List[None])
async def get_products_by_id(products_ids, session: AsyncSession = Depends(get_async_session)):
    products_ids = list(map(int, products_ids.split()))
    products = []
    for i in products_ids:
        query = await session.get(ProductModel, i)
        products.append(query)
    print(products, type(products))
    return products


@router.get("/get_all_products", response_model=List[Product])
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(ProductModel).order_by(ProductModel.id)
    result = await session.execute(query)
    rows = len(result.all())
    products: List[ProductModel] = []
    for i in range(rows):
        user = await session.get(ProductModel, i + 1)
        print(user.id)
        products.append(Product)
    return products

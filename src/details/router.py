from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from details.models import Brand, Category, Style, Color, Material, Stone, Cutting, Weaving
from details.schemas import BrandCreate, CategoryCreate, StyleCreate, ColorCreate, MaterialCreate, StoneCreate, \
    CuttingCreate, WeavingCreate

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


@router.post("/add_category")
async def add_category(new_category: CategoryCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Category).values(**new_category.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_style")
async def add_style(new_style: StyleCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Style).values(**new_style.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_color")
async def add_color(new_color: ColorCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Color).values(**new_color.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_material")
async def add_material(new_material: MaterialCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Material).values(**new_material.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_stone")
async def add_stone(new_stone: StoneCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Stone).values(**new_stone.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_cutting")
async def add_cutting(new_cutting: CuttingCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Cutting).values(**new_cutting.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_weaving")
async def add_weaving(new_weaving: WeavingCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Weaving).values(**new_weaving.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
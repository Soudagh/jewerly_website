from database import get_async_session
from details.models import Brand, Category, Style, Color, Material, Stone, Cutting, Weaving
from details.schemas import Brand as BrandModel
from details.schemas import BrandCreate, CategoryCreate, StyleCreate, ColorCreate, MaterialCreate, StoneCreate, \
    CuttingCreate, WeavingCreate
from details.schemas import BrandFilter, CategoryFilter, StyleFilter, ColorFilter, MaterialFilter, StoneFilter, \
    CuttingFilter, WeavingFilter
from details.schemas import Category as CategoryModel
from details.schemas import Color as ColorModel
from details.schemas import Cutting as CuttingModel
from details.schemas import Material as MaterialModel
from details.schemas import Stone as StoneModel
from details.schemas import Style as StyleModel
from details.schemas import Weaving as WeavingModel
from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from pydantic.types import List
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

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


@router.get("/get_all_brands", response_model=List[BrandModel] | List[None])
async def get_all_brands(session: AsyncSession = Depends(get_async_session),
                         brand_filter: BrandFilter = FilterDepends(BrandFilter)):
    query = select(Brand).order_by(Brand.id)
    query = brand_filter.filter(query)
    query = brand_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_category")
async def add_category(new_category: CategoryCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Category).values(**new_category.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_categories", response_model=List[CategoryModel] | List[None])
async def get_all_categories(session: AsyncSession = Depends(get_async_session),
                             category_filter: CategoryFilter = FilterDepends(CategoryFilter)):
    query = select(Category).order_by(Category.id)
    query = category_filter.filter(query)
    query = category_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_style")
async def add_style(new_style: StyleCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Style).values(**new_style.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_styles", response_model=List[StyleModel] | List[None])
async def get_all_styles(session: AsyncSession = Depends(get_async_session),
                         style_filter: StyleFilter = FilterDepends(StyleFilter)):
    query = select(Style).order_by(Style.id)
    query = style_filter.filter(query)
    query = style_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_color")
async def add_color(new_color: ColorCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Color).values(**new_color.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_colors", response_model=List[ColorModel] | List[None])
async def get_all_colors(session: AsyncSession = Depends(get_async_session),
                         color_filter: ColorFilter = FilterDepends(ColorFilter)):
    query = select(Color).order_by(Color.id)
    query = color_filter.filter(query)
    query = color_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_material")
async def add_material(new_material: MaterialCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Material).values(**new_material.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_materials", response_model=List[MaterialModel] | List[None])
async def get_all_materials(session: AsyncSession = Depends(get_async_session),
                            material_filter: MaterialFilter = FilterDepends(MaterialFilter)):
    query = select(Material).order_by(Material.id)
    query = material_filter.filter(query)
    query = material_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_stone")
async def add_stone(new_stone: StoneCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Stone).values(**new_stone.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_stones", response_model=List[StoneModel] | List[None])
async def get_all_stones(session: AsyncSession = Depends(get_async_session),
                         stone_filter: StoneFilter = FilterDepends(StoneFilter)):
    query = select(Stone).order_by(Stone.id)
    query = stone_filter.filter(query)
    query = stone_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_cutting")
async def add_cutting(new_cutting: CuttingCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Cutting).values(**new_cutting.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_cuttings", response_model=List[CuttingModel] | List[None])
async def get_all_cuttings(session: AsyncSession = Depends(get_async_session),
                           cutting_filter: CuttingFilter = FilterDepends(CuttingFilter)):
    query = select(Cutting).order_by(Cutting.id)
    query = cutting_filter.filter(query)
    query = cutting_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/add_weaving")
async def add_weaving(new_weaving: WeavingCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Weaving).values(**new_weaving.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/get_all_weavings", response_model=List[WeavingModel] | List[None])
async def get_all_cuttings(session: AsyncSession = Depends(get_async_session),
                           weaving_filter: WeavingFilter = FilterDepends(WeavingFilter)):
    query = select(Weaving).order_by(Weaving.id)
    query = weaving_filter.filter(query)
    query = weaving_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()

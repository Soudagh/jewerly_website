from auth.models import User
from auth.schemas import UserModel, UserFilter
from auth.utils import ids_initialize, ids_initialize_with_count
from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException
from fastapi_filter import FilterDepends
from products.router import get_products_by_id
from products.schemas import Product
from pydantic.types import List, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/get_user_by_id", response_model=UserModel)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/get_all_users", response_model=List[UserModel] | List[None])
async def get_all_users(session: AsyncSession = Depends(get_async_session),
                        user_filter: UserFilter = FilterDepends(UserFilter)):
    query = select(User).order_by(User.id)
    query = user_filter.filter(query)
    query = user_filter.sort(query)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/get_user_cart", response_model=List[Tuple[Product, int]])
async def get_user_cart(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(User, user_id)
    if query.cart is None or len(query.cart) == 0:
        return list()

    user_cart_ids = await get_products_by_id(" ".join(str(product) for product in query.cart), session)
    user_cart_ids_set = set(user_cart_ids)
    user_cart = list()
    for product in user_cart_ids_set:
        user_cart.append((product, user_cart_ids.count(product)))

    return user_cart


@router.get("/get_user_favorite", response_model=List[Product] | List[None])
async def get_user_favorite(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = await session.get(User, user_id)
    if query.favorite is None:
        return []
    user_favorite = await get_products_by_id(" ".join(str(product) for product in query.favorite), session)
    return user_favorite


@router.post("/add_product_to_favorite")
async def add_product_to_favorite(user_id: int, product_id: int, session: AsyncSession = Depends(get_async_session)):
    favorite_new = await get_user_favorite(user_id, session)
    favorite_new_ids = [favorite_product.id for favorite_product in favorite_new]
    if product_id in favorite_new_ids:
        return {"detail": "Product already in favorite"}

    favorite_new_ids.append(product_id)
    stmt = update(User).where(User.id == user_id).values(favorite=favorite_new_ids)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/add_product_to_cart")
async def add_product_to_cart(user_id: int, product_id: int, count: int = 1,
                              session: AsyncSession = Depends(get_async_session)):
    cart_new = await get_user_cart(user_id, session)

    cart_new_ids = ids_initialize_with_count(cart_new)

    for i in range(count):
        cart_new_ids.append(product_id)

    stmt = update(User).where(User.id == user_id).values(cart=cart_new_ids)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/delete_product_from_cart")
async def delete_product_from_cart(user_id: int, product_id: int, count: int,
                                   session: AsyncSession = Depends(get_async_session)):
    prev_cart = await get_user_cart(user_id, session)
    if not prev_cart:
        raise HTTPException(status_code=404, detail="Cart is empty")
    prev_cart_ids = ids_initialize_with_count(prev_cart)

    product_count = prev_cart_ids.count(product_id)
    if product_count != 0:
        for i in range(count):
            prev_cart_ids.remove(product_id)
            count -= 1
            product_count -= 1
            if count == 0 or product_count == 0:
                break
        stmt = update(User).where(User.id == user_id).values(cart=prev_cart_ids)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}

    else:
        return {"details": "Product is not in cart"}


@router.post("/delete_product_from_favorite")
async def delete_product_from_favorite(user_id: int, product_id: int,
                                       session: AsyncSession = Depends(get_async_session)):
    favorite = await get_user_favorite(user_id, session)
    print(favorite)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite is empty")

    favorite_ids = ids_initialize(favorite)

    if product_id in favorite_ids:
        favorite_ids.remove(product_id)
        stmt = update(User).where(User.id == user_id).values(favorite=favorite_ids)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    else:
        return {"details": "Product is not in favorite"}


@router.post("/clear_user_cart")
async def clear_user_cart(user_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(User).where(User.id == user_id).values(cart=[])
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/clear_user_favorite")
async def clear_user_favorite(user_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(User).where(User.id == user_id).values(favorite=[])
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

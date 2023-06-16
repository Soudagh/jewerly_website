from fastapi import FastAPI

from auth.base_config import fastapi_users, auth_backend
from auth.router import router as router_user
from auth.schemas import UserRead, UserCreate
from details.router import router as router_detail
from orders.router import router as router_order
from products.router import router as router_product

app = FastAPI(
    title="Jewerly App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


app.include_router(router_order)
app.include_router(router_product)
app.include_router(router_detail)
app.include_router(router_user)

current_user = fastapi_users.current_user()



# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"
#
#
# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, Anonym"

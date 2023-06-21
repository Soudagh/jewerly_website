from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from auth.base_config import fastapi_users, auth_backend
from auth.router import router as router_user
from auth.schemas import UserRead, UserCreate
from details.router import router as router_detail
from orders.router import router as router_order
from products.router import router as router_product

app = FastAPI(
    title="Jewerly App"
)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:3001",
    "http://localhost:8000",
    "https://jewerly-service.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
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

add_pagination(app)

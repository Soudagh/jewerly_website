from fastapi import FastAPI, Depends

from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate


app = FastAPI(
    title="Jewerly App App"
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

current_user = fastapi_users.current_user()


# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"
#
#
# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, Anonym"

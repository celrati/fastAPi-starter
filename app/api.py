from fastapi import FastAPI, Body, Depends

from app.model import UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from app.routers.travels import travels_router
from app.routers.users import users_router

users = []

app = FastAPI()



app.include_router(travels_router,prefix="/travels",tags=["travels"])
app.include_router(users_router,prefix="/users",tags=["users"])


# helpers

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello world lena server say ohayo"}

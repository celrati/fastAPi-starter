from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import List
import json
from app.model import TravelsSchema, UserSchema, UserLoginSchema
from fastapi import FastAPI, Body, Depends
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT


users_router = APIRouter()



def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers


@users_router.post("/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@users_router.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
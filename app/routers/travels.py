from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import List
import json
from app.model import TravelsSchema, UserSchema, UserLoginSchema
from fastapi import FastAPI, Body, Depends
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

travels_router = APIRouter()

travels = [
    {
        "id": 1,
        "title": "t1",
        "content": "Lorem Ipsum ..."
    }
]


@travels_router.get("/", tags=["travels"])
async def get_travels() -> dict:
    return { "data": travels }


@travels_router.get("/{id}", tags=["travels"])
async def get_single_travel(id: int) -> dict:
    if id > len(travels):
        return {
            "error": "No such post with the supplied ID."
        }

    for t in travels:
        if t["id"] == id:
            return {
                "data": t
            }


@travels_router.post("/", dependencies=[Depends(JWTBearer())], tags=["travels"])
async def add_travel(add_travel: TravelsSchema) -> dict:
    add_travel.id = len(travels) + 1
    travels.append(add_travel.dict())
    return {
        "data": "post added."
    }

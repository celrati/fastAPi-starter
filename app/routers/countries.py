from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import List
import json


countries_router = APIRouter()

from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import List
import json

plannings_router = APIRouter()

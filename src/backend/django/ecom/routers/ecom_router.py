from typing import Optional, List
from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl


router = APIRouter()
class Product(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

@router.post("/add_product")
def hello(file: UploadFile = File(...)):
    return {"tonn": 1}

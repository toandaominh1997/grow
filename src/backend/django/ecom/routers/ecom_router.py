from typing import Optional, List
from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

from ecom.core.ecom_adapter import EcomAdapter


router = APIRouter()
ecom = EcomAdapter()
class Product(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None

class SearchProduct(BaseModel):
    text: Optional[str] = None
@router.get("/get_product")
def getproduct():
    return ecom.get_product()

@router.post("/add_product")
def hello(item: Product):
    ecom.add_product(title= item.title, description = item.description, image_url = item.image_url)

    return True


@router.post("/search_product")
def search_product(item: SearchProduct):
    return ecom.search_product(text = item.text)

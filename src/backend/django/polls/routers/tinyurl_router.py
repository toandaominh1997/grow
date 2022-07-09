from fastapi import APIRouter, Depends
from polls.adapters import tinyurl

router = APIRouter()

@router.get("/")
def get_tinyurl():
    return tinyurl.get_tinyurl()

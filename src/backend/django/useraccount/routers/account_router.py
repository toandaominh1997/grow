from sqlite3 import adapters
from typing import Optional, List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from prometheus_client import Summary, Counter
from useraccount.core.account_adapter import UserAdapter


router = APIRouter()
adapter = UserAdapter()
class User(BaseModel):
    email: str
    password: str
@router.get("/hello")
def  hello():
    return "Heloo"
@router.post("/add_user")
def validate_user(user: User):
    return adapter.add_user(email = user.email, password = user.password)
@router.post("/validate_user")
def validate_user(user: User):
    return adapter.validate_user(email = user.email, password = user.password)


@router.post("/user")
def get_user(user: User):
    return adapter.get_user(email = user.email, password = user.password)


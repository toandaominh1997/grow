from typing import Optional, List
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel

import subprocess
from fastapi.responses import HTMLResponse
import requests

from db.user import USERDB
router = APIRouter()

userdb = USERDB()
def init_db():
    print("hello")
class User(BaseModel):
    email: str
    password: Optional[str] = None
@router.post("/v1/api/signin/")
async def user_account(user: User):
    print('user: ', user)

    out = userdb.validate_user(user.email, user.password)
    if out is None:
        userdb.insert_user(user_name = user.email, password = user.password)
        return False
    return True


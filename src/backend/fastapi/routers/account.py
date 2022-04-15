from typing import Optional, List
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel

import subprocess
from fastapi.responses import HTMLResponse

from db.user import userdb

router = APIRouter()

def init_db():
    print("hello")
class User(BaseModel):
    email: str
    password: Optional[str] = None
@router.post("/api/signin/")
async def user_account(user: User):
    print('user: ', user)
    # userdb.insert_user(user_name = user.email, password = user.password)
    ok = userdb.validate_user(user.email, user.password)
    return ok

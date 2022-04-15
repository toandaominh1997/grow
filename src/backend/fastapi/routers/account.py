from typing import Optional, List
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel

import subprocess
from fastapi.responses import HTMLResponse

router = APIRouter()

def init_db():
    print("hello")

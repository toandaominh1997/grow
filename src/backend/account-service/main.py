from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from account import update_table, check_username
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:11000",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Item(BaseModel):
    username: str
    password: Optional[str] = None


@app.post("/login")
async def login(item: Item):
    print(item)
    return item

@app.post("/register")
async def register(item: Item):
    username, password = item.username, item.password
    print(username, password)
    if check_username(username) == False:
        update_table(username, password)
        print(f'Updated {username}, {password}')
        return True
    print('Exists in database')
    return True

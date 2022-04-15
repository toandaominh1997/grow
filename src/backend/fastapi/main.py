from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from db.create import CREATE 
from routers import account


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router)


@app.on_event("startup")
async def startup_event():
    print("Start DB")
    CREATE().fit()


class User(BaseModel):
    name: str
    password: Optional[str] = None

@app.get("/")
async def hello():
    return "Hello"
@app.get("/user")
async def user_account(user: User):
    print('user: ', user)
    return user

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    password: Optional[str] = None

@app.get("/user")
async def user_account(user: User):
    print('user: ', user)
    return user

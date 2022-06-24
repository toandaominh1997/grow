from fastapi import Depends, FastAPI
from dependencies import get_query_token, get_token_header
from fastapi.middleware.cors import CORSMiddleware
from routers import model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(model.router)
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

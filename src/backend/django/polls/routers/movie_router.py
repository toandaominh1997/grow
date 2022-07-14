from fastapi import APIRouter, Depends
from pydantic import BaseModel
from polls.adapters.movie import MoiveAdapter


movie = MoiveAdapter()
class Item(BaseModel):
    id: int 
    title: str 
    overview: str
    genres: str
    poster: str


router = APIRouter()

@router.on_event("startup")
async def startup():
    pass
    # await movie.init_movie()
@router.post("/v1/api/add_movie")
def add_movie(item: Item):
    movie.add_movie(id = item.id,
                    title = item.title, 
                    overview = item.overview, 
                    genres = item.genres, 
                    poster = item.poster)
    return "Done"
@router.get("/v1/api/count_movie")
def count_movie():
    result = movie.count_movie()
    return {'count': result}
    

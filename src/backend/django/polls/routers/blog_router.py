from fastapi import APIRouter, Depends
from pydantic import BaseModel
from polls.adapters.blog import BlogAdapter
from prometheus_client import Summary, Counter

REQUEST_SEARCH = Summary('request_search', 'Number of Search Engine')
count_search = Counter("count_search", "Number of Search")

blog = BlogAdapter()
class Item(BaseModel):
    id: int 
    user_id: str
    title: str 
    image_url: str
    description: str
class Search(BaseModel):
    text: str

router = APIRouter()

@router.on_event("startup")
async def startup():
    pass
    # await movie.init_movie()
@router.post("/add_blog")
def add_blog(item: Item):
    blog.add_blog(id = item.id,
                user_id = item.user_id,
                title = item.title, 
                image_url=item.image_url,
                description = item.description,
                    )
    return "Done"
@router.post("/update_blog")
def update_blog(item: Item):
    blog.add_blog(id = item.id,
                user_id = item.user_id,
                title = item.title, 
                image_url=item.image_url,
                description = item.description,
                    )
    return True
@router.get("/get_blog")
def get_blog():
    blog.get_blog()
    return "Ne"

@router.get("/recommend")
def recommend_blog():
    response = blog.recommend_blog()
    print(response)
    return response

@router.get("/sync-search")
def recommend_blog():
    response = blog.sync_es()
    return response

@REQUEST_SEARCH.time()
@router.post("/search")
def search(search: Search):
    response = blog.search(search.text)
    count_search.inc()
    return response

@router.get("/search_log")
def recommend_blog():
    response = blog.search_log()
    return response

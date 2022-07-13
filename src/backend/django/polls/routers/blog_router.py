from fastapi import APIRouter, Depends
from pydantic import BaseModel
from polls.adapters.blog import BlogAdapter


blog = BlogAdapter()
class Item(BaseModel):
    id: int 
    user_id: str
    title: str 
    image_url: str
    description: str


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

    

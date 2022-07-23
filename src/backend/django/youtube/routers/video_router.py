from typing import Optional, List
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from prometheus_client import Summary, Counter
from youtube.core.video_adapter import VideoAdapter


class Search(BaseModel):
    text: Optional[str] = None

router = APIRouter()
video = VideoAdapter()

@router.post("/search")
def search(item: Search):
    print(item.text)
    return video.search(item.text)




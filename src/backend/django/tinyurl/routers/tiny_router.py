from typing import Optional, List
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from prometheus_client import Summary, Counter
from tinyurl.core.tinyadapter import TinyAdapter


class TinyURL(BaseModel):
    alias: Optional[str] = None
    long_url: str
    domain: Optional[str] = 'localhost:1234'


router = APIRouter()
tiny = TinyAdapter()

@router.post("/v1/api/update_tinyurl")
def get_url(item: TinyURL):
    res = tiny.update_tinydb(alias = item.alias, long_url = item.long_url, domain = item.domain)
    return res

@router.get("/{alias}")
def gen_domain(alias):
    url = tiny.generate_domain(alias)
    if url:
        return RedirectResponse(url = url)
    return "Not available"

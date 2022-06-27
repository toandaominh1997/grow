from typing import Optional, List
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel

import subprocess
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import requests
import hashlib
import datetime
import redis
from db.tinyurl import TinyURLDB

rd = redis.Redis(host = 'redis', port = 6379, db = 0)
rd.set('foo', 'bar')
print(rd.get('foo'))
urldb = TinyURLDB()
router = APIRouter()
class TinyURL(BaseModel):
    long_url: str 
    domain: Optional[str] = 'localhost:1234'
    alias: Optional[str] = None
@router.post("/v1/api/update_tinyurl")
def get_tinyurl(tinyurl: TinyURL):
    print(f"alias:{tinyurl.alias}")
    if tinyurl.alias != '':
        print('DB', urldb.get_db())
        print('validate alias longurl')
        out =  urldb.validate_alias_longurl(alias = tinyurl.alias, long_url = tinyurl.long_url)
        if out:
            return f"{out[0][0]}/{out[0][1]}"
        print('validate alias')
        val_alias = urldb.validate_alias(alias = tinyurl.alias) 
        if val_alias:
            return "alias is not available"
        print('insert tinyurl')
        urldb.insert_tinyurl(alias = tinyurl.alias, long_url = tinyurl.long_url, domain = tinyurl.domain)
        return f"{tinyurl.domain}/{tinyurl.alias}"
    else:
        short_url = hashlib.shake_256(tinyurl.long_url.encode()).hexdigest(5)
        val_alias = urldb.validate_alias(alias = short_url)
        if val_alias is None:
            urldb.insert_tinyurl(alias = short_url, long_url = tinyurl.long_url, domain = tinyurl.domain)
            return f"{tinyurl.domain}/{short_url}"
        else:
            if val_alias[2] == tinyurl.long_url:
                return f"{tinyurl.domain}/{val_alias[1]}"
            else:
                timestamp = datetime.datetime.now().timestamp()
                short_url = short_url + str(int(timestamp))
                urldb.insert_tinyurl(alias = short_url, long_url = tinyurl.long_url, domain = tinyurl.domain)
                return f"{tinyurl.domain}/{short_url}"
@router.get("/{alias}")
def generate_domain(alias):
    long_url = rd.get(alias)
    if long_url is None:
        alias_sql = urldb.get_alias(alias = alias)
        if alias_sql is None:
            return 'Not Exist'
        else:
            long_url = alias_sql[0][0]
            rd.set(alias, long_url)
        print('From DB', long_url)
    else:
        long_url = long_url.decode()
        print('From Redis', long_url)

    if long_url:
        return RedirectResponse(url = long_url)
    return "Notvaliable"


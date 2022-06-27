from typing import Optional, List
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
import requests
from kafka import KafkaProducer
import logging
import json

router = APIRouter()

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

class SearchModel(BaseModel):
    text: str
@router.post("/v1/api/search")
def search_platform(search: SearchModel):
    print("Start search platform")
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{search.text}"
    print('send from producer')
    producer.send('data_search', value = {"text": search.text})
    return requests.get(url).text

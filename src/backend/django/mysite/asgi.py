"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()

from prometheus_client import start_http_server
start_http_server(8989)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from polls.routers import questions_router, movie_router, blog_router
from tinyurl.routers import tiny_router
from youtube.routers import video_router
from useraccount.routers import account_router
from ecom.routers import ecom_router

fastapp = FastAPI()
fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapp.include_router(questions_router.router, tags=["questions"], prefix = "/question")
fastapp.include_router(movie_router.router, tags = ['movie'])
fastapp.include_router(blog_router.router, tags = ['blog'], prefix = "/v1/api")

fastapp.include_router(tiny_router.router, tags = ['TinyApp'])

fastapp.include_router(video_router.router, tags = ['YoutubeApp'])

fastapp.include_router(account_router.router, tags = ['User Profiles'], prefix = "/v1/api")

fastapp.include_router(ecom_router.router, tags = ['Ecom'], prefix = "/v1/api/ecom")

MOUNT_DJANGO_APP = True
if MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")


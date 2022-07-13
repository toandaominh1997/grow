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

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from polls.routers import questions_router, tinyurl_router, movie_router, blog_router

fastapp = FastAPI()
fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapp.include_router(questions_router.router, tags=["questions"], prefix = "/question")
fastapp.include_router(tinyurl_router.router, tags=["tinyurl"], prefix = "/tinyurl")
fastapp.include_router(movie_router.router, tags = ['movie'])
fastapp.include_router(blog_router.router, tags = ['blog'], prefix = "/v1/api")

MOUNT_DJANGO_APP = True
if MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")


from fastapi import APIRouter

from .endpoints import (
    user,
    story_writer)

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(story_writer.router)
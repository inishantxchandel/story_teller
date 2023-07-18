from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import List, Optional

class StoryRequest(BaseModel):
    description: str


class StoryResponse(BaseModel):
    title: str
    chapters: List[str]


class ChapterRequest(BaseModel):
    story_id: int
    chapter_name: str
    description: str


class ChapterResponse(BaseModel):
    content: str
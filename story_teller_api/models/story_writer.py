from ..database import Base
from sqlalchemy import Column, Integer, String , Boolean,text,ForeignKey
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import JSON, UUID


class Story(Base):
    __tablename__ = "Story"

    id = Column(Integer, primary_key=True, index=True,nullable=False)
    story_title_chapter = Column(JSON)
    story_chapter_wise = Column(JSON,nullable=True)
    story_till_now = Column(String,nullable=True)
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

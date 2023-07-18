from ..database import Base
from sqlalchemy import Column, Integer, String , Boolean,text,ForeignKey
from sqlalchemy import TIMESTAMP

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
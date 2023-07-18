from typing import Union

from fastapi import FastAPI

from .database import engine

from . import models

from .api_v1.api import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


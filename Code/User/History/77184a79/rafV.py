from typing import Union
from fastapi import FastAPI
from db import database_connect,database_disconnect,soos

app = FastAPI()


@app.get("/")
def read_root():
    soos()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/user/new")
def new_user(user: dict):
    name = user['name']; lastname = user['lastname'];
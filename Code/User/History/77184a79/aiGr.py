from typing import Union
from fastapi import FastAPI
from db import database_connect,database_disconnect,soos

app = FastAPI()

u1 = {'name': 'Justin', 'lastname': 'Ackermann', 'jobtitle': 'Head of Soos', 'DID': 2, 'LID': 5, 'IsITResSigned': True}
u2 = {'name': 'Testo', 'lastname': 'Testoburger', 'jobtitle': 'Testuser', 'DID': 4, 'LID': 2, 'IsITResSigned': True}
u3 = {'name': 'Snens', 'lastname': 'Ator', 'jobtitle': 'Memelord', 'DID': 2, 'LID': 5, 'IsITResSigned': False}

d1 = 

@app.get("/")
def read_root():
    soos()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/filldb")
def fill_db():
    db.create
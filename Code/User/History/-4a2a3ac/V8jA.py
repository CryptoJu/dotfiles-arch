import pymysql.cursors   
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from pydantic import BaseModel

class User(BaseModel):
    uid : int
    name : str
    lastname : str
    location: str
    department : int
    groups: str


db = Database("sqlite:///db.sqlite3")

async def database_connect():
    await db.connect()

async def database_disconnect():
    await db.disconnect()

async def soos():
    sql = "DATABASE()"
    result = await db.fetch_all(query=sql)

    return result


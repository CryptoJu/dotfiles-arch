import pymysql.cursors   
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from pydantic import BaseModel

class Group(BaseModel):
    gid : int
    name : str

class inGroup(BaseModel):
    uid: int
    gid: int

db = Database("sqlite:///db.sqlite3")

async def database_connect():
    await db.connect()

async def database_disconnect():
    await db.disconnect()

async def create_table(table: str):
    sql = f"CREATE TABLE IF NOT EXISTS `{table}`"
    match table:
        case 'Departments':
            sql += """
            (DID INT PRIMARY KEY, Name TEXT NOT NULL)
            """
        case 'Groups':
            sql += """"""
        case 'Users':
            sql += """
            (UID INT PRIMARY KEY, Name TEXT NOT NULL, Lastname TEXT NOT NULL, Title TEXT, Location FOREIGN KEY (LID) REFERENCES Location)
            """


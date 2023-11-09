import os
from pathlib import Path
import shutil
import logging
from typing import Optional, List
from uuid import UUID
import uuid
from datetime import datetime

from fastapi import FastAPI, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import aiomysql
import uvicorn

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import Session

import mysql.connector

load_dotenv(".env.local")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# models.Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def test_connection():
    return {"status": "ok"}


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100):
#     cursor = cnx.cursor()
#     cursor.execute("SELECT * FROM users;")
#     rows = [row for row in cursor]
#     cursor.close()
#     return {"users": rows}


if __name__ == "__main__":
    cnx = mysql.connector.connect(user='admin', password='comp3278database',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='comp3278')
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

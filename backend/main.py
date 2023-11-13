from pathlib import Path
import logging
from typing import Optional, List

from fastapi import FastAPI, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

import mysql.connector

load_dotenv(".env.local")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# models.Base.metadata.create_all(bind=engine)
cnx = mysql.connector.connect(
    user='root',
    password='t8gESx06a5e',
    host='127.0.0.1',
    port=3306,
    database='comp3278')

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
def test_fastapi_connection():
    return {"status": "ok"}

@app.get("/db")
def test_db_connection():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Class;")
    rows = [row for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100):
#     cursor = cnx.cursor()
#     cursor.execute("SELECT * FROM users;")
#     rows = [row for row in cursor]
#     cursor.close()
#     return {"users": rows}


if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000)

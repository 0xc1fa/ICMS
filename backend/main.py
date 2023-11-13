import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import mysql.connector

load_dotenv(".env.local")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cnx = mysql.connector.connect(
    user='root',
    password='t8gESx06a5e',
    host='127.0.0.1',
    port=3306,
    database='comp3278')

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


if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000)

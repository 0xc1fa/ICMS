import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import mysql.connector
from pydantic import BaseModel

load_dotenv(".env.local")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cnx = mysql.connector.connect(
    user='root',
    password='t8gESx06a5e',
    host='127.0.0.1',
    port=3306,
    database='comp3278'
)

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
    # using list comprehension
    # rows = [{
    #     'course_id': row[0],
    #     'class_id': row[1],
    #     'class_time': row[2],
    #     'class_location': row[3],
    # } for row in cursor]

    # using zip and cursor.column_names
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}


@app.get("/student/get/{id}")
def get_student_by_id(id):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM Student WHERE student_id = {id};")
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}


def face_check(file) -> str: #student_id
    ...

class FaceProps(BaseModel):
    image: UploadFile
@app.post('/face')
def check_face(argu: FaceProps):
    return { 'student_id': face_check(argu.image)}




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

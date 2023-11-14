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

@app.get("/login-history/get/{id}")
def get_login_history_by_id(id):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM LoginHistory WHERE student_id = {id};")
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}

@app.get("/login-history/post/{id}")
def post_login_history(id,session_id,login_time,login_duration):
    cursor = cnx.cursor()
    cursor.execute(f"INSERT INTO LoginHistory (student_id, session_id, login_time, login_duration) VALUES ({id}, {session_id}, {login_time}, {login_duration});")
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}

@app.get("/login-history/put/{session_id}")
def put_login_history(session_id,new_login_duration):
    cursor = cnx.cursor()
    cursor.execute(f"UPDATE `LoginHistory` SET `login_duration`={new_login_duration} WHERE session_id = {session_id};")
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

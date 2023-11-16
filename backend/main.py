import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import datetime
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


@app.get("/timetable/get/{id}")
def get_timetable_by_id(id):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT Class.class_time, Course.course_id, Course.course_name, Classroom.classroom_address FROM Class,Course,Classroom,Student,Enrollment WHERE Student.student_id = '{id}' AND Student.student_id = Enrollment.student_id AND Enrollment.course_id = Course.course_id AND Enrollment.course_id = Class.course_id AND Enrollment.class_id = Class.class_id AND Class.classroom_id = Classroom.classroom_id ORDER BY Class.class_time ASC;")
    '''
    SELECT Class.class_time, Course.course_id, Course.course_name, Classroom.classroom_address
    FROM Class,Course,Classroom,Student,Enrollment
    WHERE Student.student_id = '{id}'
    AND Student.student_id = Enrollment.student_id
    AND Enrollment.course_id = Course.course_id
    AND Enrollment.course_id = Class.course_id
    AND Enrollment.class_id = Class.class_id
    AND Class.classroom_id = Classroom.classroom_id
    ORDER BY Class.class_time ASC;
    '''

    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"Timetable": rows}


@app.get("/teacher-message/get/{course_id}")
def get_teacher_message_by_course_id(course_id):
    
    cursor = cnx.cursor()
    cursor.execute(f"SELECT TeacherMessage.message_id, TeacherMessage.message, TeacherMessage.message_time FROM TeacherMessage WHERE TeacherMessage.course_id = '{course_id}' ORDER BY message_time DESC;")
    
    '''
    SELECT TeacherMessage.message_id, TeacherMessage.message, TeacherMessage.message_time
    FROM  TeacherMessage
    WHERE TeacherMessage.course_id = '{course_id}'
    ORDER BY message_time DESC;
    '''
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"Teacher_Messages": rows}



@app.get("/course/get/{student_id}")
def get_courses_enrolled_by_student_id(student_id):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT Course.course_id, Course.course_name FROM Student, Course, Enrollment WHERE Student.student_id = {student_id} AND Student.student_id = Enrollment.student_id AND  Enrollment.course_id = Course.course_id")
    '''
    SELECT Course.course_id, Course.course_name
    FROM Student, Course, Enrollment
    WHERE Student.student_id = {student_id}
    AND Student.student_id = Enrollment.student_id
    AND  Enrollment.course_id = Course.course_id
    '''
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"courses_enrolled": rows}

@app.get("/material/get/{course_id}")
def get_materials_by_course_id(course_id):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT Material.title, Material.url, Material.last_update FROM Material Where Material.course_id = '{course_id}';")
    
    '''
    SELECT Material.title, Material.url, Material.last_update
    FROM Material
    Where Material.course_id = {course_id};
    '''
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"Materials": rows}


@app.get(f"/upcoming-class/get/{id}")
def upcoming_class_get(id):
    cursor = cnx.cursor()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cmd = f"SELECT Class.class_time, Course.course_id, Course.course_name, Classroom.classroom_address FROM Class,Course,Classroom,Student,Enrollment WHERE Student.student_id = '{id}' AND Student.student_id = Enrollment.student_id AND Enrollment.course_id = Course.course_id AND Enrollment.course_id = Class.course_id AND Enrollment.class_id = Class.class_id AND Class.classroom_id = Classroom.classroom_id AND Class.class-time >= '{current_time}' ORDER BY Class.class_time ASC;"
    cursor.execute(cmd)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    val = "Not found" if not rows else "ok"
    return {"status": val, "rows": rows}

@app.post("/face-recognition/post")
def face_to_id():
    
    return None

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

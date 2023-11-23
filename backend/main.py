import logging
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import datetime
import mysql.connector
from pydantic import BaseModel
import check_face
import uuid
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
def get_student_by_id(id: str):
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
    cursor.execute(f"""
        SELECT Course.course_id, Course.course_name
        FROM Student
            LEFT JOIN Enrollment ON (Student.student_id = Enrollment.student_id)
            LEFT JOIN Course ON (Enrollment.course_id = Course.course_id)
        WHERE Student.student_id = {student_id};
    """)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "okay", "rows": rows}


@app.get("/material/get/{course_id}")
def get_materials_by_course_id(course_id):
    cursor = cnx.cursor()
    command = f"""
        SELECT material_id, title, url, description
        FROM Material
        Where course_id = '{course_id}';
    """
    cursor.execute(command)

    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "okay", "rows": rows}


@app.get("/upcoming-class/get/{id}")
def upcoming_class_get(id: str):
    cursor = cnx.cursor()
    cmd = f"""
        SELECT
            Class.class_time class_time,
            Course.course_id course_id,
            Course.course_name course_name,
            Classroom.classroom_address classroom_address,
            Course.course_id course_id,
            Class.teacher_message teacher_message,
            Class.zoom_link zoom_link,
            Class.duration_hour duration_hour,
            Class.class_id class_id
        FROM Student
            LEFT JOIN Enrollment ON (Student.student_id = Enrollment.student_id)
            LEFT JOIN Course ON (Enrollment.course_id = Course.course_id)
            LEFT JOIN Class ON (Enrollment.course_id = Class.course_id)
            LEFT JOIN Classroom ON (Class.classroom_id = Classroom.classroom_id)
        WHERE Student.student_id = '{id}'
            AND NOW() BETWEEN DATE_ADD(Class.class_time, INTERVAL -1 HOUR) AND DATE_ADD(Class.class_time, INTERVAL Class.duration_hour HOUR)
        ORDER BY Class.class_time ASC
        LIMIT 1;
    """
    cursor.execute(cmd)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "okay", "rows": rows}


@app.get("/login-history/{id}")
def get_login_history(id: str):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM LoginHistory where student_id = {id};")
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}


@app.put("/update-login-session/")
def update_login_session(session_id: str):
    cursor = cnx.cursor()
    command = f"""
        UPDATE `LoginHistory`
        SET login_duration = TIMESTAMPDIFF(SECOND, login_time, NOW())
        WHERE session_id = '{session_id}';
    """
    cursor.execute(command)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    cnx.commit()
    return {"status": "ok", "rows": rows}


@app.post("/add-login-session/")
def add_login_session(session_id: str, student_id: str):
    cursor = cnx.cursor()
    command = f"""
        INSERT INTO `LoginHistory` VALUES ('{student_id}', '{session_id}', NOW(), 0);
    """
    cursor.execute(command)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    cnx.commit()
    return {"status": "ok", "rows": rows}


@app.get("/face-recognition/post")
def face_to_id():
    result = check_face.check_face()
    if not result:
        return {"student_id": "none"}
    else:
        return {"student_id": result}


@app.get("/week-class/")
def get_week_class(student_id: str):
    cursor = cnx.cursor()
    command = f"""
        SELECT
            Class.course_id,
            Class.class_time,
            Classroom.classroom_address,
            Class.teacher_message,
            Class.duration_hour,
            Course.course_name
        FROM Student
            LEFT JOIN Enrollment ON (Student.student_id = Enrollment.student_id)
            LEFT JOIN Class ON (Enrollment.course_id = Class.course_id)
            LEFT JOIN Classroom ON (Class.classroom_id = Classroom.classroom_id)
            LEFT JOIN Course ON (Class.course_id = Course.course_id)
        WHERE Class.class_time BETWEEN DATE_SUB(NOW(), INTERVAL WEEKDAY(NOW()) DAY)
  AND DATE_ADD(DATE_SUB(NOW(), INTERVAL WEEKDAY(NOW()) DAY), INTERVAL 7 DAY)
            AND Student.student_id = '{student_id}'
    """
    cursor.execute(command)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    return {"status": "ok", "rows": rows}


@app.post(path="/send-email/")
def send_email(class_id: str, recipient: str):
    cursor = cnx.cursor()
    command = f"""
        SELECT
            Class.course_id,
            Class.class_time,
            Classroom.classroom_address,
            Class.teacher_message,
            Class.duration_hour,
            Course.course_name,
            Class.zoom_link
        FROM Class
            LEFT JOIN Course ON (Class.course_id = Course.course_id)
            LEFT JOIN Classroom ON (Class.classroom_id = Classroom.classroom_id)
        WHERE Class.class_id = '{class_id}'
    """
    cursor.execute(command)
    rows = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()
    row = rows[0]

    cursor = cnx.cursor()
    command = f"""
        SELECT
            Material.title title,
            Material.url url
        FROM Material
        WHERE Material.course_id = '{row["course_id"]}'
    """
    cursor.execute(command)
    materials = [dict(zip(cursor.column_names, row)) for row in cursor]
    cursor.close()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Course {row["course_id"]} information'
    msg['From'] = recipient
    msg['To'] = recipient
    html_content = f"""
<h2>{row['course_id']}: {row['course_name']}<h2>
<h4>Class Time: {row['class_time']}</h4>
<h4>Location: {row['classroom_address']}</h4>
<h4>Teacher Message: {row['teacher_message']}</h4>
<h4>Zoom Link: {row['zoom_link']}</h4>
------------------------
<h3>Course Material</h3>
""" + "\n".join([f'<h4><a href="{material["url"]}"target="__blank">{material["title"]}</a></h4>' for material in materials])

    # Add HTML content
    part = MIMEText(html_content, 'html')
    msg.attach(part)
    try:
        with SMTP('smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login('chanyatfu0616@gmail.com', 'aaig dxpw koju ggte')
            server.sendmail('chanyatfu0616@gmail.com', recipient, msg.as_string())
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

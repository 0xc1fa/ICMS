# ICMS

This repo present an Intelligent Course Management System (ICMS) with a facial login component, which contains the following functions:

- When a student login with his/her face, his/her information such as name, login time, and welcome message will be presented in the graphics user interface (GUI).
- If the student has class within one hour, the corresponding course information, classroom address, teacher’s message, links of Zoom, tutorial/lecture notes, other course materials and so on and so forth will be presented in the GUI. The student could click the links to redirect to Zoom or other materials. The GUI should also allow the student to send the above information to his/her email address by email.
- If the student does not have class at the moment, the GUI could present a personal class timetable for the student.
- The system should record the latest behaviour of the student, such as when he/she logins the system, how long the student stays in the system, etc.

- Login with **face**
- Shown **name**, **login time**, welcome message after login
- (If has class within one hour) Show **course information**, **classroom address**, **teacher’s message**, **links of Zoom**, **tutorial/lecture notes**, **other course materials**
- (If has class within one hour) Send the above information to his/her **email address** by email
- (Else) show personal **class timetable**
- (Else) quick add to google calendar
- Record **login time**, **stay time**, etc.

## Little Extra Function
- Add timetable to Google calendar

## Development Tools.
Face Login: Python + OpenCV (full codes provided.)
GUI: Python GUI or Qt. (sample codes provided.)
Database: Python + MySQL (sample codes provided.)
Other: You can use any other Python packages if you see fit.

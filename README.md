# ICMS
This repo present an Intelligent Course Management System (ICMS) with a facial login component, which contains the following functions:

**You can change the page shown by going to App.py and change `self.pages.setCurrentIndex(1)`, 0 is login page, 1 is after login**

- When a student login with his/her face, his/her information such as name, login time, and welcome message will be presented in the graphics user interface (GUI).
- If the student has class within one hour, the corresponding course information, classroom address, teacher’s message, links of Zoom, tutorial/lecture notes, other course materials and so on and so forth will be presented in the GUI. The student could click the links to redirect to Zoom or other materials. The GUI should also allow the student to send the above information to his/her email address by email.
- If the student does not have class at the moment, the GUI could present a personal class timetable for the student.
- The system should record the latest behaviour of the student, such as when he/she logins the system, how long the student stays in the system, etc.

## Requirements.
GUI: Each group may design GUI based on the understanding of the above user requirement (You could make your own design choice, because in real project, clients typically don’t know what they really want).
Database: your database should have at least five tables. How to design the tables is your design choice.

## Little Extra Function
- Add timetable to Google calendar

## Development Tools.
Face Login: Python + OpenCV (full codes provided.)
GUI: Python GUI or Qt. (sample codes provided.)
Database: Python + MySQL (sample codes provided.)
Other: You can use any other Python packages if you see fit.

## Marks (course project 20% of the final mark).
- 10% for software development. (4% GUI + 6% database)
- Other 10% for 5-minute presentation, including but not limited to development plan, milestones, contribution of each group member, video recording of demo, software design, database design (ER Diagram, tables), difficulties you encountered and how to solve them, etc.
- Live demo is allowed, but please make sure your program works well and stably in order to save time in presentation.
- Creative GUI design, creative software functions or creative DB design will have bonus points.

## LLM Related
- You are welcome to involve ChatGPTin your design loop.
- You have toclearly discuss what and how ChatGPThelp your projects (e.g., which part you used ChatGPT, the percentage (%) of contribution of ChatGPTin the project) in the 5-min presentation. Submit all prompts and returns from ChatGPTas supplementary materials.
- Excellent use of LLMs may have bonus points.

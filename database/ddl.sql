INSERT INTO `Student` VALUES ('3035690201', 'Chan Yat Man', "chantaiman1@gmail.com" , "password1");
INSERT INTO `Student` VALUES ('3035690202', 'Chan Yi Man', "chanyiman2@gmail.com", 'password2');
INSERT INTO `Student` VALUES ('3035690203', 'Chan Sam Man', "chansamman1234@gmail.com", 'password3');
INSERT INTO `Student` VALUES ('3035690001', 'Chan Tai Man', "testing@gmail.com", 'password');


INSERT INTO `Classroom` VALUES ('1', 'Room 1');
INSERT INTO `Classroom` VALUES ('2', 'Room 2');
INSERT INTO `Classroom` VALUES ('3', 'Room 3');
INSERT INTO `Classroom` VALUES ('4', 'Room 4');
INSERT INTO `Classroom` VALUES ('5', 'Room 5');

INSERT INTO `Course` VALUES ('COMP3111', 'Software Engineering', 'A course about software engineering');
INSERT INTO `Course` VALUES ('COMP3278', 'Introduction to database management system', 'The course that you are currently enrolling');
INSERT INTO `Course` VALUES ('MATH3333', 'Linear Algebar', 'This is an introductory course on linear algebra, which is a prerequisite for many courses in mathematics, statistics, engineering, and the sciences.');

INSERT INTO `Class` VALUES ('COMP3111', '1', '2023-11-22 22:40:00', '1', 'Welcome to COMP3111', 'https://zoom.us/j/123456789');
INSERT INTO `Class` VALUES ('COMP3111', '2', '2023-11-23 11:30:00', '2', 'Bring your laptop', 'https://zoom.us/j/123456789');
INSERT INTO `Class` VALUES ('COMP3278', '1', '2018-23-24 13:30:00', '3', 'have quiz today', 'https://zoom.us/j/123456789');
INSERT INTO `Class` VALUES ('COMP3278', '2', '2018-23-25 14:30:00', '3', 'More quiz today', 'https://zoom.us/j/123456789');
INSERT INTO `Class` VALUES ('MATH3333', '1', '2018-23-26 16:30:00', '4', 'Endless assignments', 'https://zoom.us/j/123456789');
INSERT INTO `Class` VALUES ('MATH3333', '2', '2018-23-28 15:30:00', '5', 'Almost end sem', 'https://zoom.us/j/123456789');

INSERT INTO `TeacherMessage` VALUES ('1', 'COMP3111', 'Welcome to COMP3111', '2018-11-01 10:30:00');
INSERT INTO `TeacherMessage` VALUES ('2', 'COMP3278', 'The project is due on 23rd Nov', '2018-11-02 10:30:00');

INSERT INTO `LoginHistory` VALUES ('3035690001', 'ae48a13d-a68f-47eb-a225-188e56807327', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', 'fb1cdf8a-971c-4ec5-87a1-3e48cdef309c', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', '94750f3f-3709-4705-8682-8c108fd618a7', '2018-11-01 10:30:00', '523');

INSERT INTO `Material` VALUES ('1', 'COMP3278', 'Lecture 1', 'someurl_to_dropbox', '2018-11-01 10:30:00', 'PPT of lecture 1');
INSERT INTO `Material` VALUES ('2', 'COMP3278', 'Lecture 2', 'someurl_to_dropbox', '2018-09-01 10:30:00', 'PPT of lecture 2');
INSERT INTO `Material` VALUES ('3', 'COMP3278', 'Tutorial 1', 'someurl_to_dropbox', '2018-09-16 10:30:00', 'PPT of lecture 3');
INSERT INTO `Material` VALUES ('4', 'COMP3111', 'Lecture 1', 'someurl_to_dropbox', '2018-11-01 10:30:00', 'PPT of lecture 1');
INSERT INTO `Material` VALUES ('5', 'COMP3111', 'Lecture 2', 'someurl_to_dropbox', '2018-09-01 10:30:00', 'PPT of lecture 2');
INSERT INTO `Material` VALUES ('6', 'COMP3111', 'Tutorial 1', 'someurl_to_dropbox', '2018-09-16 10:30:00', 'PPT of lecture 3');

INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3278');
INSERT INTO `Enrollment` VALUES ('3035690001', 'MATH3333');
INSERT INTO `Enrollment` VALUES ('3035690201', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690202', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690203', 'COMP3278');


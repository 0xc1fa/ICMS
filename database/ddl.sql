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

INSERT INTO `Class` VALUES ('COMP3111', '1', '2018-11-01 10:30:00', '1');
INSERT INTO `Class` VALUES ('COMP3111', '2', '2018-11-02 10:30:00', '2');
INSERT INTO `Class` VALUES ('COMP3278', '1', '2018-11-03 10:30:00', '3');
INSERT INTO `Class` VALUES ('COMP3278', '2', '2018-11-04 10:30:00', '3');
INSERT INTO `Class` VALUES ('MATH3333', '1', '2018-11-05 10:30:00', '4');
INSERT INTO `Class` VALUES ('MATH3333', '2', '2018-11-06 10:30:00', '5');

INSERT INTO `TeacherMessage` VALUES ('1', 'COMP3111', 'Welcome to COMP3111', '2018-11-01 10:30:00');
INSERT INTO `TeacherMessage` VALUES ('2', 'COMP3278', 'The project is due on 23rd Nov', '2018-11-02 10:30:00');

INSERT INTO `LoginHistory` VALUES ('3035690001', '1', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', '2', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', '3', '2018-11-01 10:30:00', '523');

INSERT INTO `Material` VALUES ('1', 'COMP3278', 'Lecture 1', 'someurl_to_dropbox', '2018-11-01 10:30:00');
INSERT INTO `Material` VALUES ('2', 'COMP3278', 'Lecture 2', 'someurl_to_dropbox', '2018-09-01 10:30:00');
INSERT INTO `Material` VALUES ('3', 'COMP3278', 'Tutorial 1', 'someurl_to_dropbox', '2018-09-16 10:30:00');

INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3278');
INSERT INTO `Enrollment` VALUES ('3035690001', 'MATH3333');
INSERT INTO `Enrollment` VALUES ('3035690201', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690202', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690203', 'COMP3278');


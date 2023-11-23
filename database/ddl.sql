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

INSERT INTO `Class` VALUES ('COMP3111', '451758fa-8d50-47f0-a0a2-2468ec9a3c5c', '2023-11-23 03:30:00', '1', 'Welcome to COMP3111', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3111', '429a9167-3a23-4f64-beed-535fbb31afee', '2023-11-23 04:30:00', '2', 'Bring your laptop', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3278', '1f3784f5-b278-4d08-919e-1449592cde4b', '2023-11-24 13:30:00', '3', 'have quiz today', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3278', '72e777c2-76f6-42f9-917d-6c41c7a41a33', '2023-11-25 14:30:00', '3', 'More quiz today', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('MATH3333', '8c92197a-e6cb-44d0-aa89-9d7bc392ee54', '2023-11-26 16:30:00', '4', 'Endless assignments', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('MATH3333', '4d0dfcac-79d2-4b88-8d8f-8f06ff887821', '2023-11-27 15:30:00', '5', 'Almost end sem', 'https://zoom.us/j/123456789', 1);

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


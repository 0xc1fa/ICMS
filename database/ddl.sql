INSERT INTO `Student` VALUES ('3035690201', 'Chan Yat Man', "chantaiman1@gmail.com" , "password1");
INSERT INTO `Student` VALUES ('3035690202', 'Chan Yi Man', "chanyiman2@gmail.com", 'password2');
INSERT INTO `Student` VALUES ('3035690203', 'Chan Sam Man', "chansamman1234@gmail.com", 'password3');
INSERT INTO `Student` VALUES ('3035690001', 'Chan Tai Man', "chanyatfu0616@gmail.com", 'password');

INSERT INTO `Classroom` VALUES ('1', 'Room 1');
INSERT INTO `Classroom` VALUES ('2', 'Room 2');
INSERT INTO `Classroom` VALUES ('3', 'Room 3');
INSERT INTO `Classroom` VALUES ('4', 'Room 4');
INSERT INTO `Classroom` VALUES ('5', 'Room 5');
INSERT INTO `Classroom` VALUES ('6', 'CPD-G.02');
INSERT INTO `Classroom` VALUES ('7', 'KB132');
INSERT INTO `Classroom` VALUES ('8', 'CPD-1.43');
INSERT INTO `Classroom` VALUES ('9', 'MWT1');
INSERT INTO `Classroom` VALUES ('10', 'CBLG205');

INSERT INTO `Course` VALUES ('COMP3111', 'Software Engineering', 'A course about software engineering');
INSERT INTO `Course` VALUES ('COMP3278', 'Introduction to database management system', 'The course that you are currently enrolling');
INSERT INTO `Course` VALUES ('MATH3333', 'Linear Algebar', 'This is an introductory course on linear algebra, which is a prerequisite for many courses in mathematics, statistics, engineering, and the sciences.');
INSERT INTO `Course` VALUES ('ELEC4342', 'Embedded machine learning', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');
INSERT INTO `Course` VALUES ('ELEC3361', 'Natural Language Processing', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');
INSERT INTO `Course` VALUES ('CAES9541', 'ED for EEEng', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');

INSERT INTO `Class` VALUES ('COMP3111', '451758fa-8d50-47f0-a0a2-2468ec9a3c5c', '2023-11-23 11:30:00', '1', 'Welcome to COMP3111', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3111', '429a9167-3a23-4f64-beed-535fbb31afee', '2023-11-23 04:30:00', '2', 'Bring your laptop', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3278', '1f3784f5-b278-4d08-919e-1449592cde4b', '2023-11-24 13:30:00', '3', 'have quiz today', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3278', '72e777c2-76f6-42f9-917d-6c41c7a41a33', '2023-11-25 14:30:00', '3', 'More quiz today', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('MATH3333', '8c92197a-e6cb-44d0-aa89-9d7bc392ee54', '2023-11-26 16:30:00', '4', 'Endless assignments', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('MATH3333', '4d0dfcac-79d2-4b88-8d8f-8f06ff887821', '2023-11-27 15:30:00', '5', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('ELEC4342', 'f68098ad-a8c8-4e58-836d-670a36dabbcf', '2023-11-20 09:30:00', '6', 'Almost end sem', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3278', 'afef8f36-092d-414d-8918-f8764a38f6df', '2023-11-20 14:30:00', '9', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('ELEC3361', 'a24cc2e7-fb38-480b-a467-fb7db68c5579', '2023-11-21 09:30:00', '7', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('ELEC3848', 'f2b1b331-da57-41e6-916b-abb8b63636d3', '2023-11-21 15:30:00', '10', 'Almost end sem', 'https://zoom.us/j/123456789', 3);
INSERT INTO `Class` VALUES ('ELEC4342', '1b19529c-f368-487c-ab96-96f1d3b38a66', '2023-11-23 09:30:00', '6', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3278', '57cd4634-aa77-4b7e-8fd0-5f99bfc4cc0a', '2023-11-23 09:30:00', '9', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3361', '54ba4ac4-5877-40ef-bc42-fdf12b0aa276', '2023-11-24 09:30:00', '7', 'Almost end sem', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('CAES9541', '9f4905d6-6c20-4546-ba98-874101fadc83', '2023-11-24 15:30:00', '8', 'Almost end sem', 'https://zoom.us/j/123456789', 2);


INSERT INTO `LoginHistory` VALUES ('3035690001', 'ae48a13d-a68f-47eb-a225-188e56807327', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', 'fb1cdf8a-971c-4ec5-87a1-3e48cdef309c', '2018-11-01 10:30:00', '100');
INSERT INTO `LoginHistory` VALUES ('3035690001', '94750f3f-3709-4705-8682-8c108fd618a7', '2018-11-01 10:30:00', '523');

INSERT INTO `Material` VALUES ('1', 'COMP3278', 'Lecture 1', 'https://www.dropbox.com/scl/fi/6aqbundo0p3i200vm45ja/Lecture_1_Introduction.pdf?rlkey=44084i8m3ojuiyq1bi7tk3igo&dl=0', '2018-11-01 10:30:00', 'Lecture_1_Introduction.pdf');
INSERT INTO `Material` VALUES ('2', 'COMP3278', 'Lecture 2', 'https://www.dropbox.com/scl/fi/bgrkm0i5f20gff4ievz1z/Lecture_2_ER_model.pdf?rlkey=qxs4tfprk4vf0orwqchmeabwn&dl=0', '2018-09-01 17:10:00', 'Lecture_2_ER_model.pdf');
INSERT INTO `Material` VALUES ('3', 'COMP3278', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/og4ylr01mpbvgoeu540ad/tutorial-1_MySQL_2023-5.pdf?rlkey=my6vr5i1nh00q8ttgqv860hwp&dl=0', '2018-10-16 11:30:00', 'Tutorial 1_MySQL_2023-5.pdf');
INSERT INTO `Material` VALUES ('4', 'COMP3111', 'Lecture 1', 'https://www.dropbox.com/scl/fi/5iez5qijpugbie304608j/L0-Course-Preliminaries-and-Motivation-v1-4.pdf?rlkey=ppwsza5n1t9vxyvmr1eixcqcn&dl=0', '2018-11-01 10:30:00', 'L0 - Course Preliminaries and Motivation v1-4.pdf');
INSERT INTO `Material` VALUES ('5', 'COMP3111', 'Lecture 2', 'https://www.dropbox.com/scl/fi/3m0n6nbuijfvr3g6k9a88/L1-Introduction-v1-3.pdf?rlkey=u2spm232wvmsd5z1xj5aq8697&dl=0', '2018-09-03 15:09:00', 'L1 - Introduction v1-3.pdf');
INSERT INTO `Material` VALUES ('6', 'COMP3111', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/7clf49qpzew2fny3o6s75/Tutorial-1-Quiz-Preparation_v3-3.pdf?rlkey=pysj5ybquc6qtsg3i24uk0mn4&dl=0', '2018-09-18 00:30:53', 'Tutorial 1 - Quiz Preparation_v3-3.pdf');
INSERT INTO `Material` VALUES ('7', 'ELEC4342', 'Lecture 1', 'https://www.dropbox.com/scl/fi/d376xnfeacz2v78gh52wf/lab1_handout_ELEC3443.pdf?rlkey=anmiowomgxvglpdhork5wy8oc&dl=0', '2018-11-12 10:45:03', 'lab1_handout_ELEC3443.pdf');
INSERT INTO `Material` VALUES ('8', 'ELEC4342', 'Lecture 2', 'https://www.dropbox.com/scl/fi/b2ua60n6rvq8r4ymupki0/lab2_handout_ELEC3443-1.pdf?rlkey=ceikhwk8d5ayuydhfgzqmmo0i&dl=0', '2018-09-23 17:30:00', 'lab2_handout_ELEC3443-1.pdf');
INSERT INTO `Material` VALUES ('9', 'ELEC4342', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/baps194jh4ssh2c5xvc3p/lab3_handout_ELEC3443-2.pdf?rlkey=6su4b3c0cwkb7pq1h8vv2ki9z&dl=0', '2018-10-01 10:30:50', 'lab3_handout_ELEC3443-2.pdf');
INSERT INTO `Material` VALUES ('10', 'CAES9541', 'Lecture 1', 'https://www.dropbox.com/scl/fi/bk0skgcaexuzimpiyxha1/CCST9054-LECTURE-1-INTRO-AND-PPG.pdf?rlkey=1f4rqt3slmmz2f67325v7xi3e&dl=0', '2018-10-16 18:50:00', 'CAES9541 LECTURE 1 - INTRO AND PPG.pdf');
INSERT INTO `Material` VALUES ('11', 'CAES9541', 'Lecture 2', 'https://www.dropbox.com/scl/fi/892io72e7hwhw3i7el8dy/CCST9054-LECTURE-2_Congo_Wars.pdf?rlkey=me8rwwbg8fdf5q1ey1eru7kpo&dl=0', '2018-11-16 10:30:04', 'CAES9541 LECTURE 2_Congo_Wars.pdf');
INSERT INTO `Material` VALUES ('12', 'CAES9541', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/1cxzzx0w6i3d20wsrp5tu/CCST9054-TUTORIAL-1_Slides.pdf?rlkey=m9blgsgeurjfxadpoau8wq9ue&dl=0', '2018-09-16 10:20:30', 'CAES9541 TUTORIAL 1_Slides.pdf');
INSERT INTO `Material` VALUES ('13', 'MATH3333', 'Lecture 1', 'https://www.dropbox.com/scl/fi/6p1ah02lr4mzwbhj57adf/Discrete-Math-Lecture-1.pdf?rlkey=emzue5zxwjob737q338p4ijai&dl=0', '2018-09-01 10:30:01', 'Discrete Math Lecture 1.pdf');
INSERT INTO `Material` VALUES ('14', 'MATH3333', 'Lecture 2', 'https://www.dropbox.com/scl/fi/rn9up903tbiusajzewqcv/Discrete-Math-Lecture-2.pdf?rlkey=agp25x40i3hul9v30q6de77oj&dl=0', '2018-10-16 01:10:22', 'Discrete Math Lecture 2.pdf');
INSERT INTO `Material` VALUES ('15', 'MATH3333', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/7mg1awxojwqaa2lh75en5/Discrete-Math-T1_E.pdf?rlkey=meerg5495p0gqldlxxeaxapl6&dl=0', '2018-09-01 10:30:00', 'Discrete Math T1_E.pdf');
INSERT INTO `Material` VALUES ('13', 'ELEC3361', 'Lecture 1', 'https://www.dropbox.com/scl/fi/s7vmljnlpem6xz0ensmgi/COMP2396_Ch1_Introduction.pdf?rlkey=shuuh7989brrlsrlbcd1m0hme&dl=0', '2018-11-16 00:10:01', 'Ch1_Introduction.pdf');
INSERT INTO `Material` VALUES ('14', 'ELEC3361', 'Lecture 2', 'https://www.dropbox.com/scl/fi/endt10vfba34jagvvflhq/COMP2396_Ch2_Class_And_Objects-1.pdf?rlkey=li6socsqi6gg21b6yz928sz5x&dl=0', '2018-11-12 13:10:22', 'Ch2_Class_And_Objects-1.pdf');
INSERT INTO `Material` VALUES ('15', 'ELEC3361', 'Tutorial 1', 'https://www.dropbox.com/scl/fi/7t9bl5ksao9ftyabysunr/COMP2396_Ch3_Primitives_and_References.pdf?rlkey=zwbmgt95f4847xoenqdmfgi1y&dl=0', '2018-09-16 10:30:00', 'Ch3_Primitives_and_References.pdf');

INSERT INTO `Enrollment` VALUES ('3035690001', 'ELEC4342');
INSERT INTO `Enrollment` VALUES ('3035690001', 'MATH3333');
INSERT INTO `Enrollment` VALUES ('3035690001', 'ELEC3361');
INSERT INTO `Enrollment` VALUES ('3035690001', 'CAES9541');
INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3278');
INSERT INTO `Enrollment` VALUES ('3035690201', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690202', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690203', 'COMP3278');

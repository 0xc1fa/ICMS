INSERT INTO `Student` VALUES ('3035690201', 'Chan Yat Man', "chantaiman1@gmail.com" , "password1");
INSERT INTO `Student` VALUES ('3035690202', 'Chan Yi Man', "chanyiman2@gmail.com", 'password2');
INSERT INTO `Student` VALUES ('3035690203', 'Chan Sam Man', "chansamman1234@gmail.com", 'password3');
INSERT INTO `Student` VALUES ('3035690001', 'Chan Tai Man', "chanyatfu0616@gmail.com", 'password');

INSERT INTO `Classroom` VALUES ('1', 'LE3');
INSERT INTO `Classroom` VALUES ('2', 'KKLG1.05');
INSERT INTO `Classroom` VALUES ('3', 'MB217');
INSERT INTO `Classroom` VALUES ('4', 'CYM 105');
INSERT INTO `Classroom` VALUES ('5', 'TTB210');
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
INSERT INTO `Course` VALUES ('ELEC3848', 'Intergrated design project', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');
INSERT INTO `Course` VALUES ('ELEC3848', 'Intergrated design project', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');
INSERT INTO `Course` VALUES ('COMP3361', 'Natural language processing', 'The group project emphasizes on exercising students’ creativity to provide innovative solutions for solving real-world problems/issues through sophisticated technologies related to IoT or embedded systems.');


INSERT INTO `Class` VALUES ('ELEC4342', 'f68098ad-a8c8-4e58-836d-670a36dabbcf', '2023-11-20 09:30:00', '6', 'Almost end sem', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('COMP3278', 'afef8f36-092d-414d-8918-f8764a38f6df', '2023-11-20 14:30:00', '9', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('ELEC3361', 'a24cc2e7-fb38-480b-a467-fb7db68c5579', '2023-11-21 09:30:00', '7', 'Almost end sem', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('ELEC3848', 'f2b1b331-da57-41e6-916b-abb8b63636d3', '2023-11-21 15:30:00', '10', 'Almost end sem', 'https://zoom.us/j/123456789', 3);
INSERT INTO `Class` VALUES ('ELEC4342', '1b19529c-f368-487c-ab96-96f1d3b38a66', '2023-11-23 09:30:00', '6', 'prsentation today', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3278', '57cd4634-aa77-4b7e-8fd0-5f99bfc4cc0a', '2023-11-23 09:30:00', '9', 'Mid-term at 11:00', 'https://zoom.us/j/123456789', 1);
INSERT INTO `Class` VALUES ('COMP3361', '54ba4ac4-5877-40ef-bc42-fdf12b0aa276', '2023-11-24 09:30:00', '7', 'Bring 3 laptops', 'https://zoom.us/j/123456789', 2);
INSERT INTO `Class` VALUES ('CAES9541', '9f4905d6-6c20-4546-ba98-874101fadc83', '2023-11-24 15:30:00', '8', 'Reading week this time extra lecture', 'https://zoom.us/j/123456789', 2);


INSERT INTO `LoginHistory` VALUES ('3035690001', 'ae48a13d-a68f-47eb-a225-188e56807327', '2018-11-21 10:31:57', '32');
INSERT INTO `LoginHistory` VALUES ('3035690001', 'fb1cdf8a-971c-4ec5-87a1-3e48cdef309c', '2018-11-21 13:19:22', '503');
INSERT INTO `LoginHistory` VALUES ('3035690001', '94750f3f-3709-4705-8682-8c108fd618a7', '2018-11-22 15:17:36', '1021');
INSERT INTO `LoginHistory` VALUES ('3035690001', '195da1c5-1c9f-1087-1a2c-8c72b6dfc18a1', '2018-11-22 17:00:08', '42');
INSERT INTO `LoginHistory` VALUES ('3035690001', 'b948da1d-1998-ac01-0135-a7c789d119b81', '2018-11-23 09:22:37', '27');
INSERT INTO `LoginHistory` VALUES ('3035690001', '51c238b4-d3a8-be11-1473-c55108f156487', '2018-11-24 21:58:52', '3015');
INSERT INTO `LoginHistory` VALUES ('3035690001', 'b1d234e7-9937-1341-d81a-86828c1618a7', '2018-11-25 11:48:03', '492');

INSERT INTO `Material` VALUES ('1', 'COMP3278', 'Lecture 1 Slides', 'https://www.dropbox.com/scl/fi/6aqbundo0p3i200vm45ja/Lecture_1_Introduction.pdf?rlkey=44084i8m3ojuiyq1bi7tk3igo&dl=1', '2018-11-01 10:30:00', 'Lecture_1_Introduction.pdf');
INSERT INTO `Material` VALUES ('2', 'COMP3278', 'Lecture 2 Slides', 'https://www.dropbox.com/scl/fi/bgrkm0i5f20gff4ievz1z/Lecture_2_ER_model.pdf?rlkey=qxs4tfprk4vf0orwqchmeabwn&dl=1', '2018-09-01 17:10:00', 'Lecture_2_ER_model.pdf');
INSERT INTO `Material` VALUES ('3', 'COMP3278', 'Lecture 3 Slides', 'https://www.dropbox.com/scl/fi/og4ylr01mpbvgoeu540ad/tutorial-1_MySQL_2023-5.pdf?rlkey=my6vr5i1nh00q8ttgqv860hwp&dl=1', '2018-10-16 11:30:00', 'Tutorial 1_MySQL_2023-5.pdf');
INSERT INTO `Material` VALUES ('4', 'COMP3278', 'Lecture 4 Slides', 'https://www.dropbox.com/scl/fi/5iez5qijpugbie304608j/L0-Course-Preliminaries-and-Motivation-v1-4.pdf?rlkey=ppwsza5n1t9vxyvmr1eixcqcn&dl=1', '2018-11-01 10:30:00', 'L0 - Course Preliminaries and Motivation v1-4.pdf');
INSERT INTO `Material` VALUES ('5', 'COMP3278', 'Lecture 5 Slides', 'https://www.dropbox.com/scl/fi/3m0n6nbuijfvr3g6k9a88/L1-Introduction-v1-3.pdf?rlkey=u2spm232wvmsd5z1xj5aq8697&dl=1', '2018-09-03 15:09:00', 'L1 - Introduction v1-3.pdf');
INSERT INTO `Material` VALUES ('6', 'COMP3278', 'Tutorial 1 Slides', 'https://www.dropbox.com/scl/fi/7clf49qpzew2fny3o6s75/Tutorial-1-Quiz-Preparation_v3-3.pdf?rlkey=pysj5ybquc6qtsg3i24uk0mn4&dl=1', '2018-09-18 00:30:53', 'Tutorial 1 - Quiz Preparation_v3-3.pdf');
INSERT INTO `Material` VALUES ('7', 'COMP3278', 'Tutorial 2 Slides', 'https://www.dropbox.com/scl/fi/d376xnfeacz2v78gh52wf/lab1_handout_ELEC3443.pdf?rlkey=anmiowomgxvglpdhork5wy8oc&dl=1', '2018-11-12 10:45:03', 'lab1_handout_COMP3278.pdf');
INSERT INTO `Material` VALUES ('8', 'ELEC4342', 'Lecture 1 Slides', 'https://www.dropbox.com/scl/fi/b2ua60n6rvq8r4ymupki0/lab2_handout_ELEC3443-1.pdf?rlkey=ceikhwk8d5ayuydhfgzqmmo0i&dl=1', '2018-09-23 17:30:00', 'lab2_handout_ELEC4342-1.pdf');
INSERT INTO `Material` VALUES ('9', 'ELEC4342', 'Tutorial 1 Slides', 'https://www.dropbox.com/scl/fi/baps194jh4ssh2c5xvc3p/lab3_handout_ELEC3443-2.pdf?rlkey=6su4b3c0cwkb7pq1h8vv2ki9z&dl=1', '2018-10-01 10:30:50', 'lab3_handout_ELEC4342-2.pdf');
INSERT INTO `Material` VALUES ('10', 'CAES9541', 'Lecture 1 Slides', 'https://www.dropbox.com/scl/fi/bk0skgcaexuzimpiyxha1/CCST9054-LECTURE-1-INTRO-AND-PPG.pdf?rlkey=1f4rqt3slmmz2f67325v7xi3e&dl=1', '2018-10-16 18:50:00', 'CAES9541 LECTURE 1 - INTRO AND PPG.pdf');
INSERT INTO `Material` VALUES ('11', 'CAES9541', 'Lecture 2 Slides', 'https://www.dropbox.com/scl/fi/892io72e7hwhw3i7el8dy/CCST9054-LECTURE-2_Congo_Wars.pdf?rlkey=me8rwwbg8fdf5q1ey1eru7kpo&dl=1', '2018-11-16 10:30:04', 'CAES9541 LECTURE 2_Congo_Wars.pdf');
INSERT INTO `Material` VALUES ('12', 'CAES9541', 'Tutorial 1 Slides', 'https://www.dropbox.com/scl/fi/1cxzzx0w6i3d20wsrp5tu/CCST9054-TUTORIAL-1_Slides.pdf?rlkey=m9blgsgeurjfxadpoau8wq9ue&dl=1', '2018-09-16 10:20:30', 'CAES9541 TUTORIAL 1_Slides.pdf');
INSERT INTO `Material` VALUES ('13', 'ELEC3361', 'Lecture 1 Slides', 'https://www.dropbox.com/scl/fi/6p1ah02lr4mzwbhj57adf/Discrete-Math-Lecture-1.pdf?rlkey=emzue5zxwjob737q338p4ijai&dl=1', '2018-09-01 10:30:01', 'ELEC3361 Lecture 1.pdf');
INSERT INTO `Material` VALUES ('14', 'ELEC3361', 'Lecture 2 Slides', 'https://www.dropbox.com/scl/fi/rn9up903tbiusajzewqcv/Discrete-Math-Lecture-2.pdf?rlkey=agp25x40i3hul9v30q6de77oj&dl=1', '2018-10-16 01:10:22', 'ELEC3361 Lecture 2.pdf');
INSERT INTO `Material` VALUES ('15', 'ELEC3361', 'Lecture 1 Slides', 'https://www.dropbox.com/scl/fi/7mg1awxojwqaa2lh75en5/Discrete-Math-T1_E.pdf?rlkey=meerg5495p0gqldlxxeaxapl6&dl=0&dl=1', '2018-09-01 10:30:00', 'ELEC3361 T1_E.pdf');
INSERT INTO `Material` VALUES ('16', 'ELEC3361', 'Lecture 2 Slides', 'https://www.dropbox.com/scl/fi/s7vmljnlpem6xz0ensmgi/COMP2396_Ch1_Introduction.pdf?rlkey=shuuh7989brrlsrlbcd1m0hme&dl=1', '2018-11-16 00:10:01', 'Ch1_Introduction.pdf');
INSERT INTO `Material` VALUES ('17', 'ELEC3361', 'Lecture 3 Slides', 'https://www.dropbox.com/scl/fi/endt10vfba34jagvvflhq/COMP2396_Ch2_Class_And_Objects-1.pdf?rlkey=li6socsqi6gg21b6yz928sz5x&dl=1', '2018-11-12 13:10:22', 'Ch2_Class_And_Objects-1.pdf');
INSERT INTO `Material` VALUES ('18', 'ELEC3361', 'Tutorial 1 Slides', 'https://www.dropbox.com/scl/fi/7t9bl5ksao9ftyabysunr/COMP2396_Ch3_Primitives_and_References.pdf?rlkey=zwbmgt95f4847xoenqdmfgi1y&dl=1', '2018-09-16 10:30:00', 'Ch3_Primitives_and_References.pdf');
INSERT INTO `Material` VALUES ('19', 'COMP3278', 'Sample Presentation Video', 'https://www.dropbox.com/scl/fi/ifamtu3k357ngec37t4lz/Sample-Presentation.mp4?rlkey=t1ch2bypayajhhan1i4ir0pub&dl=1', '2018-10-27 17:25:31', 'sample_video.mp4');

INSERT INTO `Enrollment` VALUES ('3035690001', 'ELEC4342');
INSERT INTO `Enrollment` VALUES ('3035690001', 'ELEC3361');
INSERT INTO `Enrollment` VALUES ('3035690001', 'CAES9541');
INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3361');
INSERT INTO `Enrollment` VALUES ('3035690001', 'COMP3278');
INSERT INTO `Enrollment` VALUES ('3035690001', 'ELEC3848');
INSERT INTO `Enrollment` VALUES ('3035690201', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690202', 'COMP3111');
INSERT INTO `Enrollment` VALUES ('3035690203', 'COMP3278');

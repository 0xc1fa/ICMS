DROP TABLE IF EXISTS `Student`;
CREATE TABLE `Student` (
  `student_id` VARCHAR(10) NOT NULL,
  `student_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Classroom`;
CREATE TABLE `Classroom` (
  `classroom_id` INT NOT NULL,
  `classroom_address` varchar(50) NOT NULL,
  PRIMARY KEY (`classroom_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Course`;
CREATE TABLE `Course` (
  `course_id` VARCHAR(10) NOT NULL,
  `course_name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Class`;
CREATE TABLE `Class` (
  `course_id` VARCHAR(10) NOT NULL,
  `class_id` VARCHAR(36) NOT NULL,
  `class_time` DATETIME NOT NULL,
  `classroom_id` INT NOT NULL,
  `teacher_message` VARCHAR(255),
  `zoom_link` VARCHAR(1023),
  `duration_hour` INT NOT NULL,
  PRIMARY KEY (`class_id`),
  FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`) ON DELETE CASCADE,
  FOREIGN KEY (`classroom_id`) REFERENCES `Classroom`(`classroom_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `LoginHistory`;
CREATE TABLE `LoginHistory` (
  `student_id` VARCHAR(10) NOT NULL,
  `session_id` VARCHAR(36) NOT NULL,
  `login_time` DATETIME NOT NULL,
  `login_duration` int NOT NULL,
  PRIMARY KEY (`session_id`, `student_id`),
  FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Material`;
CREATE TABLE `Material` (
  `material_id` INT NOT NULL,
  `course_id` VARCHAR(10) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `url` VARCHAR(255) NOT NULL,
  `last_update` DATETIME NOT NULL,
  `description` VARCHAR(255),
  PRIMARY KEY (`material_id`, `course_id`),
  FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Enrollment`;
CREATE TABLE `Enrollment` (
  `student_id` VARCHAR(10) NOT NULL,
  `course_id` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`student_id`, `course_id`),
  FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`) ON DELETE CASCADE,
  FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

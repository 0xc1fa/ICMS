CREATE TABLE Users {
    id PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
};

CREATE TABLE Courses {
    course_id PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    created_at DATETIME NOT NULL,
    classroom VARCHAR(10),
    zoom_link VARCHAR(255)
};

CREATE ZoomLinks {
    id PRIMARY KEY AUTOINCREMENT,
    link VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    course_id FOREIGN KEY REFERENCES Courses(course_id)
};

CREATE TABLE Materials {
    material_id PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    link VARCHAR(255),
    created_at DATETIME NOT NULL,
    course_id FOREIGN KEY REFERENCES Courses(course_id)
};

create Notes {
    note_id PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL
};

CREATE TABLE Enrollments {
    user_id FOREIGN KEY REFERENCES Users(id),
    course_id FOREIGN KEY REFERENCES Courses(course_id)
};

CREATE TABLE LoginHistroies {
    id PRIMARY KEY AUTOINCREMENT,
    user_id FOREIGN KEY REFERENCES Users(id),
    login_at DATETIME NOT NULL,
    duration INT NOT NULL
};

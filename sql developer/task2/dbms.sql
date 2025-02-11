CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT
);

CREATE TABLE Enrolments (
    enrolment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrolment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students (student_id, name, email) VALUES
(1, 'Alice Johnson', 'alice@example.com'),
(2, 'Bob Smith', 'bob@example.com'),
(3, 'Charlie Brown', 'charlie@example.com');

INSERT INTO Courses (course_id, course_name, course_description) VALUES
(1, 'Mathematics', 'Basic Math Course'),
(2, 'Physics', 'Fundamentals of Physics'),
(3, 'Chemistry', 'Introduction to Chemistry');

INSERT INTO Enrolments (enrolment_id, student_id, course_id, enrolment_date) VALUES
(1, 1, 1, '2024-01-10'),
(2, 2, 1, '2024-01-12'),
(3, 1, 2, '2024-02-15'),
(4, 3, 3, '2024-03-05');

SELECT s.name AS student_name, c.course_name
FROM Students s
INNER JOIN Enrolments e ON s.student_id = e.student_id
INNER JOIN Courses c ON e.course_id = c.course_id;

SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM Courses c
LEFT JOIN Enrolments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT s.student_id, s.name, COUNT(e.course_id) AS course_count
FROM Enrolments e
JOIN Students s ON e.student_id = s.student_id
GROUP BY s.student_id, s.name
HAVING COUNT(e.course_id) > 1;

SELECT c.course_name
FROM Courses c
LEFT JOIN Enrolments e ON c.course_id = e.course_id
WHERE e.enrolment_id IS NULL;

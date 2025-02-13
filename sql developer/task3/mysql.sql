CREATE DATABASE student_db;
USE student_db;

CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    math_score INT NOT NULL,
    science_score INT NOT NULL,
    english_score INT NOT NULL,
    total_score INT GENERATED ALWAYS AS (math_score + science_score + english_score) STORED
);
INSERT INTO Students (name, math_score, science_score, english_score) VALUES
('Alice', 85, 90, 88),
('Bob', 78, 85, 80),
('Charlie', 92, 95, 91),
('David', 65, 70, 68),
('Emma', 88, 89, 87),
('Frank', 74, 79, 76),
('Grace', 90, 94, 92);
SELECT student_id, name, math_score, science_score, english_score, total_score
FROM Students
ORDER BY total_score DESC
LIMIT 5;
SELECT AVG(total_score) AS avg_total_score
FROM Students
WHERE math_score > 70;
SELECT AVG(total_score) AS avg_total_score_200_250
FROM Students
WHERE total_score BETWEEN 200 AND 250;
SELECT MAX(math_score) AS second_highest_math_score
FROM Students
WHERE math_score < (SELECT MAX(math_score) FROM Students);
SELECT * FROM Students;
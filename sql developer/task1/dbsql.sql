-- Step 1: Create the database
CREATE DATABASE StudentManagement;

-- Use the newly created database
USE StudentManagement;

-- Step 2: Create the Students table
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(1),
    Age INT,
    Grade VARCHAR(10),
    MathScore INT,
    ScienceScore INT,
    EnglishScore INT
);
-- Inserting sample records into the Students table
INSERT INTO Students (Name, Gender, Age, Grade, MathScore, ScienceScore, EnglishScore)
VALUES
('John Doe', 'M', 18, 'A', 85, 90, 88),
('Jane Smith', 'F', 17, 'B', 75, 80, 78),
('Emily Davis', 'F', 19, 'C', 68, 70, 65),
('Michael Brown', 'M', 20, 'A', 92, 85, 89),
('Sarah Wilson', 'F', 18, 'B', 80, 85, 82),
('James Johnson', 'M', 17, 'C', 70, 60, 65),
('Lucas Martinez', 'M', 19, 'B', 80, 88, 85),
('Olivia Taylor', 'F', 20, 'A', 90, 95, 93),
('David Lee', 'M', 18, 'A', 87, 91, 85),
('Sophia Harris', 'F', 17, 'C', 72, 75, 70);
SELECT * FROM Students;
SELECT 
    AVG(MathScore) AS AvgMathScore, 
    AVG(ScienceScore) AS AvgScienceScore, 
    AVG(EnglishScore) AS AvgEnglishScore
FROM Students;
SELECT Name, 
       MathScore + ScienceScore + EnglishScore AS TotalScore
FROM Students
ORDER BY TotalScore DESC
LIMIT 1;
SELECT Grade, COUNT(*) AS NumberOfStudents
FROM Students
GROUP BY Grade;
SELECT Grade, COUNT(*) AS NumberOfStudents
FROM Students
GROUP BY Grade;
SELECT Name, MathScore
FROM Students
WHERE MathScore > 80;
UPDATE Students
SET Grade = 'B'
WHERE StudentID = 3;
SELECT * FROM Students;
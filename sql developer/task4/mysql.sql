CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    MathScore INT,
    TotalScore INT
);

INSERT INTO Students (StudentID, Name, MathScore, TotalScore) VALUES
(1, 'Alice', 85, 250),
(2, 'Bob', 90, 270),
(3, 'Charlie', 78, 240),
(4, 'David', 92, 280),
(5, 'Eve', 88, 260),
(6, 'Frank', 85, 250);
SELECT 
    StudentID,
    Name,
    TotalScore,
    RANK() OVER (ORDER BY TotalScore DESC) AS StudentRank  -- Changed alias
FROM Students;
SELECT 
    StudentID,
    Name,
    MathScore,
    SUM(MathScore) OVER (ORDER BY StudentID) AS RunningTotal
FROM Students;

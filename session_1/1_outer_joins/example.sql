-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 university.db
-- 2. Load this script: .read example.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

SELECT Students.name AS students, Department.name AS department 
FROM 
Students JOIN Department 
ON Students.department_id = Department.id
ORDER BY department;


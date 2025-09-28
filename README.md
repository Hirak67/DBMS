# Student Database - ORDER BY Clause Project

A MySQL database project demonstrating the use of the **ORDER BY** clause . The project sorts student records by different fields such as marks, age, and names.

## Project Description

This project creates a student database with student data includes (name,age,marks) , showcasing the **ORDER BY** clause in SQL to sort records in ascending and descending order.

## Example
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
CREATE TABLE students (
    name VARCHAR(50),
    age INT,
    marks INT,   
);

-- Insert sample data
INSERT INTO students (name, age, marks) VALUES
('Rohit Sharma', 20, 85),
('Priya Das', 19, 72),
('Amit Kumar', 21, 90),
('Sneha Roy', 18, 65),
('Manoj Kalita', 22, 78);

-- Example queries using ORDER BY
-- Sort by marks in descending order
SELECT * FROM students ORDER BY marks DESC;

-- Sort by age in ascending order
SELECT * FROM students ORDER BY age ASC;

-- Sort by name alphabetically
SELECT * FROM students ORDER BY name ASC;

--sort by name in reverse
SELECT * FROM students ORDER BY name DESC;

--use of multiple column 
SELECT * FROM students ORDER BY column1 (DESC/ASC) , column2 (DESC/ASC);


### THERE IS A FILE NAMED nlq_to_sql.py . WHICH IS A PYTHON FILE SO THAT USER CAN FIND THE QUERIES FOR SPECIFIC WORK TO DONE

CREATE DATABASE school;
USE school;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

INSERT INTO students VALUES
(101, 'Anusha', 22, 'Electronics'),
(102, 'Ravi', 23, 'Computer Science'),
(103, 'Priya', 21, 'Mechanical');

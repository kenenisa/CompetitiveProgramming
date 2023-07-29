

-- exercise 1

-- CREATE DATABASE sample1;
-- CREATE DATABASE sample2;


-- exercise 2

-- ALTER DATABASE sample1 MODIFY NAME=hr1;
-- ALTER DATABASE sample2 MODIFY NAME=hr2;


-- exercise 3

-- DROP DATABASE hr1;
-- USE master;
-- DROP DATABASE hr2;


-- exercise 4

-- CREATE DATABASE hilco;
-- USE hilco;

-- CREATE TABLE students (
--     SID INT NOT NULL,
--     sname TEXT NOT NULL,
--     Email TEXT,
--     advisor INT,
--     PRIMARY KEY (SID)
-- );
-- CREATE TABLE advisors (
--     Aid INT NOT NULL,
--     Aname TEXT NOT NULL,
--     PRIMARY KEY (Aid)
-- );


-- exercise 5

-- CREATE DATABASE shop;
-- USE shop;
-- CREATE TABLE groceries (
--     id INT NOT NULL,
--     item TEXT NOT NULL,
--     amount INT,
--     aisle INT,
--     PRIMARY KEY (id)
-- );

-- ALTER DATABASE shop MODIFY NAME=shopping;


-- exercise 6

-- USE shopping;
-- DROP TABLE groceries;
-- USE master;
-- DROP DATABASE shopping;


-- CREATE DATABASE Hilcoe;

USE Hilcoe;
-- DROP TABLE students;

-- CREATE TABLE students (
--     SID INT PRIMARY KEY IDENTITY,
--     sname TEXT NOT NULL,
--     Email TEXT,
--     advisor INT
-- );
-- CREATE TABLE advisors (
--     Aid INT PRIMARY KEY,
--     Aname TEXT NOT NULL
-- );

-- INSERT INTO students (sname,Email,advisor) VALUES ('Abebe','ab@gmail.com',3)
-- INSERT INTO students (sname,Email,advisor) VALUES ('Girma','gir@gmail.com',2)
-- INSERT INTO students (sname,Email) VALUES ('saba','saba@gmail.com')

-- INSERT INTO advisors (Aid,Aname) VALUES (1,'Dr Alemu')
-- INSERT INTO advisors (Aid,Aname) VALUES (2,'Dr biruck')
-- INSERT INTO advisors (Aid,Aname) VALUES (3,'Dr gebre')


-- 1
-- SELECT * FROM students;
-- SELECT * FROM advisors;

--2
-- SELECT sname FROM students;
-- SELECT sname as [student_name], Email as [student_email] from students;
-- SELECT * FROM students;

--3
-- ALTER TABLE advisors ADD Aemail varchar(30);

-- ALTER TABLE students ADD Saddress varchar(100);

-- ALTER TABLE students DROP COLUMN Saddress;

-- ALTER TABLE students ALTER COLUMN sname VARCHAR(100);

SELECT * FROM students;

-- EXEC SP_HELP students;

ALTER TABLE student
ADD CONSTRAINT fk_advisor
FOREIGN KEY (advisor) REFERENCES advisors(aid);



-- Bonus

-- DROP DATABASE hr;

-- USE hr;
USE hr;

-- CREATE TABLE teacher(
--     Tid INT PRIMARY KEY IDENTITY,
--     TName TEXT NOT NULL,
--     Email TEXT
-- );

-- INSERT INTO teacher (TName,Email) VALUES ('abebe','a@g.co');
-- INSERT INTO teacher (TName,Email) VALUES ('kebede','k@g.co');
-- INSERT INTO teacher (TName,Email) VALUES ('chala','c@g.co');

-- SELECT * FROM teacher;

-- CREATE TABLE stud(
--     Tid INT NOT NULL PRIMARY KEY IDENTITY(3,5),
--     TName TEXT NOT NULL,
--     Email TEXT
-- );

-- INSERT INTO stud (TName,Email) VALUES ('abebe','a@g.co');
-- INSERT INTO stud (TName,Email) VALUES ('kebede','k@g.co');
-- INSERT INTO stud (TName,Email) VALUES ('chala','c@g.co');

-- SELECT * FROM teacher;
-- SELECT * FROM stud;





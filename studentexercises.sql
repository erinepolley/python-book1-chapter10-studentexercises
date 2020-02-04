DROP TABLE IF EXISTS Cohort;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS AssignedExercises;

CREATE TABLE 'Cohort' (
	'Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'Name' TEXT NOT NULL
);

CREATE TABLE 'Student' (
	'Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'First_name' TEXT NOT NULL,
    'Last_name' TEXT NOT NULL,
    'Slack_handle' TEXT NOT NULL,
    'Cohort_Id' INTEGER,
    FOREIGN KEY('Cohort_Id') REFERENCES
    'Cohort'('Id')
);

CREATE TABLE 'Instructor' (
	'Id'   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'First_name' TEXT NOT NULL,
    'Last_name' TEXT NOT NULL,
    'Slack_handle' TEXT NOT NULL,
    'Specialty' TEXT NOT NULL,
    'Cohort_Id' INTEGER,
     FOREIGN KEY('Cohort_Id') REFERENCES
    'Cohort'('Id')
 );
    
 CREATE TABLE 'Exercise' (
    'Id'   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'Name' TEXT NOT NULL,
    'Language' TEXT NOT NULL
 );

CREATE TABLE 'AssignedExercises' (
	'Assigned_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'Student_Id' INTEGER,
    'Exercise_Id' INTEGER,
    FOREIGN KEY('Student_Id') REFERENCES 'Student'('Id'),
    FOREIGN KEY('Exercise_Id') REFERENCES 'Exercise'('Id')
);

INSERT INTO Cohort
VALUES (NULL, 'Cohort 34'),
 (NULL, 'Cohort 35'),
 (NULL, 'Cohort 36');

INSERT INTO Exercise
VALUES (NULL, 'Ex1', 'JavaScript'),
 (NULL, 'Ex2', 'JavaScript'),
 (NULL, 'Ex3', 'Python'),
 (NULL, 'Ex4', 'Python'),
 (NULL, 'Ex5', 'SQL');

INSERT INTO Instructor
SELECT null, 'Joe', 'Shepherd', 'joe', '80s jokes', Id
FROM Cohort 
WHERE Name = 'Cohort 36';

INSERT INTO Instructor
SELECT null, 'Jisie', 'David', 'jisie', 'polite shut ups', Id
FROM Cohort
WHERE Name = 'Cohort 34';

INSERT INTO Instructor
SELECT NULL, 'Jenna', 'Solis', 'jenna', 'fashion and knowing her shit', Id
FROM Cohort
WHERE Name = 'Cohort 35';

INSERT INTO Student
SELECT NULL, 'Erin', 'Polley', 'erin', Id 
FROM Cohort
WHERE Name = 'Cohort 36';

INSERT INTO Student
SELECT NULL, 'Matt', 'Blagg', 'matt', Id 
FROM Cohort
WHERE Name = 'Cohort 36';

INSERT INTO Student
SELECT NULL, 'Corri', 'Golden', 'corri', Id 
FROM Cohort
WHERE Name = 'Cohort 35';

INSERT INTO Student
SELECT NULL, 'Ryan', 'Cunningham', 'ryan', Id 
FROM Cohort
WHERE Name = 'Cohort 35';

INSERT INTO Student
SELECT NULL, 'Ryan', 'Bishop', 'ryan', Id 
FROM Cohort
WHERE Name = 'Cohort 34';

INSERT INTO Student
SELECT NULL, 'Chase', 'Fite', 'chase', Id 
FROM Cohort
WHERE Name = 'Cohort 34';

INSERT INTO Student
SELECT NULL, 'Sam', 'Pita', 'sam', Id 
FROM Cohort
WHERE Name = 'Cohort 35';
--(SELECT id from Cohort WHERE Cohort.Name = "Cohort 36")

INSERT INTO AssignedExercises
SELECT NULL, 1, 1;

INSERT INTO AssignedExercises
SELECT NULL, 1, 2;

INSERT INTO AssignedExercises
SELECT NULL, 2, 3;

INSERT INTO AssignedExercises
SELECT NULL, 2, 4;

INSERT INTO AssignedExercises
SELECT NULL, 3, 5;

INSERT INTO AssignedExercises
SELECT NULL, 3, 1;

INSERT INTO AssignedExercises
SELECT NULL, 4, 2;

INSERT INTO AssignedExercises
SELECT NULL, 4, 3;

INSERT INTO AssignedExercises
SELECT NULL, 5, 4;

INSERT INTO AssignedExercises
SELECT NULL, 5, 5;

INSERT INTO AssignedExercises
SELECT NULL, 6, 1;

INSERT INTO AssignedExercises
SELECT NULL, 6, 2;

INSERT INTO AssignedExercises
SELECT NULL, 7, 3;

INSERT INTO AssignedExercises
SELECT NULL, 7, 4;

INSERT INTO AssignedExercises
SELECT NULL, 8, 5;

INSERT INTO AssignedExercises
SELECT NULL, 8, 1;



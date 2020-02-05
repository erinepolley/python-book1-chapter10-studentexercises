import sqlite3
from students import Student
from instructor import Instructor

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')

class Reports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Erin Polley/workspace/python/book1/chapter10-studentexercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

    def create_instructor(self, cursor, row):
        return Instructor(row[1], row[2], row[3], row[4], row[6])

#ONE REPORT!!!!!!!!!!!!!!!!!!#
    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_student

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_name,
                s.Last_name,
                s.Slack_handle,
                s.Cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                    print(f'{student.first_name} {student.last_name} is in {student.cohort}.')

#ALL INSTRUCTORS REPORT!!!!!!!!!!
    def all_instructors(self):
        """Retrieve all instructors and their cohorts."""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_instructor

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id Instructor_Id,
            i.First_name,
            i.Last_name,
            i.Slack_handle,
            i.Specialty,
            i.Cohort_Id,
            c.Name
            from Instructor i 
            join Cohort c on i.Cohort_Id = c.Id
            """)

            all_instructors = db_cursor.fetchall()
            # print(all_instructors)

            for instructor in all_instructors:
                print(f'{instructor.first_name} {instructor.last_name} is the fearless leader of {instructor.cohort}.')

#BEAUTIFUL STUDENTS AND EXERCISES REPORT!!!!!!!!!!!!!!!!!!!!
    def exercises_with_students(self):
        """Retrieve all exercises and the students working on each one"""

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                e.Id ExerciseId,
                e.Name,
                s.Id StudentId,
                s.First_name,
                s.Last_name
                from Exercise e
                join AssignedExercises ae on ae.Exercise_Id = e.Id
                join Student s on s.Id = ae.Student_Id
                """)

            all_exercises_with_students = db_cursor.fetchall()

            # for exercise_student in all_exercises_with_students:
            #     print(f'{exercise_student[1]}: {exercise_student[3]} {exercise_student[4]}')

            # Takes our list of tuples and converts it to a dictionary with the exercise name as the key and a list of students as the value.
            exercises = dict()

            for exercise_student in all_exercises_with_students:
                exercise_id = exercise_student[0]
                exercise_name = exercise_student[1]
                student_id = exercise_student[2]
                student_name = f'{exercise_student[3]} {exercise_student[4]}'

                if exercise_name not in exercises:
                    # exercises[exercise_name] is adding a new key/value pair to the exercises dictionary, where exercise_name is the variable containing the key value which is string

                    # [student_name] is creating a list with one item, that item is the string contained in the variable student_name
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            # print(exercises)
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

#COHORTS REPORT!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def all_cohorts(self):

        """Retrieve all cohort names"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                   c.Name
            from Cohort c 
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                    print(f'{cohort[1]}')

#EXERCISES REPORT!!!!!!!!!!!!!!!!!!!
    def all_exercises(self):

        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                   e.Name,
                   e.Language
            from Exercise e  
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                    print(f'{exercise[1]}')

# JAVASCRIPT REPORT!!!!!!!!!!!!!!!!!!!!
    def all_javascript(self):

        """Retrieve all cohort names"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                   e.Name,
                   e.Language
            from Exercise e  
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                # print(exercise)
                if exercise[2] == "JavaScript":
                    print(f'{exercise[1]} is a JavaScript Exercise')
                elif exercise[2] == "Python":
                    print(f'{exercise[1]} is a Python Exercise')
                elif exercise[2] == "SQL":
                    print(f'{exercise[1]} is a SQL Exercise')

    def students_with_exercises(self):
        """Prints which exercises every student is working on"""

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                e.Id ExerciseId,
                e.Name,
                s.Id Student_Id,
                s.First_name,
                s.Last_name
                from Exercise e
                join AssignedExercises ae on ae.Exercise_Id = e.Id
                join Student s on s.Id = ae.Student_Id
                """)

            all_students_with_exercises = db_cursor.fetchall()
            print(all_students_with_exercises)
            exercises = dict()

            for student in all_students_with_exercises:
                # exercise_id = student[0]
                exercise_name = student[1]
                # student_id = student[2]
                student_name = f'{student[3]} {student[4]}'

                if student_name not in exercises:
reports = Reports()
reports.all_students()
reports.all_instructors()
reports.exercises_with_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript()
reports.students_with_exercises()




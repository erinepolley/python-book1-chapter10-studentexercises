import sqlite3

class Student():
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Erin Polley/workspace/python/book1/chapter10-studentexercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

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
                    print(f'{student.first_name} {student.last_name} is in {student.cohort}')


# reports = StudentExerciseReports()
# reports.all_students()

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


reports = StudentExerciseReports()
# reports.all_students()
reports.exercises_with_students()
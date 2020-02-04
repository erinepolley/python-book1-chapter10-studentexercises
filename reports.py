import sqlite3

class Student():
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort

student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
print(f'{student.first_name} {student.last_name} is in {student.cohort}')

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Erin Polley/workspace/python/book1/chapter10-studentexercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = StudentExerciseReports()
reports.all_students()

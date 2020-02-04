import sqlite3

# class Student():
#     def __init__(self, first_name, last_name, slack, cohort):
#         super().__init__()
#         self.first_name = first_name
#         self.last_name = last_name
#         self.slack = slack
#         self.cohort = cohort

class AllCohortReport():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Erin Polley/workspace/python/book1/chapter10-studentexercises/studentexercises.db"

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

AllCohortReport().all_cohorts()
# reports.all_students()
# reports.all_cohorts()


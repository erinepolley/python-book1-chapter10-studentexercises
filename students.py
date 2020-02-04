#first name, last name, slack handle, cohort, exercises[]

from people import People 

class Student(People):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort
        self.exercises = []
    def add_exercises(self, exercises_list):
        self.exercises.extend(exercises_list)


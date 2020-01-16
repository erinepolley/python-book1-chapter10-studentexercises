#first name, last name, slack handle, cohort, exercises[]

class Student:
    def __init__(self, first_name, last_name, slack, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort
        self.exercises = []
    def add_exercises(self, exercises_list):
        self.exercises.extend(exercises_list)


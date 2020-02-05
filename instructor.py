from people import People 

class Instructor(People):
    def __init__(self, first_name, last_name, slack, specialty, cohort):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.specialty = specialty
        self.cohort = cohort
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)

#instructor needs the ability to make an exercise, and then do a dot notation to append the exercise to the student's list. 
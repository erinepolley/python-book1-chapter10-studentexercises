from cohorts import Cohort
from exercise import Exercise
from instructor import Instructor
from students import Student

ex_1 = Exercise("1", "python",)
ex_2 = Exercise("2", "python")
ex_3 = Exercise("3", "python")
ex_4 = Exercise("4", "python")

three_six = Cohort("Cohort 36")
three_seven = Cohort("Cohort 37")
three_eight = Cohort("Cohort 38")

erin = Student("Erin", "Polley", "erin", "Cohort 36")
corri = Student("Corri", "Golden", "corri", "Cohort 36")
bito = Student("Bito", "Mann", "bito", "Cohort 38")
matt = Student("Matt", "Cragg", "cragg", "Cohort 36")

joe = Instructor("Joe", "Shepherd", "joe", "Cohort 36", "80s jokes")
jisie = Instructor("Jisie", "David", "jisie", "Cohort 36", "polite shut ups")
jenna = Instructor("Jenna", "Solis", "jenna", "Cohort 36", "fashion and knowing her shit")

joe.assign_exercise(matt, ex_1)
jisie.assign_exercise(bito, ex_2)
jenna.assign_exercise(corri, ex_3) 

def exercise_list(list):
    for list_item in list:
        print(f"{list_item.name} is what I have to do today")

exercise_list(matt.exercises)

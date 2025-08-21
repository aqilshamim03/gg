class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, student):
        self.student = student  

    def show_student(self):

        print(f"Student name is {self.student.name}")

s1 = Student("Aqil")

school = School(s1)
school.show_student()

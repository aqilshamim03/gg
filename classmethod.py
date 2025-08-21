class Students():

    count = 0
    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1


    #instance method
    def get_info(self):
            return f"{self.name} {self.gpa}"
        
    @classmethod     #decorator
    def get_count(cls):
            return f"total # of students: {cls.count}"
        
s1 = Students('Aqil', 3.5)
s2 = Students('Nasir', 3.8)

print(Students.get_count()) 
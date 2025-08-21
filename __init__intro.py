class Owner():
    def __init__(self,name,age):       #__init__ is a constructor method,it is automatically called when object of class is created
        self.name = name
        self.age = age

s1 = Owner('Aqil', 23)
print(s1.name)
print(s1.age)
class Computer:
    def config(self):
        print('i5 ,16gb ,1TB')
comp1 = Computer()

Computer.config(comp1)
comp1.config()


class Student:
    def set_name(self, name):
        self.name = name                            # Assigns name to the instance

    def greet(self):
        print(f"Hello, my name is {self.name}")

s1 = Student()
s1.set_name("Aqil")
s1.greet()

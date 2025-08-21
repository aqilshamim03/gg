
from class1_file import Class1     # Import Class1 from class1_file

class Class2:
    def __init__(self):
        self.obj1 = Class1("Aqil")    # Create an object of Class1 inside Class2

    def use_class1_methods(self):
        # Call Class1 methods
        print(self.obj1.greet())
        print("Square of 5 is:", self.obj1.square(5))



if __name__ == "__main__":
    c2 = Class2()
    c2.use_class1_methods()

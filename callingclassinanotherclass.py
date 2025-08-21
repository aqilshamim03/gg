class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # creating an object of Engine inside Car

    def drive(self):
        self.engine.start()  # calling Engine's method
        print("Car is driving.")


my_car = Car()
my_car.drive()

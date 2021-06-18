#oop
class Vehicle:
    def horn(self):
        print("Beep!")
class Car:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
obj = Car("BMW", "red")


#oop
class Vehicle:
    def horn(self):
        print("Beep!")
class Car(Vehicle):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
obj = Car("BMW", "red")
obj.horn()

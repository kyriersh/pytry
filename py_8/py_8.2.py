class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def vol(self):
        print(self.h * self.w)
w = int(input(" widght : "))
h = int(input(" height : "))
obj = Rectangle(w, h)
obj.vol()

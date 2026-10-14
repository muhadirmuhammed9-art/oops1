class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

r1 = Rectangle(length, width)

print("Area of rectangle:", r1.calculate_area())
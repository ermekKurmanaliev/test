import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.validate_triangle()

    def validate_triangle(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError("The sides do not form a valid triangle")

    def area(self):
        # Using Heron's formula to calculate area
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("The provided object is not a valid shape")
    return shape.area()

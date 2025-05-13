from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c
    
    def area(self):
        p = round((self.a + self.b + self.c)/2, 2)
        s = math.sqrt(p * (p - self.a) * (p- self.b) * (p - self.c))
        return round(s, 2)
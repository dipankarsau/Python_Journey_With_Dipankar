
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def get_dimensions(self, *args):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Polygon):

    def get_dimensions(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Polygon):

    def get_dimensions(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


# Rectangle object
R = Rectangle()
R.get_dimensions(5, 10)
print("Rectangle Area:", R.calculate_area())


# Triangle object
T = Triangle()
T.get_dimensions(6, 4)
print("Triangle Area:", T.calculate_area())
